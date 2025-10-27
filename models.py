from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    degree = db.Column(db.String(100))
    skills = db.Column(db.String(200))
    cv_filename = db.Column(db.String(255))
    
    
    # used ai for security
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    company = db.relationship('Company', backref=db.backref('internships', lazy=True))

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'), nullable=False)
    date_applied = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected
    
    # Application details
    cv_filename = db.Column(db.String(255))  # CV file uploaded during application
    cover_letter = db.Column(db.Text)  # Cover letter/motivation
    expected_salary = db.Column(db.String(100))  # Expected salary range
    availability_start = db.Column(db.String(100))  # When they can start
    availability_duration = db.Column(db.String(100))  # How long they can work
    relevant_experience = db.Column(db.Text)  # Relevant experience
    why_interested = db.Column(db.Text)  # Why they're interested in this role

    student = db.relationship('Student', backref=db.backref('applications', lazy=True))
    internship = db.relationship('Internship', backref=db.backref('applications', lazy=True))
    
    # Ensure one application per student per internship
    __table_args__ = (db.UniqueConstraint('student_id', 'internship_id'),)
