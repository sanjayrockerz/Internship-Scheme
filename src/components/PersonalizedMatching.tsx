import React, { useState, useMemo } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  User, 
  Mail, 
  GraduationCap, 
  Code, 
  Star, 
  Globe, 
  Search,
  Filter,
  TrendingUp,
  Award,
  MapPin,
  Building,
  Calendar,
  DollarSign,
  Target,
  ChevronRight,
  Heart,
  Bookmark,
  Share2,
  Eye
} from 'lucide-react';
import { generateMockInterns } from '../data/mockDataGenerator';
import { enhancedInternships, calculateMatchScore, sampleUserProfiles } from '../data/enhancedInternships';
import { MatchingDemo } from './MatchingDemo';
import { cn } from '../lib/utils';

interface UserProfile {
  name: string;
  email: string;
  skills: string[];
  cgpa: number;
  portfolio: string;
  university: string;
  year: string;
  preferences: {
    location: string[];
    domains: string[];
    salaryRange: [number, number];
    workMode: string;
  };
}

interface InternshipMatch {
  id: string;
  title: string;
  company: string;
  location: string;
  domain: string;
  duration: string;
  salary: string;
  requirements: {
    skills: string[];
    minCgpa: number;
    experience: string;
  };
  description: string;
  benefits: string[];
  matchScore: number;
  matchReasons: string[];
  applicationDeadline: string;
  startDate: string;
  isRemote: boolean;
  companyRating: number;
  applicants: number;
}

const mockInternships: InternshipMatch[] = [
  {
    id: '1',
    title: 'Software Development Engineer Intern',
    company: 'TechCorp Solutions',
    location: 'Bangalore, India',
    domain: 'Software Development',
    duration: '6 months',
    salary: '₹45,000/month',
    requirements: {
      skills: ['React', 'JavaScript', 'Python', 'Node.js', 'MongoDB'],
      minCgpa: 7.5,
      experience: '0-1 years'
    },
    description: 'Work on cutting-edge web applications and contribute to our core platform development.',
    benefits: ['Health Insurance', 'Learning Budget', 'Flexible Hours', 'Mentorship Program'],
    matchScore: 0,
    matchReasons: [],
    applicationDeadline: '2024-02-15',
    startDate: '2024-03-01',
    isRemote: false,
    companyRating: 4.2,
    applicants: 847
  },
  {
    id: '2',
    title: 'Full Stack Developer Intern',
    company: 'StartupXYZ',
    location: 'Remote',
    domain: 'Web Development',
    duration: '4 months',
    salary: '₹40,000/month',
    requirements: {
      skills: ['React', 'Node.js', 'TypeScript', 'PostgreSQL', 'AWS'],
      minCgpa: 7.0,
      experience: 'Fresher'
    },
    description: 'Build scalable web applications and work directly with the founding team.',
    benefits: ['Stock Options', 'Remote Work', 'Learning Resources', 'Performance Bonus'],
    matchScore: 0,
    matchReasons: [],
    applicationDeadline: '2024-02-20',
    startDate: '2024-03-15',
    isRemote: true,
    companyRating: 4.5,
    applicants: 523
  },
  {
    id: '3',
    title: 'Data Science Intern',
    company: 'DataMind Analytics',
    location: 'Hyderabad, India',
    domain: 'Data Science',
    duration: '5 months',
    salary: '₹50,000/month',
    requirements: {
      skills: ['Python', 'Machine Learning', 'Pandas', 'TensorFlow', 'SQL'],
      minCgpa: 8.0,
      experience: '0-1 years'
    },
    description: 'Work on ML models and data analysis for enterprise clients.',
    benefits: ['Health Insurance', 'Gym Membership', 'Learning Budget', 'Conference Tickets'],
    matchScore: 0,
    matchReasons: [],
    applicationDeadline: '2024-02-10',
    startDate: '2024-02-28',
    isRemote: false,
    companyRating: 4.3,
    applicants: 642
  },
  {
    id: '4',
    title: 'Mobile App Developer Intern',
    company: 'MobileFirst Inc',
    location: 'Pune, India',
    domain: 'Mobile Development',
    duration: '6 months',
    salary: '₹42,000/month',
    requirements: {
      skills: ['React Native', 'Flutter', 'JavaScript', 'Firebase', 'Mobile UI/UX'],
      minCgpa: 7.2,
      experience: 'Fresher'
    },
    description: 'Develop cross-platform mobile applications for consumer and enterprise markets.',
    benefits: ['Health Insurance', 'Device Allowance', 'Flexible Hours', 'Team Outings'],
    matchScore: 0,
    matchReasons: [],
    applicationDeadline: '2024-02-25',
    startDate: '2024-03-10',
    isRemote: false,
    companyRating: 4.1,
    applicants: 398
  },
  {
    id: '5',
    title: 'Backend Developer Intern',
    company: 'CloudTech Systems',
    location: 'Chennai, India',
    domain: 'Backend Development',
    duration: '4 months',
    salary: '₹38,000/month',
    requirements: {
      skills: ['Java', 'Spring Boot', 'MySQL', 'Docker', 'Microservices'],
      minCgpa: 7.3,
      experience: '0-1 years'
    },
    description: 'Build robust backend systems and APIs for enterprise applications.',
    benefits: ['Health Insurance', 'Learning Budget', 'Work From Home', 'Certification Support'],
    matchScore: 0,
    matchReasons: [],
    applicationDeadline: '2024-02-18',
    startDate: '2024-03-05',
    isRemote: true,
    companyRating: 4.0,
    applicants: 756
  }
];

export function PersonalizedMatching() {
  const [userProfile, setUserProfile] = useState<UserProfile>({
    name: '',
    email: '',
    skills: [],
    cgpa: 0,
    portfolio: '',
    university: '',
    year: '',
    preferences: {
      location: [],
      domains: [],
      salaryRange: [30000, 60000],
      workMode: 'hybrid'
    }
  });

  const [showResults, setShowResults] = useState(false);
  const [savedInternships, setSavedInternships] = useState<string[]>([]);
  const [skillInput, setSkillInput] = useState('');

  // Load sample profile for quick testing
  const loadSampleProfile = (profileIndex: number) => {
    const sample = sampleUserProfiles[profileIndex];
    setUserProfile(sample);
  };

  // Calculate match scores and reasons using enhanced algorithm
  const matchedInternships = useMemo(() => {
    if (!userProfile.skills.length || !userProfile.cgpa) return [];

    return enhancedInternships.map(internship => {
      const { score, matchReasons } = calculateMatchScore(userProfile, internship);
      return {
        ...internship,
        matchScore: score,
        matchReasons
      };
    }).sort((a, b) => b.matchScore - a.matchScore);
  }, [userProfile]);

  const addSkill = () => {
    if (skillInput.trim() && !userProfile.skills.includes(skillInput.trim())) {
      setUserProfile(prev => ({
        ...prev,
        skills: [...prev.skills, skillInput.trim()]
      }));
      setSkillInput('');
    }
  };

  const removeSkill = (skillToRemove: string) => {
    setUserProfile(prev => ({
      ...prev,
      skills: prev.skills.filter(skill => skill !== skillToRemove)
    }));
  };

  const toggleSaveInternship = (id: string) => {
    setSavedInternships(prev => 
      prev.includes(id) 
        ? prev.filter(item => item !== id)
        : [...prev, id]
    );
  };

  const handleSearch = () => {
    if (userProfile.name && userProfile.skills.length > 0 && userProfile.cgpa > 0) {
      setShowResults(true);
    }
  };

  const getMatchColor = (score: number) => {
    if (score >= 80) return 'text-green-500 bg-green-50';
    if (score >= 60) return 'text-blue-500 bg-blue-50';
    if (score >= 40) return 'text-yellow-500 bg-yellow-50';
    return 'text-red-500 bg-red-50';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-12"
        >
          <h1 className="text-5xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-4">
            Personalized Internship Matching
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Get perfectly matched internships based on your skills, CGPA, and preferences using our AI-powered matching algorithm
          </p>
        </motion.div>

        {/* Demo Section */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-12"
        >
          <MatchingDemo />
        </motion.div>

        {!showResults ? (
          /* Profile Input Form */
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white rounded-3xl shadow-2xl p-8 mb-8 border border-gray-100"
          >
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              {/* Basic Information */}
              <div className="space-y-6">
                <h3 className="text-2xl font-bold text-gray-900 flex items-center">
                  <User className="w-6 h-6 mr-3 text-blue-500" />
                  Basic Information
                </h3>

                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Full Name</label>
                    <input
                      type="text"
                      value={userProfile.name}
                      onChange={(e) => setUserProfile(prev => ({ ...prev, name: e.target.value }))}
                      className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                      placeholder="Enter your full name"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Email Address</label>
                    <input
                      type="email"
                      value={userProfile.email}
                      onChange={(e) => setUserProfile(prev => ({ ...prev, email: e.target.value }))}
                      className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                      placeholder="your.email@university.edu"
                    />
                  </div>

                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">CGPA</label>
                      <input
                        type="number"
                        step="0.1"
                        min="0"
                        max="10"
                        value={userProfile.cgpa || ''}
                        onChange={(e) => setUserProfile(prev => ({ ...prev, cgpa: parseFloat(e.target.value) || 0 }))}
                        className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                        placeholder="8.5"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">Year of Study</label>
                      <select
                        value={userProfile.year}
                        onChange={(e) => setUserProfile(prev => ({ ...prev, year: e.target.value }))}
                        className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                      >
                        <option value="">Select Year</option>
                        <option value="1st Year">1st Year</option>
                        <option value="2nd Year">2nd Year</option>
                        <option value="3rd Year">3rd Year</option>
                        <option value="4th Year">4th Year</option>
                      </select>
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">University</label>
                    <input
                      type="text"
                      value={userProfile.university}
                      onChange={(e) => setUserProfile(prev => ({ ...prev, university: e.target.value }))}
                      className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                      placeholder="Your University Name"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Portfolio URL</label>
                    <input
                      type="url"
                      value={userProfile.portfolio}
                      onChange={(e) => setUserProfile(prev => ({ ...prev, portfolio: e.target.value }))}
                      className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                      placeholder="https://yourportfolio.com"
                    />
                  </div>
                </div>
              </div>

              {/* Skills and Preferences */}
              <div className="space-y-6">
                <h3 className="text-2xl font-bold text-gray-900 flex items-center">
                  <Code className="w-6 h-6 mr-3 text-purple-500" />
                  Skills & Preferences
                </h3>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Technical Skills</label>
                  <div className="flex gap-2 mb-3">
                    <input
                      type="text"
                      value={skillInput}
                      onChange={(e) => setSkillInput(e.target.value)}
                      onKeyPress={(e) => e.key === 'Enter' && addSkill()}
                      className="flex-1 px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      placeholder="Add a skill (e.g., React, Python, etc.)"
                    />
                    <button
                      onClick={addSkill}
                      className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
                    >
                      Add
                    </button>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {userProfile.skills.map((skill, index) => (
                      <span
                        key={index}
                        className="inline-flex items-center px-3 py-1 rounded-full text-sm bg-blue-100 text-blue-800"
                      >
                        {skill}
                        <button
                          onClick={() => removeSkill(skill)}
                          className="ml-2 text-blue-600 hover:text-blue-800"
                        >
                          ×
                        </button>
                      </span>
                    ))}
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Preferred Locations</label>
                  <div className="grid grid-cols-2 gap-2">
                    {['Bangalore', 'Mumbai', 'Delhi', 'Hyderabad', 'Pune', 'Chennai', 'Remote'].map((location) => (
                      <label key={location} className="flex items-center space-x-2">
                        <input
                          type="checkbox"
                          checked={userProfile.preferences.location.includes(location)}
                          onChange={(e) => {
                            if (e.target.checked) {
                              setUserProfile(prev => ({
                                ...prev,
                                preferences: {
                                  ...prev.preferences,
                                  location: [...prev.preferences.location, location]
                                }
                              }));
                            } else {
                              setUserProfile(prev => ({
                                ...prev,
                                preferences: {
                                  ...prev.preferences,
                                  location: prev.preferences.location.filter(l => l !== location)
                                }
                              }));
                            }
                          }}
                          className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                        />
                        <span className="text-sm text-gray-700">{location}</span>
                      </label>
                    ))}
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Preferred Domains</label>
                  <div className="grid grid-cols-2 gap-2">
                    {['Software Development', 'Web Development', 'Data Science', 'Mobile Development', 'Backend Development', 'AI/ML'].map((domain) => (
                      <label key={domain} className="flex items-center space-x-2">
                        <input
                          type="checkbox"
                          checked={userProfile.preferences.domains.includes(domain)}
                          onChange={(e) => {
                            if (e.target.checked) {
                              setUserProfile(prev => ({
                                ...prev,
                                preferences: {
                                  ...prev.preferences,
                                  domains: [...prev.preferences.domains, domain]
                                }
                              }));
                            } else {
                              setUserProfile(prev => ({
                                ...prev,
                                preferences: {
                                  ...prev.preferences,
                                  domains: prev.preferences.domains.filter(d => d !== domain)
                                }
                              }));
                            }
                          }}
                          className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                        />
                        <span className="text-sm text-gray-700">{domain}</span>
                      </label>
                    ))}
                  </div>
                </div>
            </div>
          </div>

          {/* Search Button */}
          {/* Sample Profiles for Quick Testing */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-gray-50 rounded-2xl p-6 mb-8"
          >
            <h3 className="text-lg font-semibold text-gray-900 mb-4 text-center">
              🚀 Try with Sample Profiles
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-3">
              {sampleUserProfiles.map((profile, index) => (
                <button
                  key={index}
                  onClick={() => loadSampleProfile(index)}
                  className="p-3 bg-white rounded-lg border border-gray-200 hover:border-blue-300 hover:shadow-md transition-all text-left"
                >
                  <div className="font-medium text-sm text-gray-900">{profile.name}</div>
                  <div className="text-xs text-gray-600 mt-1">{profile.university}</div>
                  <div className="text-xs text-blue-600 mt-1">CGPA: {profile.cgpa}</div>
                  <div className="text-xs text-gray-500 mt-1">
                    {profile.skills.slice(0, 2).join(', ')}
                    {profile.skills.length > 2 && '...'}
                  </div>
                </button>
              ))}
            </div>
          </motion.div>

          {/* Search Button */}
          <motion.div
            className="text-center"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <button
              onClick={handleSearch}
              disabled={!userProfile.name || userProfile.skills.length === 0 || !userProfile.cgpa}
              className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-2xl shadow-lg hover:shadow-xl transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <Search className="w-5 h-5 mr-2" />
              Find My Perfect Internships
            </button>
          </motion.div>
        </motion.div>
        ) : (
          /* Results Display */
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="space-y-8"
          >
            {/* Results Header */}
            <div className="bg-white rounded-2xl shadow-lg p-6 border border-gray-100">
              <div className="flex items-center justify-between">
                <div>
                  <h2 className="text-2xl font-bold text-gray-900">
                    Hello {userProfile.name}! 👋
                  </h2>
                  <p className="text-gray-600 mt-2">
                    Found {matchedInternships.length} internships matching your profile
                  </p>
                </div>
                <button
                  onClick={() => setShowResults(false)}
                  className="px-4 py-2 text-blue-600 border border-blue-600 rounded-lg hover:bg-blue-50 transition-colors"
                >
                  Update Profile
                </button>
              </div>
            </div>

            {/* Matched Internships */}
            <div className="grid gap-6">
              {matchedInternships.map((internship, index) => (
                <motion.div
                  key={internship.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden hover:shadow-xl transition-all"
                >
                  <div className="p-6">
                    <div className="flex items-start justify-between mb-4">
                      <div className="flex-1">
                        <div className="flex items-center gap-3 mb-2">
                          <h3 className="text-xl font-bold text-gray-900">{internship.title}</h3>
                          <span className={cn(
                            "px-3 py-1 rounded-full text-sm font-medium",
                            getMatchColor(internship.matchScore)
                          )}>
                            {internship.matchScore.toFixed(0)}% Match
                          </span>
                        </div>
                        <div className="flex items-center gap-4 text-sm text-gray-600 mb-3">
                          <span className="flex items-center">
                            <Building className="w-4 h-4 mr-1" />
                            {internship.company}
                          </span>
                          <span className="flex items-center">
                            <MapPin className="w-4 h-4 mr-1" />
                            {internship.location}
                          </span>
                          <span className="flex items-center">
                            <Calendar className="w-4 h-4 mr-1" />
                            {internship.duration}
                          </span>
                          <span className="flex items-center">
                            <DollarSign className="w-4 h-4 mr-1" />
                            {internship.salary}
                          </span>
                        </div>
                        <p className="text-gray-700 mb-4">{internship.description}</p>
                        
                        {/* Match Reasons */}
                        <div className="mb-4">
                          <h4 className="text-sm font-semibold text-gray-900 mb-2">Why this matches you:</h4>
                          <div className="space-y-1">
                            {internship.matchReasons.map((reason, idx) => (
                              <div key={idx} className="flex items-center text-sm text-green-600">
                                <Target className="w-3 h-3 mr-2" />
                                {reason}
                              </div>
                            ))}
                          </div>
                        </div>

                        {/* Required Skills */}
                        <div className="mb-4">
                          <h4 className="text-sm font-semibold text-gray-900 mb-2">Required Skills:</h4>
                          <div className="flex flex-wrap gap-2">
                            {internship.requirements.skills.map((skill, idx) => {
                              const hasSkill = userProfile.skills.some(userSkill => 
                                userSkill.toLowerCase().includes(skill.toLowerCase())
                              );
                              return (
                                <span
                                  key={idx}
                                  className={cn(
                                    "px-2 py-1 rounded-full text-xs font-medium",
                                    hasSkill 
                                      ? "bg-green-100 text-green-800" 
                                      : "bg-gray-100 text-gray-600"
                                  )}
                                >
                                  {skill}
                                  {hasSkill && <span className="ml-1">✓</span>}
                                </span>
                              );
                            })}
                          </div>
                        </div>

                        {/* Benefits */}
                        <div className="mb-4">
                          <h4 className="text-sm font-semibold text-gray-900 mb-2">Benefits:</h4>
                          <div className="flex flex-wrap gap-2">
                            {internship.benefits.map((benefit, idx) => (
                              <span
                                key={idx}
                                className="px-2 py-1 rounded-full text-xs bg-blue-100 text-blue-800"
                              >
                                {benefit}
                              </span>
                            ))}
                          </div>
                        </div>
                      </div>

                      <div className="flex flex-col items-end space-y-2 ml-4">
                        <button
                          onClick={() => toggleSaveInternship(internship.id)}
                          className={cn(
                            "p-2 rounded-lg transition-colors",
                            savedInternships.includes(internship.id)
                              ? "bg-red-100 text-red-600"
                              : "bg-gray-100 text-gray-600 hover:bg-gray-200"
                          )}
                        >
                          <Heart className={cn(
                            "w-4 h-4",
                            savedInternships.includes(internship.id) && "fill-current"
                          )} />
                        </button>
                        <button className="p-2 rounded-lg bg-gray-100 text-gray-600 hover:bg-gray-200 transition-colors">
                          <Share2 className="w-4 h-4" />
                        </button>
                      </div>
                    </div>

                    {/* Footer */}
                    <div className="flex items-center justify-between pt-4 border-t border-gray-100">
                      <div className="flex items-center space-x-4 text-sm text-gray-500">
                        <span className="flex items-center">
                          <Star className="w-4 h-4 mr-1 text-yellow-500" />
                          {internship.companyRating}
                        </span>
                        <span className="flex items-center">
                          <Eye className="w-4 h-4 mr-1" />
                          {internship.applicants} applicants
                        </span>
                        <span>Deadline: {internship.applicationDeadline}</span>
                      </div>
                      <button className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
                        Apply Now
                        <ChevronRight className="w-4 h-4 ml-1" />
                      </button>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </motion.div>
        )}
      </div>
    </div>
  );
}