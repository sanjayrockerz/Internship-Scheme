import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import json
import numpy as np
from typing import Dict, List, Tuple, Any

# Configure Streamlit page
st.set_page_config(
    page_title="Smart Internship Matching Platform",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    
    .match-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .match-score {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    .high-match { background-color: #d4edda; color: #155724; }
    .medium-match { background-color: #fff3cd; color: #856404; }
    .low-match { background-color: #f8d7da; color: #721c24; }
    
    .skill-tag {
        display: inline-block;
        background-color: #007bff;
        color: white;
        padding: 4px 8px;
        border-radius: 15px;
        font-size: 12px;
        margin: 2px;
    }
    
    .stSelectbox > div > div > select {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Enhanced internships data
@st.cache_data
def load_internships_data():
    internships = [
        {
            "id": "fe-001",
            "title": "Frontend Developer Intern",
            "company": "TechnoWeb Solutions",
            "location": "Bangalore, India",
            "domain": "Frontend Development",
            "duration": "6 months",
            "salary": 42000,
            "requirements": {
                "skills": ["React", "JavaScript", "HTML", "CSS", "TypeScript"],
                "minCgpa": 7.0,
                "experience": "Fresher"
            },
            "description": "Work on modern React applications with cutting-edge UI/UX designs. Build responsive and interactive web interfaces.",
            "benefits": ["Health Insurance", "Learning Budget ₹15k", "Flexible Hours", "Mentorship Program", "Certification Support"],
            "applicationDeadline": "2024-03-15",
            "startDate": "2024-04-01",
            "isRemote": False,
            "companyRating": 4.2,
            "applicants": 892,
            "tags": ["React", "Frontend", "UI/UX", "JavaScript"]
        },
        {
            "id": "fe-002",
            "title": "React Developer Intern",
            "company": "InnovateUI",
            "location": "Remote",
            "domain": "Web Development",
            "duration": "4 months",
            "salary": 45000,
            "requirements": {
                "skills": ["React", "Redux", "JavaScript", "Material-UI", "Git"],
                "minCgpa": 7.5,
                "experience": "0-1 years"
            },
            "description": "Build scalable React applications with Redux state management. Work with a team of senior developers.",
            "benefits": ["100% Remote", "Stock Options", "Learning Resources", "Global Team Exposure"],
            "applicationDeadline": "2024-03-20",
            "startDate": "2024-04-15",
            "isRemote": True,
            "companyRating": 4.6,
            "applicants": 567,
            "tags": ["React", "Redux", "Remote", "Frontend"]
        },
        {
            "id": "be-001",
            "title": "Backend Developer Intern",
            "company": "ServerTech Systems",
            "location": "Hyderabad, India",
            "domain": "Backend Development",
            "duration": "5 months",
            "salary": 40000,
            "requirements": {
                "skills": ["Node.js", "Express", "MongoDB", "JavaScript", "REST APIs"],
                "minCgpa": 7.2,
                "experience": "Fresher"
            },
            "description": "Develop robust backend systems and APIs. Work with microservices architecture and cloud platforms.",
            "benefits": ["Health Insurance", "Cloud Certification", "Gym Membership", "Transport Allowance"],
            "applicationDeadline": "2024-03-10",
            "startDate": "2024-03-25",
            "isRemote": False,
            "companyRating": 4.1,
            "applicants": 743,
            "tags": ["Node.js", "Backend", "APIs", "MongoDB"]
        },
        {
            "id": "fs-001",
            "title": "Full Stack Developer Intern",
            "company": "StartupHub Technologies",
            "location": "Mumbai, India",
            "domain": "Full Stack Development",
            "duration": "6 months",
            "salary": 48000,
            "requirements": {
                "skills": ["React", "Node.js", "MongoDB", "Express", "JavaScript"],
                "minCgpa": 7.3,
                "experience": "Fresher"
            },
            "description": "Work on end-to-end web applications using MERN stack. Experience startup culture and rapid development.",
            "benefits": ["Equity Options", "Flexible Hours", "Learning Budget", "Team Outings", "Latest Tech Stack"],
            "applicationDeadline": "2024-03-18",
            "startDate": "2024-04-10",
            "isRemote": False,
            "companyRating": 4.4,
            "applicants": 634,
            "tags": ["MERN", "Full Stack", "Startup", "JavaScript"]
        },
        {
            "id": "ds-001",
            "title": "Data Science Intern",
            "company": "Analytics Pro",
            "location": "Delhi, India",
            "domain": "Data Science",
            "duration": "5 months",
            "salary": 50000,
            "requirements": {
                "skills": ["Python", "Machine Learning", "Pandas", "NumPy", "Scikit-learn"],
                "minCgpa": 8.0,
                "experience": "Fresher"
            },
            "description": "Work on real-world data science projects. Build ML models and create data-driven insights.",
            "benefits": ["Health Insurance", "ML Courses", "Conference Tickets", "Research Publications"],
            "applicationDeadline": "2024-03-22",
            "startDate": "2024-04-05",
            "isRemote": False,
            "companyRating": 4.5,
            "applicants": 1234,
            "tags": ["Python", "ML", "Data Science", "Analytics"]
        },
        {
            "id": "ml-001",
            "title": "AI/ML Engineering Intern",
            "company": "DeepTech AI",
            "location": "Bangalore, India",
            "domain": "Artificial Intelligence",
            "duration": "6 months",
            "salary": 55000,
            "requirements": {
                "skills": ["Python", "TensorFlow", "PyTorch", "Deep Learning", "Computer Vision"],
                "minCgpa": 8.2,
                "experience": "Some projects"
            },
            "description": "Build cutting-edge AI models for computer vision and NLP applications. Work with latest ML frameworks.",
            "benefits": ["GPU Access", "Research Papers", "AI Conferences", "Mentorship by PhDs", "Publication Opportunities"],
            "applicationDeadline": "2024-03-25",
            "startDate": "2024-04-15",
            "isRemote": False,
            "companyRating": 4.7,
            "applicants": 987,
            "tags": ["AI", "Deep Learning", "Computer Vision", "Research"]
        },
        {
            "id": "mob-001",
            "title": "Android Developer Intern",
            "company": "MobileFirst Solutions",
            "location": "Chennai, India",
            "domain": "Mobile Development",
            "duration": "4 months",
            "salary": 38000,
            "requirements": {
                "skills": ["Android", "Kotlin", "Java", "Firebase", "REST APIs"],
                "minCgpa": 7.0,
                "experience": "Fresher"
            },
            "description": "Develop native Android applications with modern architecture patterns. Work on consumer-facing mobile apps.",
            "benefits": ["Device Allowance", "Google Play Console Access", "Mobile Dev Courses", "Team Building"],
            "applicationDeadline": "2024-03-14",
            "startDate": "2024-03-30",
            "isRemote": False,
            "companyRating": 4.0,
            "applicants": 456,
            "tags": ["Android", "Kotlin", "Mobile", "Firebase"]
        },
        {
            "id": "devops-001",
            "title": "DevOps Engineering Intern",
            "company": "CloudOps Technologies",
            "location": "Pune, India",
            "domain": "DevOps",
            "duration": "5 months",
            "salary": 44000,
            "requirements": {
                "skills": ["Docker", "Kubernetes", "AWS", "CI/CD", "Linux"],
                "minCgpa": 7.5,
                "experience": "Basic cloud knowledge"
            },
            "description": "Learn infrastructure as code and automate deployment pipelines. Work with cloud platforms and containers.",
            "benefits": ["AWS Certification", "Cloud Credits", "Linux Training", "24/7 Lab Access"],
            "applicationDeadline": "2024-03-16",
            "startDate": "2024-04-02",
            "isRemote": False,
            "companyRating": 4.3,
            "applicants": 678,
            "tags": ["DevOps", "AWS", "Docker", "Kubernetes"]
        },
        {
            "id": "ui-001",
            "title": "UI/UX Design Intern",
            "company": "DesignCraft Studio",
            "location": "Mumbai, India",
            "domain": "Design",
            "duration": "4 months",
            "salary": 35000,
            "requirements": {
                "skills": ["Figma", "Adobe XD", "Photoshop", "User Research", "Prototyping"],
                "minCgpa": 6.5,
                "experience": "Portfolio required"
            },
            "description": "Create user-centered designs for web and mobile applications. Conduct user research and usability testing.",
            "benefits": ["Adobe Creative Suite", "Design Courses", "Portfolio Review", "Industry Mentorship"],
            "applicationDeadline": "2024-03-20",
            "startDate": "2024-04-08",
            "isRemote": True,
            "companyRating": 4.4,
            "applicants": 389,
            "tags": ["UI/UX", "Figma", "Design", "Prototyping"]
        },
        {
            "id": "cyber-001",
            "title": "Cybersecurity Analyst Intern",
            "company": "SecureNet Solutions",
            "location": "Delhi, India",
            "domain": "Cybersecurity",
            "duration": "6 months",
            "salary": 46000,
            "requirements": {
                "skills": ["Network Security", "Python", "Ethical Hacking", "Linux", "SIEM"],
                "minCgpa": 7.8,
                "experience": "Security basics"
            },
            "description": "Learn about threat detection, vulnerability assessment, and security incident response.",
            "benefits": ["Security Certifications", "Lab Environment", "Industry Tools", "Expert Mentorship"],
            "applicationDeadline": "2024-03-19",
            "startDate": "2024-04-12",
            "isRemote": False,
            "companyRating": 4.2,
            "applicants": 567,
            "tags": ["Cybersecurity", "Ethical Hacking", "Python", "Security"]
        }
    ]
    return internships

# Sample user profiles
@st.cache_data
def get_sample_profiles():
    return {
        "Arjun Sharma (Frontend Developer)": {
            "name": "Arjun Sharma",
            "email": "arjun.sharma@example.com",
            "skills": ["React", "JavaScript", "HTML", "CSS", "Git"],
            "cgpa": 8.2,
            "portfolio": "https://arjundev.portfolio.com",
            "university": "IIT Delhi",
            "year": "3rd Year",
            "preferences": {
                "location": ["Bangalore", "Mumbai", "Remote"],
                "domains": ["Frontend Development", "Web Development"],
                "salaryRange": [35000, 50000],
                "workMode": "Hybrid"
            }
        },
        "Priya Patel (Data Scientist)": {
            "name": "Priya Patel",
            "email": "priya.patel@example.com",
            "skills": ["Python", "Machine Learning", "Pandas", "NumPy", "TensorFlow"],
            "cgpa": 8.7,
            "portfolio": "https://priyadata.github.io",
            "university": "NIT Surat",
            "year": "4th Year",
            "preferences": {
                "location": ["Bangalore", "Delhi", "Hyderabad"],
                "domains": ["Data Science", "Artificial Intelligence"],
                "salaryRange": [45000, 60000],
                "workMode": "Office"
            }
        },
        "Rahul Kumar (Backend Developer)": {
            "name": "Rahul Kumar",
            "email": "rahul.kumar@example.com",
            "skills": ["Java", "Spring Boot", "MySQL", "REST APIs", "Docker"],
            "cgpa": 7.9,
            "portfolio": "https://rahulbackend.dev",
            "university": "BITS Pilani",
            "year": "3rd Year",
            "preferences": {
                "location": ["Pune", "Hyderabad", "Chennai"],
                "domains": ["Backend Development", "Enterprise Development"],
                "salaryRange": [40000, 55000],
                "workMode": "Office"
            }
        },
        "Sneha Gupta (Full Stack Developer)": {
            "name": "Sneha Gupta",
            "email": "sneha.gupta@example.com",
            "skills": ["React", "Node.js", "MongoDB", "Express", "JavaScript"],
            "cgpa": 8.4,
            "portfolio": "https://snehafullstack.com",
            "university": "Delhi University",
            "year": "4th Year",
            "preferences": {
                "location": ["Mumbai", "Bangalore", "Remote"],
                "domains": ["Full Stack Development", "Web Development"],
                "salaryRange": [42000, 58000],
                "workMode": "Remote"
            }
        },
        "Vikash Singh (Mobile Developer)": {
            "name": "Vikash Singh",
            "email": "vikash.singh@example.com",
            "skills": ["Android", "Kotlin", "Firebase", "Java", "REST APIs"],
            "cgpa": 7.6,
            "portfolio": "https://vikashmobile.dev",
            "university": "Jadavpur University",
            "year": "3rd Year",
            "preferences": {
                "location": ["Chennai", "Bangalore", "Kolkata"],
                "domains": ["Mobile Development", "Android Development"],
                "salaryRange": [35000, 45000],
                "workMode": "Hybrid"
            }
        }
    }

def calculate_match_score(user_profile: Dict, internship: Dict) -> Tuple[float, Dict]:
    """Calculate match score between user profile and internship"""
    score = 0
    reasons = []
    
    # Skills matching (50% weight)
    user_skills = set([skill.lower() for skill in user_profile["skills"]])
    required_skills = set([skill.lower() for skill in internship["requirements"]["skills"]])
    
    skill_overlap = user_skills.intersection(required_skills)
    skill_match_ratio = len(skill_overlap) / len(required_skills) if required_skills else 0
    skill_score = skill_match_ratio * 50
    score += skill_score
    
    if skill_overlap:
        reasons.append(f"Strong skill match: {', '.join(skill_overlap)}")
    
    # CGPA matching (25% weight)
    cgpa_requirement = internship["requirements"]["minCgpa"]
    user_cgpa = user_profile["cgpa"]
    
    if user_cgpa >= cgpa_requirement:
        cgpa_score = 25
        if user_cgpa >= cgpa_requirement + 0.5:
            reasons.append(f"Exceeds CGPA requirement ({user_cgpa} > {cgpa_requirement})")
        else:
            reasons.append(f"Meets CGPA requirement ({user_cgpa} ≥ {cgpa_requirement})")
    else:
        # Partial credit for close CGPAs
        cgpa_diff = cgpa_requirement - user_cgpa
        if cgpa_diff <= 0.3:
            cgpa_score = 15
            reasons.append(f"Close to CGPA requirement ({user_cgpa} vs {cgpa_requirement})")
        else:
            cgpa_score = 0
            reasons.append(f"Below CGPA requirement ({user_cgpa} < {cgpa_requirement})")
    
    score += cgpa_score
    
    # Location matching (15% weight)
    preferred_locations = [loc.lower() for loc in user_profile["preferences"]["location"]]
    internship_location = internship["location"].lower()
    
    location_score = 0
    if "remote" in preferred_locations and internship["isRemote"]:
        location_score = 15
        reasons.append("Matches remote work preference")
    elif any(loc in internship_location for loc in preferred_locations):
        location_score = 15
        reasons.append(f"Matches location preference")
    elif "remote" in internship_location.lower():
        location_score = 10
        reasons.append("Remote option available")
    else:
        location_score = 5
    
    score += location_score
    
    # Domain matching (10% weight)
    preferred_domains = [domain.lower() for domain in user_profile["preferences"]["domains"]]
    internship_domain = internship["domain"].lower()
    
    domain_score = 0
    if any(domain in internship_domain for domain in preferred_domains):
        domain_score = 10
        reasons.append("Matches domain preference")
    else:
        domain_score = 5
    
    score += domain_score
    
    return min(score, 100), {
        "reasons": reasons,
        "skill_match": skill_score,
        "cgpa_match": cgpa_score,
        "location_match": location_score,
        "domain_match": domain_score,
        "skill_overlap": list(skill_overlap)
    }

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎯 Smart Internship Matching Platform</h1>
        <p>Find your perfect internship match based on your skills, CGPA, and preferences</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    internships = load_internships_data()
    sample_profiles = get_sample_profiles()
    
    # Sidebar for user profile
    st.sidebar.header("👤 Your Profile")
    
    # Option to load sample profile
    sample_profile_option = st.sidebar.selectbox(
        "Load Sample Profile (optional)",
        ["Create New Profile"] + list(sample_profiles.keys())
    )
    
    # Initialize profile
    if sample_profile_option != "Create New Profile":
        selected_profile = sample_profiles[sample_profile_option]
        default_name = selected_profile["name"]
        default_email = selected_profile["email"]
        default_skills = selected_profile["skills"]
        default_cgpa = selected_profile["cgpa"]
        default_portfolio = selected_profile["portfolio"]
        default_university = selected_profile["university"]
        default_year = selected_profile["year"]
        default_locations = selected_profile["preferences"]["location"]
        default_domains = selected_profile["preferences"]["domains"]
        default_salary_range = selected_profile["preferences"]["salaryRange"]
        default_work_mode = selected_profile["preferences"]["workMode"]
    else:
        default_name = ""
        default_email = ""
        default_skills = []
        default_cgpa = 7.0
        default_portfolio = ""
        default_university = ""
        default_year = "3rd Year"
        default_locations = []
        default_domains = []
        default_salary_range = [30000, 60000]
        default_work_mode = "Office"
    
    # User input form
    name = st.sidebar.text_input("Full Name", value=default_name)
    email = st.sidebar.text_input("Email", value=default_email)
    cgpa = st.sidebar.slider("CGPA", 0.0, 10.0, default_cgpa, 0.1)
    portfolio = st.sidebar.text_input("Portfolio URL", value=default_portfolio)
    university = st.sidebar.text_input("University", value=default_university)
    year = st.sidebar.selectbox("Year of Study", ["1st Year", "2nd Year", "3rd Year", "4th Year"], 
                               index=["1st Year", "2nd Year", "3rd Year", "4th Year"].index(default_year))
    
    # Skills input
    st.sidebar.subheader("🛠️ Technical Skills")
    all_skills = ["React", "JavaScript", "Python", "Java", "Node.js", "HTML", "CSS", "TypeScript", 
                  "MongoDB", "MySQL", "Express", "Spring Boot", "Git", "Docker", "AWS", "Kubernetes",
                  "Machine Learning", "TensorFlow", "PyTorch", "Pandas", "NumPy", "Scikit-learn",
                  "Android", "Kotlin", "Firebase", "REST APIs", "Redux", "Material-UI", "Figma",
                  "Adobe XD", "Photoshop", "Linux", "CI/CD", "Network Security", "Ethical Hacking"]
    
    selected_skills = st.sidebar.multiselect("Select your skills", all_skills, default=default_skills)
    
    # Add custom skill
    custom_skill = st.sidebar.text_input("Add custom skill")
    if custom_skill and st.sidebar.button("Add Skill"):
        if custom_skill not in selected_skills:
            selected_skills.append(custom_skill)
            st.sidebar.success(f"Added {custom_skill}")
    
    # Preferences
    st.sidebar.subheader("🎯 Preferences")
    
    location_options = ["Bangalore", "Mumbai", "Delhi", "Hyderabad", "Pune", "Chennai", "Kolkata", "Remote"]
    preferred_locations = st.sidebar.multiselect("Preferred Locations", location_options, default=default_locations)
    
    domain_options = ["Frontend Development", "Backend Development", "Full Stack Development", 
                     "Data Science", "Artificial Intelligence", "Mobile Development", "DevOps", 
                     "Design", "Cybersecurity", "Web Development"]
    preferred_domains = st.sidebar.multiselect("Preferred Domains", domain_options, default=default_domains)
    
    salary_range = st.sidebar.slider("Salary Range (₹/month)", 20000, 80000, default_salary_range, 5000)
    work_mode = st.sidebar.selectbox("Work Mode Preference", ["Office", "Remote", "Hybrid"], 
                                    index=["Office", "Remote", "Hybrid"].index(default_work_mode))
    
    # Create user profile
    user_profile = {
        "name": name,
        "email": email,
        "skills": selected_skills,
        "cgpa": cgpa,
        "portfolio": portfolio,
        "university": university,
        "year": year,
        "preferences": {
            "location": preferred_locations,
            "domains": preferred_domains,
            "salaryRange": salary_range,
            "workMode": work_mode
        }
    }
    
    # Main content area
    if name and email and selected_skills:
        st.header("🔍 Your Personalized Internship Matches")
        
        # Calculate matches
        matches = []
        for internship in internships:
            score, details = calculate_match_score(user_profile, internship)
            matches.append({
                "internship": internship,
                "score": score,
                "details": details
            })
        
        # Sort by match score
        matches.sort(key=lambda x: x["score"], reverse=True)
        
        # Filter by salary preference
        filtered_matches = [
            match for match in matches 
            if salary_range[0] <= match["internship"]["salary"] <= salary_range[1]
        ]
        
        if not filtered_matches:
            st.warning("No internships found matching your salary range. Showing all matches:")
            filtered_matches = matches
        
        # Display summary stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Matches", len(filtered_matches))
        with col2:
            high_matches = len([m for m in filtered_matches if m["score"] >= 80])
            st.metric("Excellent Matches (≥80%)", high_matches)
        with col3:
            avg_score = np.mean([m["score"] for m in filtered_matches])
            st.metric("Average Match Score", f"{avg_score:.1f}%")
        with col4:
            avg_salary = np.mean([m["internship"]["salary"] for m in filtered_matches])
            st.metric("Average Salary", f"₹{avg_salary:,.0f}")
        
        # Match score distribution chart
        scores = [match["score"] for match in filtered_matches]
        fig = px.histogram(x=scores, nbins=10, title="Match Score Distribution",
                          labels={'x': 'Match Score (%)', 'y': 'Number of Internships'})
        fig.update_layout(showlegend=False, height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        # Display top matches
        st.subheader("🏆 Top Internship Matches")
        
        for i, match in enumerate(filtered_matches[:10], 1):
            internship = match["internship"]
            score = match["score"]
            details = match["details"]
            
            # Determine match level and color
            if score >= 80:
                match_class = "high-match"
                match_level = "Excellent Match"
            elif score >= 60:
                match_class = "medium-match"
                match_level = "Good Match"
            else:
                match_class = "low-match"
                match_level = "Fair Match"
            
            with st.expander(f"#{i} {internship['title']} at {internship['company']} - {score:.1f}% Match"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Company:** {internship['company']}")
                    st.markdown(f"**Location:** {internship['location']}")
                    st.markdown(f"**Duration:** {internship['duration']}")
                    st.markdown(f"**Domain:** {internship['domain']}")
                    st.markdown(f"**Description:** {internship['description']}")
                    
                    # Required skills
                    st.markdown("**Required Skills:**")
                    skill_tags = ""
                    for skill in internship["requirements"]["skills"]:
                        if skill.lower() in [s.lower() for s in selected_skills]:
                            skill_tags += f'<span class="skill-tag" style="background-color: #28a745;">{skill} ✓</span>'
                        else:
                            skill_tags += f'<span class="skill-tag" style="background-color: #dc3545;">{skill}</span>'
                    st.markdown(skill_tags, unsafe_allow_html=True)
                    
                    # Benefits
                    st.markdown("**Benefits:**")
                    for benefit in internship["benefits"]:
                        st.write(f"• {benefit}")
                
                with col2:
                    st.markdown(f'<div class="match-score {match_class}">{score:.1f}%<br>{match_level}</div>', 
                               unsafe_allow_html=True)
                    
                    st.markdown(f"**Salary:** ₹{internship['salary']:,}/month")
                    st.markdown(f"**Min CGPA:** {internship['requirements']['minCgpa']}")
                    st.markdown(f"**Company Rating:** {'⭐' * int(internship['companyRating'])} {internship['companyRating']}")
                    st.markdown(f"**Applicants:** {internship['applicants']:,}")
                    st.markdown(f"**Remote:** {'Yes' if internship['isRemote'] else 'No'}")
                    
                    # Application deadline
                    deadline = datetime.strptime(internship['applicationDeadline'], '%Y-%m-%d')
                    days_left = (deadline - datetime.now()).days
                    if days_left > 0:
                        st.markdown(f"**Deadline:** {days_left} days left")
                    else:
                        st.markdown("**Deadline:** Expired")
                
                # Match reasons
                st.markdown("**Why this matches you:**")
                for reason in details["reasons"]:
                    st.write(f"✅ {reason}")
                
                # Score breakdown
                with st.expander("Score Breakdown"):
                    breakdown_data = {
                        'Criteria': ['Skills Match', 'CGPA Match', 'Location Match', 'Domain Match'],
                        'Score': [details['skill_match'], details['cgpa_match'], 
                                 details['location_match'], details['domain_match']],
                        'Weight': ['50%', '25%', '15%', '10%']
                    }
                    df_breakdown = pd.DataFrame(breakdown_data)
                    st.dataframe(df_breakdown, use_container_width=True)
        
        # Skills analysis
        st.subheader("📊 Skills Analysis")
        
        # Most in-demand skills
        all_required_skills = []
        for internship in internships:
            all_required_skills.extend(internship["requirements"]["skills"])
        
        skill_counts = pd.Series(all_required_skills).value_counts().head(10)
        
        fig_skills = px.bar(x=skill_counts.values, y=skill_counts.index, 
                           orientation='h', title="Most In-Demand Skills")
        fig_skills.update_layout(yaxis={'categoryorder':'total ascending'}, height=400)
        st.plotly_chart(fig_skills, use_container_width=True)
        
        # User's skill coverage
        user_skill_lower = [skill.lower() for skill in selected_skills]
        covered_skills = [skill for skill in skill_counts.index if skill.lower() in user_skill_lower]
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Skills You Have", len(covered_skills))
        with col2:
            coverage_pct = len(covered_skills) / len(skill_counts.index) * 100
            st.metric("Top Skills Coverage", f"{coverage_pct:.1f}%")
    
    else:
        st.info("👈 Please fill in your profile details in the sidebar to see personalized internship matches!")
        
        # Show demo content
        st.header("🎯 How It Works")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 1. Create Your Profile
            - Add your personal details
            - List your technical skills
            - Set your preferences
            """)
        
        with col2:
            st.markdown("""
            ### 2. AI-Powered Matching
            - Skills matching (50% weight)
            - CGPA requirements (25% weight)
            - Location preferences (15% weight)
            - Domain alignment (10% weight)
            """)
        
        with col3:
            st.markdown("""
            ### 3. Get Ranked Results
            - Personalized match scores
            - Detailed explanations
            - Application deadlines
            - Company insights
            """)
        
        # Sample statistics
        st.header("📈 Platform Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Internships", len(internships))
        with col2:
            st.metric("Partner Companies", len(set([i["company"] for i in internships])))
        with col3:
            avg_salary = np.mean([i["salary"] for i in internships])
            st.metric("Average Salary", f"₹{avg_salary:,.0f}")
        with col4:
            st.metric("Success Rate", "94%")

if __name__ == "__main__":
    main()