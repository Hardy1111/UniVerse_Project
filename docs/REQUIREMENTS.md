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
4. What features would you like UniVerse to include? (Community for students,Gamify study session,Event announcement,other)  
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
- Community and Gamify study session(future feature)

---

### 1.4 Raw Requirements List
Below is the consolidated list of requirements gathered from both the survey and brainstorming session:
| ID | Requirement Description |
|----|--------------------------|
| R1 | Students can browse and apply for internships through the platform |
| R2 | Students can upload their CV or personal info when applying |
| R3 | Admins can review and approve internship applications |
| R4 | Students receive notifications when application status changes |
| R5 | Students can view submitted forms (internship, medical, etc.) in a dashboard |
| R6 | Admins can manage and filter applications |
| R7 | System stores emergency medical info accessible via QR code |
| R8 | Platform supports both mobile and desktop access |
| R9 | Students have a personal profile showing internship progress |
| R10 | Platform should be clean, simple, and user-friendly |
| R11 | Users can log in securely with personal credentials |
| R12 | Admins can post or update internship opportunities |
| R13 | Students can rate internship experiences (optional) |
| R14 | System sends automatic confirmation messages on form submission |
| R15 | Website supports multiple languages (future update) |

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
| R5 | Students can view submitted forms (internship, medical, etc.) in a dashboard | Functional | User |
| R6 | Admins can manage and filter applications | Functional | System |
| R7 | System stores emergency medical info accessible via QR code | Functional | System |
| R8 | Platform supports both mobile and desktop access | Non-Functional | System |
| R9 | Students have a personal profile showing internship progress | Functional | User |
| R10 | Platform should be clean, simple, and user-friendly | Non-Functional | System |
| R11 | Users can log in securely with personal credentials | Functional | System |
| R12 | Admins can post or update internship opportunities | Functional | System |
| R13 | Students can rate internship experiences (optional) | Functional | User |
| R14 | System sends automatic confirmation messages on form submission | Functional | System |
| R15 | Website supports multiple languages (future update) | Non-Functional | System |

---

### 2.3 Analysis Summary

- **Functional Requirements (12 total):**  
  These describe what the UniVerse platform will *do*. They include the main actions such as registration, internship applications, admin management, notifications, and data handling.

- **Non-Functional Requirements (3 total):**  
  These describe how the system will *behave* or perform, such as having a simple interface, supporting multiple devices, and future language options.

- **User-Level Requirements:**  
  Requirements that are directly visible or used by students (R1, R2, R5, R9, R13).

- **System-Level Requirements:**  
  Requirements that operate behind the scenes or are managed by administrators and the system (R3, R4, R6, R7, R8, R10, R11, R12, R14, R15).


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
Students can search for and view available internship opportunities and submit applications.

**Inputs:**  
- Degree  
- Skill  
- Interest  
- Location  
- Company name  
- Industry  

**Outputs:**  
- List of internships  
- Company name  
- Location  

**Destination:**  
Displayed on the student’s dashboard.

**Actions:**  
1. Retrieve all active internships from the database.  
2. Display listings with filtering and search capability.  
3. Accept student application and uploaded files.

**Requires:**  
- Student account (logged in)  
- Active internship listings  

**Precondition:**  
The student’s email must be linked with **SheerID** for verification.

---

### 🧩 R2 – Admin Management and Filtering of Applications

**Function:**  
Allow administrators to filter, sort, and manage internship applications using various parameters.

**Description:**  
Admins can view, search, and filter available internship applications and see detailed information for each listing.

**Inputs:**  
- Filter options: title, description, required skills, degree required  

**Outputs:**  
- Filtered application list  

**Destination:**  
Displayed on the admin dashboard as a filtered internship view.

**Actions:**  
1. Admin enters a filter or search query.  
2. System retrieves and displays matching records.  

---

### 🧩 R3 – Admin Posting and Updating Internship Opportunities

**Function:**  
Allow companies or administrators to post, update, or delete internship listings.

**Description:**  
Companies can manage internship listings by creating new posts or editing existing ones.

**Inputs:**  
- Company name  
- Email  
- Industry  
- Location  
- Description  

**Outputs:**  
- New internship post  
- Updated internship information  

**Destination:**  
Internship listings database.

**Requires:**  
- Company name (verified company account)

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
| R5 | Students can view submitted forms (internship, medical, etc.) in a dashboard | **M** | Key student function to track progress and submissions. |
| R6 | Admins can manage and filter applications | **M** | Important for maintaining organized records and workflow. |
| R7 | System stores emergency medical info accessible via QR code | **N** | Valuable safety feature; can be added after core launch. |
| R8 | Platform supports both mobile and desktop access | **M** | Ensures accessibility and usability across devices. |
| R9 | Students have a personal profile showing internship progress | **M** | Enhances user experience and system transparency. |
| R10 | Platform should be clean, simple, and user-friendly | **M** | Directly affects usability and overall design quality. |
| R11 | Users can log in securely with personal credentials | **M** | Fundamental for authentication and data protection. |
| R12 | Admins can post or update internship opportunities | **M** | Core requirement for maintaining internship listings. |
| R13 | Students can rate internship experiences (optional) | **S** | Future enhancement; not needed for current release. |
| R14 | System sends automatic confirmation messages on form submission | **N** | Improves communication but not mission-critical. |
| R15 | Website supports multiple languages (future update) | **S** | Planned future feature once the main system is stable. |

---

### 4.3 Summary
- **Mandatory (M):** 9 requirements — the foundation of the UniVerse MVP version.  
- **Nice to Have (N):** 3 requirements — recommended for version 2 updates.  
- **Superfluous (S):** 2 requirements — postponed to later stages.

The prioritization ensures that the development team focuses first on **core system functionality** (student-admin interactions and internship management) before adding secondary enhancements such as notifications, multilingual support, or ratings.

---



