import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure Generative AI with the API key
genai.configure(api_key=os.getenv("AIzaSyBV-DVYwAJA8SQ3WHjDiSO29C_pMmeVQ-o"))

# Function to get the response from Google's Generative AI model
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from an uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

# Define the input prompt template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analysis, 
and big data engineering. Your task is to evaluate the resume based on the given job description. 
You must consider that the job market is very competitive, and you should provide 
the best assistance for improving the resume. Assign the percentage Matching based 
on the JD and the missing keywords with high accuracy.

Resume: {text}
Description: {jd}

I want the response in one single string with the structure:
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
"""

# Streamlit app starts here
st.set_page_config(page_title="Smart ATS", layout="centered")

# Title and description
st.title("💼 Smart ATS Resume Evaluator")
st.write("""
    Upload your resume and paste the job description to get personalized feedback 
    on how well your resume matches the job posting and how to improve it.
""")

# Job Description Input Section
st.subheader("Job Description")
jd = st.text_area(
    "Paste the Job Description here", 
    help="Enter the job description you want your resume to be evaluated against."
)

# File Uploader for Resume
st.subheader("Upload Your Resume (PDF Format)")
uploaded_file = st.file_uploader(
    "Upload Your Resume", type="pdf", 
    help="Please upload your resume in PDF format for evaluation."


)

# Submit button with proper validation and response handling
if st.button("Evaluate My Resume"):
    if uploaded_file is not None and jd.strip():
        with st.spinner('Analyzing your resume...'):
            text = input_pdf_text(uploaded_file)
            # Prepare the final prompt to be sent to the model
            final_prompt = input_prompt.format(text=text, jd=jd)
            # Get the model's response
            response = get_gemini_response(final_prompt)
        
        # Displaying the result
        st.subheader("Your Resume Evaluation")
        st.json(response)
    else:
        st.error("Please provide both a job description and a PDF resume for evaluation.")

# Footer
st.write("---")
st.markdown("Developed by [Hemanth](https://www.linkedin.com/in/g-hemanth-kumar-442767278/)")






