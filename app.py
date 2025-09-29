import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import time
import random
import hashlib

# Configure the page
st.set_page_config(
    page_title="PM Internship Smart Allocation Engine",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'allocation_results' not in st.session_state:
    st.session_state.allocation_results = []
if 'notifications' not in st.session_state:
    st.session_state.notifications = []
if 'page' not in st.session_state:
    st.session_state.page = 'Dashboard'

# Custom CSS for modern design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .sub-header {
        font-size: 1.25rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 500;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    
    .gradient-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
    }
    
    .status-card {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem;
        border-left: 4px solid #10b981;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 0.75rem;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    
    .sidebar-button {
        width: 100%;
        margin: 0.5rem 0;
        padding: 0.75rem;
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 1px solid #e2e8f0;
        border-radius: 0.75rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .sidebar-button:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .notification-badge {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 1rem;
        font-size: 0.75rem;
        font-weight: 600;
        margin-left: 0.5rem;
    }
    
    .success-badge {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .warning-badge {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .alert-badge {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .allocation-card {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #e2e8f0;
        margin: 1rem 0;
        box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .allocation-card:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 0.5rem;
        border-radius: 0.25rem;
        transition: width 0.3s ease;
    }
    
    .animate-pulse {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: .5;
        }
    }
</style>
""", unsafe_allow_html=True)

# Mock Data
@st.cache_data
def load_mock_data():
    """Load mock candidate and internship data"""
    candidates_data = {
        'name': ['Rajesh Kumar', 'Priya Sharma', 'Amit Patel', 'Sneha Singh', 'Vikram Reddy', 
                'Anita Das', 'Rohit Gupta', 'Meera Jain', 'Arjun Nair', 'Kavitha Rao'],
        'skills': [
            ['Python', 'Machine Learning', 'Data Analysis'],
            ['JavaScript', 'React', 'Node.js'],
            ['Java', 'Spring Boot', 'Microservices'],
            ['UI/UX Design', 'Figma', 'Adobe XD'],
            ['DevOps', 'AWS', 'Docker'],
            ['Data Science', 'R', 'Statistics'],
            ['Mobile Development', 'Flutter', 'Firebase'],
            ['Cybersecurity', 'Ethical Hacking', 'Network Security'],
            ['Blockchain', 'Solidity', 'Web3'],
            ['AI/ML', 'TensorFlow', 'Computer Vision']
        ],
        'education': ['B.Tech CSE', 'B.Tech IT', 'B.Tech ECE', 'BCA', 'M.Tech', 
                     'B.Sc Computer Science', 'B.Tech', 'MCA', 'B.Tech CSE', 'M.Sc Data Science'],
        'location': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Hyderabad', 
                    'Pune', 'Kolkata', 'Ahmedabad', 'Jaipur', 'Lucknow'],
        'experience': [0, 1, 2, 0, 3, 1, 0, 2, 1, 0],
        'score': [85, 78, 92, 73, 88, 91, 67, 84, 79, 94]
    }
    
    internships_data = {
        'title': ['Software Developer Intern', 'Data Analyst Intern', 'UI/UX Designer Intern',
                 'DevOps Engineer Intern', 'Mobile App Developer Intern', 'Cybersecurity Intern',
                 'AI/ML Research Intern', 'Full Stack Developer Intern', 'Cloud Engineer Intern',
                 'Business Analyst Intern'],
        'company': ['TechCorp India', 'DataInsights Ltd', 'DesignHub', 'CloudTech Solutions',
                   'MobileTech', 'SecureNet', 'AI Innovations', 'WebSolutions', 'CloudFirst',
                   'BusinessLogic Inc'],
        'location': ['Bangalore', 'Mumbai', 'Delhi', 'Hyderabad', 'Pune',
                    'Chennai', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore'],
        'duration': ['3 months', '6 months', '4 months', '3 months', '6 months',
                    '4 months', '6 months', '3 months', '4 months', '3 months'],
        'stipend': [15000, 12000, 18000, 20000, 16000, 22000, 25000, 17000, 21000, 14000],
        'required_skills': [
            ['Python', 'JavaScript', 'Git'],
            ['Python', 'SQL', 'Excel'],
            ['Figma', 'Adobe XD', 'Sketch'],
            ['AWS', 'Docker', 'Linux'],
            ['Flutter', 'React Native', 'Firebase'],
            ['Network Security', 'Linux', 'Python'],
            ['TensorFlow', 'Python', 'Machine Learning'],
            ['React', 'Node.js', 'MongoDB'],
            ['AWS', 'Azure', 'Kubernetes'],
            ['Excel', 'PowerBI', 'SQL']
        ]
    }
    
    candidates_df = pd.DataFrame(candidates_data)
    internships_df = pd.DataFrame(internships_data)
    
    return candidates_df, internships_df

def calculate_match_score(candidate_skills, required_skills):
    """Calculate matching score between candidate and internship"""
    candidate_set = set([skill.lower() for skill in candidate_skills])
    required_set = set([skill.lower() for skill in required_skills])
    
    intersection = len(candidate_set.intersection(required_set))
    union = len(candidate_set.union(required_set))
    
    if union == 0:
        return 0
    
    jaccard_score = intersection / union
    skill_match_score = (intersection / len(required_set)) * 100
    
    # Add some randomness to make it more realistic
    final_score = min(100, skill_match_score + random.randint(-10, 15))
    return max(0, final_score)

def create_sidebar():
    """Create enhanced sidebar with navigation"""
    st.sidebar.markdown("### 🎯 Navigation")
    
    pages = {
        '🏠 Dashboard': 'Dashboard',
        '👥 Candidates': 'Candidates', 
        '🏢 Internships': 'Internships',
        '🤖 Smart Allocation': 'Smart Allocation',
        '📊 Analytics': 'Analytics',
        '🔔 Notifications': 'Notifications',
        '⚙️ Settings': 'Settings'
    }
    
    for idx, (icon_name, page_name) in enumerate(pages.items()):
        # Create unique safe key using simple concatenation
        safe_page_name = page_name.replace(' ', '_').lower()
        unique_key = f"sidebar_nav_{idx}_{safe_page_name}"
        if st.sidebar.button(icon_name, key=unique_key, help=f"Go to {page_name}"):
            st.session_state.page = page_name
            st.rerun()
    
    # Notification counter
    unread_notifications = len([n for n in st.session_state.notifications if not n.get('read', False)])
    if unread_notifications > 0:
        st.sidebar.markdown(f"### 🔔 Notifications <span class='notification-badge'>{unread_notifications}</span>", 
                          unsafe_allow_html=True)

def show_dashboard():
    """Enhanced dashboard with modern UI"""
    st.title('📊 PM Internship Dashboard')
    st.markdown('**Real-time overview of allocation system performance**')
    
    candidates_df, internships_df = load_mock_data()
    
    # Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #3b82f6; margin: 0;">👥 Total Candidates</h3>
            <h2 style="color: #1f2937; margin: 0.5rem 0 0 0;">{}</h2>
            <p style="color: #10b981; margin: 0; font-size: 0.875rem;">+12% from last month</p>
        </div>
        """.format(len(candidates_df)), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #8b5cf6; margin: 0;">🏢 Available Positions</h3>
            <h2 style="color: #1f2937; margin: 0.5rem 0 0 0;">{}</h2>
            <p style="color: #10b981; margin: 0; font-size: 0.875rem;">+8% from last month</p>
        </div>
        """.format(len(internships_df)), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #10b981; margin: 0;">✅ Success Rate</h3>
            <h2 style="color: #1f2937; margin: 0.5rem 0 0 0;">87%</h2>
            <p style="color: #10b981; margin: 0; font-size: 0.875rem;">+5% from last month</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #f59e0b; margin: 0;">⏱️ Avg. Time</h3>
            <h2 style="color: #1f2937; margin: 0.5rem 0 0 0;">2.3h</h2>
            <p style="color: #10b981; margin: 0; font-size: 0.875rem;">-15% from last month</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Recent Activity and Quick Actions
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📈 Recent Activity")
        
        activities = [
            {"time": "2 min ago", "activity": "New candidate registered: Rajesh Kumar", "type": "success"},
            {"time": "5 min ago", "activity": "Allocation completed for batch #234", "type": "success"},
            {"time": "10 min ago", "activity": "12 applications require approval", "type": "warning"},
            {"time": "15 min ago", "activity": "System maintenance scheduled", "type": "info"},
            {"time": "30 min ago", "activity": "Monthly report generated", "type": "success"}
        ]
        
        for activity in activities:
            badge_class = {
                "success": "success-badge",
                "warning": "warning-badge", 
                "info": "alert-badge"
            }.get(activity["type"], "success-badge")
            
            st.markdown(f"""
            <div class="status-card">
                <div style="display: flex; justify-content: between; align-items: center;">
                    <div>
                        <p style="margin: 0; font-weight: 500;">{activity['activity']}</p>
                        <p style="margin: 0; color: #64748b; font-size: 0.875rem;">{activity['time']}</p>
                    </div>
                    <span class="{badge_class}">{activity['type'].title()}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### ⚡ Quick Actions")
        
        if st.button("🚀 Run AI Allocation", key="dashboard_run_allocation", help="Start automated allocation process"):
            st.session_state.page = 'Smart Allocation'
            st.rerun()
        
        if st.button("👥 View Candidates", key="dashboard_view_candidates", help="Manage candidate profiles"):
            st.session_state.page = 'Candidates'
            st.rerun()
            
        if st.button("🏢 Manage Internships", key="dashboard_manage_internships", help="View internship positions"):
            st.session_state.page = 'Internships'
            st.rerun()
            
        if st.button("📊 Analytics Report", key="dashboard_analytics_report", help="View detailed analytics"):
            st.session_state.page = 'Analytics'
            st.rerun()
        
        st.markdown("### 🔔 System Status")
        st.markdown("""
        <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                    color: white; padding: 1rem; border-radius: 0.75rem; text-align: center;">
            <h4 style="margin: 0;">🟢 All Systems Operational</h4>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.875rem;">Last updated: 2 minutes ago</p>
        </div>
        """, unsafe_allow_html=True)

def show_candidates():
    """Enhanced candidates management interface"""
    st.title('👥 Candidate Management')
    st.markdown('**Manage and view candidate profiles with advanced filtering**')
    
    candidates_df, _ = load_mock_data()
    
    # Search and Filter
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search_term = st.text_input("🔍 Search candidates", placeholder="Search by name, skills, or location...")
    
    with col2:
        location_filter = st.selectbox("📍 Filter by Location", 
                                     ['All'] + sorted(candidates_df['location'].unique().tolist()))
    
    with col3:
        education_filter = st.selectbox("🎓 Filter by Education", 
                                      ['All'] + sorted(candidates_df['education'].unique().tolist()))
    
    # Apply filters
    filtered_df = candidates_df.copy()
    
    if search_term:
        filtered_df = filtered_df[
            filtered_df['name'].str.contains(search_term, case=False) |
            filtered_df['location'].str.contains(search_term, case=False) |
            filtered_df['education'].str.contains(search_term, case=False)
        ]
    
    if location_filter != 'All':
        filtered_df = filtered_df[filtered_df['location'] == location_filter]
        
    if education_filter != 'All':
        filtered_df = filtered_df[filtered_df['education'] == education_filter]
    
    st.markdown(f"### 📋 Candidates ({len(filtered_df)} found)")
    
    # Display candidates in cards
    for idx, row in filtered_df.iterrows():
        skills_str = ", ".join(row['skills'][:3]) + ("..." if len(row['skills']) > 3 else "")
        
        # Use proper Streamlit components instead of raw HTML
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader(f"👤 {row['name']}")
                st.write(f"**{row['education']}** • {row['location']}")
                st.write(f"🛠️ **Skills:** {skills_str}")
                
                # Experience and status badges
                exp_text = f"💼 {row['experience']} years exp"
                st.write(f"{exp_text} | ✅ Available")
            
            with col2:
                st.metric("Match Score", f"{row['score']}%", help="AI-calculated compatibility score")
        
        st.divider()

def show_internships():
    """Enhanced internships management interface"""
    st.title('🏢 Internship Positions')
    st.markdown('**Manage available internship opportunities and requirements**')
    
    _, internships_df = load_mock_data()
    
    # Search and Filter
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search_term = st.text_input("🔍 Search internships", placeholder="Search by title, company, or skills...")
    
    with col2:
        location_filter = st.selectbox("📍 Filter by Location", 
                                     ['All'] + sorted(internships_df['location'].unique().tolist()))
    
    with col3:
        duration_filter = st.selectbox("⏱️ Filter by Duration", 
                                     ['All'] + sorted(internships_df['duration'].unique().tolist()))
    
    # Apply filters
    filtered_df = internships_df.copy()
    
    if search_term:
        filtered_df = filtered_df[
            filtered_df['title'].str.contains(search_term, case=False) |
            filtered_df['company'].str.contains(search_term, case=False)
        ]
    
    if location_filter != 'All':
        filtered_df = filtered_df[filtered_df['location'] == location_filter]
        
    if duration_filter != 'All':
        filtered_df = filtered_df[filtered_df['duration'] == duration_filter]
    
    st.markdown(f"### 📋 Available Positions ({len(filtered_df)} found)")
    
    # Display internships in cards
    for idx, row in filtered_df.iterrows():
        skills_str = ", ".join(row['required_skills'][:3]) + ("..." if len(row['required_skills']) > 3 else "")
        
        # Use proper Streamlit components instead of raw HTML
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader(f"🏢 {row['title']}")
                st.write(f"**{row['company']}**")
                st.write(f"📍 {row['location']} • ⏱️ {row['duration']}")
                st.write(f"🛠️ **Required Skills:** {skills_str}")
                st.write("🟡 Open | 📋 Remote Friendly")
            
            with col2:
                st.metric("Monthly Stipend", f"₹{row['stipend']:,}", help="Stipend amount per month")
        
        st.divider()

def show_smart_allocation():
    """Enhanced AI allocation interface"""
    st.title('🤖 Smart AI Allocation Engine')
    st.markdown('**Intelligent matching system with real-time processing and detailed analytics**')
    
    candidates_df, internships_df = load_mock_data()
    
    # Algorithm Configuration
    st.markdown("### ⚙️ Algorithm Configuration")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        skills_weight = st.slider("🎯 Skills Weight", 0, 100, 40, help="Importance of skill matching")
    
    with col2:
        location_weight = st.slider("📍 Location Weight", 0, 100, 20, help="Importance of location preference")
    
    with col3:
        experience_weight = st.slider("💼 Experience Weight", 0, 100, 20, help="Importance of experience level")
    
    with col4:
        availability_weight = st.slider("⏰ Availability Weight", 0, 100, 20, help="Importance of time availability")
    
    # Allocation Controls
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 🚀 Allocation Control Panel")
        
        # Algorithm overview
        with st.expander("🧠 View Algorithm Details", expanded=False):
            st.markdown("""
            **AI Matching Algorithm:**
            - **Skills Analysis (40%)**: NLP-based skill compatibility scoring
            - **Location Match (20%)**: Geographic preference alignment
            - **Experience Level (20%)**: Background and expertise matching
            - **Availability (20%)**: Duration and timing compatibility
            
            **Machine Learning Features:**
            - Jaccard similarity for skill matching
            - Weighted scoring system
            - Real-time processing with progress tracking
            - Detailed reasoning for each allocation
            """)
    
    with col2:
        if st.button("🚀 Run AI Allocation", key="smart_allocation_run", help="Start the intelligent allocation process", type="primary"):
            run_allocation_process(candidates_df, internships_df)
    
    # Show allocation results if available
    if st.session_state.allocation_results:
        show_allocation_results()

def run_allocation_process(candidates_df, internships_df):
    """Run the AI allocation process with progress tracking"""
    st.markdown("### 🔄 Processing Allocations...")
    
    # Progress tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    results = []
    total_candidates = len(candidates_df)
    
    for idx, candidate_row in candidates_df.iterrows():
        # Update progress
        progress = (idx + 1) / total_candidates
        progress_bar.progress(progress)
        status_text.text(f"Processing candidate {idx + 1}/{total_candidates}: {candidate_row['name']}")
        
        # Simulate processing time
        time.sleep(0.5)
        
        # Calculate match scores for all internships
        candidate_scores = []
        for _, internship_row in internships_df.iterrows():
            score = calculate_match_score(candidate_row['skills'], internship_row['required_skills'])
            candidate_scores.append({
                'internship_title': internship_row['title'],
                'company': internship_row['company'],
                'score': score,
                'internship_data': internship_row
            })
        
        # Get best match
        best_match = max(candidate_scores, key=lambda x: x['score'])
        
        # Determine status
        if best_match['score'] >= 70:
            status = 'allocated'
        elif best_match['score'] >= 50:
            status = 'waitlisted'
        else:
            status = 'not-matched'
        
        # Generate reasoning
        reasoning = generate_allocation_reasoning(candidate_row, best_match, best_match['score'])
        
        results.append({
            'candidate_name': candidate_row['name'],
            'candidate_data': candidate_row,
            'best_match': best_match,
            'status': status,
            'reasoning': reasoning
        })
    
    # Store results in session state
    st.session_state.allocation_results = results
    
    # Add success notification
    st.session_state.notifications.append({
        'type': 'success',
        'title': 'Allocation Completed',
        'message': f'Successfully processed {len(results)} candidates',
        'timestamp': datetime.now(),
        'read': False
    })
    
    progress_bar.progress(1.0)
    status_text.text("✅ Allocation process completed!")
    
    st.success(f"🎉 Successfully allocated {len(results)} candidates!")
    st.balloons()

def generate_allocation_reasoning(candidate, best_match, score):
    """Generate human-readable reasoning for allocation decisions"""
    reasons = []
    
    if score >= 90:
        reasons.append("🎯 Perfect skills alignment detected")
        reasons.append("📍 Ideal location and preference match")
    elif score >= 70:
        reasons.append("✨ Strong skills compatibility found")
        reasons.append("🏢 Good organizational culture fit")
    elif score >= 50:
        reasons.append("⚠️ Partial skills overlap identified")
        reasons.append("📚 Additional training may be required")
    else:
        reasons.append("❌ Limited skills compatibility")
        reasons.append("🔄 Consider alternative positions")
    
    reasons.append(f"💼 {best_match['company']} sector experience relevant")
    reasons.append(f"🎓 {candidate['education']} background suitable")
    
    return reasons

def show_allocation_results():
    """Display allocation results with modern UI"""
    st.markdown("### 📊 Allocation Results")
    
    results = st.session_state.allocation_results
    
    # Summary stats
    allocated_count = len([r for r in results if r['status'] == 'allocated'])
    waitlisted_count = len([r for r in results if r['status'] == 'waitlisted'])
    not_matched_count = len([r for r in results if r['status'] == 'not-matched'])
    avg_score = np.mean([r['best_match']['score'] for r in results])
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("✅ Allocated", allocated_count, help="Successfully allocated candidates")
    
    with col2:
        st.metric("⏳ Waitlisted", waitlisted_count, help="Candidates on waitlist")
    
    with col3:
        st.metric("❌ Not Matched", not_matched_count, help="Candidates without suitable matches")
    
    with col4:
        st.metric("📊 Avg Score", f"{avg_score:.1f}%", help="Average matching score")
    
    # Filter results
    status_filter = st.selectbox("Filter by Status", ['All', 'allocated', 'waitlisted', 'not-matched'])
    
    filtered_results = results
    if status_filter != 'All':
        filtered_results = [r for r in results if r['status'] == status_filter]
    
    # Display results
    for result in filtered_results[:10]:  # Show first 10 results
        status_colors = {
            'allocated': 'background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white;',
            'waitlisted': 'background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: white;',
            'not-matched': 'background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); color: white;'
        }
        
        status_text = {
            'allocated': '✅ Allocated',
            'waitlisted': '⏳ Waitlisted', 
            'not-matched': '❌ Not Matched'
        }
        
        st.markdown(f"""
        <div class="allocation-card">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <div style="flex: 1;">
                    <h3 style="margin: 0; color: #1f2937;">{result['candidate_name']}</h3>
                    <p style="margin: 0.25rem 0; color: #64748b;">→ {result['best_match']['internship_title']}</p>
                    <p style="margin: 0; color: #64748b; font-size: 0.875rem;">{result['best_match']['company']}</p>
                </div>
                <div style="text-align: right;">
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                color: white; padding: 0.5rem 1rem; border-radius: 0.75rem; 
                                font-weight: 600; margin-bottom: 0.5rem;">{result['best_match']['score']}%</div>
                    <div style="{status_colors[result['status']]} padding: 0.25rem 0.75rem; 
                                border-radius: 0.75rem; font-size: 0.875rem; font-weight: 500;">
                        {status_text[result['status']]}
                    </div>
                </div>
            </div>
            
            <div style="margin-bottom: 1rem;">
                <p style="margin: 0; font-weight: 500; color: #374151;">🧠 AI Reasoning:</p>
        """, unsafe_allow_html=True)
        
        for reason in result['reasoning'][:3]:  # Show first 3 reasons
            st.markdown(f"<p style='margin: 0.25rem 0 0 1rem; color: #64748b; font-size: 0.875rem;'>• {reason}</p>", 
                       unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

def show_settings():
    """Application settings page"""
    st.title('⚙️ Settings')
    st.markdown('<p class="sub-header">Configure application preferences and system parameters</p>', 
                unsafe_allow_html=True)
    
    st.markdown("### 🎨 Application Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.selectbox("🎨 Theme", ["Light", "Dark", "Auto"], help="Choose your preferred theme")
        st.slider("🎯 Matching Threshold", 0.0, 1.0, 0.8, help="Minimum score for allocation matches")
        st.checkbox("🔔 Enable Notifications", True, help="Receive real-time system notifications")
        st.checkbox("🔄 Auto-refresh Dashboard", False, help="Automatically refresh dashboard data")
    
    with col2:
        st.selectbox("🌐 Language", ["English", "Hindi", "Tamil", "Bengali"], help="Select your preferred language")
        st.number_input("📄 Max Results per Page", min_value=10, max_value=100, value=25, help="Number of results to display per page")
        st.selectbox("📊 Default Chart Type", ["Bar", "Line", "Pie"], help="Default visualization type")
        st.slider("⚡ Processing Speed", 1, 10, 5, help="AI processing speed (1=Slow, 10=Fast)")
    
    st.markdown("### 🔐 Security Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("🔒 Two-Factor Authentication", False, help="Enable 2FA for enhanced security")
        st.checkbox("📝 Audit Logging", True, help="Log all system activities")
    
    with col2:
        st.selectbox("🕐 Session Timeout", ["15 min", "30 min", "1 hour", "2 hours"], index=1, help="Automatic logout time")
        st.checkbox("🔐 Secure Mode", True, help="Enable additional security measures")
    
    st.markdown("### 🎯 AI Algorithm Settings")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.slider("🎯 Skills Weight", 0, 100, 40, help="Importance of skill matching")
    
    with col2:
        st.slider("📍 Location Weight", 0, 100, 20, help="Importance of location preference")
    
    with col3:
        st.slider("💼 Experience Weight", 0, 100, 20, help="Importance of experience level")
    
    with col4:
        st.slider("⏰ Availability Weight", 0, 100, 20, help="Importance of time availability")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("💾 Save Settings", key="save_settings_main", type="primary"):
            st.success("✅ Settings saved successfully!")
    
    with col2:
        if st.button("🔄 Reset to Defaults", key="reset_settings"):
            st.info("🔄 Settings reset to default values!")
    
    with col3:
        if st.button("📤 Export Settings", key="export_settings"):
            st.info("📤 Settings exported successfully!")

def show_analytics():
    """Enhanced analytics dashboard with interactive charts"""
    st.title('📊 Analytics Dashboard')
    st.markdown('**Comprehensive insights and performance metrics with interactive visualizations**')
    
    candidates_df, internships_df = load_mock_data()
    
    # Key Performance Indicators
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📈 Total Applications", "1,247", "12%", help="Total applications received")
    
    with col2:
        st.metric("🎯 Success Rate", "87.3%", "5.2%", help="Successful allocation percentage")
    
    with col3:
        st.metric("⚡ Avg Processing Time", "2.3h", "-15%", help="Average time to process applications")
    
    with col4:
        st.metric("💼 Active Positions", len(internships_df), "8%", help="Currently available positions")
    
    st.markdown("---")
    
    # Charts Section
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Skills Analysis", "📍 Geographic Distribution", "📈 Trends", "🏆 Performance"])
    
    with tab1:
        st.markdown("### 🎯 Top Skills in Demand")
        
        # Flatten skills data
        all_skills = []
        for skills_list in candidates_df['skills']:
            all_skills.extend(skills_list)
        
        skills_count = pd.Series(all_skills).value_counts().head(10)
        
        fig_skills = px.bar(
            x=skills_count.values,
            y=skills_count.index,
            orientation='h',
            title="Most Common Skills Among Candidates",
            color=skills_count.values,
            color_continuous_scale="viridis"
        )
        fig_skills.update_layout(
            height=500,
            showlegend=False,
            yaxis_title="Skills",
            xaxis_title="Number of Candidates"
        )
        st.plotly_chart(fig_skills, use_container_width=True)
    
    with tab2:
        st.markdown("### 📍 Geographic Distribution")
        
        location_counts = candidates_df['location'].value_counts()
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_pie = px.pie(
                values=location_counts.values,
                names=location_counts.index,
                title="Candidates by Location"
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            internship_locations = internships_df['location'].value_counts()
            fig_pie2 = px.pie(
                values=internship_locations.values,
                names=internship_locations.index,
                title="Internships by Location"
            )
            fig_pie2.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie2, use_container_width=True)
    
    with tab3:
        st.markdown("### 📈 Allocation Trends")
        
        # Generate mock trend data
        dates = pd.date_range(start='2024-01-01', end='2024-06-30', freq='W')
        applications = np.random.randint(40, 80, len(dates))
        allocations = np.random.randint(30, 60, len(dates))
        
        trend_data = pd.DataFrame({
            'Date': dates,
            'Applications': applications,
            'Successful Allocations': allocations
        })
        
        fig_trend = px.line(
            trend_data,
            x='Date',
            y=['Applications', 'Successful Allocations'],
            title="Weekly Application and Allocation Trends"
        )
        fig_trend.update_layout(height=400)
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Success rate over time
        trend_data['Success Rate'] = (trend_data['Successful Allocations'] / trend_data['Applications'] * 100)
        fig_success = px.area(
            trend_data,
            x='Date',
            y='Success Rate',
            title="Success Rate Trend Over Time (%)"
        )
        fig_success.update_layout(height=300)
        st.plotly_chart(fig_success, use_container_width=True)
    
    with tab4:
        st.markdown("### 🏆 Performance Metrics")
        
        # Success rates by sector
        sectors = ['Technology', 'Healthcare', 'Finance', 'Education', 'Manufacturing', 'Retail']
        success_rates = [92, 88, 85, 90, 82, 78]
        
        fig_perf = px.bar(
            x=sectors,
            y=success_rates,
            title="Success Rates by Sector (%)",
            color=success_rates,
            color_continuous_scale="RdYlGn",
        )
        fig_perf.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_perf, use_container_width=True)
        
        # Processing time distribution
        processing_times = np.random.normal(2.3, 0.8, 1000)
        processing_times = processing_times[processing_times > 0]  # Remove negative values
        
        fig_hist = px.histogram(
            x=processing_times,
            nbins=30,
            title="Processing Time Distribution (Hours)",
            labels={'x': 'Processing Time (Hours)', 'y': 'Frequency'}
        )
        fig_hist.update_layout(height=300)
        st.plotly_chart(fig_hist, use_container_width=True)

def show_notifications():
    """Enhanced notification system"""
    st.markdown('<h1 class="main-header">🔔 Notification Center</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Stay updated with real-time system alerts and important updates</p>', 
                unsafe_allow_html=True)
    
    # Generate sample notifications if none exist
    if not st.session_state.notifications:
        sample_notifications = [
            {
                'type': 'success',
                'title': 'Allocation Completed',
                'message': '25 candidates successfully allocated to internship positions',
                'timestamp': datetime.now() - timedelta(minutes=5),
                'read': False,
                'priority': 'high',
                'category': 'allocation'
            },
            {
                'type': 'warning',
                'title': 'Pending Approvals',
                'message': '12 allocations require supervisor approval',
                'timestamp': datetime.now() - timedelta(minutes=15),
                'read': False,
                'priority': 'high',
                'category': 'approval'
            },
            {
                'type': 'info',
                'title': 'New Applications',
                'message': '8 new internship applications received',
                'timestamp': datetime.now() - timedelta(minutes=30),
                'read': True,
                'priority': 'medium',
                'category': 'application'
            },
            {
                'type': 'alert',
                'title': 'System Maintenance',
                'message': 'Scheduled maintenance window: Tonight 11 PM - 2 AM',
                'timestamp': datetime.now() - timedelta(hours=2),
                'read': False,
                'priority': 'medium',
                'category': 'system'
            }
        ]
        st.session_state.notifications.extend(sample_notifications)
    
    notifications = st.session_state.notifications
    
    # Notification stats
    total_notifications = len(notifications)
    unread_count = len([n for n in notifications if not n.get('read', False)])
    high_priority_count = len([n for n in notifications if n.get('priority') == 'high'])
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📬 Total Notifications", total_notifications)
    
    with col2:
        st.metric("🔔 Unread", unread_count)
    
    with col3:
        st.metric("🚨 High Priority", high_priority_count)
    
    with col4:
        if st.button("✅ Mark All Read", key="notifications_mark_all_read"):
            for notification in st.session_state.notifications:
                notification['read'] = True
            st.rerun()
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        status_filter = st.selectbox("Status", ["All", "Unread", "Read"])
    
    with col2:
        priority_filter = st.selectbox("Priority", ["All", "high", "medium", "low"])
    
    with col3:
        category_filter = st.selectbox("Category", ["All", "allocation", "approval", "application", "system"])
    
    # Apply filters
    filtered_notifications = notifications
    
    if status_filter == "Unread":
        filtered_notifications = [n for n in filtered_notifications if not n.get('read', False)]
    elif status_filter == "Read":
        filtered_notifications = [n for n in filtered_notifications if n.get('read', False)]
    
    if priority_filter != "All":
        filtered_notifications = [n for n in filtered_notifications if n.get('priority') == priority_filter]
    
    if category_filter != "All":
        filtered_notifications = [n for n in filtered_notifications if n.get('category') == category_filter]
    
    # Display notifications
    st.markdown(f"### 📋 Notifications ({len(filtered_notifications)} shown)")
    
    for idx, notification in enumerate(filtered_notifications):
        notification_types = {
            'success': {'color': '#10b981', 'icon': '✅'},
            'warning': {'color': '#f59e0b', 'icon': '⚠️'},
            'info': {'color': '#3b82f6', 'icon': 'ℹ️'},
            'alert': {'color': '#ef4444', 'icon': '🚨'}
        }
        
        type_info = notification_types.get(notification['type'], notification_types['info'])
        read_style = "opacity: 0.7;" if notification.get('read', False) else ""
        
        time_str = notification['timestamp'].strftime("%H:%M") if 'timestamp' in notification else "Unknown"
        
        st.markdown(f"""
        <div class="allocation-card" style="{read_style}">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 1rem; flex: 1;">
                    <div style="background: {type_info['color']}20; color: {type_info['color']}; 
                                width: 3rem; height: 3rem; border-radius: 50%; 
                                display: flex; align-items: center; justify-content: center; 
                                font-size: 1.5rem;">{type_info['icon']}</div>
                    <div style="flex: 1;">
                        <h3 style="margin: 0; color: #1f2937;">{notification['title']}</h3>
                        <p style="margin: 0.25rem 0; color: #64748b;">{notification['message']}</p>
                        <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
                            <span style="background: {type_info['color']}20; color: {type_info['color']}; 
                                         padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.875rem;">
                                {notification.get('category', 'general').title()}
                            </span>
                            <span style="background: #f3f4f6; color: #374151; 
                                         padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.875rem;">
                                {notification.get('priority', 'medium').title()} Priority
                            </span>
                            <span style="color: #9ca3af; font-size: 0.875rem;">
                                🕒 {time_str}
                            </span>
                        </div>
                    </div>
                </div>
                <div style="text-align: right;">
                    {"🔔" if not notification.get('read', False) else "✅"}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Main application function"""
    # Header
    st.markdown("""
    <div class="gradient-card">
        <h1 style="margin: 0; font-size: 3rem; font-weight: 700;">🎯 PM Internship Smart Allocation Engine</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.25rem; opacity: 0.9;">
            Advanced AI-powered system for intelligent internship allocation with real-time analytics
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create sidebar
    create_sidebar()
    
    # Route to appropriate page
    current_page = st.session_state.get('page', 'Dashboard')
    
    if current_page == 'Dashboard':
        show_dashboard()
    elif current_page == 'Candidates':
        show_candidates()
    elif current_page == 'Internships':
        show_internships()
    elif current_page == 'Smart Allocation':
        show_smart_allocation()
    elif current_page == 'Analytics':
        show_analytics()
    elif current_page == 'Notifications':
        show_notifications()
    elif current_page == 'Settings':
        show_settings()

if __name__ == "__main__":
    main()