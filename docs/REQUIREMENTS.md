# 🪐 UniVerse – Requirements Specification

## 1. Requirements Elicitation

### 1.1 Techniques Used
To gather requirements for the **UniVerse** project, we applied **two elicitation techniques**:
1. **Online Survey**
2. **Team Brainstorming Session**

---

### 1.2 Online Survey
An online Google Form was distributed among university students to collect feedback about what services they would like in a student-focused platform.  
The survey focused mainly on **internship support** and additional **digital student services**.

- **Participants:** 75 university students (responses still being collected)  
- **Purpose:** Identify students’ needs, frustrations, and expectations for a multi-service platform  
- **Target group:** Students from different majors and academic years

**Example Survey Questions:**
1. How do you currently find internship opportunities?  
2. What are the main challenges you face when applying for internships?  
3. Would you be interested in using a verified platform (like UniVerse) designed for university students to find internships?  
4. What features would you like UniVerse to include? (Community for students, Gamify study session, Event announcement, other)  
5. What feature should we add that would be most helpful for students?

**Key Findings:**
- Most students struggle to find and apply for internships easily  
- Many want a **single platform** that includes multiple student services  
- Students expect an **organized dashboard** to track applications and forms  
- **Community** and **Gamify Study session** were highly requested  
- Interest in **filtering system** and **strong community features** was noted  

---

### 1.3 Brainstorming Session
A brainstorming session was held among all team members to refine the project’s concept and identify realistic features for the first release.

- **Participants:** All 5 UniVerse team members  
- **Purpose:** Combine individual ideas and prioritize the most feasible features  
- **Approach:** Informal group discussion focused on practicality and user value  

**Ideas Generated:**
- Internship application and tracking system  
- Student medical record with QR access (future feature)  
- Student dashboard for status and notifications  
- **Company manager panel** for approving/rejecting applications  
- Community and Gamify study session (future feature)

---

### 1.4 Raw Requirements List

| ID  | Requirement Description |
|-----|--------------------------|
| R1  | Students can browse and apply for internships through the platform |
| R2  | Students can upload their CV or personal info when applying |
| R3  | Company managers can review and approve internship applications |
| R4  | Students receive notifications when application status changes |
| R5  | System stores emergency medical info accessible via QR code |
| R6  | Platform supports both mobile and desktop access |
| R7  | Platform should be clean, simple, and user-friendly |
| R8  | Users can log in securely with personal credentials |
| R9  | Company managers can post or update internship opportunities |
| R10 | Website supports multiple languages (future update) |

---

## 2. Requirements Classification

### 2.1 Purpose
This section organizes all raw requirements identified during the elicitation phase.  
Each is categorized by **type** (Functional / Non-Functional) and **level** (User / System).

---

### 2.2 Classification Table

| ID  | Requirement Description | Type | Level |
|-----|--------------------------|-------|--------|
| R1  | Students can browse and apply for internships through the platform | Functional | User |
| R2  | Students can upload their CV or personal info when applying | Functional | User |
| R3  | Company managers can review and approve internship applications | Functional | System |
| R4  | Students receive notifications when application status changes | Functional | System |
| R5  | System stores emergency medical info accessible via QR code | Functional | System |
| R6  | Platform supports both mobile and desktop access | Non-Functional | System |
| R7  | Platform should be clean, simple, and user-friendly | Non-Functional | System |
| R8  | Users can log in securely with personal credentials | Functional | System |
| R9  | Company managers can post or update internship opportunities | Functional | System |
| R10 | Website supports multiple languages (future update) | Non-Functional | System |

---

### 2.3 Analysis Summary
- **Functional Requirements (7):** Core system actions like applying for internships, reviewing applications, authentication, etc.  
- **Non-Functional Requirements (3):** Define how the system behaves — simplicity, responsiveness, and accessibility.  
- **User-Level Requirements:** R1, R2  
- **System-Level Requirements:** R3 → R10  

---

## 3. Structured Specification Developer

### 3.1 Purpose
Below are structured specifications for three critical **functional requirements** of UniVerse.  
Each includes its function, inputs, outputs, and system behavior.

---

### 🧩 R1 – Students Can Browse and Apply for Internships

**Function:**  
Allow students to browse active internship listings and apply directly through the platform.

**Description:**  
Students can search and view internship opportunities filtered by their **degree**, **skills**, **interests**, **location**, or **preferred company**.  
They can then submit applications through the same interface.

**Inputs:**  
- Degree  
- Skill  
- Interest  
- Location  
- Company name  
- Industry  

**Source:**  
Recommendation system based on user input.  

**Outputs:**  
- Internship listings  
- Company name  
- Location  

**Destination:**  
Student dashboard  

**Actions:**  
- Retrieve all active internships  
- Display listings with filtering/search capability  
- Accept and store student applications and files  

**Requires:**  
- Active student account  
- Internship data in the database  

**Precondition:**  
Student’s email must be verified via **SheerID**.  

**Postcondition:**  
Internship offers are displayed to the student.  

**Side Effect:**  
If a company manager forgets to update a filled internship, students may continue applying to unavailable listings.  

---

### 🧩 R2 – Company Manager Reviews and Approves Internships

**Function:**  
Allow company managers to review student applications and approve or reject them.

**Description:**  
Verified company managers can access student profiles, review their **CV**, **skills**, and **degree**, and decide to accept or reject.  

**Inputs:**  
- Student name  
- Degree  
- Skill  
- CV  

**Source:**  
Company manager dashboard  

**Outputs:**  
- Student info (name, skills, degree)  
- Application decision  

**Destination:**  
Student profile view  

**Actions:**  
- Select and review student applications  
- Approve or reject application  

**Requires:**  
- Verified company account  

**Precondition:**  
Company manager must be authenticated.  

**Postcondition:**  
Decision stored and optionally triggers student notification.  

**Side Effect:**  
If notifications fail, the student may not be informed of the decision.  

---

### 🧩 R3 – User Login (Secure Authentication)

**Function:**  
Allow users (students or company managers) to log in securely using credentials.  

**Description:**  
Users log in with their registered **email** and **password**. The system verifies credentials, applies **encryption**, and redirects users based on their role.  

**Inputs:**  
- Email  
- Password  

**Source:**  
Login interface  

**Outputs:**  
- Authentication success/failure message  

**Destination:**  
- User dashboard (if successful)  
- Error screen (if failed)  

**Requires:**  
- Verified student/company email  
- Encryption  

**Precondition:**  
Registered email and password exist in the system.  

**Postcondition:**  
Account access granted or login attempt limited after multiple failures.  

**Side Effect:**  
Temporary account lock after repeated failed attempts.  

---

## 4. Requirements Prioritization

### 4.1 Purpose
This section assigns **priority levels** to requirements based on importance, feasibility, and impact.

- **M – Mandatory:** Core system features  
- **N – Nice to Have:** Optional improvements  
- **S – Superfluous:** Future or low-priority features  

---

### 4.2 Prioritization Table

| ID  | Requirement Description | Priority | Justification |
|-----|--------------------------|-----------|----------------|
| R1  | Students can browse and apply for internships | **M** | Central goal of UniVerse |
| R2  | Students can upload CV/personal info when applying | **M** | Required for applications |
| R3  | Company managers can review and approve applications | **M** | Core management functionality |
| R4  | Students receive notifications on application status | **N** | Improves UX, not core MVP |
| R5  | System stores medical info via QR code | **N** | Safety feature; later phase |
| R6  | Platform supports mobile and desktop | **M** | Accessibility essential |
| R7  | Clean, simple, and user-friendly UI | **M** | Key usability factor |
| R8  | Secure user login | **M** | Authentication critical |
| R9  | Company managers can post/update internships | **M** | Core data maintenance |
| R10 | Multi-language support | **S** | Planned for future release |

---

### 4.3 Summary
- **Mandatory (M):** 5 requirements – foundation of MVP  
- **Nice to Have (N):** 2 – later enhancement  
- **Superfluous (S):** 1 – future roadmap  

The focus is first on **core student–company manager interactions** and **internship workflows** before introducing secondary or multilingual features.

---


