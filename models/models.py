#テーブル定義
#テーブルのカラム情報を定義するためのクラスを格納

from sqlalchemy import Column, Integer, String
from models.database import Base
from datetime import datetime

class MedicineInfo(Base):
    __tablename__ = 'medinfo'
    id = Column(Integer,primary_key=True)
    title = Column(String(128),unique=True)
    time = Column(String(5))
    
    def __init__(self,title=None,time=None):
        self.title = title
        if time:
            self.time = datetime.strptime(time,"%H:%M").time().strftime("%H:%M")
        else:
            self.time = None
            
    def __repr__(self):
        return '<Title %r>' % (self.title)