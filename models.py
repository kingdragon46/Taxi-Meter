from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Meter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Meter('{self.id}', '{self.label}')"

class Meter_Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meter.id'), nullable=False)
    time_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    value = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Meter Data('{self.id}', '{self.meter_id}', '{self.time_stamp}', '{self.value}')"
