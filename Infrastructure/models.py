from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Contract(db.Model):
    __tablename__ = 'contracts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), default="Contratto di ScopaAmici")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="draft")

    clauses = db.relationship('Clause', backref='contract', cascade="all, delete-orphan")
    answers = db.relationship('Answer', backref='contract', cascade="all, delete-orphan")


class Clause(db.Model):
    __tablename__ = 'clauses'
    id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer)
    is_custom = db.Column(db.Boolean, default=False)


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    field_type = db.Column(db.String(50), default='text')


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    value = db.Column(db.Text, nullable=False)

    question = db.relationship('Question')
