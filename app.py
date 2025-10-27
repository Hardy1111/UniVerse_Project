#imports

from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from models import db, Student, Company, Internship, Application
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.secret_key = 'universe-secret-key'

# SQLite setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///universe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Helper function for file uploads
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file, prefix='cv'):
    if file and allowed_file(file.filename):
        # Generate unique filename
        filename = secure_filename(file.filename)
        unique_filename = f"{prefix}_{uuid.uuid4().hex}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        return unique_filename
    return None

db.init_app(app)

with app.app_context():
    db.create_all()
    
    # Create sample data if database is empty
    try:
        if not Company.query.first():
            # Create sample company
            company = Company(name="Tech Corp", email="company@tech.com")
            company.set_password("password123")
            db.session.add(company)
            db.session.flush()  # Get the ID without committing
            
            # Create sample internship
            internship = Internship(
                title="Software Development Intern",
                description="Join our team as a software development intern and work on exciting projects!",
                location="New York, NY",
                company_id=company.id
            )
            db.session.add(internship)
            db.session.commit()
            print("Sample data created successfully!")
    except Exception as e:
        print(f"Error creating sample data: {e}")
        db.session.rollback()

@app.route('/')
def home():
    return render_template('index.html')

# ---------- Debug Route ----------
@app.route('/debug')
def debug():
    companies = Company.query.all()
    internships = Internship.query.all()
    students = Student.query.all()
    
    debug_info = {
        'companies': len(companies),
        'internships': len(internships),
        'students': len(students),
        'company_list': [{'name': c.name, 'email': c.email} for c in companies],
        'internship_list': [{'title': i.title, 'company': i.company.name if i.company else 'No Company'} for i in internships]
    }
    
    return f"<pre>{debug_info}</pre>"

# ---------- Registration ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_type = request.form['user_type']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        if user_type == 'student':
            existing_user = Student.query.filter_by(email=email).first()
        else:
            existing_user = Company.query.filter_by(email=email).first()

        if existing_user:
            flash('Email already registered. Please use a different email.', 'error')
            return render_template('register.html')

        if user_type == 'student':
            new_user = Student(name=name, email=email)
            new_user.set_password(password)
        else:
            new_user = Company(name=name, email=email)
            new_user.set_password(password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')

    return render_template('register.html')

# ---------- Login ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']

        if user_type == 'student':
            user = Student.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['student_id'] = user.id
                flash(f'Welcome back, {user.name}!', 'success')
                return redirect(url_for('student_dashboard'))
            else:
                flash('Invalid email or password for student account.', 'error')
        else:
            user = Company.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['company_id'] = user.id
                flash(f'Welcome back, {user.name}!', 'success')
                return redirect(url_for('company_dashboard'))
            else:
                flash('Invalid email or password for company account.', 'error')

    return render_template('login.html')

# ---------- Student Dashboard ----------
@app.route('/student/dashboard')
def student_dashboard():
    if 'student_id' not in session:
        flash('Please login to access your dashboard.', 'error')
        return redirect(url_for('login'))
    
    try:
        internships = Internship.query.all()
        print(f"Found {len(internships)} internships for student dashboard")
        return render_template('student_dashboard.html', internships=internships)
    except Exception as e:
        print(f"Error in student dashboard: {e}")
        flash('Error loading internships. Please try again.', 'error')
        return render_template('student_dashboard.html', internships=[])

# ---------- Company Dashboard ----------
@app.route('/company/dashboard', methods=['GET', 'POST'])
def company_dashboard():
    if 'company_id' not in session:
        flash('Please login to access your dashboard.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            title = request.form['title']
            description = request.form['description']
            location = request.form['location']
            company_id = session.get('company_id')

            new_internship = Internship(title=title, description=description, location=location, company_id=company_id)
            db.session.add(new_internship)
            db.session.commit()
            flash('Internship posted successfully!', 'success')
            print(f"New internship posted: {title}")
        except Exception as e:
            db.session.rollback()
            flash('Failed to post internship. Please try again.', 'error')
            print(f"Error posting internship: {e}")

    try:
        internships = Internship.query.filter_by(company_id=session.get('company_id')).all()
        print(f"Found {len(internships)} internships for company dashboard")
        return render_template('company_dashboard.html', internships=internships)
    except Exception as e:
        print(f"Error in company dashboard: {e}")
        flash('Error loading internships. Please try again.', 'error')
        return render_template('company_dashboard.html', internships=[])

# ---------- Apply for Internship Form ----------
@app.route('/apply/<int:id>')
def apply_internship_form(id):
    if 'student_id' not in session:
        flash('Please login to apply for internships.', 'error')
        return redirect(url_for('login'))
    
    internship = Internship.query.get_or_404(id)
    return render_template('apply_internship.html', internship=internship)

# ---------- Apply for Internship ----------
@app.route('/apply', methods=['POST'])
def apply_internship():
    if 'student_id' not in session:
        flash('Please login to apply for internships.', 'error')
        return redirect(url_for('login'))
    
    internship_id = request.form['internship_id']
    student_id = session['student_id']
    
    # Check if already applied
    existing_application = Application.query.filter_by(
        student_id=student_id, 
        internship_id=internship_id
    ).first()
    
    if existing_application:
        flash('You have already applied for this internship.', 'error')
    else:
        try:
            # Handle CV file upload
            cv_filename = None
            if 'cv_file' in request.files:
                cv_file = request.files['cv_file']
                if cv_file and cv_file.filename:
                    cv_filename = save_uploaded_file(cv_file, 'application_cv')
                    if not cv_filename:
                        flash('Invalid file type. Please upload PDF, DOC, or DOCX files only.', 'error')
                        return redirect(url_for('student_dashboard'))
            
            # Create new application with all details
            new_application = Application(
                student_id=student_id,
                internship_id=internship_id,
                cv_filename=cv_filename,
                cover_letter=request.form.get('cover_letter', ''),
                availability_start=request.form.get('availability_start', ''),
                availability_duration=request.form.get('availability_duration', ''),
                relevant_experience=request.form.get('relevant_experience', ''),
                why_interested=request.form.get('why_interested', '')
            )
            
            db.session.add(new_application)
            db.session.commit()
            flash('Application submitted successfully! The company will review your CV and details.', 'success')
        except Exception as e:
            db.session.rollback()
            print(f"Error submitting application: {e}")
            flash('Failed to submit application. Please try again.', 'error')
    
    return redirect(url_for('student_dashboard'))

# ---------- Logout ----------
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('home'))

# ---------- Search Internships ----------
@app.route('/search')
def search_internships():
    if 'student_id' not in session:
        flash('Please login to search internships.', 'error')
        return redirect(url_for('login'))
    
    keyword = request.args.get('keyword', '')
    if keyword:
        internships = Internship.query.filter(
            Internship.title.contains(keyword) | 
            Internship.description.contains(keyword) |
            Internship.location.contains(keyword)
        ).all()
    else:
        internships = Internship.query.all()
    
    return render_template('student_dashboard.html', internships=internships, search_keyword=keyword)

# ---------- My Applications ----------
@app.route('/my-applications')
def my_applications():
    if 'student_id' not in session:
        flash('Please login to view your applications.', 'error')
        return redirect(url_for('login'))
    
    applications = Application.query.filter_by(student_id=session['student_id']).all()
    return render_template('applications.html', applications=applications)

# ---------- Edit Internship ----------
@app.route('/edit-internship/<int:id>', methods=['GET', 'POST'])
def edit_internship(id):
    if 'company_id' not in session:
        flash('Please login to edit internships.', 'error')
        return redirect(url_for('login'))
    
    internship = Internship.query.get_or_404(id)
    if internship.company_id != session['company_id']:
        flash('You can only edit your own internships.', 'error')
        return redirect(url_for('company_dashboard'))
    
    if request.method == 'POST':
        internship.title = request.form['title']
        internship.description = request.form['description']
        internship.location = request.form['location']
        
        try:
            db.session.commit()
            flash('Internship updated successfully!', 'success')
            return redirect(url_for('company_dashboard'))
        except Exception as e:
            db.session.rollback()
            flash('Failed to update internship.', 'error')
    
    return render_template('edit_internship.html', internship=internship)

# ---------- Delete Internship ----------
@app.route('/delete-internship/<int:id>')
def delete_internship(id):
    if 'company_id' not in session:
        flash('Please login to delete internships.', 'error')
        return redirect(url_for('login'))
    
    internship = Internship.query.get_or_404(id)
    if internship.company_id != session['company_id']:
        flash('You can only delete your own internships.', 'error')
        return redirect(url_for('company_dashboard'))
    
    try:
        # Delete all applications for this internship first
        Application.query.filter_by(internship_id=id).delete()
        db.session.delete(internship)
        db.session.commit()
        flash('Internship deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Failed to delete internship.', 'error')
    
    return redirect(url_for('company_dashboard'))

# ---------- View Applications ----------
@app.route('/view-applications/<int:id>')
def view_applications(id):
    if 'company_id' not in session:
        flash('Please login to view applications.', 'error')
        return redirect(url_for('login'))
    
    internship = Internship.query.get_or_404(id)
    if internship.company_id != session['company_id']:
        flash('You can only view applications for your own internships.', 'error')
        return redirect(url_for('company_dashboard'))
    
    applications = Application.query.filter_by(internship_id=id).all()
    return render_template('view_applications.html', internship=internship, applications=applications)

# ---------- Update Application Status ----------
@app.route('/update-application-status/<int:id>/<status>')
def update_application_status(id, status):
    if 'company_id' not in session:
        flash('Please login to update application status.', 'error')
        return redirect(url_for('login'))
    
    application = Application.query.get_or_404(id)
    internship = application.internship
    
    if internship.company_id != session['company_id']:
        flash('You can only update applications for your own internships.', 'error')
        return redirect(url_for('company_dashboard'))
    
    if status in ['accepted', 'rejected']:
        application.status = status
        try:
            db.session.commit()
            flash(f'Application {status} successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Failed to update application status.', 'error')
    
    return redirect(url_for('view_applications', id=internship.id))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
