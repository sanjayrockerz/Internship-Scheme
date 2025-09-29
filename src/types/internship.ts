export interface Candidate {
  id: string;
  name: string;
  email: string;
  phone: string;
  dateOfBirth: string;
  gender: 'male' | 'female' | 'other';
  category: 'general' | 'obc' | 'sc' | 'st';
  location: {
    state: string;
    district: string;
    isRural: boolean;
    isAspirational: boolean;
  };
  education: {
    degree: string;
    specialization: string;
    university: string;
    cgpa: number;
    graduationYear: number;
  };
  skills: string[];
  preferredSectors: string[];
  preferredLocations: string[];
  pastInternships: number;
  resume?: string;
  createdAt: string;
}

export interface InternshipOpportunity {
  id: string;
  companyName: string;
  title: string;
  description: string;
  sector: string;
  location: {
    state: string;
    district: string;
    city: string;
  };
  requiredSkills: string[];
  preferredQualifications: string[];
  duration: number; // in months
  stipend: number;
  capacity: number;
  filled: number;
  requirements: {
    minCGPA: number;
    eligibleDegrees: string[];
    maxAge: number;
  };
  benefits: string[];
  applicationDeadline: string;
  startDate: string;
  status: 'open' | 'closed' | 'draft';
  createdAt: string;
}

export interface AllocationResult {
  candidateId: string;
  internshipId: string;
  score: number;
  breakdown: {
    skillsMatch: number;
    locationMatch: number;
    sectorMatch: number;
    affirmativeAction: number;
    pastParticipation: number;
  };
  status: 'allocated' | 'waitlisted' | 'rejected';
  allocatedAt: string;
}

export interface AllocationWeights {
  skills: number;
  location: number;
  sector: number;
  affirmativeAction: number;
  pastParticipation: number;
}

export const DEFAULT_WEIGHTS: AllocationWeights = {
  skills: 0.4,
  location: 0.2,
  sector: 0.2,
  affirmativeAction: 0.1,
  pastParticipation: 0.1,
};

export interface AnalyticsData {
  totalCandidates: number;
  totalInternships: number;
  totalAllocations: number;
  allocationRate: number;
  categoryDistribution: Record<string, number>;
  sectorDistribution: Record<string, number>;
  locationDistribution: Record<string, number>;
  averageScore: number;
}