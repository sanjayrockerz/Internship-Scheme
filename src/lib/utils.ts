import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// Format numbers with appropriate suffixes
export function formatNumber(num: number): string {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M';
  }
  if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'K';
  }
  return num.toString();
}

// Format percentage
export function formatPercentage(num: number): string {
  return `${Math.round(num)}%`;
}

// Format currency
export function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
  }).format(amount);
}

// Get initials from name
export function getInitials(name: string): string {
  return name
    .split(' ')
    .map(word => word.charAt(0).toUpperCase())
    .join('')
    .slice(0, 2);
}

// Get skill category color
export function getSkillCategoryColor(category: string): string {
  const colorMap: Record<string, string> = {
    programming: 'bg-blue-100 text-blue-800',
    design: 'bg-pink-100 text-pink-800',
    'data-science': 'bg-green-100 text-green-800',
    marketing: 'bg-orange-100 text-orange-800',
    business: 'bg-purple-100 text-purple-800',
    research: 'bg-indigo-100 text-indigo-800',
    management: 'bg-gray-100 text-gray-800',
  };
  return colorMap[category] || 'bg-gray-100 text-gray-800';
}

// Get status color
export function getStatusColor(status: string): string {
  const colorMap: Record<string, string> = {
    available: 'bg-green-100 text-green-800',
    allocated: 'bg-blue-100 text-blue-800',
    unavailable: 'bg-red-100 text-red-800',
    open: 'bg-green-100 text-green-800',
    'in-progress': 'bg-yellow-100 text-yellow-800',
    completed: 'bg-blue-100 text-blue-800',
    cancelled: 'bg-red-100 text-red-800',
    pending: 'bg-yellow-100 text-yellow-800',
    approved: 'bg-green-100 text-green-800',
    rejected: 'bg-red-100 text-red-800',
  };
  return colorMap[status] || 'bg-gray-100 text-gray-800';
}

// Fuzzy search function
export function fuzzySearch(query: string, text: string): boolean {
  const queryLower = query.toLowerCase();
  const textLower = text.toLowerCase();
  
  if (textLower.includes(queryLower)) return true;
  
  // Simple fuzzy matching - character by character
  let queryIndex = 0;
  for (let i = 0; i < textLower.length && queryIndex < queryLower.length; i++) {
    if (textLower[i] === queryLower[queryIndex]) {
      queryIndex++;
    }
  }
  
  return queryIndex === queryLower.length;
}

export function formatDate(date: Date | string) {
  return new Date(date).toLocaleDateString('en-IN', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  });
}

export function calculateMatchScore(candidate: any, internship: any): number {
  let score = 0;
  
  // Skills match (40% weight)
  if (candidate.skills && internship.requiredSkills) {
    const candidateSkills = candidate.skills.map((s: string) => s.toLowerCase());
    const requiredSkills = internship.requiredSkills.map((s: string) => s.toLowerCase());
    const matchingSkills = candidateSkills.filter((skill: string) => 
      requiredSkills.some((req: string) => req.includes(skill) || skill.includes(req))
    );
    score += (matchingSkills.length / requiredSkills.length) * 40;
  }
  
  // Location preference (20% weight)
  if (candidate.location === internship.location) {
    score += 20;
  }
  
  // Experience level (20% weight)  
  if (candidate.experience && internship.experienceLevel) {
    if (candidate.experience === internship.experienceLevel) {
      score += 20;
    } else if (
      (candidate.experience === 'Intermediate' && internship.experienceLevel === 'Beginner') ||
      (candidate.experience === 'Advanced' && internship.experienceLevel !== 'Advanced')
    ) {
      score += 10;
    }
  }
  
  // Availability (20% weight)
  if (candidate.availability === internship.duration) {
    score += 20;
  }
  
  return Math.min(100, Math.round(score));
}