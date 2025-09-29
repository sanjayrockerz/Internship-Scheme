// Enhanced mock internships with detailed matching criteria
export const enhancedInternships = [
  // Frontend Development Internships
  {
    id: 'fe-001',
    title: 'Frontend Developer Intern',
    company: 'TechnoWeb Solutions',
    location: 'Bangalore, India',
    domain: 'Frontend Development',
    duration: '6 months',
    salary: '₹42,000/month',
    requirements: {
      skills: ['React', 'JavaScript', 'HTML', 'CSS', 'TypeScript'],
      minCgpa: 7.0,
      experience: 'Fresher'
    },
    description: 'Work on modern React applications with cutting-edge UI/UX designs. Build responsive and interactive web interfaces.',
    benefits: ['Health Insurance', 'Learning Budget ₹15k', 'Flexible Hours', 'Mentorship Program', 'Certification Support'],
    applicationDeadline: '2024-03-15',
    startDate: '2024-04-01',
    isRemote: false,
    companyRating: 4.2,
    applicants: 892,
    tags: ['React', 'Frontend', 'UI/UX', 'JavaScript']
  },
  {
    id: 'fe-002',
    title: 'React Developer Intern',
    company: 'InnovateUI',
    location: 'Remote',
    domain: 'Web Development',
    duration: '4 months',
    salary: '₹45,000/month',
    requirements: {
      skills: ['React', 'Redux', 'JavaScript', 'Material-UI', 'Git'],
      minCgpa: 7.5,
      experience: '0-1 years'
    },
    description: 'Build scalable React applications with Redux state management. Work with a team of senior developers.',
    benefits: ['100% Remote', 'Stock Options', 'Learning Resources', 'Global Team Exposure'],
    applicationDeadline: '2024-03-20',
    startDate: '2024-04-15',
    isRemote: true,
    companyRating: 4.6,
    applicants: 567,
    tags: ['React', 'Redux', 'Remote', 'Frontend']
  },

  // Backend Development Internships
  {
    id: 'be-001',
    title: 'Backend Developer Intern',
    company: 'ServerTech Systems',
    location: 'Hyderabad, India',
    domain: 'Backend Development',
    duration: '5 months',
    salary: '₹40,000/month',
    requirements: {
      skills: ['Node.js', 'Express', 'MongoDB', 'JavaScript', 'REST APIs'],
      minCgpa: 7.2,
      experience: 'Fresher'
    },
    description: 'Develop robust backend systems and APIs. Work with microservices architecture and cloud platforms.',
    benefits: ['Health Insurance', 'Cloud Certification', 'Gym Membership', 'Transport Allowance'],
    applicationDeadline: '2024-03-10',
    startDate: '2024-03-25',
    isRemote: false,
    companyRating: 4.1,
    applicants: 743,
    tags: ['Node.js', 'Backend', 'APIs', 'MongoDB']
  },
  {
    id: 'be-002',
    title: 'Java Backend Intern',
    company: 'Enterprise Solutions Ltd',
    location: 'Pune, India',
    domain: 'Enterprise Development',
    duration: '6 months',
    salary: '₹38,000/month',
    requirements: {
      skills: ['Java', 'Spring Boot', 'MySQL', 'Maven', 'JUnit'],
      minCgpa: 7.8,
      experience: 'Fresher'
    },
    description: 'Work on enterprise Java applications using Spring Framework. Build scalable backend systems.',
    benefits: ['Health Insurance', 'Training Programs', 'Cafeteria', 'Performance Bonus'],
    applicationDeadline: '2024-03-12',
    startDate: '2024-04-01',
    isRemote: false,
    companyRating: 4.0,
    applicants: 934,
    tags: ['Java', 'Spring Boot', 'Enterprise', 'Backend']
  },

  // Full Stack Development Internships
  {
    id: 'fs-001',
    title: 'Full Stack Developer Intern',
    company: 'StartupHub Technologies',
    location: 'Mumbai, India',
    domain: 'Full Stack Development',
    duration: '6 months',
    salary: '₹50,000/month',
    requirements: {
      skills: ['React', 'Node.js', 'MongoDB', 'Express', 'JavaScript'],
      minCgpa: 8.0,
      experience: '0-1 years'
    },
    description: 'End-to-end web development using MERN stack. Work directly with founders on product development.',
    benefits: ['Equity Options', 'Flexible Work', 'Learning Budget', 'Team Retreats', 'MacBook Provided'],
    applicationDeadline: '2024-03-25',
    startDate: '2024-04-15',
    isRemote: true,
    companyRating: 4.7,
    applicants: 1234,
    tags: ['MERN Stack', 'Startup', 'Full Stack', 'Equity']
  },
  {
    id: 'fs-002',
    title: 'MEAN Stack Developer Intern',
    company: 'WebCraft Solutions',
    location: 'Chennai, India',
    domain: 'Web Development',
    duration: '4 months',
    salary: '₹43,000/month',
    requirements: {
      skills: ['Angular', 'Node.js', 'MongoDB', 'Express', 'TypeScript'],
      minCgpa: 7.3,
      experience: 'Fresher'
    },
    description: 'Build modern web applications using MEAN stack. Focus on scalable architecture and best practices.',
    benefits: ['Health Insurance', 'Skill Certification', 'Flexible Hours', 'Team Events'],
    applicationDeadline: '2024-03-18',
    startDate: '2024-04-05',
    isRemote: false,
    companyRating: 4.2,
    applicants: 678,
    tags: ['MEAN Stack', 'Angular', 'Full Stack', 'TypeScript']
  },

  // Data Science & AI/ML Internships
  {
    id: 'ds-001',
    title: 'Data Science Intern',
    company: 'DataMind Analytics',
    location: 'Bangalore, India',
    domain: 'Data Science',
    duration: '5 months',
    salary: '₹55,000/month',
    requirements: {
      skills: ['Python', 'Pandas', 'NumPy', 'Scikit-learn', 'SQL'],
      minCgpa: 8.2,
      experience: 'Fresher'
    },
    description: 'Work on real-world data science projects. Build predictive models and analyze large datasets.',
    benefits: ['Health Insurance', 'Conferences', 'GPU Access', 'Research Publications', 'Mentorship'],
    applicationDeadline: '2024-03-08',
    startDate: '2024-03-22',
    isRemote: false,
    companyRating: 4.5,
    applicants: 1567,
    tags: ['Data Science', 'Python', 'ML', 'Analytics']
  },
  {
    id: 'ml-001',
    title: 'Machine Learning Engineer Intern',
    company: 'AI Innovations Lab',
    location: 'Hyderabad, India',
    domain: 'Artificial Intelligence',
    duration: '6 months',
    salary: '₹60,000/month',
    requirements: {
      skills: ['Python', 'TensorFlow', 'PyTorch', 'Machine Learning', 'Deep Learning'],
      minCgpa: 8.5,
      experience: '0-1 years'
    },
    description: 'Develop ML models for computer vision and NLP. Work on cutting-edge AI research projects.',
    benefits: ['High-end Hardware', 'Research Papers', 'Conference Funding', 'PhD Pathway', 'Industry Connections'],
    applicationDeadline: '2024-03-05',
    startDate: '2024-03-20',
    isRemote: true,
    companyRating: 4.8,
    applicants: 2134,
    tags: ['Machine Learning', 'AI', 'Deep Learning', 'Research']
  },

  // Mobile Development Internships
  {
    id: 'mob-001',
    title: 'Android Developer Intern',
    company: 'MobileFirst Technologies',
    location: 'Delhi, India',
    domain: 'Mobile Development',
    duration: '5 months',
    salary: '₹41,000/month',
    requirements: {
      skills: ['Android', 'Kotlin', 'Java', 'Firebase', 'REST APIs'],
      minCgpa: 7.1,
      experience: 'Fresher'
    },
    description: 'Develop native Android applications. Work on user-facing mobile apps with millions of users.',
    benefits: ['Device Allowance', 'Health Insurance', 'Google Certifications', 'Flexible Hours'],
    applicationDeadline: '2024-03-22',
    startDate: '2024-04-10',
    isRemote: false,
    companyRating: 4.3,
    applicants: 823,
    tags: ['Android', 'Mobile', 'Kotlin', 'Firebase']
  },
  {
    id: 'mob-002',
    title: 'Flutter Developer Intern',
    company: 'CrossPlatform Solutions',
    location: 'Remote',
    domain: 'Mobile Development',
    duration: '4 months',
    salary: '₹44,000/month',
    requirements: {
      skills: ['Flutter', 'Dart', 'Firebase', 'REST APIs', 'Git'],
      minCgpa: 7.4,
      experience: 'Fresher'
    },
    description: 'Build cross-platform mobile apps using Flutter. Create beautiful and performant mobile experiences.',
    benefits: ['100% Remote', 'Device Support', 'Learning Resources', 'Global Team'],
    applicationDeadline: '2024-03-28',
    startDate: '2024-04-20',
    isRemote: true,
    companyRating: 4.4,
    applicants: 456,
    tags: ['Flutter', 'Cross-platform', 'Remote', 'Dart']
  },

  // DevOps & Cloud Internships
  {
    id: 'dev-001',
    title: 'DevOps Engineer Intern',
    company: 'CloudOps Systems',
    location: 'Bangalore, India',
    domain: 'DevOps',
    duration: '6 months',
    salary: '₹47,000/month',
    requirements: {
      skills: ['Docker', 'Kubernetes', 'AWS', 'Jenkins', 'Linux'],
      minCgpa: 7.6,
      experience: 'Fresher'
    },
    description: 'Learn infrastructure automation and CI/CD pipelines. Work with containerization and cloud platforms.',
    benefits: ['AWS Certification', 'Health Insurance', 'Learning Budget', 'Laptop Provided'],
    applicationDeadline: '2024-03-14',
    startDate: '2024-04-01',
    isRemote: false,
    companyRating: 4.2,
    applicants: 692,
    tags: ['DevOps', 'AWS', 'Docker', 'Cloud']
  },

  // UI/UX Design Internships
  {
    id: 'ux-001',
    title: 'UI/UX Design Intern',
    company: 'DesignCraft Studio',
    location: 'Mumbai, India',
    domain: 'Design',
    duration: '4 months',
    salary: '₹35,000/month',
    requirements: {
      skills: ['Figma', 'Adobe XD', 'Sketch', 'Prototyping', 'User Research'],
      minCgpa: 6.8,
      experience: 'Fresher'
    },
    description: 'Design intuitive user interfaces and experiences. Work on web and mobile app designs.',
    benefits: ['Design Software Licenses', 'Portfolio Development', 'Mentor Support', 'Design Conferences'],
    applicationDeadline: '2024-03-30',
    startDate: '2024-04-25',
    isRemote: true,
    companyRating: 4.6,
    applicants: 234,
    tags: ['UI/UX', 'Design', 'Figma', 'Remote']
  },

  // Cybersecurity Internships
  {
    id: 'sec-001',
    title: 'Cybersecurity Analyst Intern',
    company: 'SecureNet Solutions',
    location: 'Pune, India',
    domain: 'Cybersecurity',
    duration: '5 months',
    salary: '₹48,000/month',
    requirements: {
      skills: ['Network Security', 'Python', 'Linux', 'Ethical Hacking', 'SIEM'],
      minCgpa: 7.7,
      experience: 'Fresher'
    },
    description: 'Learn cybersecurity fundamentals and work on real security incidents. Gain hands-on security experience.',
    benefits: ['Security Certifications', 'Health Insurance', 'Training Programs', 'Industry Exposure'],
    applicationDeadline: '2024-03-16',
    startDate: '2024-04-02',
    isRemote: false,
    companyRating: 4.4,
    applicants: 512,
    tags: ['Cybersecurity', 'Security', 'Ethical Hacking', 'Python']
  }
];

// Sample user profiles for testing
export const sampleUserProfiles = [
  {
    name: 'Arjun Sharma',
    email: 'arjun.sharma@university.edu',
    skills: ['React', 'JavaScript', 'HTML', 'CSS', 'Git'],
    cgpa: 8.2,
    portfolio: 'https://arjunsharma.dev',
    university: 'IIT Delhi',
    year: '3rd Year',
    preferences: {
      location: ['Bangalore', 'Remote'],
      domains: ['Frontend Development', 'Web Development'],
      salaryRange: [40000, 50000] as [number, number],
      workMode: 'hybrid'
    }
  },
  {
    name: 'Priya Patel',
    email: 'priya.patel@college.ac.in',
    skills: ['Python', 'Machine Learning', 'Pandas', 'NumPy', 'TensorFlow'],
    cgpa: 8.7,
    portfolio: 'https://priyapatel-ds.github.io',
    university: 'NIT Surat',
    year: '4th Year',
    preferences: {
      location: ['Bangalore', 'Hyderabad', 'Mumbai'],
      domains: ['Data Science', 'Artificial Intelligence'],
      salaryRange: [50000, 65000] as [number, number],
      workMode: 'office'
    }
  },
  {
    name: 'Rahul Kumar',
    email: 'rahul.k@tech.edu.in',
    skills: ['Java', 'Spring Boot', 'MySQL', 'REST APIs', 'Maven'],
    cgpa: 7.9,
    portfolio: 'https://rahulkumar-backend.com',
    university: 'BITS Pilani',
    year: '3rd Year',
    preferences: {
      location: ['Pune', 'Bangalore', 'Chennai'],
      domains: ['Backend Development', 'Enterprise Development'],
      salaryRange: [35000, 45000] as [number, number],
      workMode: 'office'
    }
  },
  {
    name: 'Sneha Gupta',
    email: 'sneha.gupta@univ.ac.in',
    skills: ['React', 'Node.js', 'MongoDB', 'Express', 'JavaScript'],
    cgpa: 8.4,
    portfolio: 'https://snehagupta-fullstack.dev',
    university: 'Delhi University',
    year: '4th Year',
    preferences: {
      location: ['Remote', 'Delhi', 'Mumbai'],
      domains: ['Full Stack Development', 'Web Development'],
      salaryRange: [45000, 55000] as [number, number],
      workMode: 'remote'
    }
  },
  {
    name: 'Vikash Singh',
    email: 'vikash.singh@engineering.edu',
    skills: ['Android', 'Kotlin', 'Firebase', 'Java', 'REST APIs'],
    cgpa: 7.6,
    portfolio: 'https://vikashsingh-mobile.github.io',
    university: 'Jadavpur University',
    year: '3rd Year',
    preferences: {
      location: ['Bangalore', 'Hyderabad', 'Remote'],
      domains: ['Mobile Development', 'Android Development'],
      salaryRange: [40000, 48000] as [number, number],
      workMode: 'hybrid'
    }
  }
];

// Advanced matching algorithm
export const calculateMatchScore = (userProfile: any, internship: any) => {
  let score = 0;
  const matchReasons: string[] = [];

  // Skills matching (50% weight)
  const userSkills = userProfile.skills.map((s: string) => s.toLowerCase());
  const requiredSkills = internship.requirements.skills.map((s: string) => s.toLowerCase());
  
  const skillMatches = requiredSkills.filter(skill => 
    userSkills.some(userSkill => userSkill.includes(skill) || skill.includes(userSkill))
  );
  
  const skillScore = (skillMatches.length / requiredSkills.length) * 50;
  score += skillScore;

  if (skillMatches.length > 0) {
    matchReasons.push(`${skillMatches.length}/${requiredSkills.length} skills match: ${skillMatches.join(', ')}`);
  }

  // CGPA matching (25% weight)
  if (userProfile.cgpa >= internship.requirements.minCgpa) {
    score += 25;
    matchReasons.push(`CGPA exceeds requirement (${userProfile.cgpa} ≥ ${internship.requirements.minCgpa})`);
  } else {
    const cgpaGap = internship.requirements.minCgpa - userProfile.cgpa;
    if (cgpaGap <= 0.3) {
      score += 20;
      matchReasons.push(`CGPA close to requirement (gap: ${cgpaGap.toFixed(1)})`);
    } else if (cgpaGap <= 0.5) {
      score += 15;
      matchReasons.push(`CGPA moderately close (gap: ${cgpaGap.toFixed(1)})`);
    }
  }

  // Location preference (15% weight)
  const prefersRemote = userProfile.preferences.workMode === 'remote' || 
                       userProfile.preferences.location.includes('Remote');
  const locationMatch = userProfile.preferences.location.some((loc: string) => 
    internship.location.toLowerCase().includes(loc.toLowerCase())
  );
  
  if (internship.isRemote && prefersRemote) {
    score += 15;
    matchReasons.push('Remote work preference matched');
  } else if (locationMatch) {
    score += 15;
    matchReasons.push('Preferred location matched');
  } else if (internship.isRemote || userProfile.preferences.location.length === 0) {
    score += 10;
    matchReasons.push('Location flexibility');
  }

  // Domain preference (10% weight)
  const domainMatch = userProfile.preferences.domains.length === 0 ||
                     userProfile.preferences.domains.some((domain: string) => 
                       internship.domain.toLowerCase().includes(domain.toLowerCase())
                     );
  
  if (domainMatch) {
    score += 10;
    matchReasons.push('Domain preference matched');
  }

  // Salary preference bonus
  const salaryValue = parseInt(internship.salary.replace(/[^\d]/g, ''));
  if (salaryValue >= userProfile.preferences.salaryRange[0] && 
      salaryValue <= userProfile.preferences.salaryRange[1]) {
    matchReasons.push('Salary within preferred range');
  }

  return {
    score: Math.min(score, 100),
    matchReasons
  };
};