import datetime as dt
from sqlalchemy import Column, DateTime, Integer, String, Boolean, Text

from flask_spirits.database import Model


class Game(Model):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    title = Column(String, info={'label': 'Title'})
    theme = Column(String, info={'label': 'Theme'})
    description = Column(Text, info={'label': 'Description'})
    start = Column(DateTime, nullable=False, info={'label': 'Start'})
    end = Column(DateTime, info={'label': 'End (optional)'})
    location_one = Column(String, info={'label': 'Location One'})
    location_two = Column(String, info={'label': 'Location Two'})
    created_at = Column(DateTime, default=dt.datetime.now)
    updated_at = Column(DateTime)

    @classmethod
    def current_playings(cls):
        tomorrow = dt.datetime.now() + dt.timedelta(days=1)
        return cls.query.filter(cls.start > tomorrow).all()