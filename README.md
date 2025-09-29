# SIHH - PM Internship Allocation System

A sophisticated AI-driven **Prime Minister's Internship Scheme** allocation system built for Smart India Hackathon (SIHH). This application uses advanced algorithms to optimally match candidates with internship opportunities across various government and public sector organizations.

## 🚀 Features

### 🎯 Smart Allocation Engine
- **AI-powered matching** with weighted scoring algorithm
- **Skills matching** (40% weight) - Advanced NLP-based skill compatibility
- **Location preference** (20% weight) - Geographic optimization
- **Experience level** (20% weight) - Candidate background alignment  
- **Availability matching** (20% weight) - Duration and timeline compatibility

### 👥 Candidate Management
- Comprehensive candidate profiles with education, skills, and preferences
- Advanced search and filtering capabilities
- Experience-based categorization (Freshers vs Experienced)
- Location-based sorting with rural/aspirational district priority

### 🏢 Internship Management  
- Complete internship opportunity database
- Sector-wise categorization (Technology, Healthcare, Finance, etc.)
- Real-time status tracking (Active/Expired positions)
- Capacity and stipend management

### 📊 Analytics Dashboard
- Real-time statistics and KPIs
- Match score analytics and trending
- Recent activity tracking
- Top performing matches visualization

## 🛠️ Tech Stack

- **Frontend**: React 18.3.1 + TypeScript
- **Build Tool**: Vite 5.4.20
- **Styling**: Tailwind CSS 3.4.7
- **UI Components**: shadcn/ui with Radix UI primitives
- **Icons**: Lucide React
- **State Management**: React Hooks
- **Type Safety**: Full TypeScript implementation

## � Project Structure

```
src/
├── components/
│   ├── ui/           # Reusable UI components (shadcn/ui)
│   ├── Header.tsx    # Navigation header
│   ├── Dashboard.tsx # Analytics dashboard
│   ├── Candidates.tsx# Candidate management
│   ├── Internships.tsx# Internship management
│   └── SmartAllocation.tsx # AI allocation engine
├── data/
│   └── mockData.ts   # Sample candidate & internship data
├── lib/
│   └── utils.ts      # Utility functions & matching algorithm
├── types/
│   └── internship.ts # TypeScript type definitions
└── pages/            # Page components
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd SIHH
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:5173](http://localhost:5173) in your browser

### Build for Production
```bash
npm run build
```

## 🎯 Key Algorithms

### Smart Matching Algorithm
The core allocation engine uses a sophisticated scoring system:

```typescript
function calculateMatchScore(candidate, internship): number {
  let score = 0;
  
  // Skills compatibility (40% weight)
  score += skillsMatch * 0.4;
  
  // Location preference (20% weight)  
  score += locationMatch * 0.2;
  
  // Experience alignment (20% weight)
  score += experienceMatch * 0.2;
  
  // Availability matching (20% weight)
  score += availabilityMatch * 0.2;
  
  return Math.min(100, Math.round(score));
}
```

### Allocation Statuses
- **Allocated** (70%+ match): Direct placement
- **Waitlisted** (50-69% match): Secondary consideration
- **Not Matched** (<50% match): Requires manual review

## 🌟 Smart India Hackathon Context

This project addresses the critical challenge of **efficient internship allocation** in government schemes, ensuring:

- **Optimal resource utilization** across all participating organizations
- **Fair and transparent** candidate selection process  
- **Geographic diversity** with rural and aspirational district focus
- **Skill-based matching** for maximum learning outcomes
- **Scalable solution** for nationwide implementation

## 🔧 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## 📊 Sample Data

The application includes comprehensive mock data featuring:
- **50+ candidate profiles** with diverse backgrounds
- **25+ internship opportunities** across multiple sectors
- **Realistic government organization** structure
- **Location data** covering rural and urban areas

## 🚀 Deployment Options

### Vite (Primary)
```bash
npm run build
npm run preview
```

### Streamlit (Alternative)
```bash
pip install streamlit
streamlit run app.py
```

## 👥 Team & Contribution

Developed for **Smart India Hackathon 2024** - addressing PM Internship Scheme challenges with innovative technology solutions.

---

**Built with ❤️ for Digital India Initiative**