import streamlit as st
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq
import re

# Page config
st.set_page_config(
    page_title="ResumeGenius AI - ATS Score Analyzer", 
    layout="wide", 
    page_icon="📄"
)

# Custom CSS for professional look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    .tagline {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .score-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .score-number {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
    }
    
    .score-label {
        font-size: 1rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
        padding: 0.8rem;
        border: none;
        border-radius: 12px;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Initialize Groq client
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("⚠️ GROQ_API_KEY not found in Streamlit Secrets!")
    st.info("Please add your Groq API key in Settings → Secrets")
    st.stop()

# Session States
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False
if "resume" not in st.session_state:
    st.session_state.resume = ""
if "job_desc" not in st.session_state:
    st.session_state.job_desc = ""

# Header
st.markdown('<h1 class="main-header">📄 ResumeGenius AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="tagline">Get Your ATS Score & Professional Feedback Instantly</p>', unsafe_allow_html=True)
st.markdown("---")

# Functions
@st.cache_resource
def load_model():
    """Load the sentence transformer model (cached)"""
    return SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def extract_pdf_text(uploaded_file):
    """Extract text from PDF file"""
    try:
        extracted_text = extract_text(uploaded_file)
        if not extracted_text.strip():
            return None
        return extracted_text
    except Exception as e:
        st.error(f"Error extracting text: {str(e)}")
        return None

def calculate_similarity_bert(text1, text2):
    """Calculate similarity between resume and job description"""
    try:
        model = load_model()
        embeddings1 = model.encode([text1])
        embeddings2 = model.encode([text2])
        similarity = cosine_similarity(embeddings1, embeddings2)[0][0]
        return round(similarity * 100, 1)  # Convert to percentage
    except Exception as e:
        st.error(f"Error calculating similarity: {str(e)}")
        return 0

def get_report(resume, job_desc):
    """Get AI analysis report from Groq"""
    prompt = f"""
You are ResumeGenius AI, an expert ATS and resume consultant. Analyze the candidate's resume against the job description.

# Instructions:
1. Evaluate the resume on key criteria from the job description
2. For each criterion, provide:
   - Score out of 5 (format: X/5)
   - ✅ if aligned, ❌ if missing, ⚠️ if unclear
   - Detailed explanation

3. Structure your response with these sections:
   - **Skills Match**
   - **Experience Alignment**
   - **Education & Certifications**
   - **Keywords & ATS Optimization**
   - **Overall Presentation**

4. End with "## 💡 Suggestions to Improve Your Resume:" section with actionable tips

# Inputs:
**Resume:**
{resume[:3000]}

**Job Description:**
{job_desc[:1500]}

# Output Format:
Use clear headers, scores at the start of each point, and provide specific, actionable feedback.
"""

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=2500
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating report: {str(e)}")
        return None

def extract_scores(text):
    """Extract numeric scores from report"""
    pattern = r'(\d+(?:\.\d+)?)/5'
    matches = re.findall(pattern, text)
    scores = [float(match) for match in matches]
    return scores

# Main App Logic
if not st.session_state.form_submitted:
    # Upload Form
    st.markdown("### 📤 Upload Your Resume")
    
    with st.form("upload_form"):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            resume_file = st.file_uploader(
                "Upload Resume (PDF only)",
                type="pdf",
                help="Upload your resume in PDF format"
            )
        
        with col2:
            st.markdown("**Resume Requirements:**")
            st.markdown("""
            - ✅ PDF format only
            - ✅ Clear, readable text
            - ✅ Up to date information
            - ✅ No password protection
            """)
        
        st.markdown("### 📋 Job Description")
        st.session_state.job_desc = st.text_area(
            "Paste the job description you're applying for:",
            placeholder="Paste the complete job description here including required skills, experience, qualifications...",
            height=200,
            help="Include the full job posting for best results"
        )
        
        submitted = st.form_submit_button("🚀 Analyze My Resume", type="primary")
        
        if submitted:
            if st.session_state.job_desc and resume_file:
                with st.spinner("📄 Extracting resume text..."):
                    st.session_state.resume = extract_pdf_text(resume_file)
                
                if st.session_state.resume:
                    st.session_state.form_submitted = True
                    st.rerun()
                else:
                    st.error("❌ Could not extract text from PDF. Please ensure it's a valid, readable PDF.")
            else:
                st.warning("⚠️ Please upload both resume and job description!")

# Results Display
if st.session_state.form_submitted:
    st.success("✅ Analysis Complete!")
    st.markdown("---")
    
    # Calculate Scores
    with st.spinner("🔍 Calculating ATS similarity score..."):
        ats_score = calculate_similarity_bert(
            st.session_state.resume, 
            st.session_state.job_desc
        )
    
    with st.spinner("🤖 Generating detailed AI analysis..."):
        report = get_report(
            st.session_state.resume, 
            st.session_state.job_desc
        )
    
    if report:
        # Extract scores from report
        report_scores = extract_scores(report)
        if report_scores:
            avg_score = (sum(report_scores) / len(report_scores)) * 20  # Convert to percentage
        else:
            avg_score = 0
        
        # Display Scores
        st.markdown("## 📊 Your Scores")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="score-box">
                <div class="score-label">ATS Similarity Score</div>
                <div class="score-number">{ats_score}%</div>
                <div class="score-label">Keyword Match with Job Description</div>
            </div>
            """, unsafe_allow_html=True)
            
            if ats_score >= 75:
                st.success("🎉 Excellent match! Your resume aligns well with the job.")
            elif ats_score >= 60:
                st.info("👍 Good match! Some improvements possible.")
            else:
                st.warning("⚠️ Needs improvement. Review suggestions below.")
        
        with col2:
            st.markdown(f"""
            <div class="score-box">
                <div class="score-label">AI Evaluation Score</div>
                <div class="score-number">{avg_score:.0f}%</div>
                <div class="score-label">Based on detailed analysis below</div>
            </div>
            """, unsafe_allow_html=True)
            
            if avg_score >= 80:
                st.success("🌟 Outstanding resume! Strong candidate profile.")
            elif avg_score >= 60:
                st.info("💪 Solid resume! Minor enhancements recommended.")
            else:
                st.warning("🔧 Significant improvements needed.")
        
        st.markdown("---")
        
        # Display Report
        st.markdown("## 📝 Detailed AI Analysis Report")
        st.markdown(report)
        
        # Download Button
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.download_button(
                label="📥 Download Full Report",
                data=report,
                file_name="resume_analysis_report.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        # Reset Button
        if st.button("🔄 Analyze Another Resume", use_container_width=True):
            st.session_state.form_submitted = False
            st.session_state.resume = ""
            st.session_state.job_desc = ""
            st.rerun()
    
    else:
        st.error("❌ Failed to generate analysis report. Please try again.")

# Sidebar
with st.sidebar:
    st.markdown("### 📄 About ResumeGenius AI")
    st.markdown("""
    **ResumeGenius AI** helps you optimize your resume for Applicant Tracking Systems (ATS) and get professional feedback.
    
    **What You Get:**
    - 📊 ATS similarity score
    - 🤖 AI-powered detailed analysis
    - ✅ Strengths identification
    - ⚠️ Weakness detection
    - 💡 Actionable improvement tips
    
    **100% FREE • Unlimited Use**
    """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 How It Works")
    st.markdown("""
    **1. Upload Resume**
    PDF format, clear text
    
    **2. Paste Job Description**
    Complete job posting
    
    **3. Get Analysis**
    - ATS score
    - AI evaluation
    - Suggestions
    
    **4. Improve & Apply!**
    Implement feedback
    """)
    
    st.markdown("---")
    
    st.markdown("### 💡 Pro Tips")
    st.markdown("""
    - Use keywords from job description
    - Quantify achievements
    - Keep format clean & ATS-friendly
    - Update for each application
    - Highlight relevant skills
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚙️ Powered By")
    st.markdown("""
    **AI Model**: Groq (Llama 3.3 70B)  
    **ATS Analysis**: BERT Embeddings  
    
    🟢 **Status**: Active
    """)

# Footer
st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.link_button(
        "🔗 Connect on LinkedIn",
        "https://linkedin.com/in/kanavchauhan23",
        use_container_width=True,
        type="primary"
    )

st.markdown("""
<div style='text-align: center; color: #666; margin-top: 1rem;'>
    <p style='font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;'>✨ Built with ❤️ by Kanav Chauhan ✨</p>
    
    <p style='font-size: 0.85rem; margin-top: 1rem; color: #999;'>
        <a href='https://github.com/KanavChauhan23/resume-genius-ai' target='_blank' style='color: #667eea; text-decoration: none; margin: 0 8px;'>📂 View Source Code</a> •
        <a href='https://github.com/KanavChauhan23' target='_blank' style='color: #667eea; text-decoration: none; margin: 0 8px;'>💻 GitHub Profile</a>
    </p>
    
    <p style='font-size: 0.9rem; margin-top: 1.5rem; color: #888;'>
        📄 ResumeGenius AI - Get Your Dream Job Faster
    </p>
    <p style='font-size: 0.8rem; color: #aaa; margin-top: 0.5rem;'>
        Beat the ATS, Impress the Recruiter
    </p>
</div>
""", unsafe_allow_html=True)
