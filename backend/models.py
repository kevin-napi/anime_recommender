from app import db

class Ani(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(300), nullable=True)
    
    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "rating": self.rating,
            "description": self.description,
            "imgUrl": self.img_url
        }