"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMG = 'https://tinyurl.com/demo-cupcake'

db = SQLAlchemy()

def connect_db(app):
    """Connects to database"""

    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Model for Cupcakes"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float,nullable=False)
    image = db.Column(db.Text,nullable=False, default = DEFAULT_IMG)

    def to_dict(self):
        """Serializes cupcake to a dict for info"""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }
