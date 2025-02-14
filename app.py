from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import pandas as pd
import io
import datetime

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String, nullable=False)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    job = Column(String, nullable=False)

class HiredEmployee(Base):
    __tablename__ = "hired_employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload-csv/")
async def upload_csv(department_file: UploadFile = File(None), job_file: UploadFile = File(None), employee_file: UploadFile = File(None), db: Session = Depends(get_db)):
    try:
        if department_file:
            df = pd.read_csv(io.StringIO(await department_file.read().decode("utf-8")))
            for _, row in df.iterrows():
                db.add(Department(id=row["id"], department=row["department"]))
        
        if job_file:
            df = pd.read_csv(io.StringIO(await job_file.read().decode("utf-8")))
            for _, row in df.iterrows():
                db.add(Job(id=row["id"], job=row["job"]))
        
        if employee_file:
            df = pd.read_csv(io.StringIO(await employee_file.read().decode("utf-8")))
            for _, row in df.iterrows():
                db.add(HiredEmployee(id=row["id"], name=row["name"], datetime=datetime.datetime.fromisoformat(row["datetime"].replace("Z", "")), department_id=row["department_id"], job_id=row["job_id"]))
        
        db.commit()
        return {"message": "Files uploaded and data inserted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
