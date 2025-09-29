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
    page_title="Smart Allocation System - All India Internship Hub",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS styling for allocation system
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .main > div {
        padding-top: 0rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        font-family: 'Inter', sans-serif;
        animation: gradientShift 20s ease infinite;
        min-height: 100vh;
    }
    
    @keyframes gradientShift {
        0% { background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%); }
        25% { background: linear-gradient(135deg, #f093fb 0%, #4facfe 25%, #00f2fe 50%, #667eea 75%, #764ba2 100%); }
        50% { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 25%, #667eea 50%, #764ba2 75%, #f093fb 100%); }
        75% { background: linear-gradient(135deg, #00f2fe 0%, #667eea 25%, #764ba2 50%, #f093fb 75%, #4facfe 100%); }
        100% { background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%); }
    }
    
    .allocation-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 2.5rem;
        margin: 1rem;
        backdrop-filter: blur(25px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.8);
        position: relative;
        overflow: hidden;
        color: #1f2937;
    }
    
    .allocation-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #4facfe, #00f2fe);
        animation: shimmer 3s linear infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .allocation-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .allocation-subheader {
        text-align: center;
        color: #6b7280;
        font-size: 1.3rem;
        font-weight: 500;
        margin-bottom: 3rem;
    }
    
    .preference-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.95));
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 2px solid rgba(102, 126, 234, 0.2);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .preference-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 50px rgba(102, 126, 234, 0.2);
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    .preference-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
    }
    
    .allocation-result {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.3);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .allocation-result::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(248,250,252,0.9));
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(102, 126, 234, 0.2);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.1);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.2);
    }
    
    .progress-container {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .allocation-button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 1rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3) !important;
    }
    
    .allocation-button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4) !important;
    }
    
    .sidebar-content {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.95));
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        border: 1px solid rgba(102, 126, 234, 0.3);
    }
    
    .stSlider > div > div {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }
</style>
""", unsafe_allow_html=True)

# Mock data for comprehensive allocation system
def load_allocation_data():
    """Load comprehensive data for allocation system"""
    
    # Enhanced internship data with detailed information
    internships_data = {
        'Technology': [
            {
                'id': 'TECH001',
                'title': 'Full Stack Developer Intern',
                'company': 'TechCorp India',
                'location': 'Bangalore',
                'duration': '6 months',
                'stipend': '₹25,000/month',
                'skills_required': ['React', 'Node.js', 'MongoDB', 'JavaScript'],
                'difficulty': 'Intermediate',
                'remote_option': True,
                'start_date': '2025-11-01',
                'slots': 15,
                'filled': 3
            },
            {
                'id': 'TECH002',
                'title': 'AI/ML Research Intern',
                'company': 'DeepMind India',
                'location': 'Hyderabad',
                'duration': '4 months',
                'stipend': '₹35,000/month',
                'skills_required': ['Python', 'TensorFlow', 'Machine Learning', 'Data Science'],
                'difficulty': 'Advanced',
                'remote_option': True,
                'start_date': '2025-10-15',
                'slots': 8,
                'filled': 1
            },
            {
                'id': 'TECH003',
                'title': 'Mobile App Developer',
                'company': 'AppSolutions',
                'location': 'Pune',
                'duration': '5 months',
                'stipend': '₹22,000/month',
                'skills_required': ['Flutter', 'Dart', 'Firebase', 'REST APIs'],
                'difficulty': 'Intermediate',
                'remote_option': False,
                'start_date': '2025-12-01',
                'slots': 12,
                'filled': 5
            }
        ],
        'Finance': [
            {
                'id': 'FIN001',
                'title': 'Investment Banking Analyst',
                'company': 'Goldman Sachs India',
                'location': 'Mumbai',
                'duration': '6 months',
                'stipend': '₹40,000/month',
                'skills_required': ['Financial Analysis', 'Excel', 'Bloomberg Terminal', 'Valuation'],
                'difficulty': 'Advanced',
                'remote_option': False,
                'start_date': '2025-11-15',
                'slots': 6,
                'filled': 2
            },
            {
                'id': 'FIN002',
                'title': 'Risk Management Intern',
                'company': 'ICICI Bank',
                'location': 'Delhi',
                'duration': '4 months',
                'stipend': '₹28,000/month',
                'skills_required': ['Risk Analysis', 'Statistics', 'R/Python', 'Financial Modeling'],
                'difficulty': 'Intermediate',
                'remote_option': True,
                'start_date': '2025-10-30',
                'slots': 10,
                'filled': 3
            }
        ],
        'Healthcare': [
            {
                'id': 'HEALTH001',
                'title': 'Medical Research Assistant',
                'company': 'AIIMS Delhi',
                'location': 'Delhi',
                'duration': '6 months',
                'stipend': '₹18,000/month',
                'skills_required': ['Research Methods', 'Data Analysis', 'Medical Knowledge', 'Statistics'],
                'difficulty': 'Intermediate',
                'remote_option': False,
                'start_date': '2025-11-01',
                'slots': 20,
                'filled': 8
            }
        ],
        'Marketing': [
            {
                'id': 'MKT001',
                'title': 'Digital Marketing Strategist',
                'company': 'Ogilvy India',
                'location': 'Mumbai',
                'duration': '5 months',
                'stipend': '₹24,000/month',
                'skills_required': ['SEO/SEM', 'Social Media', 'Analytics', 'Content Strategy'],
                'difficulty': 'Intermediate',
                'remote_option': True,
                'start_date': '2025-10-20',
                'slots': 15,
                'filled': 7
            }
        ]
    }
    
    # Student profiles for matching
    student_profiles = [
        {
            'id': 'STU001',
            'name': 'Arjun Sharma',
            'skills': ['Python', 'Machine Learning', 'Data Science', 'TensorFlow'],
            'gpa': 8.7,
            'year': 'Final Year',
            'branch': 'Computer Science',
            'location_preference': ['Bangalore', 'Hyderabad', 'Remote'],
            'field_interest': 'Technology',
            'experience_level': 'Intermediate'
        },
        {
            'id': 'STU002',
            'name': 'Priya Patel',
            'skills': ['Financial Analysis', 'Excel', 'Bloomberg', 'Statistics'],
            'gpa': 9.1,
            'year': 'Third Year',
            'branch': 'Finance',
            'location_preference': ['Mumbai', 'Delhi'],
            'field_interest': 'Finance',
            'experience_level': 'Advanced'
        },
        {
            'id': 'STU003',
            'name': 'Rahul Kumar',
            'skills': ['React', 'Node.js', 'JavaScript', 'MongoDB'],
            'gpa': 8.3,
            'year': 'Final Year',
            'branch': 'Computer Science',
            'location_preference': ['Bangalore', 'Pune', 'Remote'],
            'field_interest': 'Technology',
            'experience_level': 'Intermediate'
        }
    ]
    
    return internships_data, student_profiles

def calculate_match_score(student, internship):
    """Calculate match score between student and internship"""
    score = 0
    
    # Skills match (40% weight)
    student_skills = set([skill.lower() for skill in student['skills']])
    required_skills = set([skill.lower() for skill in internship['skills_required']])
    skill_match = len(student_skills.intersection(required_skills)) / len(required_skills)
    score += skill_match * 40
    
    # Location preference (20% weight)
    if internship['location'] in student['location_preference'] or internship['remote_option']:
        score += 20
    
    # Field interest match (25% weight)
    if student['field_interest'].lower() == internship.get('field', '').lower():
        score += 25
    
    # Experience level match (15% weight)
    experience_match = {
        ('Beginner', 'Beginner'): 15,
        ('Intermediate', 'Intermediate'): 15,
        ('Advanced', 'Advanced'): 15,
        ('Intermediate', 'Beginner'): 12,
        ('Advanced', 'Intermediate'): 12,
        ('Advanced', 'Beginner'): 8
    }
    score += experience_match.get((student['experience_level'], internship['difficulty']), 5)
    
    return min(100, score)

def smart_allocation_algorithm(students, internships, preferences):
    """Advanced allocation algorithm based on preferences and constraints"""
    allocations = []
    
    # Calculate all possible matches with scores
    matches = []
    for student in students:
        for field, field_internships in internships.items():
            for internship in field_internships:
                if internship['filled'] < internship['slots']:
                    score = calculate_match_score(student, internship)
                    matches.append({
                        'student': student,
                        'internship': internship,
                        'score': score,
                        'field': field
                    })
    
    # Sort matches by score (descending)
    matches.sort(key=lambda x: x['score'], reverse=True)
    
    # Apply preferences and constraints
    allocated_students = set()
    internship_counts = {}
    
    for match in matches:
        student_id = match['student']['id']
        internship_id = match['internship']['id']
        
        # Check if student already allocated
        if student_id in allocated_students:
            continue
            
        # Check internship capacity
        current_filled = internship_counts.get(internship_id, match['internship']['filled'])
        if current_filled >= match['internship']['slots']:
            continue
            
        # Apply preference filters
        if preferences['min_match_score'] > 0 and match['score'] < preferences['min_match_score']:
            continue
            
        # Allocate
        allocations.append({
            'student_name': match['student']['name'],
            'student_id': student_id,
            'internship_title': match['internship']['title'],
            'company': match['internship']['company'],
            'location': match['internship']['location'],
            'match_score': match['score'],
            'stipend': match['internship']['stipend'],
            'field': match['field'],
            'start_date': match['internship']['start_date']
        })
        
        allocated_students.add(student_id)
        internship_counts[internship_id] = current_filled + 1
        
        # Stop if we've allocated enough
        if len(allocations) >= preferences['max_allocations']:
            break
    
    return allocations

def main():
    # Custom CSS container
    st.markdown('<div class="allocation-container">', unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="allocation-header">🎯 Smart Allocation System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="allocation-subheader">AI-Powered Internship Allocation Based on Your Preferences</p>', unsafe_allow_html=True)
    
    # Load data
    internships_data, student_profiles = load_allocation_data()
    
    # Sidebar for preferences and controls
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown("### 🎛️ Allocation Preferences")
        
        # Allocation parameters
        max_allocations = st.slider("Maximum Allocations", 1, 50, 20)
        min_match_score = st.slider("Minimum Match Score (%)", 0, 100, 60)
        
        st.markdown("### 📊 Filter Options")
        selected_fields = st.multiselect(
            "Select Fields", 
            list(internships_data.keys()),
            default=list(internships_data.keys())
        )
        
        location_filter = st.selectbox(
            "Location Priority",
            ["All Locations", "Remote Preferred", "On-site Only", "Bangalore", "Mumbai", "Delhi", "Hyderabad", "Pune"]
        )
        
        experience_filter = st.selectbox(
            "Experience Level",
            ["All Levels", "Beginner", "Intermediate", "Advanced"]
        )
        
        st.markdown("### ⚡ Quick Actions")
        run_allocation = st.button("🚀 Run Smart Allocation", key="allocation_btn", help="Run the AI allocation algorithm")
        reset_allocation = st.button("🔄 Reset All", help="Reset all preferences")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Allocation preferences card
        st.markdown('<div class="preference-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Allocation Preferences Setup")
        
        preferences = {
            'max_allocations': max_allocations,
            'min_match_score': min_match_score,
            'selected_fields': selected_fields,
            'location_filter': location_filter,
            'experience_filter': experience_filter
        }
        
        # Display current preferences
        pref_col1, pref_col2, pref_col3 = st.columns(3)
        with pref_col1:
            st.metric("Max Allocations", max_allocations)
        with pref_col2:
            st.metric("Min Match Score", f"{min_match_score}%")
        with pref_col3:
            st.metric("Selected Fields", len(selected_fields))
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Run allocation
        if run_allocation:
            with st.spinner("🤖 Running Smart Allocation Algorithm..."):
                # Simulate processing time
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(i + 1)
                
                # Run allocation algorithm
                allocations = smart_allocation_algorithm(student_profiles, internships_data, preferences)
                
                # Store results in session state
                st.session_state.allocation_results = allocations
                st.session_state.allocation_timestamp = datetime.now()
                
                st.success(f"✅ Successfully allocated {len(allocations)} internships!")
        
        # Display allocation results
        if 'allocation_results' in st.session_state and st.session_state.allocation_results:
            st.markdown('<div class="allocation-result">', unsafe_allow_html=True)
            st.markdown("### 🎉 Allocation Results")
            st.markdown(f"**Generated on:** {st.session_state.allocation_timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            st.markdown(f"**Total Allocations:** {len(st.session_state.allocation_results)}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Results table
            df_results = pd.DataFrame(st.session_state.allocation_results)
            
            # Enhanced table display
            st.markdown("### 📋 Detailed Allocation Table")
            
            # Add filters for results
            result_col1, result_col2, result_col3 = st.columns(3)
            with result_col1:
                field_filter = st.selectbox("Filter by Field", ["All"] + list(df_results['field'].unique()))
            with result_col2:
                score_range = st.slider("Match Score Range", 0, 100, (60, 100))
            with result_col3:
                sort_by = st.selectbox("Sort by", ["Match Score", "Student Name", "Company", "Field"])
            
            # Apply filters
            filtered_df = df_results.copy()
            if field_filter != "All":
                filtered_df = filtered_df[filtered_df['field'] == field_filter]
            filtered_df = filtered_df[
                (filtered_df['match_score'] >= score_range[0]) & 
                (filtered_df['match_score'] <= score_range[1])
            ]
            
            # Sort results
            if sort_by == "Match Score":
                filtered_df = filtered_df.sort_values('match_score', ascending=False)
            elif sort_by == "Student Name":
                filtered_df = filtered_df.sort_values('student_name')
            elif sort_by == "Company":
                filtered_df = filtered_df.sort_values('company')
            elif sort_by == "Field":
                filtered_df = filtered_df.sort_values('field')
            
            # Display table with styling
            st.dataframe(
                filtered_df[['student_name', 'internship_title', 'company', 'location', 'match_score', 'stipend', 'field']].rename(columns={
                    'student_name': 'Student',
                    'internship_title': 'Internship',
                    'company': 'Company',
                    'location': 'Location',
                    'match_score': 'Match %',
                    'stipend': 'Stipend',
                    'field': 'Field'
                }),
                use_container_width=True,
                height=400
            )
            
            # Download results
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name=f"allocation_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
    
    with col2:
        # Statistics and analytics
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("### 📊 System Statistics")
        
        total_internships = sum(len(internships) for internships in internships_data.values())
        total_students = len(student_profiles)
        
        st.metric("Total Students", total_students)
        st.metric("Available Internships", total_internships)
        st.metric("Success Rate", "85.7%")
        
        if 'allocation_results' in st.session_state:
            allocated_count = len(st.session_state.allocation_results)
            avg_score = np.mean([r['match_score'] for r in st.session_state.allocation_results])
            st.metric("Allocated", allocated_count)
            st.metric("Avg Match Score", f"{avg_score:.1f}%")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Allocation analytics
        if 'allocation_results' in st.session_state and st.session_state.allocation_results:
            st.markdown("### 📈 Allocation Analytics")
            
            df_results = pd.DataFrame(st.session_state.allocation_results)
            
            # Match score distribution
            fig_score = px.histogram(
                df_results, 
                x='match_score', 
                nbins=10,
                title="Match Score Distribution",
                color_discrete_sequence=['#667eea']
            )
            fig_score.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=250
            )
            st.plotly_chart(fig_score, use_container_width=True)
            
            # Field distribution
            field_counts = df_results['field'].value_counts()
            fig_field = px.pie(
                values=field_counts.values,
                names=field_counts.index,
                title="Allocations by Field",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_field.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=250
            )
            st.plotly_chart(fig_field, use_container_width=True)
    
    # Available internships overview
    st.markdown("### 🏢 Available Internships Overview")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔧 Technology", "💰 Finance", "🏥 Healthcare", "📈 Marketing"])
    
    with tab1:
        if 'Technology' in selected_fields:
            for internship in internships_data['Technology']:
                with st.expander(f"{internship['title']} - {internship['company']}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**Location:** {internship['location']}")
                        st.write(f"**Duration:** {internship['duration']}")
                        st.write(f"**Stipend:** {internship['stipend']}")
                    with col2:
                        st.write(f"**Difficulty:** {internship['difficulty']}")
                        st.write(f"**Remote:** {'Yes' if internship['remote_option'] else 'No'}")
                        st.write(f"**Start Date:** {internship['start_date']}")
                    with col3:
                        st.write(f"**Available Slots:** {internship['slots'] - internship['filled']}/{internship['slots']}")
                        st.progress((internship['filled'] / internship['slots']))
                    
                    st.write(f"**Required Skills:** {', '.join(internship['skills_required'])}")
    
    with tab2:
        if 'Finance' in selected_fields:
            for internship in internships_data['Finance']:
                with st.expander(f"{internship['title']} - {internship['company']}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**Location:** {internship['location']}")
                        st.write(f"**Duration:** {internship['duration']}")
                        st.write(f"**Stipend:** {internship['stipend']}")
                    with col2:
                        st.write(f"**Difficulty:** {internship['difficulty']}")
                        st.write(f"**Remote:** {'Yes' if internship['remote_option'] else 'No'}")
                        st.write(f"**Start Date:** {internship['start_date']}")
                    with col3:
                        st.write(f"**Available Slots:** {internship['slots'] - internship['filled']}/{internship['slots']}")
                        st.progress((internship['filled'] / internship['slots']))
                    
                    st.write(f"**Required Skills:** {', '.join(internship['skills_required'])}")
    
    with tab3:
        if 'Healthcare' in selected_fields:
            for internship in internships_data['Healthcare']:
                with st.expander(f"{internship['title']} - {internship['company']}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**Location:** {internship['location']}")
                        st.write(f"**Duration:** {internship['duration']}")
                        st.write(f"**Stipend:** {internship['stipend']}")
                    with col2:
                        st.write(f"**Difficulty:** {internship['difficulty']}")
                        st.write(f"**Remote:** {'Yes' if internship['remote_option'] else 'No'}")
                        st.write(f"**Start Date:** {internship['start_date']}")
                    with col3:
                        st.write(f"**Available Slots:** {internship['slots'] - internship['filled']}/{internship['slots']}")
                        st.progress((internship['filled'] / internship['slots']))
                    
                    st.write(f"**Required Skills:** {', '.join(internship['skills_required'])}")
    
    with tab4:
        if 'Marketing' in selected_fields:
            for internship in internships_data['Marketing']:
                with st.expander(f"{internship['title']} - {internship['company']}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**Location:** {internship['location']}")
                        st.write(f"**Duration:** {internship['duration']}")
                        st.write(f"**Stipend:** {internship['stipend']}")
                    with col2:
                        st.write(f"**Difficulty:** {internship['difficulty']}")
                        st.write(f"**Remote:** {'Yes' if internship['remote_option'] else 'No'}")
                        st.write(f"**Start Date:** {internship['start_date']}")
                    with col3:
                        st.write(f"**Available Slots:** {internship['slots'] - internship['filled']}/{internship['slots']}")
                        st.progress((internship['filled'] / internship['slots']))
                    
                    st.write(f"**Required Skills:** {', '.join(internship['skills_required'])}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6b7280; padding: 2rem;'>
        <p>🎯 Smart Allocation System - Powered by AI | Part of All India Internship Hub</p>
        <p>Connecting talent with opportunities across India 🇮🇳</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()