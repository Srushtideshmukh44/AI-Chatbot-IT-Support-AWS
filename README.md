# AI Chatbot for IT Support on AWS

## 📌 Project Overview
This project is an AI-based IT Support Chatbot built using AWS serverless services.
The chatbot helps users troubleshoot common IT issues such as server downtime,
VPN problems, disk space issues, and password reset queries.
The solution is fully serverless, scalable, and cost-effective.

---

## 🏗️ Project Architecture
User  
→ Frontend (HTML, JavaScript hosted on S3)  
→ Amazon API Gateway (REST API)  
→ AWS Lambda (Backend logic)  
→ Response to User  

---

## ☁️ AWS Services Used
- **AWS Lambda** – Backend logic for chatbot responses  
- **Amazon API Gateway** – Exposes Lambda as REST API  
- **Amazon S3** – Hosts frontend as static website  
- **AWS IAM** – Manages permissions for Lambda  
- **Amazon CloudWatch** – Logs and monitoring  

---

## ⚙️ Features
- AI-style IT support chatbot
- Handles common IT issues automatically
- Serverless architecture (no EC2 required)
- CORS-enabled API for browser access
- Frontend hosted on S3 static website
- Fully documented with screenshots

---

## 🧪 Sample Queries
- Server is down  
- VPN is not working  
- Disk space full  
- Password reset issue  

---

## 🛠️ Step-by-Step Implementation

### Step 1: Project Planning
- Defined chatbot purpose (IT support automation)
- Identified common IT issues to handle
- Designed basic serverless architecture

---

### Step 2: IAM Role Creation
- Created IAM role for AWS Lambda
- Attached `AWSLambdaBasicExecutionRole` policy
- Enabled CloudWatch logging

---

### Step 3: AWS Lambda Function
- Created Lambda function using Python runtime
- Implemented IT support logic using conditional statements
- Added CORS and OPTIONS handling for browser requests

---

### Step 4: API Gateway Setup
- Created REST API
- Added `/chat` resource with POST method
- Enabled Lambda Proxy Integration
- Deployed API to `prod` stage

---

### Step 5: API Testing
- Tested API Gateway POST method
- Verified successful responses (HTTP 200)
- Confirmed Lambda integration

---

### Step 6: Frontend Development
- Built simple chat UI using HTML and JavaScript
- Integrated frontend with API Gateway endpoint
- Tested chatbot locally using localhost server

---

### Step 7: CORS Debugging
- Resolved CORS issues caused by browser restrictions
- Ensured Lambda returned correct headers
- Verified frontend-backend communication

---

### Step 8: Hosting Frontend on S3
- Created S3 bucket
- Enabled static website hosting
- Uploaded frontend files
- Configured bucket policy for public access

---

## 📸 Screenshots
All implementation steps are documented with screenshots:
- IAM Role creation
- Lambda function code
- API Gateway testing
- Frontend chatbot working
- S3 static website hosting

---

## 🌐 Live Demo
Frontend is hosted on Amazon S3 as a static website and connected to AWS API Gateway.

---

## 🧠 Learning Outcomes
- Hands-on experience with AWS Lambda and API Gateway
- Understanding of serverless architecture
- Debugging real-world CORS issues
- Building and deploying a full-stack cloud project
- Project documentation and GitHub version control

---

## 👩‍💻 Author
**Srushti Deshmukh**  
AWS & DevOps Learner  
