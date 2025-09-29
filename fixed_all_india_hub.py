import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Tuple
import time
import random

# Configure Streamlit page
st.set_page_config(
    page_title="All India Internship Hub - Fixed",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple CSS without complex animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .glassmorphism {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def init_session_state():
    """Initialize session state variables"""
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Dashboard'
    if 'run_matching' not in st.session_state:
        st.session_state.run_matching = False
    if 'run_allocation' not in st.session_state:
        st.session_state.run_allocation = False

def create_page_navigation():
    """Create page navigation"""
    st.markdown("""
    <div class="glassmorphism" style="text-align: center;">
        <h1 style="color: white; margin-bottom: 1rem;">🇮🇳 All India Internship Hub</h1>
        <p style="color: rgba(255,255,255,0.9);">AI-Powered Career Matching • 12+ Industries • 500+ Companies</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation tabs
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("📊 Dashboard", key="nav_dashboard"):
            st.session_state.current_page = 'Dashboard'
    with col2:
        if st.button("🔍 Find Matches", key="nav_matching"):
            st.session_state.current_page = 'Matching'
    with col3:
        if st.button("📈 Analytics", key="nav_analytics"):
            st.session_state.current_page = 'Analytics'
    with col4:
        if st.button("🏢 Companies", key="nav_companies"):
            st.session_state.current_page = 'Companies'
    with col5:
        if st.button("👤 My Journey", key="nav_profile"):
            st.session_state.current_page = 'Profile'

@st.cache_data
def load_sample_data():
    """Load sample internship data"""
    return [
        {
            "id": "tech_001",
            "title": "Software Developer Intern",
            "company": "Infosys Technologies",
            "industry": "Technology",
            "location": "Bangalore, Karnataka",
            "salary": 45000,
            "requirements": {"skills": ["Java", "Python", "React"], "minCgpa": 7.5},
            "companyRating": 4.2,
            "applicants": 15420
        },
        {
            "id": "health_001",
            "title": "Clinical Research Associate",
            "company": "Apollo Hospitals",
            "industry": "Healthcare",
            "location": "Chennai, Tamil Nadu",
            "salary": 35000,
            "requirements": {"skills": ["Clinical Research", "Medical Writing"], "minCgpa": 7.0},
            "companyRating": 4.4,
            "applicants": 3276
        },
        {
            "id": "fin_001",
            "title": "Investment Banking Analyst",
            "company": "HDFC Bank",
            "industry": "Finance",
            "location": "Mumbai, Maharashtra",
            "salary": 48000,
            "requirements": {"skills": ["Financial Analysis", "Excel"], "minCgpa": 8.0},
            "companyRating": 4.3,
            "applicants": 12567
        }
    ]

def dashboard_page():
    """Main dashboard with metrics and overview"""
    st.markdown("# 📊 All India Dashboard")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea;">50,000+</h3>
            <p>Active Internships</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea;">500+</h3>
            <p>Partner Companies</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea;">12+</h3>
            <p>Industries Covered</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea;">94.2%</h3>
            <p>Success Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Smart Allocation Button
    if st.button("🚀 Run All India Smart Allocation", type="primary", width="stretch"):
        with st.spinner("🚀 Running smart allocation..."):
            time.sleep(2)
        st.success("✅ Allocation completed successfully!")
        st.balloons()
        
        # Sample allocation results
        allocation_data = {
            "Student": ["Arjun Sharma", "Priya Patel", "Rajesh Kumar"],
            "Company": ["Infosys Technologies", "Apollo Hospitals", "HDFC Bank"],
            "Role": ["Software Developer", "Clinical Research", "Banking Analyst"],
            "Match Score": ["92.5%", "88.3%", "85.7%"]
        }
        
        df = pd.DataFrame(allocation_data)
        st.markdown("### 🎯 Allocation Results")
        st.dataframe(df, width="stretch")

def matching_page():
    """Find matches functionality"""
    st.markdown("# 🔍 Find My Perfect Match")
    
    # Simple profile input
    with st.sidebar:
        st.markdown("## 👤 Your Profile")
        name = st.text_input("Full Name", placeholder="Enter your name")
        skills = st.multiselect("Skills", ["Java", "Python", "React", "Clinical Research", "Financial Analysis"])
        cgpa = st.slider("CGPA", 0.0, 10.0, 7.5, 0.1)
        location = st.selectbox("Preferred Location", ["Bangalore", "Mumbai", "Chennai", "Delhi", "Remote"])
    
    if name and skills:
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎯 Find Perfect Matches", type="primary", width="stretch"):
                st.session_state.run_matching = True
        
        with col2:
            if st.button("🚀 Run Smart Allocation", type="secondary", width="stretch"):
                st.session_state.run_allocation = True
        
        if st.session_state.get("run_matching"):
            with st.spinner("🔍 Finding your matches..."):
                time.sleep(2)
            
            st.success("✅ Found 5 perfect matches!")
            
            # Sample matches
            internships = load_sample_data()
            
            for i, internship in enumerate(internships, 1):
                score = random.randint(75, 95)
                
                with st.expander(f"#{i} {internship['title']} at {internship['company']} - {score}% Match"):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.write(f"**Company:** {internship['company']}")
                        st.write(f"**Location:** {internship['location']}")
                        st.write(f"**Industry:** {internship['industry']}")
                        st.write(f"**Required Skills:** {', '.join(internship['requirements']['skills'])}")
                    
                    with col2:
                        st.markdown(f"""
                        <div style="background: #48bb78; color: white; padding: 1rem; border-radius: 10px; text-align: center;">
                            <h3>{score}%</h3>
                            <p>Excellent Match</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.write(f"**Salary:** ₹{internship['salary']:,}/month")
                        
                        if st.button(f"Apply Now", key=f"apply_{internship['id']}", width="stretch"):
                            st.success("Application submitted!")
    else:
        st.info("👈 Please fill in your profile details to start matching!")

def analytics_page():
    """Analytics dashboard"""
    st.markdown("# 📈 Analytics Dashboard")
    
    if st.button("🚀 Generate Analytics", type="primary", width="stretch"):
        with st.spinner("📊 Generating analytics..."):
            time.sleep(2)
        st.success("✅ Analytics generated!")
    
    # Sample analytics
    col1, col2 = st.columns(2)
    
    with col1:
        # Industry distribution
        fig1 = go.Figure(data=[
            go.Pie(labels=['Technology', 'Healthcare', 'Finance', 'Manufacturing'], 
                   values=[40, 25, 20, 15])
        ])
        fig1.update_layout(title="Industry Distribution", height=400)
        st.plotly_chart(fig1, width="stretch")
    
    with col2:
        # Salary trends
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=['Tech', 'Healthcare', 'Finance'], y=[45000, 35000, 48000]))
        fig2.update_layout(title="Average Salaries by Industry", height=400)
        st.plotly_chart(fig2, width="stretch")

def companies_page():
    """Companies directory"""
    st.markdown("# 🏢 Partner Companies")
    
    companies = [
        {"name": "Infosys Technologies", "industry": "Technology", "rating": 4.2, "openings": 500},
        {"name": "Apollo Hospitals", "industry": "Healthcare", "rating": 4.4, "openings": 150},
        {"name": "HDFC Bank", "industry": "Finance", "rating": 4.3, "openings": 200}
    ]
    
    for company in companies:
        st.markdown(f"""
        <div class="glassmorphism">
            <h3 style="color: white;">{company['name']}</h3>
            <p style="color: rgba(255,255,255,0.9);">Industry: {company['industry']}</p>
            <p style="color: rgba(255,255,255,0.9);">Rating: ⭐ {company['rating']}/5.0</p>
            <p style="color: rgba(255,255,255,0.9);">Open Positions: {company['openings']}</p>
        </div>
        """, unsafe_allow_html=True)

def profile_page():
    """User profile and journey"""
    st.markdown("# 👤 My Journey")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Applications", "24", "+8")
    with col2:
        st.metric("Interviews", "12", "+5")
    with col3:
        st.metric("Offers", "6", "+3")
    with col4:
        st.metric("Profile Score", "92%", "⭐")
    
    # Journey timeline
    journey_data = {
        "Date": ["2024-03-01", "2024-03-05", "2024-03-10"],
        "Activity": ["Profile Created", "Applied to Infosys", "Offer Received"],
        "Status": ["✅ Completed", "✅ Submitted", "🎉 Received"],
        "Company": ["Platform", "Infosys", "HDFC Bank"]
    }
    
    df = pd.DataFrame(journey_data)
    st.dataframe(df, width="stretch")

def main():
    """Main application entry point"""
    init_session_state()
    
    # Page navigation
    create_page_navigation()
    
    # Route to pages
    if st.session_state.current_page == 'Dashboard':
        dashboard_page()
    elif st.session_state.current_page == 'Matching':
        matching_page()
    elif st.session_state.current_page == 'Analytics':
        analytics_page()
    elif st.session_state.current_page == 'Companies':
        companies_page()
    elif st.session_state.current_page == 'Profile':
        profile_page()

if __name__ == "__main__":
    main()