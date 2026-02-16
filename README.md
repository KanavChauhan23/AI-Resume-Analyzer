# 📄 ResumeGenius AI

<div align="center">

![ResumeGenius AI Banner](https://img.shields.io/badge/ResumeGenius-AI%20Powered-blueviolet?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.39+-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Beat the ATS, Impress the Recruiter**

[Live Demo](https://resumegenius-ai.streamlit.app/) • [Report Bug](https://github.com/KanavChauhan23/resume-genius-ai/issues) • [Request Feature](https://github.com/KanavChauhan23/resume-genius-ai/issues)

*Get instant ATS scores and professional feedback on your resume*

</div>

---

## 🌟 Overview

**ResumeGenius AI** is an intelligent resume analysis tool that helps job seekers optimize their resumes for both Applicant Tracking Systems (ATS) and human recruiters. Using advanced AI and machine learning, it provides actionable feedback to improve your chances of landing interviews.

### Why ResumeGenius AI?

- 🎯 **ATS Optimization** - See exactly how your resume scores against ATS algorithms
- 🤖 **AI-Powered Analysis** - Get detailed feedback from advanced LLM (Llama 3.3 70B)
- 📊 **Dual Scoring System** - Both similarity matching and comprehensive evaluation
- 💡 **Actionable Insights** - Specific suggestions, not generic advice
- ⚡ **Instant Results** - Complete analysis in under 30 seconds
- 🆓 **100% Free** - No hidden costs, unlimited use

---

## ✨ Features

### 📤 Easy Upload
- **PDF Resume Upload** - Simply drag and drop your resume
- **Job Description Input** - Paste the job posting you're targeting
- **Instant Processing** - Results in seconds

### 📊 Comprehensive Scoring

**ATS Similarity Score (0-100%)**
- Measures keyword alignment with job description
- Uses state-of-the-art BERT embeddings
- Shows how ATS systems will rate your resume

**AI Evaluation Score (0-100%)**
- Detailed analysis across multiple criteria
- Skills match assessment
- Experience alignment check
- Education & certification review
- Overall presentation feedback

### 🎯 Detailed Analysis

- **✅ Strengths** - What's working well in your resume
- **❌ Weaknesses** - Areas that need improvement
- **⚠️ Unclear Areas** - Sections that could be more specific
- **💡 Actionable Suggestions** - Specific steps to improve

### 📥 Downloadable Reports
- Save your analysis for later reference
- Share with career coaches or friends
- Track improvements over time

---

## 🚀 Live Demo

**Try it now:** [link](https://resumegenius-ai.streamlit.app/)

### Sample Workflow
1. Upload your resume (PDF)
2. Paste the job description
3. Get instant scores and feedback
4. Download the report
5. Improve and reanalyze!

---

## 🛠️ Tech Stack

### Core Technologies
- **Frontend Framework:** [Streamlit](https://streamlit.io/) - Fast, beautiful web apps
- **AI Model:** [Groq](https://groq.com/) (Llama 3.3 70B) - Advanced language model
- **ATS Analysis:** Sentence Transformers (BERT) - Semantic similarity
- **PDF Processing:** pdfminer.six - Text extraction
- **Language:** Python 3.9+

### Key Libraries
- `streamlit` - Web application framework
- `groq` - AI inference API
- `sentence-transformers` - Embedding generation
- `scikit-learn` - Similarity calculations
- `pdfminer.six` - PDF text extraction

---

## 💻 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Groq API key ([Get free key](https://console.groq.com/))

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/KanavChauhan23/resume-genius-ai.git
   cd resume-genius-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Streamlit secrets**
   
   Create `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "your-groq-api-key-here"
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   ```
   Navigate to http://localhost:8501
   ```

---

## 📁 Project Structure

```
resume-genius-ai/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
│
├── .streamlit/
│   └── secrets.toml      # API keys (local only)
│
└── screenshots/          # App screenshots
    ├── home.png
    ├── analysis.png
    └── results.png
```

---

## 🎯 Use Cases

### For Job Seekers
- **Optimize resumes** for specific job applications
- **Understand ATS systems** and how they filter resumes
- **Get professional feedback** without hiring a consultant
- **Track improvements** over multiple iterations

### For Career Coaches
- **Efficient resume review** tool for clients
- **Data-backed recommendations** instead of subjective opinions
- **Before/after comparison** to show improvement
- **Scalable consulting** - analyze more resumes faster

### For Recruiters
- **Understand candidate quality** before manual review
- **Identify strong matches** quickly
- **Provide feedback** to unsuccessful applicants

---

## 🔑 Key Differentiators

| Feature | ResumeGenius AI | Traditional Resume Services |
|---------|----------------|----------------------------|
| **Speed** | < 30 seconds | Days to weeks |
| **Cost** | Free | $50 - $500+ |
| **ATS Analysis** | ✅ Included | Rarely provided |
| **AI Feedback** | ✅ Detailed | Human-only |
| **Unlimited Use** | ✅ Yes | Pay per review |
| **Job-Specific** | ✅ Custom analysis | Generic advice |

---

## 📊 How It Works

### 1. Text Extraction
Uses `pdfminer.six` to extract clean text from resume PDFs

### 2. Similarity Analysis
- Converts resume and job description to vector embeddings
- Uses BERT-based sentence transformers
- Calculates cosine similarity (0-100%)

### 3. AI Evaluation
- Sends resume + job description to Llama 3.3 70B via Groq
- Structured analysis across multiple criteria
- Scores each criterion out of 5
- Generates actionable improvement suggestions

### 4. Results Display
- Beautiful score visualizations
- Color-coded feedback (✅ ❌ ⚠️)
- Downloadable comprehensive report

---

## 🤝 Contributing

Contributions welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- Multi-language support (Spanish, French, etc.)
- Resume format templates
- LinkedIn profile optimization
- Cover letter analysis
- Industry-specific analysis
- Batch processing for multiple resumes

---

## 📝 Roadmap

- [x] Core ATS scoring functionality
- [x] AI-powered detailed analysis
- [x] PDF resume support
- [x] Downloadable reports
- [ ] DOCX resume support
- [ ] Cover letter analysis
- [ ] LinkedIn profile optimization
- [ ] Resume templates library
- [ ] Multi-language support
- [ ] User accounts to save history
- [ ] Batch processing

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Kanav Chauhan**

- GitHub: [@KanavChauhan23](https://github.com/KanavChauhan23)
- LinkedIn: [Kanav Chauhan](https://linkedin.com/in/kanavchauhan23)

---

## 🙏 Acknowledgments

- **Groq** for fast AI inference
- **Sentence Transformers** for semantic analysis
- **Streamlit** for the amazing framework
- The open-source community

---

## 💡 Pro Tips for Users

### Getting the Best Results

1. **Use a clean PDF** - Ensure text is selectable, not scanned images
2. **Complete job description** - Paste the entire posting for accurate analysis
3. **Update for each application** - Customize your resume per job
4. **Implement suggestions** - Act on the specific feedback provided
5. **Reanalyze after changes** - Track your improvement score

### Common ATS Mistakes to Avoid

- ❌ Using tables or complex formatting
- ❌ Missing keywords from job description
- ❌ Using images or graphics for text
- ❌ Inconsistent date formatting
- ❌ Spelling/grammar errors

---

<div align="center">

**Made with ❤️ by Kanav Chauhan**

If you found this helpful, please give it a ⭐!

[⬆ Back to Top](#-resumegenius-ai)

</div>

