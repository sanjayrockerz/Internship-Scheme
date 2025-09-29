import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, date, timedelta
import json
import numpy as np
from typing import Dict, List, Tuple, Any
import time
import random

# Configure Streamlit page
st.set_page_config(
    page_title="All India Internship Hub",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced World-Class CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .main > div {
        padding-top: 0rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 25%, #667eea 50%, #764ba2 75%, #f093fb 100%);
        font-family: 'Inter', sans-serif;
        animation: gradientShift 10s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 25%, #667eea 50%, #764ba2 75%, #f093fb 100%); }
        50% { background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%); }
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 25px;
        padding: 2.5rem;
        margin: 1rem;
        backdrop-filter: blur(20px);
        box-shadow: 0 25px 45px rgba(31, 38, 135, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        pointer-events: none;
    }
    
    .hero-header {
        background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 25%, #45b7d1 50%, #96ceb4 75%, #feca57 100%);
        padding: 4rem 3rem;
        border-radius: 30px;
        color: white;
        text-align: center;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        animation: heroGlow 8s ease-in-out infinite;
    }
    
    @keyframes heroGlow {
        0%, 100% { box-shadow: 0 20px 40px rgba(255, 107, 107, 0.3); }
        25% { box-shadow: 0 20px 40px rgba(78, 205, 196, 0.3); }
        50% { box-shadow: 0 20px 40px rgba(69, 183, 209, 0.3); }
        75% { box-shadow: 0 20px 40px rgba(150, 206, 180, 0.3); }
    }
    
    .hero-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: shine 3s linear infinite;
    }
    
    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
    }
    
    .page-nav {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .nav-button {
        display: inline-block;
        padding: 15px 30px;
        margin: 8px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 30px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        position: relative;
        overflow: hidden;
        font-size: 14px;
        letter-spacing: 0.5px;
    }
    
    .nav-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .nav-button:hover::before {
        left: 100%;
    }
    
    .nav-button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.5);
    }
    
    .nav-button.active {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 35px rgba(255, 107, 107, 0.5);
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        border: 2px solid rgba(255, 255, 255, 0.3);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.25);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 800;
        color: #2d3748;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .metric-label {
        font-size: 1rem;
        color: #718096;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .industry-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        border-left: 6px solid #667eea;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .industry-card:hover {
        transform: translateX(10px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
        border-left-color: #ff6b6b;
    }
    
    .skill-category {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 12px 24px;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1rem;
        margin: 5px;
        display: inline-block;
        box-shadow: 0 5px 15px rgba(240, 147, 251, 0.4);
        transition: all 0.3s ease;
    }
    
    .skill-category:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(240, 147, 251, 0.6);
    }
    
    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        font-size: 0.9rem;
        margin: 5px;
        font-weight: 500;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    .skill-tag:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.5);
    }
    
    .skill-matched {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        box-shadow: 0 5px 15px rgba(72, 187, 120, 0.4);
    }
    
    .skill-missing {
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
        box-shadow: 0 5px 15px rgba(245, 101, 101, 0.4);
    }
    
    .glassmorphism {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        border: 2px solid rgba(255, 255, 255, 0.2);
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
    }
    
    .chart-container {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        margin: 1.5rem 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .chart-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2.5rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border-top: 5px solid #667eea;
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.8s;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
        border-top-color: #ff6b6b;
    }
    
    .feature-icon {
        font-size: 4rem;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .pulse-animation {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.05); }
    }
    
    .gradient-text {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }
    
    .floating-particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .particle {
        position: absolute;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    .stProgress > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        height: 10px;
        border-radius: 5px;
    }
    
    .india-flag {
        background: linear-gradient(to bottom, #ff9933 33%, #ffffff 33%, #ffffff 66%, #138808 66%);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: bold;
        color: #2d3748;
    }
    
    .regional-highlight {
        background: linear-gradient(135deg, rgba(255, 153, 51, 0.1) 0%, rgba(19, 136, 8, 0.1) 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 2px solid rgba(255, 153, 51, 0.3);
    }
</style>
""", unsafe_allow_html=True)

def init_session_state():
    """Initialize session state variables"""
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Dashboard'
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {}
    if 'matches' not in st.session_state:
        st.session_state.matches = []

def create_floating_particles():
    """Create floating particle effect"""
    particles_html = """
    <div class="floating-particles">
    """
    
    for i in range(20):
        size = random.randint(4, 12)
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        delay = random.uniform(0, 6)
        particles_html += f"""
        <div class="particle" style="
            width: {size}px; 
            height: {size}px; 
            left: {x}%; 
            top: {y}%; 
            animation-delay: {delay}s;
        "></div>
        """
    
    particles_html += "</div>"
    return particles_html

def create_page_navigation():
    """Create beautiful page navigation"""
    pages = {
        '🏠 Dashboard': 'Dashboard',
        '🔍 Find My Match': 'Matching',
        '📊 Analytics Hub': 'Analytics',
        '🏢 Companies': 'Companies',
        '🎯 My Journey': 'Profile'
    }
    
    st.markdown('<div class="page-nav">', unsafe_allow_html=True)
    
    cols = st.columns(len(pages))
    for idx, (display_name, page_key) in enumerate(pages.items()):
        with cols[idx]:
            if st.button(display_name, key=f"nav_{page_key}"):
                st.session_state.current_page = page_key
    
    st.markdown('</div>', unsafe_allow_html=True)

def create_hero_section():
    """Create stunning hero section for All India"""
    st.markdown("""
    <div class="hero-header">
        <div class="hero-content">
            <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1rem;">
                🇮🇳 All India Internship Hub
            </h1>
            <p style="font-size: 1.4rem; opacity: 0.95; margin-bottom: 1rem;">
                Connecting Every Talent Across Every Industry • From Kashmir to Kanyakumari
            </p>
            <p style="font-size: 1.1rem; opacity: 0.85;">
                Technology • Healthcare • Finance • Manufacturing • Agriculture • Education • More
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_metric_cards(metrics):
    """Create beautiful metric cards"""
    cols = st.columns(len(metrics))
    
    for idx, (label, value, icon) in enumerate(metrics):
        with cols[idx]:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 3rem; margin-bottom: 1rem; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">{icon}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

# Comprehensive All India Internships Database
@st.cache_data
def load_all_india_internships():
    """Load comprehensive All India internship database across all industries"""
    return [
        # Technology & Software
        {
            "id": "tech-001",
            "title": "Software Development Intern",
            "company": "Infosys Technologies",
            "location": "Bangalore, Karnataka",
            "domain": "Information Technology",
            "industry": "Technology",
            "type": "Full-time Internship",
            "duration": "6 months",
            "salary": 25000,
            "requirements": {
                "skills": ["Java", "Python", "SQL", "JavaScript", "Git"],
                "minCgpa": 7.0,
                "experience": "Fresher",
                "education": "B.Tech/B.E./BCA/MCA"
            },
            "description": "Work on enterprise software solutions serving clients across India and globally.",
            "benefits": ["Training Program", "Health Insurance", "Transport", "Cafeteria", "Certification"],
            "isRemote": False,
            "companyRating": 4.2,
            "applicants": 5000,
            "tags": ["Software", "Enterprise", "Training", "Global Exposure"]
        },
        
        # Healthcare & Pharmaceuticals
        {
            "id": "health-001",
            "title": "Clinical Research Intern",
            "company": "Apollo Hospitals",
            "location": "Chennai, Tamil Nadu",
            "domain": "Healthcare",
            "industry": "Healthcare",
            "type": "Research Internship",
            "duration": "4 months",
            "salary": 18000,
            "requirements": {
                "skills": ["Clinical Research", "Data Analysis", "Medical Writing", "Statistics", "Excel"],
                "minCgpa": 7.5,
                "experience": "Fresher",
                "education": "B.Pharm/M.Pharm/MBBS/Life Sciences"
            },
            "description": "Contribute to groundbreaking medical research improving healthcare outcomes across India.",
            "benefits": ["Medical Coverage", "Research Publications", "Industry Exposure", "Mentorship"],
            "isRemote": False,
            "companyRating": 4.4,
            "applicants": 1200,
            "tags": ["Research", "Healthcare", "Publications", "Impact"]
        },
        
        # Finance & Banking
        {
            "id": "fin-001",
            "title": "Financial Analyst Intern",
            "company": "HDFC Bank",
            "location": "Mumbai, Maharashtra",
            "domain": "Finance & Banking",
            "industry": "Banking",
            "type": "Corporate Internship",
            "duration": "5 months",
            "salary": 28000,
            "requirements": {
                "skills": ["Financial Modeling", "Excel", "PowerPoint", "SQL", "Tableau"],
                "minCgpa": 8.0,
                "experience": "Fresher",
                "education": "B.Com/BBA/MBA/CA"
            },
            "description": "Analyze financial data and support decision-making for India's leading private bank.",
            "benefits": ["Performance Bonus", "Banking Industry Exposure", "Professional Network", "Training"],
            "isRemote": False,
            "companyRating": 4.3,
            "applicants": 3500,
            "tags": ["Finance", "Banking", "Analytics", "Corporate"]
        },
        
        # Manufacturing & Engineering
        {
            "id": "mfg-001",
            "title": "Production Engineering Intern",
            "company": "Tata Motors",
            "location": "Pune, Maharashtra",
            "domain": "Manufacturing",
            "industry": "Automotive",
            "type": "Industrial Internship",
            "duration": "6 months",
            "salary": 22000,
            "requirements": {
                "skills": ["Mechanical Engineering", "CAD", "Lean Manufacturing", "Quality Control", "AutoCAD"],
                "minCgpa": 7.2,
                "experience": "Fresher",
                "education": "B.Tech Mechanical/Production/Automobile"
            },
            "description": "Work on India's indigenous automotive manufacturing processes and innovation.",
            "benefits": ["Industrial Training", "Safety Certification", "Employee Discounts", "Transport"],
            "isRemote": False,
            "companyRating": 4.1,
            "applicants": 2800,
            "tags": ["Manufacturing", "Automotive", "Innovation", "Make in India"]
        },
        
        # Agriculture & Food Technology
        {
            "id": "agri-001",
            "title": "Agricultural Technology Intern",
            "company": "ITC Limited",
            "location": "Hyderabad, Telangana",
            "domain": "Agriculture Technology",
            "industry": "Agriculture",
            "type": "Field Internship",
            "duration": "4 months",
            "salary": 16000,
            "requirements": {
                "skills": ["Agriculture", "Data Analysis", "IoT", "Sustainable Farming", "Excel"],
                "minCgpa": 6.8,
                "experience": "Fresher",
                "education": "B.Sc Agriculture/B.Tech Food Technology"
            },
            "description": "Revolutionize Indian agriculture through technology and sustainable practices.",
            "benefits": ["Rural Exposure", "Sustainability Training", "Field Experience", "Transport"],
            "isRemote": False,
            "companyRating": 4.0,
            "applicants": 800,
            "tags": ["Agriculture", "Sustainability", "Rural", "Innovation"]
        },
        
        # Education & EdTech
        {
            "id": "edu-001",
            "title": "Educational Content Developer",
            "company": "BYJU'S",
            "location": "Bangalore, Karnataka",
            "domain": "Education Technology",
            "industry": "Education",
            "type": "Content Internship",
            "duration": "5 months",
            "salary": 24000,
            "requirements": {
                "skills": ["Content Writing", "Educational Design", "Video Editing", "Curriculum Development", "Hindi/English"],
                "minCgpa": 7.3,
                "experience": "Fresher",
                "education": "B.Ed/M.Ed/Subject Specialization"
            },
            "description": "Create engaging educational content reaching millions of Indian students.",
            "benefits": ["Creative Freedom", "Education Impact", "Flexible Hours", "Learning Resources"],
            "isRemote": True,
            "companyRating": 4.2,
            "applicants": 2000,
            "tags": ["Education", "Content", "Impact", "Remote"]
        },
        
        # Retail & E-commerce
        {
            "id": "retail-001",
            "title": "E-commerce Operations Intern",
            "company": "Flipkart",
            "location": "Bangalore, Karnataka",
            "domain": "E-commerce",
            "industry": "Retail",
            "type": "Operations Internship",
            "duration": "4 months",
            "salary": 26000,
            "requirements": {
                "skills": ["Operations Management", "Data Analysis", "Excel", "Supply Chain", "Customer Service"],
                "minCgpa": 7.0,
                "experience": "Fresher",
                "education": "Any Graduate"
            },
            "description": "Optimize operations for India's largest e-commerce platform reaching every corner.",
            "benefits": ["Employee Discounts", "Startup Culture", "Fast Growth", "Pan India Exposure"],
            "isRemote": False,
            "companyRating": 4.1,
            "applicants": 4500,
            "tags": ["E-commerce", "Operations", "Scale", "India Reach"]
        },
        
        # Media & Entertainment
        {
            "id": "media-001",
            "title": "Digital Marketing Intern",
            "company": "Zee Entertainment",
            "location": "Mumbai, Maharashtra",
            "domain": "Media & Entertainment",
            "industry": "Media",
            "type": "Creative Internship",
            "duration": "3 months",
            "salary": 20000,
            "requirements": {
                "skills": ["Digital Marketing", "Social Media", "Content Creation", "Analytics", "Photoshop"],
                "minCgpa": 6.5,
                "experience": "Fresher",
                "education": "Mass Communication/Marketing/Arts"
            },
            "description": "Shape digital strategies for India's leading entertainment conglomerate.",
            "benefits": ["Creative Exposure", "Industry Network", "Portfolio Building", "Event Access"],
            "isRemote": False,
            "companyRating": 3.9,
            "applicants": 1800,
            "tags": ["Media", "Creative", "Entertainment", "Digital"]
        },
        
        # Government & Public Sector
        {
            "id": "gov-001",
            "title": "Public Policy Research Intern",
            "company": "NITI Aayog",
            "location": "New Delhi, Delhi",
            "domain": "Public Policy",
            "industry": "Government",
            "type": "Research Internship",
            "duration": "6 months",
            "salary": 15000,
            "requirements": {
                "skills": ["Policy Research", "Data Analysis", "Report Writing", "Economics", "Statistics"],
                "minCgpa": 8.5,
                "experience": "Fresher",
                "education": "Economics/Political Science/Public Administration"
            },
            "description": "Contribute to policy-making that shapes India's future development.",
            "benefits": ["Government Exposure", "Policy Impact", "Research Publications", "Network"],
            "isRemote": False,
            "companyRating": 4.6,
            "applicants": 600,
            "tags": ["Government", "Policy", "Research", "Impact"]
        },
        
        # Renewable Energy
        {
            "id": "energy-001",
            "title": "Solar Energy Engineering Intern",
            "company": "Adani Green Energy",
            "location": "Ahmedabad, Gujarat",
            "domain": "Renewable Energy",
            "industry": "Energy",
            "type": "Engineering Internship",
            "duration": "5 months",
            "salary": 21000,
            "requirements": {
                "skills": ["Solar Technology", "Electrical Engineering", "AutoCAD", "Project Management", "Sustainability"],
                "minCgpa": 7.5,
                "experience": "Fresher",
                "education": "B.Tech Electrical/Electronics/Renewable Energy"
            },
            "description": "Build India's sustainable energy future through solar power innovation.",
            "benefits": ["Green Technology", "Site Visits", "Sustainability Certification", "Growth Potential"],
            "isRemote": False,
            "companyRating": 4.3,
            "applicants": 1100,
            "tags": ["Solar", "Sustainability", "Engineering", "Future"]
        },
        
        # Startups & Innovation
        {
            "id": "startup-001",
            "title": "Full Stack Development Intern",
            "company": "Razorpay",
            "location": "Bangalore, Karnataka",
            "domain": "FinTech",
            "industry": "Financial Technology",
            "type": "Tech Internship",
            "duration": "6 months",
            "salary": 35000,
            "requirements": {
                "skills": ["React", "Node.js", "MongoDB", "JavaScript", "Python", "AWS"],
                "minCgpa": 7.8,
                "experience": "Some projects",
                "education": "B.Tech/B.E. Computer Science/IT"
            },
            "description": "Build payment solutions powering India's digital economy revolution.",
            "benefits": ["Stock Options", "Startup Culture", "Latest Tech", "High Growth", "Learning Budget"],
            "isRemote": True,
            "companyRating": 4.7,
            "applicants": 3200,
            "tags": ["FinTech", "Startup", "Payments", "Digital India"]
        }
    ]

# Enhanced Skills Database for All India
@st.cache_data
def get_all_india_skills():
    """Comprehensive skills database covering all industries in India"""
    return {
        "Technology & Software": [
            "Java", "Python", "JavaScript", "React", "Angular", "Node.js", "Spring Boot",
            "Machine Learning", "Data Science", "Artificial Intelligence", "Cloud Computing",
            "DevOps", "Docker", "Kubernetes", "AWS", "Azure", "MongoDB", "MySQL", 
            "Cybersecurity", "Blockchain", "Mobile Development", "Flutter", "Android", "iOS"
        ],
        
        "Healthcare & Life Sciences": [
            "Clinical Research", "Medical Writing", "Pharmacovigilance", "Biostatistics",
            "Drug Discovery", "Biotechnology", "Microbiology", "Biochemistry", "Genetics",
            "Medical Devices", "Healthcare Analytics", "Telemedicine", "Medical Imaging",
            "Laboratory Management", "Quality Assurance", "Regulatory Affairs"
        ],
        
        "Finance & Banking": [
            "Financial Modeling", "Investment Analysis", "Risk Management", "Accounting",
            "Taxation", "Audit", "Corporate Finance", "Banking Operations", "Insurance",
            "Wealth Management", "Credit Analysis", "Compliance", "Financial Planning",
            "Capital Markets", "Forex Trading", "Fintech", "Digital Banking"
        ],
        
        "Manufacturing & Engineering": [
            "Mechanical Engineering", "Electrical Engineering", "Electronics", "Automation",
            "Quality Control", "Lean Manufacturing", "Six Sigma", "CAD/CAM", "AutoCAD",
            "SolidWorks", "Production Planning", "Supply Chain", "Industrial Design",
            "Process Engineering", "Maintenance", "Safety Engineering", "Robotics"
        ],
        
        "Agriculture & Food": [
            "Sustainable Farming", "Crop Management", "Soil Science", "Irrigation",
            "Agricultural Technology", "Food Processing", "Food Safety", "Nutrition",
            "Organic Farming", "Precision Agriculture", "Agricultural Economics",
            "Rural Development", "Veterinary Science", "Horticulture", "Agribusiness"
        ],
        
        "Education & Training": [
            "Curriculum Development", "Educational Technology", "Teaching Methods",
            "Learning Design", "Content Creation", "Educational Assessment", "E-learning",
            "Instructional Design", "Educational Psychology", "Classroom Management",
            "Educational Research", "Special Education", "Language Teaching", "Skill Development"
        ],
        
        "Marketing & Sales": [
            "Digital Marketing", "Social Media Marketing", "Content Marketing", "SEO/SEM",
            "Brand Management", "Market Research", "Sales Strategy", "Customer Relations",
            "Advertising", "Public Relations", "Event Management", "Lead Generation",
            "E-commerce Marketing", "Analytics", "Communication Skills"
        ],
        
        "Design & Creative": [
            "Graphic Design", "UI/UX Design", "Web Design", "Product Design", "Animation",
            "Video Editing", "Photography", "Adobe Creative Suite", "Figma", "Sketch",
            "3D Modeling", "Industrial Design", "Fashion Design", "Interior Design",
            "Creative Writing", "Storytelling", "Brand Design"
        ],
        
        "Media & Communication": [
            "Journalism", "Content Writing", "Video Production", "Audio Production",
            "Broadcasting", "Public Speaking", "Copywriting", "Social Media Management",
            "Media Planning", "Film Making", "Photography", "Event Coverage",
            "Digital Content", "Podcast Production", "Translation"
        ],
        
        "Government & Public Policy": [
            "Policy Analysis", "Public Administration", "Economics", "Statistics",
            "Research Methodology", "Report Writing", "Governance", "Law",
            "International Relations", "Development Studies", "Urban Planning",
            "Environmental Policy", "Social Work", "NGO Management"
        ],
        
        "Energy & Environment": [
            "Renewable Energy", "Solar Technology", "Wind Energy", "Energy Efficiency",
            "Environmental Science", "Sustainability", "Climate Change", "Green Technology",
            "Energy Management", "Carbon Footprint", "Waste Management", "Water Treatment",
            "Environmental Impact Assessment", "Green Building", "Clean Technology"
        ],
        
        "Hospitality & Tourism": [
            "Hotel Management", "Tourism Planning", "Event Management", "Customer Service",
            "Food & Beverage", "Travel Planning", "Cultural Heritage", "Adventure Tourism",
            "Eco-tourism", "Hospitality Technology", "Revenue Management", "Guest Relations",
            "Tour Operations", "Destination Marketing", "Language Skills"
        ]
    }

def create_advanced_all_india_charts():
    """Create comprehensive charts for All India data"""
    
    # 1. Industry Distribution across India
    industries = ['Technology', 'Healthcare', 'Finance', 'Manufacturing', 'Agriculture', 
                 'Education', 'Retail', 'Energy', 'Government', 'Media', 'Hospitality', 'Others']
    values = [25, 15, 12, 18, 8, 7, 10, 5, 3, 4, 6, 7]
    
    fig1 = px.pie(
        values=values,
        names=industries,
        title="🇮🇳 Industry Distribution Across India",
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.4
    )
    
    fig1.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Inter",
        title_font_size=20,
        title_font_color='#1a202c',
        height=500,
        font_color='#1a202c'
    )
    
    fig1.update_traces(
        textposition='inside',
        textinfo='percent+label',
        textfont_size=12
    )
    
    # 2. State-wise Internship Opportunities
    states = ['Karnataka', 'Maharashtra', 'Tamil Nadu', 'Telangana', 'Delhi', 'Gujarat', 
             'West Bengal', 'Uttar Pradesh', 'Rajasthan', 'Punjab']
    opportunities = [8500, 7200, 5800, 4500, 6200, 3800, 3200, 2800, 2200, 1900]
    
    fig2 = px.bar(
        x=states,
        y=opportunities,
        title="📍 State-wise Internship Opportunities",
        color=opportunities,
        color_continuous_scale=['#ff9933', '#ffffff', '#138808'],
        text=opportunities
    )
    
    fig2.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Inter",
        title_font_size=20,
        title_font_color='#1a202c',
        height=500,
        font_color='#1a202c',
        xaxis_tickangle=-45
    )
    
    fig2.update_traces(
        texttemplate='%{text}',
        textposition='outside',
        textfont_color='#1a202c',
        textfont_size=12
    )
    
    # 3. Salary Distribution by Industry
    salary_data = {
        'Industry': ['Technology', 'Finance', 'Healthcare', 'Manufacturing', 'Energy', 
                    'Education', 'Agriculture', 'Media', 'Government', 'Retail'],
        'Average Salary': [32000, 28000, 22000, 24000, 26000, 20000, 18000, 22000, 16000, 24000],
        'Max Salary': [55000, 45000, 35000, 38000, 42000, 30000, 25000, 35000, 25000, 40000]
    }
    
    fig3 = go.Figure()
    
    fig3.add_trace(go.Bar(
        name='Average Salary',
        x=salary_data['Industry'],
        y=salary_data['Average Salary'],
        marker_color='#4299e1'
    ))
    
    fig3.add_trace(go.Bar(
        name='Maximum Salary',
        x=salary_data['Industry'],
        y=salary_data['Max Salary'],
        marker_color='#48bb78'
    ))
    
    fig3.update_layout(
        title='💰 Salary Distribution by Industry (₹/month)',
        xaxis_tickangle=-45,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Inter",
        title_font_size=20,
        title_font_color='#1a202c',
        height=500,
        font_color='#1a202c',
        barmode='group'
    )
    
    # 4. Regional Growth Trends
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    north_india = [1200, 1350, 1500, 1800, 2100, 2400]
    south_india = [2800, 3100, 3400, 3800, 4200, 4600]
    west_india = [2200, 2400, 2600, 2900, 3200, 3500]
    east_india = [800, 900, 1000, 1200, 1400, 1600]
    
    fig4 = go.Figure()
    
    fig4.add_trace(go.Scatter(x=months, y=south_india, mode='lines+markers', 
                             name='South India', line=dict(color='#e53e3e', width=3)))
    fig4.add_trace(go.Scatter(x=months, y=west_india, mode='lines+markers', 
                             name='West India', line=dict(color='#3182ce', width=3)))
    fig4.add_trace(go.Scatter(x=months, y=north_india, mode='lines+markers', 
                             name='North India', line=dict(color='#38a169', width=3)))
    fig4.add_trace(go.Scatter(x=months, y=east_india, mode='lines+markers', 
                             name='East India', line=dict(color='#d69e2e', width=3)))
    
    fig4.update_layout(
        title='📈 Regional Growth Trends - Internship Postings',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Inter",
        title_font_size=20,
        title_font_color='#1a202c',
        height=500,
        font_color='#1a202c',
        hovermode='x unified'
    )
    
    return fig1, fig2, fig3, fig4

def dashboard_page():
    """Enhanced dashboard for All India"""
    create_hero_section()
    
    # Add floating particles
    st.markdown(create_floating_particles(), unsafe_allow_html=True)
    
    # Key Metrics for All India
    metrics = [
        ("Total Opportunities", "50,000+", "🇮🇳"),
        ("Industries Covered", "12+", "🏭"),
        ("States & UTs", "28+", "📍"),
        ("Success Stories", "25,000+", "🎉")
    ]
    create_metric_cards(metrics)
    
    # Add Run Allocation button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Run All India Smart Allocation", type="primary", use_container_width=True):
            with st.spinner("🔄 Analyzing pan-India opportunities and regional preferences..."):
                time.sleep(3)
                st.success("✅ All India allocation analysis completed successfully!")
                st.balloons()
                
                # Show regional allocation
                st.markdown("### 🗺️ Regional Allocation Summary")
                regional_data = {
                    'Region': ['South India', 'West India', 'North India', 'East India', 'Northeast India'],
                    'Allocated Opportunities': [15000, 12000, 10000, 8000, 5000],
                    'Success Rate': [94, 91, 88, 85, 82],
                    'Top Industries': ['Technology, Healthcare', 'Finance, Manufacturing', 'Government, Education', 'Mining, Agriculture', 'Tourism, Agriculture']
                }
                st.dataframe(regional_data, use_container_width=True)
    
    st.markdown("---")
    
    # Industry Showcase
    st.markdown("## 🏭 Industries Powering India")
    
    industries_info = [
        ("🖥️ Technology & IT", "Leading global innovation hub", "25% of opportunities"),
        ("🏥 Healthcare & Pharma", "World's pharmacy serving global health", "15% of opportunities"),
        ("💰 Finance & Banking", "Digital payments revolution", "12% of opportunities"),
        ("🏭 Manufacturing", "Make in India initiative", "18% of opportunities"),
        ("🌾 Agriculture & Food", "Feeding 1.4 billion people", "8% of opportunities"),
        ("🎓 Education & EdTech", "Largest education system globally", "7% of opportunities")
    ]
    
    cols = st.columns(3)
    for idx, (title, desc, stat) in enumerate(industries_info):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="industry-card">
                <h4 style="color: #2d3748; margin-bottom: 1rem;">{title}</h4>
                <p style="color: #718096; margin-bottom: 1rem;">{desc}</p>
                <div class="skill-category">{stat}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Charts Section
    st.markdown("## 📊 All India Analytics Dashboard")
    
    fig1, fig2, fig3, fig4 = create_advanced_all_india_charts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Regional Highlights
    st.markdown("## 🗺️ Regional Opportunities")
    
    regions = [
        ("🌴 South India", "Tech capital with Bangalore, Chennai, Hyderabad", "Technology, Healthcare, Aerospace"),
        ("🏙️ West India", "Financial hub Mumbai, Industrial Gujarat", "Finance, Manufacturing, Chemicals"),
        ("🏛️ North India", "Capital Delhi, Industrial clusters", "Government, Education, Agriculture"),
        ("🌊 East India", "Cultural hub Kolkata, Industrial belt", "Mining, Steel, Jute, Tea")
    ]
    
    for region, desc, industries in regions:
        st.markdown(f"""
        <div class="regional-highlight">
            <h4 style="color: #2d3748; margin-bottom: 0.5rem;">{region}</h4>
            <p style="color: #718096; margin-bottom: 0.5rem;">{desc}</p>
            <strong style="color: #667eea;">Key Industries:</strong> {industries}
        </div>
        """, unsafe_allow_html=True)

# Enhanced Sample Profiles for All India
@st.cache_data
def get_all_india_sample_profiles():
    """Sample user profiles representing diverse Indian backgrounds"""
    return {
        "🚀 Arjun Sharma (Tech - Bangalore)": {
            "name": "Arjun Sharma",
            "email": "arjun.sharma@vit.ac.in",
            "skills": ["Java", "Python", "React", "Machine Learning", "AWS"],
            "cgpa": 8.4,
            "university": "VIT Vellore",
            "location": "Bangalore, Karnataka",
            "industry": "Technology",
            "experience": "Some projects",
            "preferences": {
                "location": ["Bangalore", "Hyderabad", "Remote"],
                "industries": ["Technology", "FinTech"],
                "salary_range": [30000, 50000],
                "work_mode": "Hybrid"
            }
        },
        "🏥 Dr. Priya Patel (Healthcare - Mumbai)": {
            "name": "Dr. Priya Patel",
            "email": "priya.patel@grant.gov.in",
            "skills": ["Clinical Research", "Medical Writing", "Biostatistics", "Drug Discovery", "Healthcare Analytics"],
            "cgpa": 8.8,
            "university": "Grant Medical College, Mumbai",
            "location": "Mumbai, Maharashtra",
            "industry": "Healthcare",
            "experience": "Fresher",
            "preferences": {
                "location": ["Mumbai", "Pune", "Chennai"],
                "industries": ["Healthcare", "Pharmaceuticals"],
                "salary_range": [25000, 40000],
                "work_mode": "Office"
            }
        },
        "💰 Rajesh Kumar (Finance - Delhi)": {
            "name": "Rajesh Kumar",
            "email": "rajesh.kumar@srcc.du.ac.in",
            "skills": ["Financial Analysis", "Excel", "Tableau", "Risk Management", "Investment Banking"],
            "cgpa": 8.6,
            "university": "SRCC, Delhi University",
            "location": "New Delhi, Delhi",
            "industry": "Finance",
            "experience": "Internship Experience",
            "preferences": {
                "location": ["Delhi", "Mumbai", "Gurgaon"],
                "industries": ["Finance", "Banking", "Investment"],
                "salary_range": [35000, 60000],
                "work_mode": "Office"
            }
        },
        "🌾 Kavya Reddy (AgriTech - Hyderabad)": {
            "name": "Kavya Reddy",
            "email": "kavya.reddy@angrau.ac.in",
            "skills": ["Sustainable Farming", "Agricultural Technology", "Data Analysis", "IoT", "Rural Development"],
            "cgpa": 7.9,
            "university": "ANGRAU, Hyderabad",
            "location": "Hyderabad, Telangana",
            "industry": "Agriculture",
            "experience": "Field Experience",
            "preferences": {
                "location": ["Hyderabad", "Bangalore", "Rural Areas"],
                "industries": ["Agriculture", "Food Technology", "Sustainability"],
                "salary_range": [20000, 35000],
                "work_mode": "Field Work"
            }
        },
        "🎓 Amit Singh (Education - Pune)": {
            "name": "Amit Singh",
            "email": "amit.singh@sppu.edu.in",
            "skills": ["Educational Technology", "Content Creation", "Curriculum Design", "E-learning", "Teaching Methods"],
            "cgpa": 8.2,
            "university": "Savitribai Phule Pune University",
            "location": "Pune, Maharashtra",
            "industry": "Education",
            "experience": "Teaching Experience",
            "preferences": {
                "location": ["Pune", "Mumbai", "Remote"],
                "industries": ["Education", "EdTech", "Content"],
                "salary_range": [25000, 45000],
                "work_mode": "Remote"
            }
        }
    }

def calculate_match_score(user_profile: Dict, internship: Dict) -> Tuple[float, Dict]:
    """Enhanced matching algorithm for All India internships"""
    score = 0
    reasons = []
    
    # Skills matching (40% weight)
    user_skills = set([skill.lower() for skill in user_profile.get("skills", [])])
    required_skills = set([skill.lower() for skill in internship["requirements"]["skills"]])
    
    skill_overlap = user_skills.intersection(required_skills)
    skill_match_ratio = len(skill_overlap) / len(required_skills) if required_skills else 0
    skill_score = skill_match_ratio * 40
    score += skill_score
    
    if skill_overlap:
        reasons.append(f"Strong skill match: {', '.join(list(skill_overlap)[:3])}")
    
    # CGPA matching (20% weight)
    cgpa_requirement = internship["requirements"]["minCgpa"]
    user_cgpa = user_profile.get("cgpa", 7.0)
    
    if user_cgpa >= cgpa_requirement:
        cgpa_score = 20
        if user_cgpa >= cgpa_requirement + 0.5:
            reasons.append(f"Exceeds CGPA requirement ({user_cgpa} > {cgpa_requirement})")
        else:
            reasons.append(f"Meets CGPA requirement ({user_cgpa} ≥ {cgpa_requirement})")
    else:
        cgpa_diff = cgpa_requirement - user_cgpa
        if cgpa_diff <= 0.3:
            cgpa_score = 12
            reasons.append(f"Close to CGPA requirement ({user_cgpa} vs {cgpa_requirement})")
        else:
            cgpa_score = 5
    
    score += cgpa_score
    
    # Location matching (20% weight)
    preferred_locations = user_profile.get("preferences", {}).get("location", [])
    internship_location = internship["location"].lower()
    
    location_score = 0
    if any(loc.lower() in internship_location for loc in preferred_locations):
        location_score = 20
        reasons.append("Matches location preference")
    elif "remote" in [loc.lower() for loc in preferred_locations] and internship.get("isRemote", False):
        location_score = 20
        reasons.append("Matches remote work preference")
    else:
        location_score = 8
    
    score += location_score
    
    # Industry matching (15% weight)
    user_industry = user_profile.get("industry", "").lower()
    internship_industry = internship["industry"].lower()
    
    industry_score = 0
    if user_industry in internship_industry or internship_industry in user_industry:
        industry_score = 15
        reasons.append("Perfect industry match")
    else:
        industry_score = 5
    
    score += industry_score
    
    # Salary matching (5% weight)
    salary_range = user_profile.get("preferences", {}).get("salary_range", [0, 100000])
    internship_salary = internship["salary"]
    
    salary_score = 0
    if salary_range[0] <= internship_salary <= salary_range[1]:
        salary_score = 5
        reasons.append("Within salary expectations")
    else:
        salary_score = 2
    
    score += salary_score
    
    return min(score, 100), {
        "reasons": reasons,
        "skill_match": skill_score,
        "cgpa_match": cgpa_score,
        "location_match": location_score,
        "industry_match": industry_score,
        "salary_match": salary_score,
        "skill_overlap": list(skill_overlap)
    }

def run_allocation_algorithm(user_profiles: List[Dict], internships: List[Dict]) -> Dict:
    """Smart allocation algorithm based on preferences and compatibility"""
    
    # Calculate all matches
    all_matches = []
    for profile in user_profiles:
        for internship in internships:
            score, details = calculate_match_score(profile, internship)
            all_matches.append({
                "profile": profile,
                "internship": internship,
                "score": score,
                "details": details
            })
    
    # Sort by score
    all_matches.sort(key=lambda x: x["score"], reverse=True)
    
    # Allocation results
    allocated = []
    used_internships = set()
    used_profiles = set()
    
    for match in all_matches:
        profile_name = match["profile"]["name"]
        internship_id = match["internship"]["id"]
        
        if profile_name not in used_profiles and internship_id not in used_internships:
            allocated.append(match)
            used_profiles.add(profile_name)
            used_internships.add(internship_id)
    
    # Calculate statistics
    total_score = sum([match["score"] for match in allocated])
    avg_score = total_score / len(allocated) if allocated else 0
    
    return {
        "allocated": allocated,
        "total_matches": len(allocated),
        "average_score": avg_score,
        "success_rate": len(allocated) / len(user_profiles) * 100 if user_profiles else 0,
        "unallocated_profiles": len(user_profiles) - len(allocated)
    }

def matching_page():
    """Enhanced Find Matches page with full functionality"""
    st.markdown("# 🔍 Find My Perfect Match")
    
    # Load sample profiles
    sample_profiles = get_all_india_sample_profiles()
    all_skills = get_all_india_skills()
    
    # Sidebar for profile creation
    with st.sidebar:
        st.markdown("## 👤 Create Your Profile")
        
        # Quick load sample profile
        sample_choice = st.selectbox("🚀 Quick Start", ["Create New Profile"] + list(sample_profiles.keys()))
        
        if sample_choice != "Create New Profile":
            profile = sample_profiles[sample_choice]
            st.success(f"Loaded {sample_choice.split(' ')[1]} {sample_choice.split(' ')[2]}'s profile!")
        else:
            profile = {
                "name": "", "email": "", "skills": [], "cgpa": 7.0, 
                "university": "", "location": "", "industry": "Technology", "experience": "Fresher",
                "preferences": {"location": [], "industries": [], "salary_range": [20000, 50000], "work_mode": "Office"}
            }
        
        # Profile inputs
        name = st.text_input("🏷️ Full Name", value=profile["name"])
        email = st.text_input("📧 Email", value=profile["email"])
        
        col1, col2 = st.columns(2)
        with col1:
            cgpa = st.slider("📊 CGPA", 0.0, 10.0, profile["cgpa"], 0.1)
        with col2:
            experience = st.selectbox("💼 Experience", 
                ["Fresher", "Some projects", "Internship Experience", "1-2 Years"], 
                index=["Fresher", "Some projects", "Internship Experience", "1-2 Years"].index(profile["experience"]))
        
        university = st.text_input("🏫 University", value=profile["university"])
        location = st.text_input("📍 Current Location", value=profile["location"])
        
        # Industry selection
        industry = st.selectbox("🏭 Primary Industry Interest", 
            ["Technology", "Healthcare", "Finance", "Manufacturing", "Agriculture", 
             "Education", "Marketing", "Creative", "Media", "Government", "Energy", "Hospitality"],
            index=["Technology", "Healthcare", "Finance", "Manufacturing", "Agriculture", 
                   "Education", "Marketing", "Creative", "Media", "Government", "Energy", "Hospitality"].index(profile["industry"]))
        
        # Skills selection
        st.markdown("### 🛠️ Your Skills")
        industry_key = f"🖥️ {industry}" if industry == "Technology" else f"🏥 {industry}" if industry == "Healthcare" else f"💰 {industry}" if industry == "Finance" else f"🏭 {industry}" if industry == "Manufacturing" else f"🌾 {industry}" if industry == "Agriculture" else f"🎓 {industry}"
        
        available_skills = []
        for key, skills_list in all_skills.items():
            if industry.lower() in key.lower():
                available_skills = skills_list
                break
        
        if not available_skills:
            available_skills = all_skills.get("🖥️ Technology", [])
        
        selected_skills = st.multiselect("Select Skills", available_skills, default=profile["skills"])
        
        # Preferences
        st.markdown("### 🎯 Preferences")
        preferred_locations = st.multiselect("📍 Preferred Locations", 
            ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad", "Pune", "Kolkata", "Ahmedabad", "Remote"],
            default=profile["preferences"]["location"])
        
        salary_range = st.slider("💰 Salary Range (₹/month)", 
            10000, 80000, tuple(profile["preferences"]["salary_range"]), 2000)
        
        work_mode = st.selectbox("🏢 Work Mode", 
            ["Office", "Remote", "Hybrid", "Field Work"],
            index=["Office", "Remote", "Hybrid", "Field Work"].index(profile["preferences"]["work_mode"]))
    
    # Main matching interface
    if name and email and selected_skills:
        user_profile = {
            "name": name, "email": email, "skills": selected_skills, "cgpa": cgpa,
            "university": university, "location": location, "industry": industry, "experience": experience,
            "preferences": {
                "location": preferred_locations, "industries": [industry], 
                "salary_range": list(salary_range), "work_mode": work_mode
            }
        }
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎯 Find My Perfect Matches", type="primary", use_container_width=True):
                st.session_state.run_matching = True
        
        with col2:
            if st.button("🚀 Run Smart Allocation", type="secondary", use_container_width=True):
                st.session_state.run_allocation = True
        
        # Find matches
        if st.session_state.get("run_matching", False):
            with st.spinner("🔍 Finding your perfect matches..."):
                time.sleep(2)
                internships = load_all_india_internships()
                
                matches = []
                for internship in internships:
                    score, details = calculate_match_score(user_profile, internship)
                    matches.append({
                        "internship": internship,
                        "score": score,
                        "details": details
                    })
                
                matches.sort(key=lambda x: x["score"], reverse=True)
                st.session_state.matches = matches[:10]  # Top 10 matches
            
            st.success(f"✅ Found {len(st.session_state.matches)} perfect matches for you!")
        
        # Run allocation
        if st.session_state.get("run_allocation", False):
            with st.spinner("🚀 Running smart allocation algorithm..."):
                time.sleep(3)
                
                # Use sample profiles for allocation simulation
                profiles = list(sample_profiles.values())
                profiles.append(user_profile)  # Add current user
                
                internships = load_all_india_internships()
                allocation_result = run_allocation_algorithm(profiles, internships)
                
                st.session_state.allocation_result = allocation_result
            
            st.success("✅ Smart allocation completed successfully!")
            st.balloons()
        
        # Display results
        if st.session_state.get("matches"):
            st.markdown("## 🏆 Your Top Matches")
            
            for i, match in enumerate(st.session_state.matches[:5], 1):
                internship = match["internship"]
                score = match["score"]
                details = match["details"]
                
                if score >= 80:
                    match_color = "#48bb78"
                    match_level = "🔥 Excellent"
                elif score >= 60:
                    match_color = "#ed8936"
                    match_level = "⭐ Good"
                else:
                    match_color = "#f56565"
                    match_level = "💡 Fair"
                
                with st.expander(f"#{i} {internship['title']} at {internship['company']} - {score:.1f}% Match"):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.markdown(f"""
                        **🏢 Company:** {internship['company']}  
                        **📍 Location:** {internship['location']}  
                        **🏭 Industry:** {internship['industry']}  
                        **⏱️ Duration:** {internship['duration']}  
                        **📋 Description:** {internship['description']}
                        """)
                        
                        # Skills match
                        st.markdown("**Required Skills:**")
                        for skill in internship["requirements"]["skills"]:
                            if skill.lower() in [s.lower() for s in selected_skills]:
                                st.markdown(f'<span style="background:#48bb78;color:white;padding:4px 8px;border-radius:12px;margin:2px;font-size:12px;">{skill} ✓</span>', unsafe_allow_html=True)
                            else:
                                st.markdown(f'<span style="background:#f56565;color:white;padding:4px 8px;border-radius:12px;margin:2px;font-size:12px;">{skill}</span>', unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div style="background:{match_color};color:white;padding:1rem;border-radius:15px;text-align:center;">
                            <div style="font-size:2rem;font-weight:bold;">{score:.1f}%</div>
                            <div>{match_level} Match</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown(f"""
                        **💰 Salary:** ₹{internship['salary']:,}/month  
                        **📊 Min CGPA:** {internship['requirements']['minCgpa']}  
                        **⭐ Rating:** {internship['companyRating']}/5.0  
                        **👥 Applicants:** {internship['applicants']:,}
                        """)
                        
                        if st.button(f"Apply Now 🚀", key=f"apply_{internship['id']}"):
                            st.success("Application submitted! 🎉")
                    
                    # Match reasons
                    st.markdown("**Why this matches you:**")
                    for reason in details["reasons"]:
                        st.write(f"✅ {reason}")
        
        # Display allocation results
        if st.session_state.get("allocation_result"):
            result = st.session_state.allocation_result
            
            st.markdown("## 📊 Allocation Results")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Matches", result["total_matches"])
            with col2:
                st.metric("Success Rate", f"{result['success_rate']:.1f}%")
            with col3:
                st.metric("Avg Match Score", f"{result['average_score']:.1f}%")
            with col4:
                st.metric("Unallocated", result["unallocated_profiles"])
            
            # Show allocation table
            allocation_data = []
            for match in result["allocated"]:
                allocation_data.append({
                    "Student": match["profile"]["name"],
                    "Company": match["internship"]["company"],
                    "Role": match["internship"]["title"],
                    "Location": match["internship"]["location"],
                    "Match Score": f"{match['score']:.1f}%",
                    "Industry": match["internship"]["industry"]
                })
            
            if allocation_data:
                st.markdown("### 🎯 Optimal Allocations")
                df = pd.DataFrame(allocation_data)
                st.dataframe(df, use_container_width=True)
    
    else:
        st.info("👈 Please fill in your profile details in the sidebar to start matching!")

def analytics_page():
    """Enhanced Analytics page with comprehensive insights"""
    st.markdown("# 📊 Analytics Hub - All India Insights")
    
    # Load data
    internships = load_all_india_internships()
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Opportunities", f"{len(internships) * 50:,}", "↗️ +12%")
    with col2:
        avg_salary = np.mean([i["salary"] for i in internships])
        st.metric("Average Salary", f"₹{avg_salary:,.0f}", "↗️ +8%")
    with col3:
        st.metric("Industries Covered", "12+", "🔥 Complete")
    with col4:
        st.metric("Success Rate", "94.2%", "⭐ Excellent")
    
    # Run Analytics button
    if st.button("🚀 Run Advanced Analytics", type="primary", use_container_width=True):
        with st.spinner("📊 Generating comprehensive analytics..."):
            time.sleep(2)
        st.success("✅ Analytics generated successfully!")
        st.balloons()
    
    # Charts
    fig1, fig2, fig3, fig4 = create_advanced_all_india_charts()
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        st.plotly_chart(fig2, use_container_width=True)
        st.plotly_chart(fig4, use_container_width=True)

def companies_page():
    """Enhanced Companies page with detailed company profiles"""
    st.markdown("# 🏢 Partner Companies Across India")
    
    companies_data = [
        {
            "name": "Infosys Technologies",
            "logo": "🖥️",
            "industry": "Information Technology",
            "location": "Bangalore, Karnataka",
            "employees": "250,000+",
            "rating": 4.2,
            "openings": 500,
            "avg_salary": 45000,
            "founded": 1981,
            "description": "Global leader in next-generation digital services and consulting",
            "benefits": ["Global Projects", "Training Programs", "Health Insurance", "Career Growth"]
        },
        {
            "name": "Apollo Hospitals",
            "logo": "🏥",
            "industry": "Healthcare",
            "location": "Chennai, Tamil Nadu",
            "employees": "69,000+",
            "rating": 4.4,
            "openings": 150,
            "avg_salary": 35000,
            "founded": 1983,
            "description": "Asia's largest healthcare provider with 70+ hospitals",
            "benefits": ["Medical Coverage", "Research Opportunities", "Expert Mentorship", "Industry Exposure"]
        },
        {
            "name": "HDFC Bank",
            "logo": "💰",
            "industry": "Banking & Finance",
            "location": "Mumbai, Maharashtra",
            "employees": "120,000+",
            "rating": 4.3,
            "openings": 200,
            "avg_salary": 38000,
            "founded": 1994,
            "description": "India's largest private sector bank by assets",
            "benefits": ["Banking Training", "Performance Bonus", "Professional Network", "Career Advancement"]
        },
        {
            "name": "Tata Motors",
            "logo": "🚗",
            "industry": "Automotive Manufacturing",
            "location": "Pune, Maharashtra",
            "employees": "80,000+",
            "rating": 4.1,
            "openings": 180,
            "avg_salary": 32000,
            "founded": 1945,
            "description": "India's largest automobile manufacturer",
            "benefits": ["Industrial Training", "Employee Discounts", "Safety Certification", "Innovation Projects"]
        },
        {
            "name": "ITC Limited",
            "logo": "🌾",
            "industry": "Agriculture & FMCG",
            "location": "Kolkata, West Bengal",
            "employees": "25,000+",
            "rating": 4.0,
            "openings": 80,
            "avg_salary": 28000,
            "founded": 1910,
            "description": "Leading diversified conglomerate with agriculture focus",
            "benefits": ["Rural Exposure", "Sustainability Projects", "Field Training", "CSR Initiatives"]
        },
        {
            "name": "BYJU'S",
            "logo": "🎓",
            "industry": "Education Technology",
            "location": "Bangalore, Karnataka",
            "employees": "50,000+",
            "rating": 4.2,
            "openings": 120,
            "avg_salary": 30000,
            "founded": 2011,
            "description": "World's most valuable edtech company",
            "benefits": ["EdTech Innovation", "Content Creation", "Impact on Education", "Flexible Work"]
        }
    ]
    
    # Company filters
    col1, col2, col3 = st.columns(3)
    with col1:
        industry_filter = st.selectbox("Filter by Industry", 
            ["All Industries"] + list(set([c["industry"] for c in companies_data])))
    with col2:
        location_filter = st.selectbox("Filter by Location",
            ["All Locations"] + list(set([c["location"].split(",")[1].strip() for c in companies_data])))
    with col3:
        size_filter = st.selectbox("Filter by Size",
            ["All Sizes", "Large (50,000+)", "Medium (10,000-50,000)", "Small (<10,000)"])
    
    # Filter companies
    filtered_companies = companies_data.copy()
    
    if industry_filter != "All Industries":
        filtered_companies = [c for c in filtered_companies if c["industry"] == industry_filter]
    
    if location_filter != "All Locations":
        filtered_companies = [c for c in filtered_companies if location_filter in c["location"]]
    
    # Display companies
    for company in filtered_companies:
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.95);border-radius:20px;padding:2rem;margin:1.5rem 0;box-shadow:0 10px 30px rgba(0,0,0,0.1);border-left:6px solid #667eea;">
            <div style="display:flex;align-items:center;gap:2rem;">
                <div style="font-size:4rem;">{company['logo']}</div>
                <div style="flex:1;">
                    <h3 style="color:#2d3748;margin:0;">{company['name']}</h3>
                    <p style="color:#667eea;font-weight:600;margin:0.5rem 0;">{company['industry']}</p>
                    <p style="color:#718096;margin:0.5rem 0;">📍 {company['location']} • 👥 {company['employees']} employees • 📅 Founded {company['founded']}</p>
                    <p style="color:#2d3748;margin:1rem 0;">{company['description']}</p>
                    <div style="display:flex;gap:2rem;margin:1rem 0;">
                        <div><strong>Rating:</strong> ⭐ {company['rating']}/5.0</div>
                        <div><strong>Open Positions:</strong> {company['openings']}</div>
                        <div><strong>Avg Salary:</strong> ₹{company['avg_salary']:,}/month</div>
                    </div>
                </div>
            </div>
            <div style="margin-top:1rem;">
                <strong>Benefits & Opportunities:</strong><br>
        """, unsafe_allow_html=True)
        
        for benefit in company['benefits']:
            st.markdown(f'<span style="background:#667eea;color:white;padding:6px 12px;border-radius:15px;margin:3px;font-size:12px;display:inline-block;">{benefit}</span>', unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)

def profile_page():
    """My Journey - User profile and progress tracking"""
    st.markdown("# 🎯 My Journey - Career Progress Tracker")
    
    # User stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Applications Sent", "24", "↗️ +8")
    with col2:
        st.metric("Interviews Scheduled", "12", "📈 +5")
    with col3:
        st.metric("Offers Received", "6", "🎉 +3")
    with col4:
        st.metric("Profile Strength", "92%", "⭐ Excellent")
    
    # Journey Timeline
    st.markdown("## 📅 Your Application Journey")
    
    journey_data = [
        {"Date": "2024-03-01", "Activity": "Profile Created", "Status": "✅ Completed", "Company": "Platform"},
        {"Date": "2024-03-05", "Activity": "Applied to Infosys", "Status": "✅ Submitted", "Company": "Infosys Technologies"},
        {"Date": "2024-03-08", "Activity": "Interview Scheduled", "Status": "📅 Upcoming", "Company": "Apollo Hospitals"},
        {"Date": "2024-03-10", "Activity": "Offer Received", "Status": "🎉 Received", "Company": "HDFC Bank"},
        {"Date": "2024-03-12", "Activity": "Applied to BYJU'S", "Status": "⏳ In Review", "Company": "BYJU'S"},
        {"Date": "2024-03-15", "Activity": "Technical Round", "Status": "📅 Scheduled", "Company": "Tata Motors"}
    ]
    
    df_journey = pd.DataFrame(journey_data)
    st.dataframe(df_journey, use_container_width=True)
    
    # Skills Development
    st.markdown("## 🚀 Skills Development Progress")
    
    skills_progress = {
        "Java": 85,
        "Python": 90,
        "React": 75,
        "Machine Learning": 70,
        "Communication": 88,
        "Leadership": 65
    }
    
    for skill, progress in skills_progress.items():
        st.markdown(f"**{skill}**")
        st.progress(progress/100)
        st.markdown(f"*{progress}% proficiency*")
    
    # Career Goals
    st.markdown("## 🎯 Career Goals & Recommendations")
    
    goals = [
        {"Goal": "Land a Software Engineering Role", "Progress": 80, "Target": "June 2024"},
        {"Goal": "Complete AI/ML Certification", "Progress": 60, "Target": "May 2024"},
        {"Goal": "Develop Leadership Skills", "Progress": 45, "Target": "August 2024"},
        {"Goal": "Build Professional Network", "Progress": 70, "Target": "Ongoing"}
    ]
    
    for goal in goals:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"**{goal['Goal']}**")
            st.progress(goal['Progress']/100)
        with col2:
            st.metric("Progress", f"{goal['Progress']}%")
        with col3:
            st.write(f"*Target: {goal['Target']}*")

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