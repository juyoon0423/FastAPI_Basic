from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 연결 (파일 기반 DB)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# SQLAlchemy 엔진 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성 (모델 상속용)
Base = declarative_base()

# Dependency: DB 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
