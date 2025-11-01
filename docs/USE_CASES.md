# USE_CASES.md

## 1. Actors
The UniVerse system involves the following main actors:

- **Student** – The primary user who applies for internships, views recommendations, and manages their account.
- **Company** – Posts internship opportunities and manages listings.
- **Admin** – Verifies companies and internship listings, and oversees overall system management.
- **Recommendation System** – Suggests suitable internships based on student profiles.
- **SheerID** – Third-party verification service used to authenticate student identity.

---

## 2. Use Case Descriptions

### **Use Case 1: Student Registration and Login**
**Actor:** Student  
**Goal:** Enable a student to create an account and log into the UniVerse platform.  

**Preconditions:**
- The student must have an active email account.  
- The student must not be pre-registered.  

**Main Flow:**
1. The student accesses the UniVerse registration page.  
2. Inputs name, email, password, and other required details.  
3. The system performs validation on the entered data.  
4. A new student record is created, and registration is confirmed.  
5. The student logs in with their email and password.  
6. The system checks credentials and grants access to the dashboard.

---

### **Use Case 2: Apply for Internship**
**Actor:** Student  
**Goal:** Allow students to browse available internships and submit applications.  

**Preconditions:**
- The student must be logged in.  
- There must be active internship postings available.  

**Main Flow:**
1. The student navigates to the internship listings page.  
2. The system displays all available internships.  
3. The student selects an internship and clicks “Apply.”  
4. The system checks eligibility (skills, requirements, etc.).  
5. If qualified, the system submits the application.  
6. The relevant company is notified of the student’s application.

---

### **Use Case 3: Manage Internship Listings**
**Actors:** Company, Admin  
**Goal:** Allow companies to create, edit, and manage internship listings, while Admins review and approve them.  

**Preconditions:**
- The company must be registered and logged in.  
- Internship postings must be valid and complete.  

**Main Flow:**
1. The company logs into the system.  
2. Selects the “Internship Management” option.  
3. Inputs or edits an internship posting.  
4. The system records the internship details.  
5. The Admin reviews and approves the posting.  
6. Once approved, the internship becomes visible to students.

---

### **Use Case 4: View Internship Recommendations**
**Actors:** Student, Recommendation System  
**Goal:** Provide personalized internship suggestions based on a student’s skills and preferences.  

**Preconditions:**
- The student’s profile must be complete.  
- The recommendation system must have access to internship data.  

**Main Flow:**
1. The student logs into their UniVerse account.  
2. The system identifies the student’s skills and preferences from their profile.  
3. The recommendation system analyzes available internship data.  
4. The system displays a list of recommended internships.  
5. The student can directly apply or view the details of each recommendation.

---

### **Use Case 5: Confirm Internships and Companies**
**Actors:** Admin, Verification System  
**Goal:** Ensure all listed internships and companies are verified and legitimate.  

**Preconditions:**
- Verification requests for companies or internships must exist.  

**Main Flow:**
1. The Admin opens the verification dashboard.  
2. The system fetches all pending verification requests.  
3. The Admin reviews the company and internship information.  
4. The system verifies the submitted details.  
5. The Admin updates the status to “Approved” or “Rejected.”  
6. The system marks the verified entities as trusted and visible to students.

---

## 3. UML Use Case Diagram
Below is the use case diagram representing the relationships between actors and use cases in the UniVerse system.

*(Insert your UML diagram image here)*  
Example:
```markdown
![Use Case Diagram](assets/universe_usecase_diagram.png)

