import time
import streamlit as st
import openai
import PyPDF2 as pdf
import json

# Set OpenAI API Key directly in the code
openai.api_key = "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"

# Custom CSS for the background
def add_custom_css():
    st.markdown(
        """
        <style>
            /* Apply a two-tone background */
            .main {
                background: linear-gradient(180deg, #2196F3 50%, white 50%);
                color: white;
            }

            /* Style sidebar for consistency */
            [data-testid="stSidebar"] {
                background: white;
                color: #2196F3;
            }

            /* Style text areas, inputs, and other text */
            .stTextInput, .stTextArea, .stButton > button {
                color: #2196F3;
                background-color: white;
                border: 1px solid #2196F3;
                border-radius: 5px;
            }

            /* Ensure buttons align with theme */
            .stButton > button:hover {
                background-color: #1976D2;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Retry logic for quota errors
def get_openai_response(input):
    retries = 5
    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a skilled ATS (Application Tracking System)."},
                    {"role": "user", "content": input}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            if "rate limit" in str(e).lower() and attempt < retries - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
            else:
                st.error(f"Error: {e}")
                raise e

# Extract text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

# Input prompt template
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

# Add custom CSS
add_custom_css()

st.title("💼 Smart ATS Resume Evaluator")
st.write("Upload your resume and paste the job description to get personalized feedback.")

# Job description input
st.subheader("Job Description")
jd = st.text_area("Paste the Job Description here")

# File upload
st.subheader("Upload Your Resume (PDF Format)")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf")

# Submit button
if st.button("Evaluate My Resume"):
    if uploaded_file and jd.strip():
        with st.spinner('Analyzing your resume...'):
            try:
                text = input_pdf_text(uploaded_file)
                final_prompt = input_prompt.format(text=text, jd=jd)
                response = get_openai_response(final_prompt)
                st.subheader("Your Resume Evaluation")
                st.json(json.loads(response))
            except Exception as e:
                st.error(f"Error processing your request: {e}")
    else:
        st.error("Please provide both a job description and a PDF resume.")
