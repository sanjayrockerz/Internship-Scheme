import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from typing import Dict, List, Tuple, Any
import time
import random
from datetime import datetime, timedelta

# Enhanced Find Matches Page with Realistic UI Effects
def create_find_matches_page():
    """Create a separate, stunning Find Matches page with advanced UI effects"""
    
    st.markdown("""
    <style>
        .match-finder-hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
            padding: 4rem 2rem;
            border-radius: 30px;
            color: white;
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
            animation: backgroundFlow 15s ease-in-out infinite;
            box-shadow: 0 30px 60px rgba(0,0,0,0.3);
        }
        
        @keyframes backgroundFlow {
            0%, 100% { 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
            }
            25% { 
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 25%, #667eea 50%, #764ba2 75%, #f093fb 100%);
            }
            50% { 
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 25%, #4facfe 50%, #00f2fe 75%, #667eea 100%);
            }
            75% { 
                background: linear-gradient(135deg, #764ba2 0%, #f093fb 25%, #f5576c 50%, #4facfe 75%, #00f2fe 100%);
            }
        }
        
        .match-finder-hero::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 50%);
            animation: rotate 20s linear infinite;
        }
        
        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .profile-builder {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 25px;
            padding: 2.5rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            border: 2px solid rgba(255,255,255,0.3);
            position: relative;
            overflow: hidden;
        }
        
        .profile-builder::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c);
            animation: gradientMove 3s ease-in-out infinite;
        }
        
        @keyframes gradientMove {
            0%, 100% { transform: translateX(-100%); }
            50% { transform: translateX(100%); }
        }
        
        .skill-selector {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border-radius: 20px;
            padding: 2rem;
            margin: 1.5rem 0;
            border: 2px solid rgba(102, 126, 234, 0.2);
            transition: all 0.3s ease;
        }
        
        .skill-selector:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
        }
        
        .industry-tabs {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 1rem 0;
        }
        
        .industry-tab {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            font-weight: 600;
            font-size: 0.9rem;
            border: none;
            position: relative;
            overflow: hidden;
        }
        
        .industry-tab:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }
        
        .industry-tab.active {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            box-shadow: 0 8px 20px rgba(240, 147, 251, 0.4);
        }
        
        .matching-animation {
            text-align: center;
            padding: 3rem;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(240, 147, 251, 0.1) 100%);
            border-radius: 25px;
            margin: 2rem 0;
            position: relative;
            overflow: hidden;
        }
        
        .matching-loader {
            width: 80px;
            height: 80px;
            border: 4px solid rgba(102, 126, 234, 0.2);
            border-left: 4px solid #667eea;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .match-result-card {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 20px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            border-left: 6px solid #667eea;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        .match-result-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.6s;
        }
        
        .match-result-card:hover::before {
            left: 100%;
        }
        
        .match-result-card:hover {
            transform: translateX(10px) translateY(-5px) scale(1.02);
            box-shadow: 0 25px 50px rgba(0,0,0,0.2);
            border-left-color: #f093fb;
        }
        
        .match-score-circle {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            font-weight: 800;
            color: white;
            margin: 0 auto 1rem;
            position: relative;
            background: conic-gradient(from 0deg, #667eea, #764ba2, #f093fb, #667eea);
            animation: rotate 3s linear infinite;
        }
        
        .match-score-inner {
            width: 100px;
            height: 100px;
            background: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #2d3748;
        }
        
        .pulse-button {
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            color: white;
            padding: 20px 40px;
            border-radius: 30px;
            font-weight: 700;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }
        
        .pulse-button:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 20px 50px rgba(102, 126, 234, 0.5);
        }
        
        @keyframes pulse {
            0%, 100% { 
                box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
            }
            50% { 
                box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
                transform: scale(1.02);
            }
        }
        
        .preference-slider {
            background: linear-gradient(135deg, rgba(240, 147, 251, 0.1) 0%, rgba(245, 87, 108, 0.1) 100%);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 2px solid rgba(240, 147, 251, 0.2);
        }
        
        .success-animation {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, rgba(72, 187, 120, 0.1) 0%, rgba(56, 161, 105, 0.1) 100%);
            border-radius: 20px;
            border: 2px solid rgba(72, 187, 120, 0.3);
            margin: 1rem 0;
        }
        
        .floating-icon {
            position: absolute;
            animation: float 6s ease-in-out infinite;
            font-size: 2rem;
            opacity: 0.6;
        }
        
        .floating-icon:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
        .floating-icon:nth-child(2) { top: 20%; right: 15%; animation-delay: 2s; }
        .floating-icon:nth-child(3) { bottom: 15%; left: 20%; animation-delay: 4s; }
        .floating-icon:nth-child(4) { bottom: 10%; right: 10%; animation-delay: 1s; }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            33% { transform: translateY(-15px) rotate(5deg); }
            66% { transform: translateY(-10px) rotate(-3deg); }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
    <div class="match-finder-hero">
        <div class="floating-icon">🎯</div>
        <div class="floating-icon">💼</div>
        <div class="floating-icon">🚀</div>
        <div class="floating-icon">⭐</div>
        <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1rem; position: relative; z-index: 10;">
            🔍 Find Your Perfect Match
        </h1>
        <p style="font-size: 1.3rem; opacity: 0.95; margin-bottom: 1rem; position: relative; z-index: 10;">
            AI-Powered Matching Across All Industries in India
        </p>
        <p style="font-size: 1rem; opacity: 0.8; position: relative; z-index: 10;">
            From Technology to Agriculture • Healthcare to Entertainment • Finance to Education
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Skills Database
    all_india_skills = {
        "🖥️ Technology": ["Java", "Python", "JavaScript", "React", "Angular", "Node.js", "AI/ML", "Cloud Computing", "DevOps", "Cybersecurity"],
        "🏥 Healthcare": ["Clinical Research", "Medical Writing", "Biotechnology", "Pharmacology", "Medical Devices", "Healthcare Analytics"],
        "💰 Finance": ["Financial Analysis", "Investment Banking", "Risk Management", "Fintech", "Blockchain", "Accounting", "Taxation"],
        "🏭 Manufacturing": ["Lean Manufacturing", "Quality Control", "Automation", "Supply Chain", "Industrial Engineering", "CAD/CAM"],
        "🌾 Agriculture": ["Sustainable Farming", "AgriTech", "Food Processing", "Crop Management", "Organic Farming", "Rural Development"],
        "🎓 Education": ["EdTech", "Curriculum Design", "E-learning", "Teaching Methods", "Educational Psychology", "Content Creation"],
        "📱 Marketing": ["Digital Marketing", "Social Media", "Brand Management", "Content Marketing", "SEO/SEM", "Analytics"],
        "🎨 Creative": ["Graphic Design", "UI/UX", "Animation", "Video Editing", "Photography", "Creative Writing", "Brand Design"],
        "📺 Media": ["Journalism", "Broadcasting", "Content Production", "Social Media Management", "Public Relations", "Film Making"],
        "🏛️ Government": ["Policy Analysis", "Public Administration", "Economics", "Law", "Urban Planning", "Social Work"],
        "⚡ Energy": ["Renewable Energy", "Solar Technology", "Energy Management", "Sustainability", "Green Technology", "Climate Change"],
        "🏨 Hospitality": ["Hotel Management", "Tourism", "Event Management", "Customer Service", "Food & Beverage", "Travel Planning"]
    }
    
    # Profile Builder Section
    st.markdown('<div class="profile-builder">', unsafe_allow_html=True)
    st.markdown("## 👤 Build Your Professional Profile")
    
    # Basic Information
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("🏷️ Full Name", placeholder="Enter your full name")
        university = st.text_input("🏫 University/College", placeholder="Your educational institution")
        location = st.selectbox("📍 Preferred Location", 
            ["Any Location", "Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad", "Pune", "Kolkata", "Ahmedabad", "Remote Work"])
    
    with col2:
        email = st.text_input("📧 Email Address", placeholder="your.email@example.com")
        cgpa = st.slider("📊 CGPA/Percentage", 0.0, 10.0, 7.5, 0.1)
        experience_level = st.selectbox("💼 Experience Level", 
            ["Fresher", "Some Projects", "1-2 Years", "Internship Experience"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Industry Selection with Tabs
    st.markdown('<div class="skill-selector">', unsafe_allow_html=True)
    st.markdown("## 🎯 Select Your Industry & Skills")
    
    # Industry tabs
    industry_cols = st.columns(4)
    selected_industries = []
    
    for idx, (industry, skills) in enumerate(list(all_india_skills.items())[:4]):
        with industry_cols[idx]:
            if st.button(industry, key=f"ind1_{idx}"):
                st.session_state[f"selected_industry"] = industry
    
    industry_cols2 = st.columns(4)
    for idx, (industry, skills) in enumerate(list(all_india_skills.items())[4:8]):
        with industry_cols2[idx]:
            if st.button(industry, key=f"ind2_{idx}"):
                st.session_state[f"selected_industry"] = industry
    
    industry_cols3 = st.columns(4)
    for idx, (industry, skills) in enumerate(list(all_india_skills.items())[8:]):
        with industry_cols3[idx]:
            if st.button(industry, key=f"ind3_{idx}"):
                st.session_state[f"selected_industry"] = industry
    
    # Skills selection based on industry
    selected_industry = st.session_state.get("selected_industry", "🖥️ Technology")
    st.markdown(f"### Selected Industry: {selected_industry}")
    
    available_skills = all_india_skills.get(selected_industry, [])
    selected_skills = st.multiselect(
        "Select your skills from this industry:", 
        available_skills,
        help="Choose skills you have experience with"
    )
    
    # Additional skills
    custom_skills = st.text_input("🛠️ Additional Skills (comma-separated)", 
                                 placeholder="Any other skills not listed above")
    
    if custom_skills:
        selected_skills.extend([skill.strip() for skill in custom_skills.split(",")])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Preferences Section
    st.markdown('<div class="preference-slider">', unsafe_allow_html=True)
    st.markdown("## ⚙️ Your Preferences")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        salary_range = st.slider("💰 Expected Salary (₹/month)", 10000, 60000, (20000, 40000), 2000)
    with col2:
        work_mode = st.selectbox("🏢 Work Mode", ["Any", "Remote", "Office", "Hybrid"])
    with col3:
        company_size = st.selectbox("👥 Company Size", ["Any Size", "Startup (1-50)", "Medium (51-500)", "Large (500+)"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Magic Matching Button
    st.markdown('<div style="text-align: center; margin: 3rem 0;">', unsafe_allow_html=True)
    if st.button("🚀 Find My Perfect Matches", key="magic_match", help="Click to find your ideal internships"):
        if name and email and selected_skills:
            # Matching Animation
            st.markdown("""
            <div class="matching-animation">
                <div class="matching-loader"></div>
                <h3 style="color: #667eea; margin-bottom: 1rem;">🔮 AI is analyzing your profile...</h3>
                <p style="color: #718096;">Scanning 50,000+ opportunities across India</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Progress bar with realistic timing
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(100):
                progress_bar.progress(i + 1)
                if i < 30:
                    status_text.text("🔍 Analyzing your skills and preferences...")
                elif i < 60:
                    status_text.text("🎯 Matching with suitable opportunities...")
                elif i < 90:
                    status_text.text("📊 Calculating compatibility scores...")
                else:
                    status_text.text("✨ Preparing your personalized results...")
                time.sleep(0.03)
            
            # Success Animation
            st.markdown("""
            <div class="success-animation">
                <h2 style="color: #38a169; margin-bottom: 1rem;">🎉 Perfect Matches Found!</h2>
                <p style="color: #2d3748; font-size: 1.1rem;">We found amazing opportunities tailored just for you</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
            
            # Mock Results with Enhanced UI
            matches = [
                {
                    "title": f"{selected_industry.split(' ')[1] if len(selected_industry.split()) > 1 else 'Technology'} Intern",
                    "company": "TechCorp India",
                    "location": "Bangalore, Karnataka",
                    "salary": 35000,
                    "match_score": 96,
                    "skills_match": selected_skills[:3],
                    "description": f"Work on cutting-edge {selected_industry.lower()} projects with industry experts.",
                    "benefits": ["Health Insurance", "Learning Budget", "Flexible Hours", "Stock Options"]
                },
                {
                    "title": f"Junior {selected_industry.split(' ')[1] if len(selected_industry.split()) > 1 else 'Developer'} Intern",
                    "company": "InnovateHub",
                    "location": "Mumbai, Maharashtra",
                    "salary": 32000,
                    "match_score": 91,
                    "skills_match": selected_skills[:2],
                    "description": f"Join a dynamic team working on {selected_industry.lower()} innovation.",
                    "benefits": ["Remote Work", "Mentorship", "Certification", "Project Ownership"]
                },
                {
                    "title": f"{selected_industry.split(' ')[1] if len(selected_industry.split()) > 1 else 'Analyst'} Trainee",
                    "company": "Future Enterprises",
                    "location": "Chennai, Tamil Nadu",
                    "salary": 28000,
                    "match_score": 87,
                    "skills_match": selected_skills[:2],
                    "description": f"Learn and grow in the exciting field of {selected_industry.lower()}.",
                    "benefits": ["Training Program", "Career Growth", "Industry Exposure", "Team Events"]
                }
            ]
            
            st.markdown("## 🏆 Your Top Matches")
            
            for idx, match in enumerate(matches, 1):
                st.markdown(f"""
                <div class="match-result-card">
                    <div style="display: flex; align-items: center; gap: 2rem;">
                        <div class="match-score-circle">
                            <div class="match-score-inner">{match['match_score']}%</div>
                        </div>
                        <div style="flex: 1;">
                            <h3 style="color: #2d3748; margin-bottom: 0.5rem;">#{idx} {match['title']}</h3>
                            <p style="color: #667eea; font-weight: 600; margin-bottom: 0.5rem;">{match['company']}</p>
                            <p style="color: #718096; margin-bottom: 1rem;">📍 {match['location']} • 💰 ₹{match['salary']:,}/month</p>
                            <p style="color: #2d3748; margin-bottom: 1rem;">{match['description']}</p>
                            <div style="margin-bottom: 1rem;">
                                <strong style="color: #2d3748;">Matching Skills: </strong>
                """, unsafe_allow_html=True)
                
                # Skills tags
                for skill in match['skills_match']:
                    st.markdown(f'<span class="skill-tag skill-matched">{skill} ✓</span>', unsafe_allow_html=True)
                
                st.markdown("""
                            </div>
                            <div style="margin-bottom: 1rem;">
                                <strong style="color: #2d3748;">Benefits: </strong>
                """, unsafe_allow_html=True)
                
                # Benefits
                for benefit in match['benefits']:
                    st.markdown(f'<span class="skill-tag">{benefit}</span>', unsafe_allow_html=True)
                
                st.markdown("""
                            </div>
                            <button class="pulse-button" style="margin-top: 1rem;">Apply Now 🚀</button>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Additional insights
            st.markdown("## 📈 Your Match Insights")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Profile Strength", "92%", "↗️ +15%")
            with col2:
                st.metric("Market Demand", "High", "🔥 Trending")
            with col3:
                st.metric("Avg Match Score", "91.3%", "⭐ Excellent")
        else:
            st.warning("🚨 Please fill in all required fields to find your matches!")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Find Perfect Match - All India Hub",
        page_icon="🔍",
        layout="wide"
    )
    create_find_matches_page()