from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    location = Column(String)
    company = Column(String)
    job_id = Column(Integer, unique=True, index=True)
    url = Column(String)
    first_published = Column(DateTime)
    job_type = Column(String)
