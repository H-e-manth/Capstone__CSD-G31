# Agent-Employer Connect Platform

## Overview

The **Agent-Employer Connect Platform** is designed to streamline the hiring process by connecting potential agents with employers. The platform facilitates job applications, resume evaluations, and interactive communication between agents and employers. By providing a seamless hiring experience, this platform aims to simplify recruitment while ensuring both agents and employers find the best matches.

## Features

- **Agent Profile Management**: Agents can create and manage detailed profiles, including experience, skills, and availability.
- **Employer Job Listings**: Employers can post jobs, specify requirements, and receive applications.
- **Smart ATS Integration**: The platform uses an AI-powered Applicant Tracking System (ATS) to evaluate resumes against job descriptions.
- **Interactive PDF Resume Evaluation**: The platform can evaluate resumes uploaded in PDF format, offering tailored feedback.
- **Job Matching and Recommendations**: Based on agents' profiles, the platform recommends suitable jobs and employers.
- **Agent-Employer Communication**: Secure, real-time messaging allows agents and employers to communicate directly.
- **FAISS Integration**: Fast, similarity-based resume searches using FAISS vector search engine to find the most relevant resumes.

## Technologies Used

- **Backend**: Python (Flask/Django), LangChain, FAISS, Google Generative AI
- **Frontend**: Streamlit for dynamic user interaction
- **Database**: PostgreSQL/MySQL for user data and job listings
- **Cloud Storage**: AWS S3 for storing resumes and related documents
- **Embeddings**: Google Generative AI Embeddings
- **AI Model**: Google Gemini Pro for natural language understanding and question answering
- **PDF Processing**: PyPDF2 for extracting text from resumes
- **Vector Store**: FAISS for fast, similarity-based searches

## Software Requirements

- **Python 3.8+**
- **Streamlit**
- **Flask/Django**
- **LangChain**
- **PyPDF2**
- **FAISS**
- **Google Generative AI SDK**
- **PostgreSQL/MySQL**
- **Docker (for deployment)**

## Hardware Requirements

The platform is scalable and can be deployed on any cloud service provider (AWS, GCP, Azure). However, for optimal performance, the following hardware specifications are recommended:

- **Development**:
  - CPU: 4-core processor
  - RAM: 8 GB
  - Storage: 50 GB

- **Production**:
  - CPU: 8-core processor
  - RAM: 16 GB or more
  - Storage: 200 GB SSD
  - Network: High bandwidth for real-time messaging and uploads

## Installation

### Prerequisites
- Install [Python 3.8+](https://www.python.org/downloads/)
- Set up [PostgreSQL](https://www.postgresql.org/download/) or [MySQL](https://dev.mysql.com/downloads/)
- Set up your preferred cloud provider (AWS/GCP/Azure) for hosting and storage.
- Set up Docker (for deployment) if needed.

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/agent-employer-connect-platform.git
   cd agent-employer-connect-platform
