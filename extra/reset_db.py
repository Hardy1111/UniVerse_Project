#!/usr/bin/env python3
"""
Database Reset Script for UniVerse
This script recreates the database with the latest schema
"""

import os
from app import app, db
from models import Student, Company, Internship, Application

def reset_database():
    """Reset the database and create sample data"""
    print("Resetting database...")
    
    with app.app_context():
        # Drop all tables
        db.drop_all()
        print("Dropped all tables")
        
        # Create all tables with latest schema
        db.create_all()
        print("Created all tables with latest schema")
        
        # Create sample data
        print("Creating sample data...")
        
        # Create sample company
        company = Company(name="Tech Corp", email="company@tech.com")
        company.set_password("password123")
        db.session.add(company)
        db.session.flush()  # Get the ID without committing
        
        # Create sample internship
        internship = Internship(
            title="Software Development Intern",
            description="Join our team as a software development intern and work on exciting projects! You'll work with cutting-edge technologies and gain valuable experience in software development.",
            location="New York, NY",
            company_id=company.id
        )
        db.session.add(internship)
        
        # Create another sample internship
        internship2 = Internship(
            title="Marketing Intern",
            description="Help us grow our brand and reach new customers. Work on social media campaigns, content creation, and market research.",
            location="San Francisco, CA",
            company_id=company.id
        )
        db.session.add(internship2)
        
        db.session.commit()
        print("Sample data created successfully!")
        
        # Verify the data
        companies = Company.query.all()
        internships = Internship.query.all()
        
        print(f"Database stats:")
        print(f"   - Companies: {len(companies)}")
        print(f"   - Internships: {len(internships)}")
        
        print("\nDatabase reset complete!")
        print("\nTest Credentials:")
        print("   Company Login:")
        print("   - Email: company@tech.com")
        print("   - Password: password123")
        print("   - Account Type: Company")

if __name__ == "__main__":
    reset_database()
