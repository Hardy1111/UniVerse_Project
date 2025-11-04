# REQUIREMENTS VALIDATION

## Validation & Quality Assurance Lead

### Purpose
The purpose of this section is to ensure that all requirements for the **UniVerse** platform are valid, consistent, complete, and realistic.  
Validation confirms that the system design truly meets user needs, while Quality Assurance guarantees the accuracy and reliability of all requirement documents before development begins.

---

### Consistency Check
A consistency check was performed across all requirement documents, including the elicitation, classification, structured specifications, and prioritization tables.

**Findings:**
- No duplicated or contradictory requirements were found.  
- The same terminology is used across all roles (e.g., *Student*, *Admin*, *Internship*).  
- Functional and non-functional requirements align with the system’s Use Case diagram and structured specifications.  
- System workflows match what is described in the Use Case diagram.

✅ **Result:** All requirements are internally consistent and compatible for implementation.

---

### Completeness Check
The completeness check ensures that every critical system function has been captured and described properly.

**Findings:**
- All ten requirements (R1–R10) were covered and linked to corresponding system components.  
- The major functions — login, internship application, Company management, and dashboard — are fully represented.  
- Future improvements (Community, QR medical info, Gamify Study session) we would like to add if we ever expand our platform

- No essential feature or actor was omitted.

✅ **Result:** The requirements are complete and sufficient for developing the UniVerse MVP (Minimum Viable Product).

---

### Risks Identified

| ID | Risk Description | Impact | Mitigation Strategy |
|----|------------------|---------|----------------------|
| **RISK-1** | Integration errors or overwriting files when multiple members commit at the same time. | **High** | Before any commit or push, team members communicate through **Slack or WhatsApp** to confirm no one else is editing the same file. Everyone pulls the latest version first, tests their part locally, then commits with a clear message. |
| **RISK-2** | Delay in development due to team members’ limited experience with Flask or Tailwind. | **Medium** | Assign small learning tasks early, follow official documentation, and pair experienced members with beginners through code reviews. |
| **RISK-3** | Poor or confusing UI design may make navigation difficult for first-time users. | **Medium** | Conduct quick usability tests with students, gather feedback, and refine layouts before final submission. |

✅ **Result:** The main risks are technical compatibility, team skill limitations, and user-experience clarity — all manageable with early planning and GitHub-based collaboration.

---

### Validation Methods
The following validation methods will be applied to confirm requirement correctness and quality:

1. **Peer Reviews:**  
   Weekly internal review meetings will verify new or modified requirements for consistency and clarity.  

2. **Prototype Testing:**  
   Early testing of the working prototype with real students and an admin user will ensure that system behavior matches the documented requirements.    

3. **Requirement Traceability Matrix (RTM):**  
   Each requirement (R1–R10) will be mapped to its corresponding implementation task in the GitHub repository to track progress.

---



