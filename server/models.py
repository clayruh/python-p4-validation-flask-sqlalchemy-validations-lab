from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('name')
    def validate_name(self, key, value):
        if value == '' or value is None:
            raise ValueError('author has to have a name')
        return value
    
    @validates('phone_number')
    def validate_number(self, key, value):
        if len(value) == 10:
            return value
        raise ValueError('phone number has to be exactly 10 digits')

class Post(db.Model):
    __tablename__ = 'posts'
    
    @validates('category')
    def validate_category(self, key, value):
        genres = ["Fiction", "Non-Fiction"]
        if value in genres:
            return value
        else:
            raise ValueError("category is not Fiction or Non-Fiction")
        
    @validates('content')
    def validate_content(self, key, value):
        if len(value) < 250:
            raise ValueError('content is too short')
        return value
            
    @validates('summary')
    def validate_summary(self, key, value):
        if len(value) > 249:
            raise ValueError('summary is too long, over 250 characters')
        return value
    
    @validates('title')
    def validate_title(self, key, value):
        clickbait_titles = ['Wont Believe', 'Secret', 'Top', 'Guess']
        if value not in clickbait_titles:
            raise ValueError('title needs to have clickbait-y words')
        return value

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
