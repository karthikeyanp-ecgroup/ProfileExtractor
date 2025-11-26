# AI Email-to-Sheet Resume Extractor

Automatically extract resume data from incoming emails using AI and write structured information into Google Sheets.
Perfect for IT hiring teams, HR mailboxes, job portals, and automated recruitment systems.

## 🚀 Goal
Create an automated workflow that:
1. Reads emails that contain resumes
2. Extracts attachments or links
3. Parses resume content using AI
4. Writes structured data into Google Sheets
5. (Optional) Sends notifications

## 🧩 System Architecture
<img width="512" height="768" alt="ProfileExtractor" src="https://github.com/user-attachments/assets/97162512-d146-4556-858c-816385d3a469" />

## 🔍 Detailed Components
### 1. Email Inbox
Resumes come to:
* careers@company.com
* HR shared mailboxes
* Job portal relay emails
* Internal referral mails
Format support:
* PDF
* DOCX
* Images (JPG/PNG → OCR)
* Resume URLs from portals

### 2. Email Fetcher / Trigger
Options:
* IMAP client (Python)
* Gmail API

### 3. File Processor / OCR
Tools:
* PyPDF2 or pdfplumber for PDFs
* python-docx for DOCX
* Tesseract for images

### 4. AI Resume Parser (LLM)
Input provided:
* Extracted resume text
* (Optional) Job description

LLM returns structured JSON:
```
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1 444 555 6666",
  "experience_years": 4.5,
  "skills": ["React", "Node.js", "AWS"],
  "last_company": "TechCorp",
  "education": "B.Tech CSE",
  "notice_period": "30 days"
}
```

### 5. Data Transformer
Maps JSON → Sheet Columns

| Field         | Output               |
| ------------- | -------------------- |
| Name          | Candidate name       |
| Email         | Extracted email      |
| Skills        | Combined list        |
| Experience    | Years of experience  |
| Last Company  | Most recent employer |
| Notice Period | Extracted or default |
| Resume Link   | Stored or uploaded   |

### 6. Google Sheets Writer
Opens Google Sheet
* Appends a new row per candidate
* (Optional) attaches Drive link to resume

### 7. Recruiter Notifications (Optional)
Send via:
* Slack
* Email
* Microsoft Teams
* Example:
  ```
  New resume processed: John Mathew – 4.8 yrs exp – React/Node.js – Match Score: 88%.
  ```

  ## 🚀 Enhancement Ideas (Bonus Features)
  ### ⭐ Resume Matching Score
Use an LLM to compare the candidate’s resume with the job description and generate a match score (0–100%) along with strengths and gaps.

### ⭐ Automatic Resume Upload to Google Drive
Upload all resumes to Google Drive and store the generated file URL in the Google Sheet for easy access.

### ⭐ Auto-Assign Candidates to Roles
Automatically classify candidates into roles (e.g., Frontend, Backend, Full Stack, DevOps) based on extracted skills and experience.

### ⭐ Duplicate Candidate Detection
Identify duplicates using:
* Same email
* Same phone number
* Similar name (fuzzy matching)
* Similar resume content (embedding similarity)

### ⭐ Simple Web UI for Recruiters

Add a small UI dashboard where HR can:
* View processed candidates in a clean table
* Search/filter by skills, experience, or match score
* View resume preview and Drive link
* Mark candidates as shortlisted/rejected
