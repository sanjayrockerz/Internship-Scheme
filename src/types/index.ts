// Core Types for PM Internship Smart Allocation Engine

export interface Intern {
  id: string;
  name: string;
  email: string;
  avatar?: string;
  skills: Skill[];
  experience: number; // years
  availability: 'full-time' | 'part-time' | 'flexible';
  preferences: ProjectType[];
  location: string;
  university: string;
  gpa: number;
  portfolioUrl?: string;
  linkedinUrl?: string;
  status: 'available' | 'allocated' | 'unavailable';
  matchScore?: number;
  allocatedProjectId?: string;
}

export interface Project {
  id: string;
  title: string;
  description: string;
  company: string;
  companyLogo?: string;
  type: ProjectType;
  complexity: 'beginner' | 'intermediate' | 'advanced';
  duration: number; // weeks
  requiredSkills: Skill[];
  preferredSkills: Skill[];
  maxInterns: number;
  allocatedInterns: string[]; // intern IDs
  location: string;
  isRemote: boolean;
  stipend: number;
  startDate: Date;
  endDate: Date;
  mentor: string;
  status: 'open' | 'in-progress' | 'completed' | 'cancelled';
  priority: 'low' | 'medium' | 'high' | 'critical';
}

export interface Skill {
  id: string;
  name: string;
  category: SkillCategory;
  level: 'beginner' | 'intermediate' | 'advanced' | 'expert';
}

export type SkillCategory = 
  | 'programming'
  | 'design'
  | 'data-science'
  | 'marketing'
  | 'business'
  | 'research'
  | 'management';

export type ProjectType = 
  | 'software-development'
  | 'data-analytics'
  | 'ui-ux-design'
  | 'marketing'
  | 'research'
  | 'business-strategy'
  | 'product-management';

export interface Allocation {
  id: string;
  internId: string;
  projectId: string;
  matchScore: number;
  confidence: number;
  reasons: string[];
  status: 'pending' | 'approved' | 'rejected';
  allocatedAt: Date;
  allocatedBy: string;
  notes?: string;
}

export interface AllocationRecommendation {
  intern: Intern;
  project: Project;
  matchScore: number;
  confidence: number;
  reasons: string[];
  concerns: string[];
}

export interface DashboardStats {
  totalInterns: number;
  totalProjects: number;
  totalAllocations: number;
  allocationRate: number;
  avgMatchScore: number;
  activeProjects: number;
  completedProjects: number;
  pendingAllocations: number;
}

export interface FilterOptions {
  skills: string[];
  availability: string[];
  experience: { min: number; max: number };
  projectTypes: ProjectType[];
  complexity: string[];
  location: string[];
  isRemote?: boolean;
}

export interface SortOption {
  field: string;
  direction: 'asc' | 'desc';
  label: string;
}

// UI State Types
export interface UIState {
  activeView: 'dashboard' | 'allocation' | 'analytics' | 'settings';
  selectedIntern?: Intern;
  selectedProject?: Project;
  isLoading: boolean;
  filters: FilterOptions;
  sortBy: SortOption;
  searchQuery: string;
}

// Chart Data Types
export interface ChartData {
  label: string;
  value: number;
  color?: string;
  percentage?: number;
}

export interface TimeSeriesData {
  date: string;
  value: number;
  category?: string;
}

// Notification Types
export interface Notification {
  id: string;
  type: 'success' | 'error' | 'warning' | 'info';
  title: string;
  message: string;
  timestamp: Date;
  isRead: boolean;
  actionUrl?: string;
}