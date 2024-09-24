#テーブル定義
#テーブルのカラム情報を定義するためのクラスを格納

from sqlalchemy import Column, Integer, String, Text, Time
from models.database import Base
from datetime import datetime

class MedicineInfo(Base):
    __tablename__ = 'medinfo'
    id = Column(Integer,primary_key=True)
    title = Column(String(128),unique=True)
    scheduled_time = Column(Time(10), nullable=False)  # 時刻を保存するカラム