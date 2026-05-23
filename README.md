# PhishingEmailDetectorUsingStreamlit

A simple rule-based cybersecurity tool that analyzes email content and detects potential phishing attempts by scanning suspicious keywords, malicious links, and risky patterns.

The project demonstrates basic cybersecurity principles such as phishing detection, text analysis, and risk scoring using Python and Streamlit in a lightweight interactive dashboard.

---

## Features Included

- Phishing keyword detection  
- Suspicious link detection  
- Risk score calculation  
- Safe / Suspicious / Phishing classification  
- Simple user-friendly interface  
- Real-time email analysis  
- Lightweight rule-based system (no ML required)

---

## Tech Stack

### Frontend / UI
- Streamlit

### Backend
- Python

### Security Concepts
- Rule-based detection
- URL pattern analysis
- Keyword-based filtering

---

## Tools & Platforms

- VS Code  
- Python  
- Streamlit  
- Git  
- GitHub  

---

## Project Structure

```bash
PhishingEmailDetector/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## How to Run Locally

### Step 1 — Clone Repository

```bash
git clone https://github.com/your-username/PhishingEmailDetector.git
```

---

### Step 2 — Open Project Folder

```bash
cd PhishingEmailDetector
```

---

### Step 3 — Install Python Packages

```bash
pip install streamlit
```

---

### Step 4 — Run Application

```bash
streamlit run app.py
```

---

### Step 5 — Open in Browser

```
http://localhost:8501
```

---

## Sample Test Inputs and Expected Outputs

### Test Case 1 — Phishing Email

**Input**
```
URGENT!

Your bank account has been suspended.

Click here immediately:
http://secure-check-demo.com

Verify your password now.
```

**Expected Output**
```
⚠️ Phishing Email Detected
Risk Score: High (50+)

Detected Keywords:
- urgent
- bank
- password
- click here
```

---

### Test Case 2 — Suspicious Email

**Input**
```
Dear user,

Please verify your account details to continue using our service.

Click here:
http://verify-account-test.com
```

**Expected Output**
```
⚠️ Suspicious Email
Risk Score: Medium (20–49)

Detected Keywords:
- verify
- account
```

---

### Test Case 3 — Safe Email

**Input**
```
Hello,

Your meeting is scheduled for tomorrow at 10 AM.

Regards,
Admin Team
```

**Expected Output**
```
✅ Safe Email
Risk Score: Low (0–19)
```

---

## Important Note

This project is based on rule-based detection only.

It uses:
- Keyword matching
- URL detection
- Simple scoring logic

No machine learning is used.

---

## Technologies Used

- Python
- Streamlit
- Regular Expressions
- Cybersecurity Basics
- Git & GitHub

---

## Ethical Usage Notice

This tool is for educational purposes only. It does not access real email systems or perform any network activity.
---
