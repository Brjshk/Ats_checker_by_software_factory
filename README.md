# ATS Checker Application

## Overview
The ATS Checker Application is a web-based tool that allows users to upload a resume and a job description. The application analyzes the resume against the job description to determine how well it matches based on keywords, skills, and other relevant criteria.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ats_checker
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend:
   ```bash
   uvicorn backend.main:app --reload
   ```
4. Open `frontend/index.html` in your browser to access the application.

## Run Instructions
- Use the application to register, log in, upload resumes and job descriptions, and analyze them.