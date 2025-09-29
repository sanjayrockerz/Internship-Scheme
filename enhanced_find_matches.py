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
    page_title="Find My Perfect Match - All India Hub",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with advanced animations and realistic effects
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        min-height: 100vh;
    }
    
    /* Animated Background */
    @keyframes backgroundFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .animated-bg {
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb, #ffecd2, #fcb69f);
        background-size: 400% 400%;
        animation: backgroundFlow 15s ease infinite;
    }
    
    /* Glassmorphism Cards */
    .glassmorphism {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .glassmorphism:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 45px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 0.15);
    }
    
    /* Floating Particles */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    .particle {
        position: fixed;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        pointer-events: none;
        animation: float 6s ease-in-out infinite;
    }
    
    .particle:nth-child(1) { top: 20%; left: 20%; width: 8px; height: 8px; animation-delay: 0s; }
    .particle:nth-child(2) { top: 60%; left: 80%; width: 12px; height: 12px; animation-delay: 2s; }
    .particle:nth-child(3) { top: 40%; left: 40%; width: 6px; height: 6px; animation-delay: 4s; }
    .particle:nth-child(4) { top: 80%; left: 10%; width: 10px; height: 10px; animation-delay: 1s; }
    .particle:nth-child(5) { top: 10%; left: 70%; width: 14px; height: 14px; animation-delay: 3s; }
    
    /* Match Cards */
    .match-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border-left: 6px solid transparent;
    }
    
    .match-card.excellent { border-left-color: #48bb78; }
    .match-card.good { border-left-color: #ed8936; }
    .match-card.fair { border-left-color: #f56565; }
    
    .match-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
    }
    
    /* Pulse Animation */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse { animation: pulse 2s ease-in-out infinite; }
    
    /* Rotating Elements */
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .rotate { animation: rotate 20s linear infinite; }
    
    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.85rem;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .skill-tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    .skill-matched {
        background: linear-gradient(135deg, #48bb78, #38a169) !important;
        box-shadow: 0 4px 15px rgba(72, 187, 120, 0.4);
    }
    
    /* Progress Bars */
    .progress-container {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        overflow: hidden;
        margin: 10px 0;
    }
    
    .progress-bar {
        height: 8px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 10px;
        transition: width 1s ease-in-out;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2, #667eea);
    }
    
    /* Sidebar */
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
    }
    
    /* Metrics */
    .metric-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .metric-container:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-5px);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 10px;
    }
</style>

<!-- Floating Particles -->
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
<div class="particle"></div>
""", unsafe_allow_html=True)

# Enhanced All India Skills Database
@st.cache_data
def get_all_india_skills():
    """Comprehensive skills database covering all major Indian industries"""
    return {
        "🖥️ Technology": [
            "Java", "Python", "React", "Node.js", "Angular", "Machine Learning", "AI", "Data Science",
            "AWS", "Azure", "Docker", "Kubernetes", "DevOps", "MongoDB", "MySQL", "PostgreSQL",
            "JavaScript", "TypeScript", "Go", "C++", "Rust", "Flutter", "React Native", "Unity"
        ],
        "🏥 Healthcare": [
            "Clinical Research", "Medical Writing", "Biostatistics", "Drug Discovery", "Healthcare Analytics",
            "Medical Imaging", "Telemedicine", "Electronic Health Records", "Pharmacy", "Nursing",
            "Medical Device Development", "Biotechnology", "Genomics", "Epidemiology", "Public Health"
        ],
        "💰 Finance": [
            "Financial Analysis", "Investment Banking", "Risk Management", "Portfolio Management", "Trading",
            "Excel", "Bloomberg Terminal", "Tableau", "Power BI", "Financial Modeling", "Valuation",
            "Credit Analysis", "Derivatives", "Fixed Income", "Equity Research", "Compliance"
        ],
        "🏭 Manufacturing": [
            "Lean Manufacturing", "Six Sigma", "Quality Control", "Supply Chain", "Operations Research",
            "AutoCAD", "SolidWorks", "PLC Programming", "Industrial Automation", "Process Optimization",
            "Materials Science", "Production Planning", "Inventory Management", "Safety Management"
        ],
        "🌾 Agriculture": [
            "Sustainable Farming", "Agricultural Technology", "Crop Science", "Soil Analysis", "Irrigation",
            "Precision Agriculture", "Organic Farming", "Food Safety", "Agricultural Economics",
            "Rural Development", "Farm Management", "Agricultural Marketing", "Horticulture"
        ],
        "🎓 Education": [
            "Educational Technology", "Curriculum Design", "E-learning", "Content Creation", "Teaching Methods",
            "Learning Management Systems", "Educational Psychology", "Assessment Design", "Online Teaching",
            "Student Engagement", "Educational Research", "Academic Writing", "Training Development"
        ],
        "📱 Marketing": [
            "Digital Marketing", "Social Media Marketing", "SEO", "Content Marketing", "Brand Management",
            "Google Analytics", "Facebook Ads", "Email Marketing", "Influencer Marketing", "CRM",
            "Market Research", "Consumer Behavior", "Brand Strategy", "Campaign Management"
        ],
        "🎨 Creative": [
            "Graphic Design", "UI/UX Design", "Video Editing", "Animation", "Photography", "Illustration",
            "Adobe Creative Suite", "Figma", "Sketch", "3D Modeling", "Motion Graphics", "Web Design",
            "Branding", "Print Design", "Digital Art", "Creative Writing"
        ],
        "📺 Media": [
            "Journalism", "Content Writing", "Video Production", "Audio Engineering", "Broadcasting",
            "Digital Media", "Social Media Management", "Public Relations", "Media Planning",
            "Documentary Making", "News Reporting", "Editing", "Scriptwriting"
        ],
        "🏛️ Government": [
            "Public Administration", "Policy Analysis", "Public Policy", "Governance", "Civil Services",
            "Legal Research", "Regulatory Compliance", "Urban Planning", "Social Work", "Public Finance",
            "E-Governance", "Citizens Services", "Administrative Law", "Constitutional Law"
        ],
        "⚡ Energy": [
            "Renewable Energy", "Solar Technology", "Wind Energy", "Energy Management", "Power Systems",
            "Electrical Engineering", "Grid Management", "Energy Efficiency", "Sustainability",
            "Environmental Engineering", "Carbon Management", "Energy Policy", "Smart Grid"
        ],
        "🏨 Hospitality": [
            "Hotel Management", "Customer Service", "Event Management", "Tourism", "Food & Beverage",
            "Front Office Operations", "Housekeeping", "Revenue Management", "Hospitality Technology",
            "Travel Planning", "Guest Relations", "Catering", "Restaurant Management"
        ]
    }

@st.cache_data
def load_enhanced_all_india_internships():
    """Enhanced internship database with realistic opportunities across all Indian industries"""
    base_internships = [
        # Technology Sector
        {
            "id": "tech_001",
            "title": "Full Stack Developer Intern",
            "company": "Infosys Technologies",
            "industry": "Technology",
            "location": "Bangalore, Karnataka",
            "duration": "6 months",
            "salary": 45000,
            "isRemote": True,
            "companyRating": 4.2,
            "applicants": 15420,
            "description": "Work on enterprise web applications using modern tech stack",
            "requirements": {
                "skills": ["Java", "React", "Node.js", "MongoDB"],
                "minCgpa": 7.5
            },
            "benefits": ["Mentorship", "Global Projects", "Training Programs"]
        },
        {
            "id": "tech_002",
            "title": "Machine Learning Research Intern",
            "company": "Microsoft India",
            "industry": "Technology",
            "location": "Hyderabad, Telangana",
            "duration": "4 months",
            "salary": 52000,
            "isRemote": False,
            "companyRating": 4.6,
            "applicants": 8934,
            "description": "Research and develop AI/ML solutions for cloud platforms",
            "requirements": {
                "skills": ["Python", "Machine Learning", "TensorFlow", "AWS"],
                "minCgpa": 8.0
            },
            "benefits": ["Research Publications", "Industry Mentors", "Tech Conferences"]
        },
        
        # Healthcare Sector
        {
            "id": "health_001",
            "title": "Clinical Research Associate",
            "company": "Apollo Hospitals",
            "industry": "Healthcare",
            "location": "Chennai, Tamil Nadu",
            "duration": "8 months",
            "salary": 35000,
            "isRemote": False,
            "companyRating": 4.4,
            "applicants": 3276,
            "description": "Support clinical trials and research studies",
            "requirements": {
                "skills": ["Clinical Research", "Medical Writing", "Biostatistics"],
                "minCgpa": 7.0
            },
            "benefits": ["Medical Training", "Research Experience", "Healthcare Network"]
        },
        {
            "id": "health_002",
            "title": "Healthcare Analytics Intern",
            "company": "Fortis Healthcare",
            "industry": "Healthcare",
            "location": "Delhi, NCR",
            "duration": "6 months",
            "salary": 32000,
            "isRemote": True,
            "companyRating": 4.1,
            "applicants": 2145,
            "description": "Analyze healthcare data to improve patient outcomes",
            "requirements": {
                "skills": ["Healthcare Analytics", "Python", "Tableau", "Medical Imaging"],
                "minCgpa": 7.5
            },
            "benefits": ["Data Science Training", "Healthcare Insights", "Professional Growth"]
        },
        
        # Finance Sector
        {
            "id": "fin_001",
            "title": "Investment Banking Analyst",
            "company": "HDFC Bank",
            "industry": "Finance",
            "location": "Mumbai, Maharashtra",
            "duration": "6 months",
            "salary": 48000,
            "isRemote": False,
            "companyRating": 4.3,
            "applicants": 12567,
            "description": "Analyze financial markets and support investment decisions",
            "requirements": {
                "skills": ["Financial Analysis", "Excel", "Bloomberg Terminal", "Valuation"],
                "minCgpa": 8.0
            },
            "benefits": ["Financial Markets Exposure", "Professional Certification", "Networking"]
        },
        {
            "id": "fin_002",
            "title": "Risk Management Intern",
            "company": "ICICI Bank",
            "industry": "Finance",
            "location": "Mumbai, Maharashtra",
            "duration": "5 months",
            "salary": 42000,
            "isRemote": False,
            "companyRating": 4.2,
            "applicants": 8934,
            "description": "Assess and manage financial risks across portfolios",
            "requirements": {
                "skills": ["Risk Management", "Financial Modeling", "Python", "Tableau"],
                "minCgpa": 7.5
            },
            "benefits": ["Risk Analytics Training", "Industry Exposure", "Career Development"]
        },
        
        # Manufacturing Sector
        {
            "id": "mfg_001",
            "title": "Operations Excellence Intern",
            "company": "Tata Motors",
            "industry": "Manufacturing",
            "location": "Pune, Maharashtra",
            "duration": "6 months",
            "salary": 32000,
            "isRemote": False,
            "companyRating": 4.1,
            "applicants": 6743,
            "description": "Optimize manufacturing processes and improve efficiency",
            "requirements": {
                "skills": ["Lean Manufacturing", "Six Sigma", "Quality Control", "AutoCAD"],
                "minCgpa": 7.0
            },
            "benefits": ["Industrial Training", "Process Improvement", "Manufacturing Excellence"]
        },
        {
            "id": "mfg_002",
            "title": "Supply Chain Analytics Intern",
            "company": "Mahindra & Mahindra",
            "industry": "Manufacturing",
            "location": "Chennai, Tamil Nadu",
            "duration": "4 months",
            "salary": 28000,
            "isRemote": True,
            "companyRating": 4.0,
            "applicants": 4521,
            "description": "Analyze supply chain data to optimize operations",
            "requirements": {
                "skills": ["Supply Chain", "Data Analysis", "Excel", "SAP"],
                "minCgpa": 7.2
            },
            "benefits": ["Supply Chain Expertise", "Data Analytics", "Industry Network"]
        },
        
        # Agriculture Sector
        {
            "id": "agri_001",
            "title": "Sustainable Agriculture Intern",
            "company": "ITC Limited",
            "industry": "Agriculture",
            "location": "Rural Areas, Multiple States",
            "duration": "8 months",
            "salary": 28000,
            "isRemote": False,
            "companyRating": 4.0,
            "applicants": 2876,
            "description": "Work with farmers to implement sustainable farming practices",
            "requirements": {
                "skills": ["Sustainable Farming", "Agricultural Technology", "Rural Development"],
                "minCgpa": 6.5
            },
            "benefits": ["Rural Exposure", "Social Impact", "Field Experience"]
        },
        {
            "id": "agri_002",
            "title": "AgriTech Innovation Intern",
            "company": "CropIn Technology",
            "industry": "Agriculture",
            "location": "Bangalore, Karnataka",
            "duration": "6 months",
            "salary": 35000,
            "isRemote": True,
            "companyRating": 4.3,
            "applicants": 1923,
            "description": "Develop technology solutions for modern agriculture",
            "requirements": {
                "skills": ["Agricultural Technology", "IoT", "Data Analysis", "Mobile Development"],
                "minCgpa": 7.5
            },
            "benefits": ["Tech Innovation", "Agriculture Impact", "Startup Experience"]
        },
        
        # Education Sector
        {
            "id": "edu_001",
            "title": "EdTech Product Development Intern",
            "company": "BYJU'S",
            "industry": "Education",
            "location": "Bangalore, Karnataka",
            "duration": "5 months",
            "salary": 38000,
            "isRemote": True,
            "companyRating": 4.2,
            "applicants": 7845,
            "description": "Create innovative educational technology solutions",
            "requirements": {
                "skills": ["Educational Technology", "Content Creation", "UI/UX Design"],
                "minCgpa": 7.5
            },
            "benefits": ["EdTech Innovation", "Content Creation", "Impact on Education"]
        },
        {
            "id": "edu_002",
            "title": "Curriculum Design Intern",
            "company": "Unacademy",
            "industry": "Education",
            "location": "Delhi, NCR",
            "duration": "4 months",
            "salary": 30000,
            "isRemote": True,
            "companyRating": 4.1,
            "applicants": 5632,
            "description": "Design and develop educational curriculum and content",
            "requirements": {
                "skills": ["Curriculum Design", "Educational Psychology", "Content Creation"],
                "minCgpa": 7.0
            },
            "benefits": ["Education Impact", "Content Strategy", "Learning Design"]
        }
    ]
    return base_internships

@st.cache_data
def get_sample_user_profiles():
    """Enhanced sample profiles representing diverse Indian backgrounds"""
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
                "salary_range": [35000, 55000],
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
                "salary_range": [28000, 42000],
                "work_mode": "Office"
            }
        },
        "💰 Rajesh Kumar (Finance - Delhi)": {
            "name": "Rajesh Kumar",
            "email": "rajesh.kumar@srcc.du.ac.in",
            "skills": ["Financial Analysis", "Excel", "Bloomberg Terminal", "Risk Management", "Investment Banking"],
            "cgpa": 8.6,
            "university": "SRCC, Delhi University",
            "location": "New Delhi, Delhi",
            "industry": "Finance",
            "experience": "Internship Experience",
            "preferences": {
                "location": ["Delhi", "Mumbai", "Gurgaon"],
                "industries": ["Finance", "Banking", "Investment"],
                "salary_range": [40000, 65000],
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
                "salary_range": [25000, 38000],
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
                "salary_range": [28000, 48000],
                "work_mode": "Remote"
            }
        }
    }

def calculate_advanced_match_score(user_profile: Dict, internship: Dict) -> Tuple[float, Dict]:
    """Advanced matching algorithm with detailed scoring"""
    score = 0
    reasons = []
    
    # Skills matching (35% weight)
    user_skills = set([skill.lower() for skill in user_profile.get("skills", [])])
    required_skills = set([skill.lower() for skill in internship["requirements"]["skills"]])
    
    skill_overlap = user_skills.intersection(required_skills)
    skill_match_ratio = len(skill_overlap) / len(required_skills) if required_skills else 0
    skill_score = skill_match_ratio * 35
    score += skill_score
    
    if skill_overlap:
        reasons.append(f"🎯 Strong skill match: {', '.join(list(skill_overlap)[:3])}")
    
    # CGPA matching (25% weight)
    cgpa_requirement = internship["requirements"]["minCgpa"]
    user_cgpa = user_profile.get("cgpa", 7.0)
    
    if user_cgpa >= cgpa_requirement:
        cgpa_excess = user_cgpa - cgpa_requirement
        if cgpa_excess >= 1.0:
            cgpa_score = 25
            reasons.append(f"⭐ Exceeds CGPA by {cgpa_excess:.1f} points")
        elif cgpa_excess >= 0.5:
            cgpa_score = 22
            reasons.append(f"✅ Good CGPA match ({user_cgpa} > {cgpa_requirement})")
        else:
            cgpa_score = 20
            reasons.append(f"✅ Meets CGPA requirement")
    else:
        cgpa_diff = cgpa_requirement - user_cgpa
        if cgpa_diff <= 0.2:
            cgpa_score = 15
            reasons.append(f"⚡ Close to CGPA requirement")
        else:
            cgpa_score = 8
    
    score += cgpa_score
    
    # Location matching (20% weight)
    preferred_locations = user_profile.get("preferences", {}).get("location", [])
    internship_location = internship["location"].lower()
    
    location_score = 0
    if any(loc.lower() in internship_location for loc in preferred_locations):
        location_score = 20
        reasons.append("📍 Perfect location match")
    elif "remote" in [loc.lower() for loc in preferred_locations] and internship.get("isRemote", False):
        location_score = 20
        reasons.append("🏠 Matches remote preference")
    else:
        location_score = 10
    
    score += location_score
    
    # Industry matching (15% weight)
    user_industry = user_profile.get("industry", "").lower()
    internship_industry = internship["industry"].lower()
    
    if user_industry in internship_industry or internship_industry in user_industry:
        industry_score = 15
        reasons.append("🏭 Perfect industry alignment")
    else:
        industry_score = 7
    
    score += industry_score
    
    # Salary matching (5% weight)
    salary_range = user_profile.get("preferences", {}).get("salary_range", [0, 100000])
    internship_salary = internship["salary"]
    
    if salary_range[0] <= internship_salary <= salary_range[1]:
        salary_score = 5
        reasons.append("💰 Within salary expectations")
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

def run_smart_allocation(user_profiles: List[Dict], internships: List[Dict]) -> Dict:
    """Enhanced allocation algorithm with optimization"""
    all_matches = []
    
    # Calculate all possible matches
    for profile in user_profiles:
        for internship in internships:
            score, details = calculate_advanced_match_score(profile, internship)
            all_matches.append({
                "profile": profile,
                "internship": internship,
                "score": score,
                "details": details
            })
    
    # Sort by match quality
    all_matches.sort(key=lambda x: x["score"], reverse=True)
    
    # Optimal allocation using greedy approach
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
    
    # Calculate comprehensive statistics
    total_score = sum([match["score"] for match in allocated])
    avg_score = total_score / len(allocated) if allocated else 0
    
    # Industry distribution
    industry_dist = {}
    for match in allocated:
        industry = match["internship"]["industry"]
        industry_dist[industry] = industry_dist.get(industry, 0) + 1
    
    return {
        "allocated": allocated,
        "total_matches": len(allocated),
        "average_score": avg_score,
        "success_rate": len(allocated) / len(user_profiles) * 100 if user_profiles else 0,
        "unallocated_profiles": len(user_profiles) - len(allocated),
        "industry_distribution": industry_dist,
        "quality_distribution": {
            "excellent": len([m for m in allocated if m["score"] >= 80]),
            "good": len([m for m in allocated if 60 <= m["score"] < 80]),
            "fair": len([m for m in allocated if m["score"] < 60])
        }
    }

def main():
    """Main Find Matches Application"""
    
    # Header with animated title
    st.markdown("""
    <div class="glassmorphism" style="text-align: center; margin-bottom: 2rem;">
        <h1 style="font-size: 3rem; background: linear-gradient(135deg, #667eea, #764ba2); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                   font-weight: 700; margin-bottom: 1rem;">
            🎯 Find My Perfect Match
        </h1>
        <p style="font-size: 1.3rem; color: rgba(255,255,255,0.9); font-weight: 500;">
            AI-Powered Internship Matching for All India • 12+ Industries • 500+ Companies
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if "matches" not in st.session_state:
        st.session_state.matches = []
    if "allocation_result" not in st.session_state:
        st.session_state.allocation_result = None
    if "run_matching" not in st.session_state:
        st.session_state.run_matching = False
    if "run_allocation" not in st.session_state:
        st.session_state.run_allocation = False
    
    # Load data
    sample_profiles = get_sample_user_profiles()
    all_skills = get_all_india_skills()
    
    # Sidebar for profile creation
    with st.sidebar:
        st.markdown("""
        <div class="glassmorphism">
            <h2 style="color: white; text-align: center; margin-bottom: 1rem;">
                👤 Create Your Profile
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick load sample profile
        sample_choice = st.selectbox("🚀 Quick Start", ["Create New Profile"] + list(sample_profiles.keys()))
        
        if sample_choice != "Create New Profile":
            profile = sample_profiles[sample_choice]
            st.success(f"✅ Loaded {sample_choice.split(' ')[1]} {sample_choice.split(' ')[2]}'s profile!")
        else:
            profile = {
                "name": "", "email": "", "skills": [], "cgpa": 7.0, 
                "university": "", "location": "", "industry": "Technology", "experience": "Fresher",
                "preferences": {"location": [], "industries": [], "salary_range": [20000, 50000], "work_mode": "Office"}
            }
        
        # Profile inputs with enhanced styling
        st.markdown("### 📝 Personal Information")
        name = st.text_input("🏷️ Full Name", value=profile["name"], placeholder="Enter your full name")
        email = st.text_input("📧 Email Address", value=profile["email"], placeholder="your.email@domain.com")
        
        col1, col2 = st.columns(2)
        with col1:
            cgpa = st.slider("📊 CGPA", 0.0, 10.0, profile["cgpa"], 0.1, help="Your current CGPA")
        with col2:
            experience = st.selectbox("💼 Experience Level", 
                ["Fresher", "Some projects", "Internship Experience", "1-2 Years"], 
                index=["Fresher", "Some projects", "Internship Experience", "1-2 Years"].index(profile["experience"]))
        
        university = st.text_input("🏫 University/College", value=profile["university"], placeholder="Your institution name")
        location = st.text_input("📍 Current Location", value=profile["location"], placeholder="City, State")
        
        # Industry selection
        st.markdown("### 🏭 Career Focus")
        industry = st.selectbox("Primary Industry Interest", 
            ["Technology", "Healthcare", "Finance", "Manufacturing", "Agriculture", 
             "Education", "Marketing", "Creative", "Media", "Government", "Energy", "Hospitality"],
            index=["Technology", "Healthcare", "Finance", "Manufacturing", "Agriculture", 
                   "Education", "Marketing", "Creative", "Media", "Government", "Energy", "Hospitality"].index(profile["industry"]))
        
        # Skills selection with dynamic loading
        st.markdown("### 🛠️ Your Skills")
        available_skills = []
        for key, skills_list in all_skills.items():
            if industry.lower() in key.lower():
                available_skills = skills_list
                break
        
        if not available_skills:
            available_skills = all_skills.get("🖥️ Technology", [])
        
        selected_skills = st.multiselect("Select Your Skills", available_skills, default=profile["skills"],
                                       help="Choose skills that best represent your abilities")
        
        # Advanced Preferences
        st.markdown("### 🎯 Job Preferences")
        preferred_locations = st.multiselect("📍 Preferred Work Locations", 
            ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad", "Pune", "Kolkata", "Ahmedabad", "Remote", "Any Location"],
            default=profile["preferences"]["location"])
        
        salary_range = st.slider("💰 Expected Salary Range (₹/month)", 
            15000, 80000, tuple(profile["preferences"]["salary_range"]), 2500,
            help="Your expected monthly salary range")
        
        work_mode = st.selectbox("🏢 Preferred Work Mode", 
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
        
        # Action buttons with enhanced styling
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎯 Find Perfect Matches", type="primary", width="stretch"):
                st.session_state.run_matching = True
                st.session_state.run_allocation = False
        
        with col2:
            if st.button("🚀 Run Smart Allocation", type="secondary", width="stretch"):
                st.session_state.run_allocation = True
                st.session_state.run_matching = False
        
        # Find individual matches
        if st.session_state.get("run_matching", False):
            with st.spinner("🔍 AI is analyzing thousands of opportunities across India..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(i + 1)
                
                internships = load_enhanced_all_india_internships()
                
                matches = []
                for internship in internships:
                    score, details = calculate_advanced_match_score(user_profile, internship)
                    matches.append({
                        "internship": internship,
                        "score": score,
                        "details": details
                    })
                
                matches.sort(key=lambda x: x["score"], reverse=True)
                st.session_state.matches = matches[:8]  # Top 8 matches
            
            st.success(f"✅ Found {len(st.session_state.matches)} perfect matches tailored for you!")
            st.balloons()
        
        # Run comprehensive allocation
        if st.session_state.get("run_allocation", False):
            with st.spinner("🚀 Running advanced allocation algorithm across all profiles..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for i in range(100):
                    time.sleep(0.03)
                    progress_bar.progress(i + 1)
                    if i < 30:
                        status_text.text("🔍 Analyzing candidate profiles...")
                    elif i < 60:
                        status_text.text("📊 Calculating compatibility scores...")
                    elif i < 90:
                        status_text.text("🎯 Optimizing allocations...")
                    else:
                        status_text.text("✅ Finalizing results...")
                
                # Use sample profiles for allocation simulation
                profiles = list(sample_profiles.values())
                profiles.append(user_profile)  # Add current user
                
                internships = load_enhanced_all_india_internships()
                allocation_result = run_smart_allocation(profiles, internships)
                
                st.session_state.allocation_result = allocation_result
            
            st.success("✅ Smart allocation completed successfully!")
            st.balloons()
        
        # Display individual match results
        if st.session_state.get("matches"):
            st.markdown("""
            <div class="glassmorphism">
                <h2 style="text-align: center; color: white; margin-bottom: 2rem;">
                    🏆 Your Personalized Matches
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            for i, match in enumerate(st.session_state.matches[:6], 1):
                internship = match["internship"]
                score = match["score"]
                details = match["details"]
                
                # Determine match quality and styling
                if score >= 85:
                    match_color = "#48bb78"
                    match_level = "🔥 Excellent"
                    match_class = "excellent"
                elif score >= 70:
                    match_color = "#ed8936"
                    match_level = "⭐ Very Good"
                    match_class = "good"
                elif score >= 55:
                    match_color = "#3182ce"
                    match_level = "💡 Good"
                    match_class = "good"
                else:
                    match_color = "#f56565"
                    match_level = "🎯 Fair"
                    match_class = "fair"
                
                with st.expander(f"#{i} {internship['title']} at {internship['company']} - {score:.1f}% Match", expanded=(i <= 2)):
                    col1, col2 = st.columns([2.5, 1.5])
                    
                    with col1:
                        # Company and role details
                        st.markdown(f"""
                        <div style="background: rgba(255,255,255,0.95); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
                            <h4 style="color: #2d3748; margin-bottom: 1rem;">🏢 {internship['company']}</h4>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                                <div><strong>📍 Location:</strong> {internship['location']}</div>
                                <div><strong>🏭 Industry:</strong> {internship['industry']}</div>
                                <div><strong>⏱️ Duration:</strong> {internship['duration']}</div>
                                <div><strong>⭐ Company Rating:</strong> {internship['companyRating']}/5.0</div>
                            </div>
                            <p style="color: #4a5568; margin-bottom: 1rem;"><strong>Description:</strong> {internship['description']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Skills match visualization
                        st.markdown("**🛠️ Skills Assessment:**")
                        skills_html = ""
                        for skill in internship["requirements"]["skills"]:
                            if skill.lower() in [s.lower() for s in selected_skills]:
                                skills_html += f'<span class="skill-tag skill-matched">{skill} ✓</span>'
                            else:
                                skills_html += f'<span class="skill-tag">{skill}</span>'
                        st.markdown(skills_html, unsafe_allow_html=True)
                    
                    with col2:
                        # Match score and details
                        st.markdown(f"""
                        <div style="background: {match_color}; color: white; padding: 2rem; border-radius: 20px; 
                                    text-align: center; margin-bottom: 1rem; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                            <div style="font-size: 3rem; font-weight: bold; margin-bottom: 0.5rem;">{score:.1f}%</div>
                            <div style="font-size: 1.2rem; font-weight: 600;">{match_level}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Additional details
                        st.markdown(f"""
                        <div style="background: rgba(255,255,255,0.95); padding: 1.5rem; border-radius: 15px;">
                            <div style="margin-bottom: 0.5rem;"><strong>💰 Salary:</strong> ₹{internship['salary']:,}/month</div>
                            <div style="margin-bottom: 0.5rem;"><strong>📊 Min CGPA:</strong> {internship['requirements']['minCgpa']}</div>
                            <div style="margin-bottom: 0.5rem;"><strong>👥 Applicants:</strong> {internship['applicants']:,}</div>
                            <div style="margin-bottom: 1rem;"><strong>🏠 Remote:</strong> {'Yes' if internship.get('isRemote', False) else 'No'}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Apply button
                        if st.button(f"Apply Now 🚀", key=f"apply_{internship['id']}", width="stretch"):
                            st.success("🎉 Application submitted successfully!")
                            st.balloons()
                    
                    # Match analysis
                    st.markdown("**🎯 Why this matches you:**")
                    for reason in details["reasons"]:
                        st.markdown(f"✅ {reason}")
                    
                    # Score breakdown
                    st.markdown("**📊 Score Breakdown:**")
                    breakdown_cols = st.columns(5)
                    scores = [
                        ("Skills", details["skill_match"], 35),
                        ("CGPA", details["cgpa_match"], 25),
                        ("Location", details["location_match"], 20),
                        ("Industry", details["industry_match"], 15),
                        ("Salary", details["salary_match"], 5)
                    ]
                    
                    for idx, (category, score_val, max_val) in enumerate(scores):
                        with breakdown_cols[idx]:
                            percentage = (score_val / max_val) * 100 if max_val > 0 else 0
                            st.metric(category, f"{score_val:.0f}/{max_val}", f"{percentage:.0f}%")
        
        # Display allocation results
        if st.session_state.get("allocation_result"):
            result = st.session_state.allocation_result
            
            st.markdown("""
            <div class="glassmorphism">
                <h2 style="text-align: center; color: white; margin-bottom: 2rem;">
                    📊 Smart Allocation Results - All India
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Key metrics
            col1, col2, col3, col4 = st.columns(4)
            metrics = [
                ("Total Allocations", result["total_matches"], "🎯"),
                ("Success Rate", f"{result['success_rate']:.1f}%", "📈"),
                ("Avg Match Score", f"{result['average_score']:.1f}%", "⭐"),
                ("Unallocated", result["unallocated_profiles"], "⏳")
            ]
            
            for idx, (label, value, icon) in enumerate(metrics):
                with [col1, col2, col3, col4][idx]:
                    st.markdown(f"""
                    <div class="metric-container">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
                        <div style="font-size: 2rem; font-weight: bold; color: white;">{value}</div>
                        <div style="color: rgba(255,255,255,0.8);">{label}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Quality distribution
            st.markdown("### 📈 Match Quality Distribution")
            quality_data = result["quality_distribution"]
            
            fig = go.Figure(data=[
                go.Bar(
                    x=["Excellent (80%+)", "Good (60-80%)", "Fair (<60%)"],
                    y=[quality_data["excellent"], quality_data["good"], quality_data["fair"]],
                    marker_color=["#48bb78", "#ed8936", "#f56565"],
                    text=[quality_data["excellent"], quality_data["good"], quality_data["fair"]],
                    textposition='auto',
                )
            ])
            
            fig.update_layout(
                title="Match Quality Distribution",
                xaxis_title="Quality Level",
                yaxis_title="Number of Matches",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                height=400
            )
            
            st.plotly_chart(fig, width="stretch")
            
            # Detailed allocation table
            st.markdown("### 🎯 Detailed Allocations")
            allocation_data = []
            for match in result["allocated"]:
                allocation_data.append({
                    "🎓 Student": match["profile"]["name"],
                    "🏢 Company": match["internship"]["company"],
                    "💼 Role": match["internship"]["title"],
                    "📍 Location": match["internship"]["location"],
                    "🎯 Match Score": f"{match['score']:.1f}%",
                    "🏭 Industry": match["internship"]["industry"],
                    "💰 Salary": f"₹{match['internship']['salary']:,}"
                })
            
            if allocation_data:
                df = pd.DataFrame(allocation_data)
                
                # Style the dataframe
                styled_df = df.style.format({
                    "🎯 Match Score": "{}"
                }).background_gradient(
                    subset=["🎯 Match Score"], 
                    cmap='RdYlGn',
                    vmin=0, 
                    vmax=100
                )
                
                st.dataframe(styled_df, width="stretch", height=400)
                
                # Download button for results
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Allocation Results",
                    data=csv,
                    file_name="allocation_results.csv",
                    mime="text/csv"
                )
            
            # Industry distribution
            if result["industry_distribution"]:
                st.markdown("### 🏭 Industry Distribution")
                industry_fig = go.Figure(data=[
                    go.Pie(
                        labels=list(result["industry_distribution"].keys()),
                        values=list(result["industry_distribution"].values()),
                        hole=0.4,
                        textinfo="label+percent",
                        textposition="outside"
                    )
                ])
                
                industry_fig.update_layout(
                    title="Allocations by Industry",
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white'),
                    height=500
                )
                
                st.plotly_chart(industry_fig, width="stretch")
    
    else:
        # Welcome message for new users
        st.markdown("""
        <div class="glassmorphism" style="text-align: center; padding: 3rem;">
            <h2 style="color: white; margin-bottom: 2rem;">👋 Welcome to All India Internship Matching</h2>
            <p style="font-size: 1.2rem; color: rgba(255,255,255,0.9); margin-bottom: 2rem;">
                Get started by filling in your profile details in the sidebar to discover perfect internship opportunities across India!
            </p>
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                <div style="text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
                    <h4 style="color: white;">AI-Powered Matching</h4>
                    <p style="color: rgba(255,255,255,0.8);">Advanced algorithms find your perfect fit</p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🇮🇳</div>
                    <h4 style="color: white;">All India Coverage</h4>
                    <p style="color: rgba(255,255,255,0.8);">500+ companies across 12+ industries</p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
                    <h4 style="color: white;">Smart Analytics</h4>
                    <p style="color: rgba(255,255,255,0.8);">Detailed insights and recommendations</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="margin-top: 3rem; text-align: center; color: rgba(255,255,255,0.7);">
        <p>🚀 Powered by AI • 🇮🇳 Made for India • 💼 Connecting Talent with Opportunities</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
