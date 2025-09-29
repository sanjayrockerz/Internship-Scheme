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

# Configure Streamlit page
st.set_page_config(
    page_title="Smart Internship Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# World-class CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main > div {
        padding-top: 0rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .hero-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        opacity: 0.3;
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    .page-nav {
        background: white;
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    .nav-button {
        display: inline-block;
        padding: 12px 24px;
        margin: 5px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .nav-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    .nav-button.active {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.4);
    }
    
    .metric-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #718096;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .match-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .match-card:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
    }
    
    .match-score {
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        padding: 1rem;
        border-radius: 15px;
        margin: 1rem 0;
        position: relative;
    }
    
    .high-match { 
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
    }
    .medium-match { 
        background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%);
        color: white;
    }
    .low-match { 
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
        color: white;
    }
    
    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 4px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .skill-tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .skill-matched {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
    }
    
    .skill-missing {
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
    }
    
    .glassmorphism {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
        margin: 1rem 0;
    }
    
    .sidebar .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
    }
    
    .stProgress > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        height: 8px;
        border-radius: 4px;
    }
    
    .chart-container {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border-top: 4px solid #667eea;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .animate-pulse {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .gradient-text {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }
    
    .floating-action {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2rem;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        z-index: 1000;
        transition: all 0.3s ease;
    }
    
    .floating-action:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
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

def create_page_navigation():
    """Create beautiful page navigation"""
    pages = {
        '🏠 Dashboard': 'Dashboard',
        '🔍 Find Matches': 'Matching',
        '📊 Analytics': 'Analytics',
        '🏢 Companies': 'Companies',
        '💼 My Profile': 'Profile',
        '⚙️ Settings': 'Settings'
    }
    
    st.markdown('<div class="page-nav">', unsafe_allow_html=True)
    
    cols = st.columns(len(pages))
    for idx, (display_name, page_key) in enumerate(pages.items()):
        with cols[idx]:
            if st.button(display_name, key=f"nav_{page_key}"):
                st.session_state.current_page = page_key
    
    st.markdown('</div>', unsafe_allow_html=True)

def create_hero_section():
    """Create stunning hero section"""
    st.markdown("""
    <div class="hero-header">
        <div class="hero-content">
            <h1 style="font-size: 3rem; font-weight: 700; margin-bottom: 1rem;">
                🚀 Smart Internship Platform
            </h1>
            <p style="font-size: 1.2rem; opacity: 0.9; margin-bottom: 0;">
                AI-Powered Career Matching • World-Class Analytics • Dream Job Discovery
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
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{icon}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

def create_advanced_charts():
    """Create world-class interactive charts"""
    
    # Sample data for charts
    skills_data = {
        'Skills': ['React', 'Python', 'JavaScript', 'Java', 'Node.js', 'Machine Learning', 
                   'Docker', 'AWS', 'MongoDB', 'TypeScript'],
        'Demand': [95, 92, 88, 85, 82, 78, 75, 72, 70, 68],
        'Salary': [50000, 55000, 45000, 48000, 47000, 60000, 52000, 58000, 43000, 49000]
    }
    
    # 1. Advanced Skills Demand Chart with better contrast
    fig1 = px.bar(
        x=skills_data['Demand'], 
        y=skills_data['Skills'],
        orientation='h',
        title="🔥 Most In-Demand Skills 2024",
        color=skills_data['Demand'],
        color_continuous_scale=['#1a365d', '#2b77cb', '#4299e1', '#63b3ed'],
        text=skills_data['Demand']
    )
    
    fig1.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Inter",
        title_font_size=20,
        title_font_color='#1a202c',
        showlegend=False,
        height=500,
        font_color='#1a202c'
    )
    
    fig1.update_traces(
        texttemplate='%{text}%',
        textposition='outside',
        marker_line_width=1,
        marker_line_color='white',
        textfont_color='#1a202c',
        textfont_size=14
    )
    
    fig1.update_xaxes(
        showgrid=True, 
        gridcolor='rgba(0,0,0,0.2)',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    fig1.update_yaxes(
        categoryorder='total ascending',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    
    # 2. Salary vs Demand Scatter with better contrast
    fig2 = px.scatter(
        x=skills_data['Demand'],
        y=skills_data['Salary'],
        size=[15] * len(skills_data['Skills']),
        hover_name=skills_data['Skills'],
        title="💰 Skills: Demand vs Average Salary",
        labels={'x': 'Market Demand (%)', 'y': 'Average Salary (₹/month)'}
    )
    
    fig2.update_traces(
        marker=dict(
            color='#2b77cb',
            line=dict(width=2, color='#1a365d'),
            opacity=0.8
        )
    )
    
    fig2.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Inter",
        title_font_size=20,
        title_font_color='#1a202c',
        height=500,
        font_color='#1a202c'
    )
    
    fig2.update_xaxes(
        showgrid=True,
        gridcolor='rgba(0,0,0,0.2)',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    fig2.update_yaxes(
        showgrid=True,
        gridcolor='rgba(0,0,0,0.2)',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    
    # 3. Match Score Distribution with better contrast
    match_scores = np.random.normal(75, 15, 1000)
    match_scores = np.clip(match_scores, 0, 100)
    
    fig3 = px.histogram(
        x=match_scores,
        nbins=20,
        title="📈 Match Score Distribution",
        labels={'x': 'Match Score (%)', 'y': 'Number of Students'},
        color_discrete_sequence=['#2b77cb']
    )
    
    fig3.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Inter",
        title_font_size=20,
        title_font_color='#1a202c',
        showlegend=False,
        height=400,
        font_color='#1a202c'
    )
    
    fig3.update_traces(
        marker_line_width=1,
        marker_line_color='white'
    )
    
    fig3.update_xaxes(
        showgrid=True,
        gridcolor='rgba(0,0,0,0.2)',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    fig3.update_yaxes(
        showgrid=True,
        gridcolor='rgba(0,0,0,0.2)',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    
    # 4. Success Rate Gauge with better contrast
    fig4 = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = 94,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "🎯 Platform Success Rate", 'font': {'color': '#1a202c', 'size': 20}},
        delta = {'reference': 90, 'font': {'color': '#1a202c'}},
        number = {'font': {'color': '#1a202c', 'size': 48}},
        gauge = {
            'axis': {'range': [None, 100], 'tickcolor': '#1a202c', 'tickfont': {'color': '#1a202c'}},
            'bar': {'color': "#2b77cb"},
            'steps': [
                {'range': [0, 50], 'color': "#fed7d7"},
                {'range': [50, 80], 'color': "#feebc8"},
                {'range': [80, 100], 'color': "#c6f6d5"}
            ],
            'threshold': {
                'line': {'color': "#e53e3e", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig4.update_layout(
        font_family="Inter",
        height=400,
        paper_bgcolor='white',
        font_color='#1a202c'
    )
    
    return fig1, fig2, fig3, fig4

def create_timeline_chart():
    """Create application timeline chart"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
    applications = np.random.randint(100, 500, len(dates))
    placements = np.random.randint(50, 250, len(dates))
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates, y=applications,
        mode='lines+markers',
        name='Applications',
        line=dict(color='#2b77cb', width=3),
        marker=dict(size=8, color='#2b77cb'),
        fill='tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=dates, y=placements,
        mode='lines+markers',
        name='Successful Placements',
        line=dict(color='#38a169', width=3),
        marker=dict(size=8, color='#38a169'),
        fill='tozeroy'
    ))
    
    fig.update_layout(
        title="📅 Monthly Application & Placement Trends",
        xaxis_title="Month",
        yaxis_title="Number of Students",
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Inter",
        title_font_size=20,
        title_font_color='#1a202c',
        height=500,
        hovermode='x unified',
        font_color='#1a202c',
        legend=dict(font_color='#1a202c')
    )
    
    fig.update_xaxes(
        showgrid=True,
        gridcolor='rgba(0,0,0,0.2)',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor='rgba(0,0,0,0.2)',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    
    return fig

def create_company_network():
    """Create company network visualization"""
    companies = ['TechCorp', 'InnovateUI', 'StartupHub', 'DataPro', 'CloudTech', 'MobileFirst', 'DesignCraft']
    connections = np.random.randint(5, 50, len(companies))
    ratings = np.random.uniform(3.8, 4.8, len(companies))
    
    fig = px.scatter(
        x=connections,
        y=ratings,
        size=connections,
        hover_name=companies,
        title="🏢 Partner Company Network",
        labels={'x': 'Active Internships', 'y': 'Company Rating'},
        color=ratings,
        color_continuous_scale=['#1a365d', '#2b77cb', '#4299e1']
    )
    
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Inter",
        title_font_size=20,
        title_font_color='#1a202c',
        height=500,
        font_color='#1a202c'
    )
    
    fig.update_xaxes(
        showgrid=True,
        gridcolor='rgba(0,0,0,0.2)',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor='rgba(0,0,0,0.2)',
        title_font_color='#1a202c',
        tickfont_color='#1a202c'
    )
    
    return fig

# Enhanced internships data (same as before but in separate function for organization)
@st.cache_data
def load_enhanced_internships():
    """Load comprehensive internship database"""
    return [
        {
            "id": "sde-001",
            "title": "SDE Intern - Frontend",
            "company": "TechCorp Solutions",
            "location": "Bangalore, India",
            "domain": "Software Development",
            "type": "Full-time Internship",
            "duration": "6 months",
            "salary": 52000,
            "requirements": {
                "skills": ["React", "JavaScript", "TypeScript", "HTML", "CSS", "Git"],
                "minCgpa": 7.5,
                "experience": "Fresher",
                "education": "B.Tech/B.E. Computer Science"
            },
            "description": "Build cutting-edge React applications with modern UI/UX designs. Work on scalable frontend systems serving millions of users.",
            "benefits": ["Health Insurance", "Learning Budget ₹25k", "Flexible Hours", "Stock Options", "Gym Membership", "Free Meals"],
            "applicationDeadline": "2024-04-15",
            "startDate": "2024-05-01",
            "isRemote": False,
            "companyRating": 4.6,
            "applicants": 1247,
            "tags": ["React", "Frontend", "SDE", "JavaScript", "UI/UX"],
            "companySize": "1000-5000",
            "industry": "Technology",
            "workCulture": "Innovation-driven, Fast-paced",
            "mentorship": True,
            "certificationSupport": True
        },
        {
            "id": "sde-002",
            "title": "SDE Intern - Full Stack",
            "company": "InnovateUI Technologies",
            "location": "Remote",
            "domain": "Full Stack Development",
            "type": "Full-time Internship",
            "duration": "6 months",
            "salary": 58000,
            "requirements": {
                "skills": ["React", "Node.js", "MongoDB", "Express", "JavaScript", "AWS"],
                "minCgpa": 7.8,
                "experience": "Some projects",
                "education": "B.Tech/B.E. Computer Science/IT"
            },
            "description": "Develop end-to-end web applications using MERN stack. Experience microservices architecture and cloud deployment.",
            "benefits": ["100% Remote", "Stock Options", "International Team", "Conference Budget", "Latest MacBook", "Health Insurance"],
            "applicationDeadline": "2024-04-20",
            "startDate": "2024-05-15",
            "isRemote": True,
            "companyRating": 4.8,
            "applicants": 892,
            "tags": ["MERN", "Full Stack", "SDE", "Remote", "Cloud"],
            "companySize": "100-500",
            "industry": "SaaS",
            "workCulture": "Remote-first, Collaborative",
            "mentorship": True,
            "certificationSupport": True
        },
        {
            "id": "ds-001",
            "title": "Data Science Intern",
            "company": "AI Dynamics",
            "location": "Hyderabad, India",
            "domain": "Data Science",
            "type": "Research Internship",
            "duration": "5 months",
            "salary": 62000,
            "requirements": {
                "skills": ["Python", "Machine Learning", "TensorFlow", "Pandas", "NumPy", "SQL"],
                "minCgpa": 8.2,
                "experience": "ML Projects",
                "education": "B.Tech/M.Tech Computer Science/Data Science"
            },
            "description": "Work on cutting-edge AI/ML projects. Build predictive models and deploy ML pipelines in production.",
            "benefits": ["Research Publications", "Conference Presentations", "GPU Access", "Kaggle Credits", "Industry Mentorship"],
            "applicationDeadline": "2024-04-25",
            "startDate": "2024-05-10",
            "isRemote": False,
            "companyRating": 4.7,
            "applicants": 567,
            "tags": ["Python", "ML", "AI", "Research", "Data Science"],
            "companySize": "50-200",
            "industry": "AI/ML",
            "workCulture": "Research-oriented, Innovative",
            "mentorship": True,
            "certificationSupport": True
        }
        # Add more internships as needed
    ]

# Page Components
def dashboard_page():
    """Create stunning dashboard page"""
    create_hero_section()
    
    # Key Metrics
    metrics = [
        ("Active Internships", "150+", "💼"),
        ("Success Rate", "94%", "🎯"),
        ("Partner Companies", "50+", "🏢"),
        ("Students Placed", "2,500+", "🎓")
    ]
    create_metric_cards(metrics)
    
    # Charts Section
    st.markdown("## 📊 Platform Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig1, fig2, fig3, fig4 = create_advanced_charts()
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
    
    # Timeline Chart
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    timeline_fig = create_timeline_chart()
    st.plotly_chart(timeline_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Recent Activity
    st.markdown("## 🔔 Recent Activity")
    
    activities = [
        ("🎉", "New internship posted at Google India", "2 hours ago"),
        ("✅", "50 students got placed this week", "1 day ago"),
        ("🚀", "New AI matching algorithm deployed", "3 days ago"),
        ("📈", "Platform reached 10,000+ active users", "1 week ago")
    ]
    
    for icon, activity, time in activities:
        st.markdown(f"""
        <div class="match-card" style="border-left-color: #48bb78;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="font-size: 1.5rem;">{icon}</div>
                <div style="flex: 1;">
                    <div style="font-weight: 600; color: #2d3748;">{activity}</div>
                    <div style="color: #718096; font-size: 0.9rem;">{time}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def matching_page():
    """Enhanced matching page with world-class UI"""
    st.markdown("# 🔍 Find Your Perfect Internship Match")
    
    # Load sample profiles for quick testing
    sample_profiles = {
        "🚀 Arjun Sharma (Frontend Developer)": {
            "name": "Arjun Sharma", "email": "arjun.sharma@example.com",
            "skills": ["React", "JavaScript", "HTML", "CSS", "Git"], "cgpa": 8.2,
            "portfolio": "https://arjundev.portfolio.com", "university": "IIT Delhi", "year": "3rd Year"
        },
        "🧠 Priya Patel (Data Scientist)": {
            "name": "Priya Patel", "email": "priya.patel@example.com",
            "skills": ["Python", "Machine Learning", "Pandas", "NumPy", "TensorFlow"], "cgpa": 8.7,
            "portfolio": "https://priyadata.github.io", "university": "NIT Surat", "year": "4th Year"
        },
        "⚡ Rahul Kumar (Backend Developer)": {
            "name": "Rahul Kumar", "email": "rahul.kumar@example.com",
            "skills": ["Java", "Spring Boot", "MySQL", "REST APIs", "Docker"], "cgpa": 7.9,
            "portfolio": "https://rahulbackend.dev", "university": "BITS Pilani", "year": "3rd Year"
        }
    }
    
    # Sidebar Profile Form
    with st.sidebar:
        st.markdown("## 👤 Create Your Profile")
        
        # Quick load sample profile
        sample_choice = st.selectbox("🚀 Quick Start (Optional)", ["Create New Profile"] + list(sample_profiles.keys()))
        
        if sample_choice != "Create New Profile":
            profile = sample_profiles[sample_choice]
            st.success(f"Loaded {sample_choice}!")
        else:
            profile = {"name": "", "email": "", "skills": [], "cgpa": 7.0, "portfolio": "", "university": "", "year": "3rd Year"}
        
        # Profile inputs with enhanced UI
        name = st.text_input("🏷️ Full Name", value=profile["name"])
        email = st.text_input("📧 Email", value=profile["email"])
        
        col1, col2 = st.columns(2)
        with col1:
            cgpa = st.slider("📊 CGPA", 0.0, 10.0, profile["cgpa"], 0.1)
        with col2:
            year = st.selectbox("🎓 Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"], 
                               index=["1st Year", "2nd Year", "3rd Year", "4th Year"].index(profile["year"]))
        
        university = st.text_input("🏫 University", value=profile["university"])
        portfolio = st.text_input("💼 Portfolio URL", value=profile["portfolio"])
        
        # Skills selection with enhanced UI
        st.markdown("### 🛠️ Technical Skills")
        all_skills = ["React", "JavaScript", "Python", "Java", "Node.js", "HTML", "CSS", "TypeScript", 
                      "MongoDB", "MySQL", "Express", "Spring Boot", "Git", "Docker", "AWS", "Kubernetes",
                      "Machine Learning", "TensorFlow", "PyTorch", "Pandas", "NumPy", "Android", "Flutter"]
        
        selected_skills = st.multiselect("Select Skills", all_skills, default=profile["skills"])
        
        # Add custom skill
        custom_skill = st.text_input("Add Custom Skill")
        if custom_skill and st.button("➕ Add Skill"):
            if custom_skill not in selected_skills:
                selected_skills.append(custom_skill)
                st.success(f"Added {custom_skill}!")
        
        # Preferences
        st.markdown("### 🎯 Preferences")
        preferred_locations = st.multiselect("📍 Locations", 
            ["Bangalore", "Mumbai", "Delhi", "Hyderabad", "Pune", "Chennai", "Remote"])
        salary_range = st.slider("💰 Salary Range (₹/month)", 20000, 80000, (40000, 60000), 5000)
        work_mode = st.selectbox("🏢 Work Mode", ["Office", "Remote", "Hybrid"])
    
    # Main matching interface
    if name and email and selected_skills:
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            find_matches = st.button("🎯 Find My Perfect Matches", type="primary", use_container_width=True)
        with col2:
            run_allocation = st.button("🚀 Run Smart Allocation", type="secondary", use_container_width=True)
        
        if find_matches:
            with st.spinner("🔍 Analyzing your profile and finding perfect matches..."):
                time.sleep(2)  # Simulate processing
                
                internships = load_enhanced_internships()
                matches = []
                
                for internship in internships:
                    # Calculate match score (simplified)
                    user_skills_set = set([skill.lower() for skill in selected_skills])
                    req_skills_set = set([skill.lower() for skill in internship["requirements"]["skills"]])
                    
                    skill_match = len(user_skills_set.intersection(req_skills_set)) / len(req_skills_set) * 50
                    cgpa_match = 25 if cgpa >= internship["requirements"]["minCgpa"] else 10
                    salary_match = 25 if salary_range[0] <= internship["salary"] <= salary_range[1] else 15
                    
                    total_score = skill_match + cgpa_match + salary_match
                    
                    matches.append({
                        "internship": internship,
                        "score": min(total_score, 100),
                        "skill_overlap": list(user_skills_set.intersection(req_skills_set))
                    })
                
                matches.sort(key=lambda x: x["score"], reverse=True)
                st.session_state.matches = matches
        
        if run_allocation:
            with st.spinner("🚀 Running advanced allocation algorithms..."):
                time.sleep(3)  # Simulate complex processing
                st.success("✅ Smart allocation completed! Optimal matches have been calculated.")
                st.info("🎯 Allocation considers: skill compatibility, CGPA requirements, location preferences, and company capacity.")
                
                # Show allocation results
                st.markdown("### 📊 Allocation Results")
                allocation_data = {
                    'Company': ['TechCorp', 'InnovateUI', 'AI Dynamics', 'StartupHub', 'CloudTech'],
                    'Allocated Students': [25, 18, 12, 20, 15],
                    'Success Rate': [96, 94, 98, 92, 95],
                    'Avg Match Score': [87, 89, 91, 85, 88]
                }
                
                st.dataframe(allocation_data, use_container_width=True)
                st.balloons()
        
        # Display matches if available
        if st.session_state.matches:
            st.markdown("## 🏆 Your Personalized Matches")
            
            # Match summary
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Matches", len(st.session_state.matches))
            with col2:
                excellent = len([m for m in st.session_state.matches if m["score"] >= 80])
                st.metric("Excellent Matches", excellent)
            with col3:
                avg_score = np.mean([m["score"] for m in st.session_state.matches])
                st.metric("Avg Match Score", f"{avg_score:.1f}%")
            with col4:
                avg_salary = np.mean([m["internship"]["salary"] for m in st.session_state.matches])
                st.metric("Avg Salary", f"₹{avg_salary:,.0f}")
            
            # Display top matches
            for i, match in enumerate(st.session_state.matches[:5], 1):
                internship = match["internship"]
                score = match["score"]
                
                # Determine match level
                if score >= 80:
                    match_class = "high-match"
                    match_level = "🔥 Excellent Match"
                elif score >= 60:
                    match_class = "medium-match"
                    match_level = "⭐ Good Match"
                else:
                    match_class = "low-match"
                    match_level = "💡 Fair Match"
                
                with st.expander(f"#{i} {internship['title']} at {internship['company']} - {score:.1f}% Match", expanded=i==1):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.markdown(f"""
                        **🏢 Company:** {internship['company']} ({internship['companySize']} employees)  
                        **📍 Location:** {internship['location']}  
                        **⏱️ Duration:** {internship['duration']}  
                        **🎯 Domain:** {internship['domain']}  
                        **📋 Description:** {internship['description']}
                        """)
                        
                        # Skills visualization
                        st.markdown("**Required Skills:**")
                        skill_html = ""
                        for skill in internship["requirements"]["skills"]:
                            if skill.lower() in [s.lower() for s in selected_skills]:
                                skill_html += f'<span class="skill-tag skill-matched">{skill} ✓</span>'
                            else:
                                skill_html += f'<span class="skill-tag skill-missing">{skill}</span>'
                        st.markdown(skill_html, unsafe_allow_html=True)
                        
                        # Benefits
                        st.markdown("**🎁 Benefits:**")
                        for benefit in internship["benefits"]:
                            st.write(f"• {benefit}")
                    
                    with col2:
                        st.markdown(f'<div class="match-score {match_class}">{score:.1f}%<br>{match_level}</div>', 
                                   unsafe_allow_html=True)
                        
                        st.markdown(f"""
                        **💰 Salary:** ₹{internship['salary']:,}/month  
                        **📊 Min CGPA:** {internship['requirements']['minCgpa']}  
                        **⭐ Rating:** {internship['companyRating']}/5.0  
                        **👥 Applicants:** {internship['applicants']:,}  
                        **🏠 Remote:** {'Yes' if internship['isRemote'] else 'No'}  
                        **🎓 Mentorship:** {'Yes' if internship['mentorship'] else 'No'}
                        """)
                        
                        if st.button(f"Apply Now 🚀", key=f"apply_{internship['id']}"):
                            st.success("Application submitted! 🎉")
    else:
        # Landing state
        st.markdown("""
        <div class="glassmorphism">
            <h2 style="text-align: center;">🎯 Ready to Find Your Dream Internship?</h2>
            <p style="text-align: center; font-size: 1.1rem;">
                Fill in your profile details in the sidebar to get started with AI-powered matching!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature highlights
        st.markdown("### ✨ Why Our Matching System is World-Class")
        
        features = [
            ("🧠", "AI-Powered Matching", "Advanced algorithms analyze 50+ data points"),
            ("⚡", "Real-Time Results", "Get personalized matches in under 3 seconds"),
            ("🎯", "94% Accuracy", "Validated through thousands of successful placements"),
            ("🌟", "Smart Recommendations", "Learn from your preferences and improve over time")
        ]
        
        cols = st.columns(2)
        for idx, (icon, title, desc) in enumerate(features):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)

def analytics_page():
    """Advanced analytics page with world-class charts"""
    st.markdown("# 📊 Advanced Analytics Dashboard")
    
    # Add Run Allocation button at the top
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Run Smart Allocation Analysis", type="primary", use_container_width=True):
            with st.spinner("🔄 Running advanced allocation algorithms..."):
                time.sleep(2)  # Simulate processing
                st.success("✅ Allocation analysis completed successfully!")
                st.balloons()
    
    st.markdown("---")
    
    # Create comprehensive charts
    fig1, fig2, fig3, fig4 = create_advanced_charts()
    
    # Top row - Key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Custom donut chart for domains
        domains = ['Frontend', 'Backend', 'Full Stack', 'Data Science', 'Mobile', 'DevOps']
        values = [25, 20, 18, 15, 12, 10]
        
        fig_donut = go.Figure(data=[go.Pie(
            labels=domains, 
            values=values, 
            hole=.3,
            marker_colors=['#2b77cb', '#1a365d', '#38a169', '#dd6b20', '#e53e3e', '#805ad5'],
            textfont=dict(color='white', size=14),
            textinfo='label+percent'
        )])
        
        fig_donut.update_layout(
            title="🎯 Popular Domains",
            font_family="Inter",
            height=400,
            paper_bgcolor='white',
            title_font_color='#1a202c',
            font_color='#1a202c'
        )
        
        st.plotly_chart(fig_donut, use_container_width=True)
    
    with col3:
        # Application success funnel
        stages = ['Applied', 'Screened', 'Interviewed', 'Selected']
        counts = [1000, 600, 300, 150]
        
        fig_funnel = go.Figure(go.Funnel(
            y = stages,
            x = counts,
            textinfo = "value+percent initial",
            marker = {"color": ["#667eea", "#764ba2", "#48bb78", "#ed8936"]}
        ))
        
        fig_funnel.update_layout(
            title="📈 Application Funnel",
            font_family="Inter",
            height=400,
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_funnel, use_container_width=True)
    
    # Middle row - Detailed analytics
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Bottom row - Trends and insights
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    timeline_fig = create_timeline_chart()
    st.plotly_chart(timeline_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Company network
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    company_fig = create_company_network()
    st.plotly_chart(company_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def companies_page():
    """World-class companies showcase page"""
    st.markdown("# 🏢 Partner Companies")
    
    # Company data
    companies = [
        {
            "name": "TechCorp Solutions",
            "logo": "🚀",
            "rating": 4.6,
            "employees": "1000-5000",
            "industry": "Technology",
            "openings": 25,
            "avgSalary": 52000,
            "location": "Bangalore",
            "benefits": ["Health Insurance", "Stock Options", "Flexible Hours", "Learning Budget"]
        },
        {
            "name": "InnovateUI Technologies",
            "logo": "💡",
            "rating": 4.8,
            "employees": "100-500",
            "industry": "SaaS",
            "openings": 15,
            "avgSalary": 58000,
            "location": "Remote",
            "benefits": ["100% Remote", "International Team", "Conference Budget", "Latest Equipment"]
        },
        {
            "name": "AI Dynamics",
            "logo": "🧠",
            "rating": 4.7,
            "employees": "50-200",
            "industry": "AI/ML",
            "openings": 8,
            "avgSalary": 62000,
            "location": "Hyderabad",
            "benefits": ["Research Publications", "GPU Access", "Industry Mentorship", "Conference Presentations"]
        }
    ]
    
    # Company cards
    for company in companies:
        st.markdown(f"""
        <div class="match-card" style="border-left-color: #667eea;">
            <div style="display: flex; align-items: center; gap: 2rem;">
                <div style="font-size: 4rem;">{company['logo']}</div>
                <div style="flex: 1;">
                    <h3 style="margin: 0; color: #2d3748;">{company['name']}</h3>
                    <p style="margin: 0.5rem 0; color: #718096;">
                        {company['industry']} • {company['employees']} employees • {company['location']}
                    </p>
                    <div style="display: flex; gap: 2rem; margin: 1rem 0;">
                        <div><strong>Rating:</strong> ⭐ {company['rating']}/5.0</div>
                        <div><strong>Open Positions:</strong> {company['openings']}</div>
                        <div><strong>Avg Salary:</strong> ₹{company['avgSalary']:,}/month</div>
                    </div>
                    <div style="margin-top: 1rem;">
                        <strong>Benefits:</strong>
                        <div style="margin-top: 0.5rem;">
        """, unsafe_allow_html=True)
        
        benefit_html = ""
        for benefit in company['benefits']:
            benefit_html += f'<span class="skill-tag">{benefit}</span>'
        st.markdown(benefit_html, unsafe_allow_html=True)
        
        st.markdown("""
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def profile_page():
    """User profile management page"""
    st.markdown("# 💼 My Profile")
    
    st.markdown("""
    <div class="glassmorphism">
        <h3>🛠️ Profile Management</h3>
        <p>Manage your profile, view application history, and track your progress.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Profile stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Applications Sent", "12")
    with col2:
        st.metric("Interviews Scheduled", "5")
    with col3:
        st.metric("Offers Received", "2")
    with col4:
        st.metric("Profile Views", "89")
    
    # Recent applications
    st.markdown("## 📋 Recent Applications")
    
    applications = [
        ("SDE Intern at TechCorp", "Applied", "2024-03-15", "High Match"),
        ("Full Stack Intern at InnovateUI", "Interview Scheduled", "2024-03-12", "Excellent Match"),
        ("Data Science Intern at AI Dynamics", "Offer Received", "2024-03-10", "Perfect Match")
    ]
    
    for title, status, date, match in applications:
        status_color = "#48bb78" if status == "Offer Received" else "#ed8936" if status == "Interview Scheduled" else "#667eea"
        
        st.markdown(f"""
        <div class="match-card" style="border-left-color: {status_color};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h4 style="margin: 0; color: #2d3748;">{title}</h4>
                    <p style="margin: 0.5rem 0; color: #718096;">Applied on {date} • {match}</p>
                </div>
                <div style="background: {status_color}; color: white; padding: 0.5rem 1rem; border-radius: 15px; font-weight: 500;">
                    {status}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def settings_page():
    """Settings and preferences page"""
    st.markdown("# ⚙️ Settings & Preferences")
    
    st.markdown("""
    <div class="glassmorphism">
        <h3>🔧 Platform Settings</h3>
        <p>Customize your experience and manage notifications.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Settings options
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📧 Notification Settings")
        st.checkbox("Email notifications for new matches", True)
        st.checkbox("SMS alerts for interview invitations", False)
        st.checkbox("Weekly digest of new internships", True)
        st.checkbox("Application status updates", True)
    
    with col2:
        st.markdown("### 🎨 Display Preferences")
        st.selectbox("Theme", ["Light", "Dark", "Auto"])
        st.selectbox("Language", ["English", "Hindi", "Tamil"])
        st.slider("Matches per page", 5, 20, 10)

def main():
    """Main application with world-class navigation"""
    init_session_state()
    
    # Page navigation
    create_page_navigation()
    
    # Route to appropriate page
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
    elif st.session_state.current_page == 'Settings':
        settings_page()
    
    # Floating action button
    st.markdown("""
    <div class="floating-action">
        💬 Need Help?
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()