from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean

from flask_spirits.database import Model


class Playing(Model):
    __tablename__ = 'playing'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    theme = Column(String)
    description = Column(String)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime)
    location_one = Column(String)
    location_two = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)