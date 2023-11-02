import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(20), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    image_url = Column(String(200), nullable=False)
    post_date = Column(String(20), nullable=False)
    caption = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(300), nullable=False)
    username = Column(String(20), nullable=False)
    date = Column(String(20), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
