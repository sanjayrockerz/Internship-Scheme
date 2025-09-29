// Mock Data Generator for PM Internship Smart Allocation Engine

import { 
  Intern, 
  Project, 
  Skill, 
  Allocation, 
  DashboardStats,
  AllocationRecommendation,
  ProjectType,
  SkillCategory 
} from '../types';

// Skills Database
const skillsDatabase: Skill[] = [
  // Programming
  { id: 'js', name: 'JavaScript', category: 'programming', level: 'intermediate' },
  { id: 'ts', name: 'TypeScript', category: 'programming', level: 'intermediate' },
  { id: 'react', name: 'React', category: 'programming', level: 'intermediate' },
  { id: 'node', name: 'Node.js', category: 'programming', level: 'intermediate' },
  { id: 'python', name: 'Python', category: 'programming', level: 'intermediate' },
  { id: 'java', name: 'Java', category: 'programming', level: 'intermediate' },
  { id: 'cpp', name: 'C++', category: 'programming', level: 'advanced' },
  { id: 'go', name: 'Go', category: 'programming', level: 'intermediate' },
  
  // Data Science
  { id: 'ml', name: 'Machine Learning', category: 'data-science', level: 'advanced' },
  { id: 'dl', name: 'Deep Learning', category: 'data-science', level: 'advanced' },
  { id: 'pandas', name: 'Pandas', category: 'data-science', level: 'intermediate' },
  { id: 'numpy', name: 'NumPy', category: 'data-science', level: 'intermediate' },
  { id: 'sql', name: 'SQL', category: 'data-science', level: 'intermediate' },
  { id: 'tableau', name: 'Tableau', category: 'data-science', level: 'intermediate' },
  
  // Design
  { id: 'figma', name: 'Figma', category: 'design', level: 'intermediate' },
  { id: 'sketch', name: 'Sketch', category: 'design', level: 'intermediate' },
  { id: 'ps', name: 'Photoshop', category: 'design', level: 'intermediate' },
  { id: 'ai', name: 'Illustrator', category: 'design', level: 'intermediate' },
  { id: 'ux', name: 'UX Research', category: 'design', level: 'advanced' },
  
  // Business & Marketing
  { id: 'analytics', name: 'Google Analytics', category: 'marketing', level: 'intermediate' },
  { id: 'seo', name: 'SEO', category: 'marketing', level: 'intermediate' },
  { id: 'content', name: 'Content Strategy', category: 'marketing', level: 'intermediate' },
  { id: 'pm', name: 'Product Management', category: 'management', level: 'advanced' },
  { id: 'agile', name: 'Agile Methodology', category: 'management', level: 'intermediate' },
];

// Companies
const companies = [
  'Microsoft', 'Google', 'Apple', 'Amazon', 'Meta', 'Netflix', 'Tesla', 
  'Spotify', 'Airbnb', 'Uber', 'LinkedIn', 'Adobe', 'Salesforce', 'Stripe',
  'Zoom', 'Slack', 'Notion', 'Figma', 'Canva', 'Dropbox'
];

// Universities
const universities = [
  'MIT', 'Stanford', 'Harvard', 'UC Berkeley', 'CMU', 'Caltech',
  'Oxford', 'Cambridge', 'ETH Zurich', 'NUS', 'IIT Delhi', 'IIT Bombay'
];

// Locations
const locations = [
  'San Francisco, USA', 'New York, USA', 'Seattle, USA', 'Boston, USA', 'Austin, USA', 
  'London, UK', 'Berlin, Germany', 'Amsterdam, Netherlands', 'Stockholm, Sweden',
  'Singapore', 'Tokyo, Japan', 'Sydney, Australia', 'Toronto, Canada',
  'Bangalore, India', 'Mumbai, India', 'Delhi, India', 'Hyderabad, India', 'Chennai, India',
  'Tel Aviv, Israel', 'Dublin, Ireland', 'Zurich, Switzerland', 'Barcelona, Spain'
];

// Diverse first names from different cultures
const firstNames = [
  'Aarav', 'Ananya', 'Arjun', 'Priya', 'Vikram', 'Kavya', 'Rohan', 'Shreya', 'Aditya', 'Meera',
  'Alexander', 'Sophia', 'Michael', 'Emma', 'David', 'Olivia', 'James', 'Isabella', 'Daniel', 'Mia',
  'Wei', 'Mei', 'Chen', 'Xiao', 'Li', 'Juan', 'Ana', 'Carlos', 'Maria', 'Jose',
  'Hiroshi', 'Yuki', 'Takeshi', 'Sakura', 'Jin', 'Min-jun', 'So-young', 'Hyun-woo',
  'Mohammed', 'Fatima', 'Omar', 'Aisha', 'Hassan', 'Yasmin', 'Ahmed', 'Nour',
  'Lucas', 'Gabriela', 'Mateo', 'Valentina', 'Diego', 'Sofia', 'Sebastian', 'Camila'
];

const lastNames = [
  'Sharma', 'Patel', 'Singh', 'Kumar', 'Gupta', 'Agarwal', 'Verma', 'Reddy', 'Shah', 'Jain',
  'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
  'Wang', 'Li', 'Zhang', 'Liu', 'Chen', 'Yang', 'Huang', 'Zhao', 'Wu', 'Zhou',
  'Tanaka', 'Yamamoto', 'Suzuki', 'Watanabe', 'Kim', 'Park', 'Lee', 'Choi', 'Jung',
  'Al-Rashid', 'Al-Mansouri', 'Al-Zahra', 'Hassan', 'Ibrahim', 'Ahmed', 'Mohammad',
  'Silva', 'Santos', 'Oliveira', 'Rodriguez', 'Gonzalez', 'Lopez', 'Hernandez'
];

// Generate random intern data
export const generateMockInterns = (count: number = 50): Intern[] => {
  const interns: Intern[] = [];
  
  for (let i = 0; i < count; i++) {
    const firstName = firstNames[Math.floor(Math.random() * firstNames.length)];
    const lastName = lastNames[Math.floor(Math.random() * lastNames.length)];
    
    // Create specialized skill profiles based on different tracks
    const tracks = ['frontend', 'backend', 'fullstack', 'mobile', 'data', 'ai', 'design', 'business'];
    const track = tracks[Math.floor(Math.random() * tracks.length)];
    
    let skillSet: Skill[] = [];
    switch (track) {
      case 'frontend':
        skillSet = [
          skillsDatabase.find(s => s.name === 'React')!,
          skillsDatabase.find(s => s.name === 'JavaScript')!,
          skillsDatabase.find(s => s.name === 'TypeScript')!,
          skillsDatabase.find(s => s.name === 'CSS')!,
          skillsDatabase.find(s => s.name === 'Figma')!
        ].filter(Boolean);
        break;
      case 'backend':
        skillSet = [
          skillsDatabase.find(s => s.name === 'Node.js')!,
          skillsDatabase.find(s => s.name === 'Python')!,
          skillsDatabase.find(s => s.name === 'PostgreSQL')!,
          skillsDatabase.find(s => s.name === 'AWS')!,
          skillsDatabase.find(s => s.name === 'Docker')!
        ].filter(Boolean);
        break;
      case 'fullstack':
        skillSet = [
          skillsDatabase.find(s => s.name === 'React')!,
          skillsDatabase.find(s => s.name === 'Node.js')!,
          skillsDatabase.find(s => s.name === 'JavaScript')!,
          skillsDatabase.find(s => s.name === 'MongoDB')!,
          skillsDatabase.find(s => s.name === 'Git')!
        ].filter(Boolean);
        break;
      case 'mobile':
        skillSet = [
          skillsDatabase.find(s => s.name === 'React Native')!,
          skillsDatabase.find(s => s.name === 'Flutter')!,
          skillsDatabase.find(s => s.name === 'JavaScript')!,
          skillsDatabase.find(s => s.name === 'Swift')!,
          skillsDatabase.find(s => s.name === 'Figma')!
        ].filter(Boolean);
        break;
      case 'data':
        skillSet = [
          skillsDatabase.find(s => s.name === 'Python')!,
          skillsDatabase.find(s => s.name === 'Pandas')!,
          skillsDatabase.find(s => s.name === 'NumPy')!,
          skillsDatabase.find(s => s.name === 'SQL')!,
          skillsDatabase.find(s => s.name === 'Tableau')!
        ].filter(Boolean);
        break;
      case 'ai':
        skillSet = [
          skillsDatabase.find(s => s.name === 'Machine Learning')!,
          skillsDatabase.find(s => s.name === 'Deep Learning')!,
          skillsDatabase.find(s => s.name === 'Python')!,
          skillsDatabase.find(s => s.name === 'TensorFlow')!,
          skillsDatabase.find(s => s.name === 'PyTorch')!
        ].filter(Boolean);
        break;
      case 'design':
        skillSet = [
          skillsDatabase.find(s => s.name === 'Figma')!,
          skillsDatabase.find(s => s.name === 'Adobe XD')!,
          skillsDatabase.find(s => s.name === 'Sketch')!,
          skillsDatabase.find(s => s.name === 'CSS')!,
          skillsDatabase.find(s => s.name === 'Prototyping')!
        ].filter(Boolean);
        break;
      case 'business':
        skillSet = [
          skillsDatabase.find(s => s.name === 'Project Management')!,
          skillsDatabase.find(s => s.name === 'Agile')!,
          skillsDatabase.find(s => s.name === 'Analytics')!,
          skillsDatabase.find(s => s.name === 'Strategy')!,
          skillsDatabase.find(s => s.name === 'Communication')!
        ].filter(Boolean);
        break;
      default:
        skillSet = skillsDatabase.sort(() => 0.5 - Math.random()).slice(0, 5);
    }
    
    // Add some random additional skills
    const additionalSkills = skillsDatabase
      .filter(skill => !skillSet.some(s => s.id === skill.id))
      .sort(() => 0.5 - Math.random())
      .slice(0, Math.floor(Math.random() * 3) + 1);
    
    const finalSkills = [...skillSet, ...additionalSkills].slice(0, 7);
    
    const preferences: ProjectType[] = ['software-development', 'data-analytics', 'ui-ux-design', 'marketing', 'research']
      .sort(() => 0.5 - Math.random())
      .slice(0, Math.floor(Math.random() * 3) + 1) as ProjectType[];
    
    // Generate more realistic experience based on education level
    const isGraduate = Math.random() > 0.7;
    const experience = isGraduate ? Math.floor(Math.random() * 3) + 1 : Math.floor(Math.random() * 2);
    
    // More realistic GPA distribution
    const gpa = Math.round((2.8 + Math.random() * 1.2) * 100) / 100;
    
    // Diverse education backgrounds
    const educationOptions = [
      'Bachelor of Science in Computer Science',
      'Bachelor of Engineering in Information Technology',
      'Bachelor of Technology in Software Engineering',
      'Master of Science in Computer Science',
      'Bachelor of Science in Data Science',
      'Bachelor of Design in User Experience',
      'Master of Business Administration',
      'Bachelor of Arts in Digital Media',
      'Bachelor of Science in Information Systems',
      'Master of Technology in Machine Learning'
    ];
    
    const statusWeights = { 'available': 0.5, 'allocated': 0.3, 'unavailable': 0.2 };
    const rand = Math.random();
    let status: 'available' | 'allocated' | 'unavailable';
    if (rand < statusWeights.available) status = 'available';
    else if (rand < statusWeights.available + statusWeights.allocated) status = 'allocated';
    else status = 'unavailable';
    
    interns.push({
      id: `intern-${i + 1}`,
      name: `${firstName} ${lastName}`,
      email: `${firstName.toLowerCase()}.${lastName.toLowerCase()}@${universities[Math.floor(Math.random() * universities.length)].toLowerCase().replace(/\s+/g, '')}.edu`,
      avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=${firstName}${lastName}&backgroundColor=b6e3f4,c0aede,d1d4f9,ffd5dc,ffdfbf`,
      skills: finalSkills,
      experience,
      availability: ['full-time', 'part-time', 'flexible'][Math.floor(Math.random() * 3)] as any,
      preferences,
      location: locations[Math.floor(Math.random() * locations.length)],
      university: universities[Math.floor(Math.random() * universities.length)],
      gpa,

      portfolioUrl: Math.random() > 0.4 ? `https://${firstName.toLowerCase()}-${lastName.toLowerCase()}-portfolio.dev` : undefined,
      linkedinUrl: `https://linkedin.com/in/${firstName.toLowerCase()}-${lastName.toLowerCase()}`,
      status,
      matchScore: Math.floor(Math.random() * 35) + 65, // 65-100 for better distribution

    });
  }
  
  return interns;
};

// Generate random project data
export const generateMockProjects = (count: number = 30): Project[] => {
  const projects: Project[] = [];
  
  const projectTitles = [
    'AI-Powered Analytics Dashboard',
    'Mobile App Redesign',
    'E-commerce Platform',
    'Data Pipeline Optimization',
    'Social Media Campaign',
    'Machine Learning Model',
    'User Experience Research',
    'Cloud Migration Project',
    'Marketing Automation',
    'Product Strategy Initiative',
    'Content Management System',
    'Real-time Chat Application',
    'Predictive Analytics Tool',
    'Brand Identity Refresh',
    'Customer Insights Platform'
  ];
  
  for (let i = 0; i < count; i++) {
    const title = projectTitles[Math.floor(Math.random() * projectTitles.length)];
    const company = companies[Math.floor(Math.random() * companies.length)];
    
    const requiredSkills = skillsDatabase
      .sort(() => 0.5 - Math.random())
      .slice(0, Math.floor(Math.random() * 4) + 2);
    
    const preferredSkills = skillsDatabase
      .filter(skill => !requiredSkills.includes(skill))
      .sort(() => 0.5 - Math.random())
      .slice(0, Math.floor(Math.random() * 3) + 1);
    
    const startDate = new Date();
    startDate.setDate(startDate.getDate() + Math.floor(Math.random() * 60));
    
    const duration = [8, 10, 12, 16, 20][Math.floor(Math.random() * 5)];
    const endDate = new Date(startDate);
    endDate.setDate(endDate.getDate() + duration * 7);
    
    projects.push({
      id: `project-${i + 1}`,
      title,
      description: `An exciting ${title.toLowerCase()} project at ${company}. This internship will provide hands-on experience with cutting-edge technologies and real-world applications.`,
      company,
      companyLogo: `https://logo.clearbit.com/${company.toLowerCase()}.com`,
      type: ['software-development', 'data-analytics', 'ui-ux-design', 'marketing', 'research'][Math.floor(Math.random() * 5)] as ProjectType,
      complexity: ['beginner', 'intermediate', 'advanced'][Math.floor(Math.random() * 3)] as any,
      duration,
      requiredSkills,
      preferredSkills,
      maxInterns: Math.floor(Math.random() * 4) + 2,
      allocatedInterns: [],
      location: locations[Math.floor(Math.random() * locations.length)],
      isRemote: Math.random() > 0.4,
      stipend: Math.floor(Math.random() * 3000) + 2000,
      startDate,
      endDate,
      mentor: `${['Dr.', 'Prof.', ''][Math.floor(Math.random() * 3)]} ${['Sarah', 'Mike', 'Lisa', 'John', 'Emma'][Math.floor(Math.random() * 5)]} ${['Chen', 'Smith', 'Garcia', 'Kumar', 'Johnson'][Math.floor(Math.random() * 5)]}`,
      status: ['open', 'in-progress', 'completed'][Math.floor(Math.random() * 3)] as any,
      priority: ['low', 'medium', 'high', 'critical'][Math.floor(Math.random() * 4)] as any,
    });
  }
  
  return projects;
};

// Generate mock allocations
export const generateMockAllocations = (interns: Intern[], projects: Project[]): Allocation[] => {
  const allocations: Allocation[] = [];
  
  // Create some allocations
  for (let i = 0; i < Math.min(interns.length * 0.3, projects.length); i++) {
    const intern = interns[i];
    const project = projects[Math.floor(Math.random() * projects.length)];
    
    if (project.allocatedInterns.length < project.maxInterns) {
      allocations.push({
        id: `allocation-${i + 1}`,
        internId: intern.id,
        projectId: project.id,
        matchScore: Math.floor(Math.random() * 40) + 60,
        confidence: Math.floor(Math.random() * 30) + 70,
        reasons: [
          'Strong skill match in required technologies',
          'Previous experience in similar projects',
          'Excellent academic performance',
          'Location preference alignment'
        ].slice(0, Math.floor(Math.random() * 3) + 1),
        status: ['pending', 'approved', 'rejected'][Math.floor(Math.random() * 3)] as any,
        allocatedAt: new Date(Date.now() - Math.random() * 7 * 24 * 60 * 60 * 1000),
        allocatedBy: 'AI System',
        notes: Math.random() > 0.7 ? 'Excellent candidate for this role' : undefined,
      });
      
      project.allocatedInterns.push(intern.id);
      intern.status = 'allocated';
      intern.allocatedProjectId = project.id;
    }
  }
  
  return allocations;
};

// Generate AI recommendations
export const generateMockRecommendations = (
  interns: Intern[], 
  projects: Project[]
): AllocationRecommendation[] => {
  const recommendations: AllocationRecommendation[] = [];
  
  // Get available interns and open projects
  const availableInterns = interns.filter(intern => intern.status === 'available');
  const openProjects = projects.filter(project => 
    project.status === 'open' && project.allocatedInterns.length < project.maxInterns
  );
  
  // Generate recommendations
  for (let i = 0; i < Math.min(20, availableInterns.length); i++) {
    const intern = availableInterns[i];
    const project = openProjects[Math.floor(Math.random() * openProjects.length)];
    
    if (project) {
      const matchScore = Math.floor(Math.random() * 40) + 60;
      const confidence = Math.floor(Math.random() * 30) + 70;
      
      recommendations.push({
        intern,
        project,
        matchScore,
        confidence,
        reasons: [
          'Strong technical skill alignment',
          'Previous experience in similar domain',
          'Excellent communication skills',
          'High academic performance',
          'Location preference match'
        ].slice(0, Math.floor(Math.random() * 3) + 2),
        concerns: [
          'Limited experience in specific technology',
          'Availability constraints',
          'Geographic distance'
        ].slice(0, Math.floor(Math.random() * 2)),
      });
    }
  }
  
  return recommendations.sort((a, b) => b.matchScore - a.matchScore);
};

// Generate dashboard statistics
export const generateDashboardStats = (
  interns: Intern[], 
  projects: Project[], 
  allocations: Allocation[]
): DashboardStats => {
  const totalAllocations = allocations.filter(a => a.status === 'approved').length;
  const avgMatchScore = allocations.reduce((sum, a) => sum + a.matchScore, 0) / allocations.length || 0;
  
  return {
    totalInterns: interns.length,
    totalProjects: projects.length,
    totalAllocations,
    allocationRate: (totalAllocations / interns.length) * 100,
    avgMatchScore: Math.round(avgMatchScore),
    activeProjects: projects.filter(p => p.status === 'in-progress').length,
    completedProjects: projects.filter(p => p.status === 'completed').length,
    pendingAllocations: allocations.filter(a => a.status === 'pending').length,
  };
};

// Export all mock data
export const mockData = {
  interns: generateMockInterns(50),
  projects: generateMockProjects(30),
};

mockData.projects = generateMockProjects(30);
const allocations = generateMockAllocations(mockData.interns, mockData.projects);
const recommendations = generateMockRecommendations(mockData.interns, mockData.projects);
const stats = generateDashboardStats(mockData.interns, mockData.projects, allocations);

export { allocations, recommendations, stats };