from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Assistant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Assistant {self.name}>'