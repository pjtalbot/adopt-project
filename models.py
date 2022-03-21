from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet"""

    __tablename__= 'pets'
    def __repr__(self):
        p=self
        return f'<Pet Id={p.id}>'

#         id: auto-incrementing integer
# name: text, required
# species: text, required
# photo_url: text, optional
# age: integer, optional
# notes: text, optional
# available: true/false, required, should default to available
    id = db.Column(db.Integer,primary_key=True,
                    autoincrement=True,
                    nullable=False)
    name = db.Column(db.String(40), nullable=False)
    species = db.Column(db.String(40), nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(1400), nullable=True)
    available = db.Column(db.Boolean, default=True, nullable=False)

