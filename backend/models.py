from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)

class Resume(Base):
    __tablename__ = 'resumes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    file_path = Column(String)

class JobDescription(Base):
    __tablename__ = 'job_descriptions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    file_path = Column(String)

class AnalysisResult(Base):
    __tablename__ = 'analysis_results'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    job_id = Column(Integer, ForeignKey('job_descriptions.id'))
    score = Column(Integer)
    feedback = Column(String)
