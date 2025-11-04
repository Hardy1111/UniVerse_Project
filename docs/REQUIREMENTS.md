# UniVerse – Requirements Specification

## 1. Requirements Elicitation

### 1.1 Techniques Used
To gather requirements for the **UniVerse** project, we applied **two elicitation techniques**:
1. **Online Survey**
2. **Team Brainstorming Session**

---

### 1.2 Online Survey
An online Google Form was distributed among university students to collect feedback about what services they would like in a student-focused platform.  
The survey focused mainly on internship support and additional digital student services.

- **Participants:** 75 university students (responses still being collected)  
- **Purpose:** To identify students’ needs, frustrations, and expectations for a multi-service platform.
- **Target group:** Students from different majors and academic years.

**Example Survey Questions:**
1. How do you currently find internship opportunities?  
2. What are the main challenges you face when applying for internships?  
3. Would you be interested in using a verified platform (like UniVerse) designed for university students to find internships?  
4. What features would you like UniVerse to include? (Community for students, Gamify study session, Event announcement, other)  
5. What feature should we add that would be most helpful for students?

**Key Findings:**
- Most students struggle to find and apply for internships easily.  
- Many want a **single platform** that includes multiple student services.  
- Students expect an **organized dashboard** to track internship and form submissions.  
- Community and Gamify Study session were highly requested.  
- Future interest in **Strong community** and **filtering system** was noted.

---

### 1.3 Brainstorming Session
A brainstorming session was held among all team members to refine the project’s concept and identify realistic features for the first release.

- **Participants:** All 5 UniVerse team members  
- **Purpose:** Combine individual ideas and prioritize the most feasible features.  
- **Approach:** Informal group discussion focused on practicality and user value.

**Ideas Generated:**
- Internship application and tracking system  
- Student medical record with QR access (future feature)    
- Student dashboard for status and notifications  
- Admin panel for approving/rejecting applications  
- Community and Gamify study session (future feature)

---

### 1.4 Raw Requirements List
Below is the consolidated list of requirements gathered from both the survey and brainstorming session:

| ID | Requirement Description |
|----|--------------------------|
| R1 | Students can browse and apply for internships through the platform |
| R2 | Students can upload their CV or personal info when applying |
| R3 | Admins can review and approve internship applications |
| R4 | Students receive notifications when application status changes |
| R5 | System stores emergency medical info accessible via QR code |
| R6 | Platform supports both mobile and desktop access |
| R7 | Platform should be clean, simple, and user-friendly |
| R8 | Users can log in securely with personal credentials |
| R9 | Admins can post or update internship opportunities |
| R10 | Website supports multiple languages (future update) |

---

## 2. Requirements Classification

### 2.1 Purpose
The goal of this section is to organize and categorize all the raw requirements identified during the elicitation phase.  
Each requirement is classified based on its **type** (Functional or Non-Functional) and **level** (User or System).

---

### 2.2 Requirements Classification Table

| ID | Requirement Description | Type | Level |
|----|--------------------------|-------|--------|
| R1 | Students can browse and apply for internships through the platform | Functional | User |
| R2 | Students can upload their CV or personal info when applying | Functional | User |
| R3 | Admins can review and approve internship applications | Functional | System |
| R4 | Students receive notifications when application status changes | Functional | System |
| R5 | System stores emergency medical info accessible via QR code | Functional | System |
| R6 | Platform supports both mobile and desktop access | Non-Functional | System |
| R7 | Platform should be clean, simple, and user-friendly | Non-Functional | System |
| R8 | Users can log in securely with personal credentials | Functional | System |
| R9 | Admins can post or update internship opportunities | Functional | System |
| R10 | Website supports multiple languages (future update) | Non-Functional | System |

---

### 2.3 Analysis Summary

- **Functional Requirements (7 total):**  
  These describe what the UniVerse platform will *do*. They include main actions such as internship applications, admin management, login, notifications, and medical data handling.

- **Non-Functional Requirements (3 total):**  
  These describe how the system will *behave* or perform, such as having a simple interface, supporting multiple devices, and future language options.

- **User-Level Requirements:**  
  Requirements directly visible or used by students (R1, R2).

- **System-Level Requirements:**  
  Requirements managed by administrators or the system (R3, R4, R5, R6, R7, R8, R9, R10).

---

## 3. Structured Specification Developer

### 3.1 Purpose
This section presents the **structured specifications** for three critical functional requirements of the **UniVerse** platform.  
Each specification provides detailed information about the function, inputs, outputs, and actions needed to implement the feature successfully.

---

### 🧩 R1 – Student Can Browse and Apply for Internships

**Function:**  
Allow students to browse active internship listings and apply directly through the platform.

**Description:**  
students to search and view available internship opportunities filtered by their degree, skills, interests, location, and preferred company or industry. Students can then submit applications through the same interface.

**Inputs:**  
- Degree  
- Skill  
- Interest  
- Location  
- Company name  
- Industry

**Source:**
our recommendation system will provide the best interest based on the input

**Outputs:**  
- List of internships  
- Company name  
- Location  

**Destination:**  
Displayed on the student’s dashboard.

**Actions:**  
- Retrieve all active internships from the database.  
-  Display listings with filtering and search capability.  
-  Accept student application and uploaded files.

**Requires:**  
- Student account (logged in)  
- Active internship listings  

**Precondition:**  
The student’s email must be linked with **SheerID** for verification.

**Postcondition:**
internship offer show to the students based on their interest

**Side Effect:**
a internship has been filled and maybe the company manger forgets to update the page and student are still uplaying for it 

---

### 🧩 R2 – Company manger review and approve internship

**Function:**

Allow company managers to review student internship applications and approve or reject them through the platform.

**Description:**

verified company manager to access students application, review the student CV, skill, degree, and make decision to whether to accept it or reject it.

**Input:**

 - student name
 - degree
 - skill
 - CV

**Source:**

company manger looking at student profile 

**Output:**

- student name
- students’ skill
- degree

**Destination:**

student profile that the manger is reviewing it to whether to accept it or no

**Action:** 

select student profile and review them and make decision on them 

**Require:**

Company name (verified company account)

**Precondition:**

student profile who are looking for internship, the company manger must be authenticated

**Postcondition:**

after reviewing the student profile, there must option to the manager to whther to accepted or rejected it

**Side Effect:**

the student must be still active, after approving the notification may not go the student and the student may never know whether its application is accepted or not


---

### 🧩 R3 – User can log-in securely with personal credential


**Function:**

Allow users to log in securely using their personal credentials

**Description:**

verified users to access the platform by entering their registered email and password. The system validates the credentials, applies encryption for password security, and grants access to the appropriate dashboard based on the user role 

**Input:** 

- email
-  password

**Source:**

 User input through the login interface on the platform

**Output:**

 - Authentication success or failure message
 -  User taken, student email is not link with sheerID
 
**Destination:**

- user inside their profile
-  user fail to log in

**Require:**

 - student email with sheerID
 - encryption
 -  verified company email
 
**Precondition:**

- student email with sheerID
- verified company email

**Postcondition:**

after failing to log in will be repeated (limit time) until all required are done, after successfully login which user will be in his/her own email

**Side Effect:**

 May trigger temporary account lock after multiple failed attempts<


---

## 4. Requirements Prioritization

### 4.1 Purpose
The purpose of this section is to assign a **priority level** to each requirement according to its importance, feasibility, and impact on the UniVerse platform.  
The priorities follow the standard categories:
- **M – Mandatory:** Core features essential for system functionality.  
- **N – Nice to Have:** Valuable additions that can be implemented if time and resources allow.  
- **S – Superfluous:** Low-priority features planned for future versions or considered non-essential.

---

### 4.2 Prioritization Table

| ID | Requirement Description | Priority | Justification |
|----|--------------------------|-----------|----------------|
| R1 | Students can browse and apply for internships through the platform | **M** | Central feature of UniVerse; core project goal. |
| R2 | Students can upload their CV or personal info when applying | **M** | Necessary for completing internship applications. |
| R3 | Admins can review and approve internship applications | **M** | Required to validate and manage student applications. |
| R4 | Students receive notifications when application status changes | **N** | Useful for user engagement but not essential for MVP. |
| R5 | System stores emergency medical info accessible via QR code | **N** | Valuable safety feature; can be added after core launch. |
| R6 | Platform supports both mobile and desktop access | **M** | Ensures accessibility and usability across devices. |
| R7 | Platform should be clean, simple, and user-friendly | **M** | Directly affects usability and overall design quality. |
| R8 | Users can log in securely with personal credentials | **M** | Fundamental for authentication and data protection. |
| R9 | Admins can post or update internship opportunities | **M** | Core requirement for maintaining internship listings. |
| R10 | Website supports multiple languages (future update) | **S** | Planned future feature once the main system is stable. |

---

### 4.3 Summary
- **Mandatory (M):** 5 requirements — the foundation of the UniVerse MVP version.  
- **Nice to Have (N):** 2 requirements — recommended for version 2 updates.  
- **Superfluous (S):** 1 requirement — postponed to later stages.

The prioritization ensures that the development team focuses first on **core system functionality** (student-admin interactions and internship management) before adding secondary enhancements such as multilingual support or notifications.

---
