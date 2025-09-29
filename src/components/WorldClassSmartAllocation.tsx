import React, { useState, useCallback, useMemo } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  DndContext,
  DragEndEvent,
  DragOverEvent,
  DragOverlay,
  DragStartEvent,
  KeyboardSensor,
  PointerSensor,
  closestCenter,
  useSensor,
  useSensors,
} from '@dnd-kit/core';
import {
  SortableContext,
  sortableKeyboardCoordinates,
  verticalListSortingStrategy,
} from '@dnd-kit/sortable';
import {
  useSortable,
  SortableContext as DndSortableContext,
} from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import {
  Brain,
  Target,
  Users,
  Briefcase,
  Sparkles,
  ArrowRight,
  RefreshCw,
  Check,
  X,
  Filter,
  Search,
  Star,
  Zap,
  TrendingUp,
  Clock,
  Award,
  UserCheck,
  AlertTriangle,
  ChevronDown,
  ChevronUp,
} from 'lucide-react';
import toast from 'react-hot-toast';
import { generateMockInterns, generateMockProjects, generateMockAllocations } from '../data/mockDataGenerator';
import { Intern, Project, Allocation, AllocationRecommendation } from '../types';
import { cn, getStatusColor, formatPercentage } from '../lib/utils';

// Generate AI-driven recommendations
function generateRecommendations(interns: Intern[], projects: Project[]): AllocationRecommendation[] {
  const recommendations: AllocationRecommendation[] = [];
  
  interns.forEach(intern => {
    // Find best matching projects based on skills and preferences
    const matchingProjects = projects
      .map(project => {
        // Calculate skill match score
        const skillMatch = project.requiredSkills.filter(skill => 
          intern.skills.includes(skill)
        ).length / project.requiredSkills.length;
        
        // Calculate preference match
        const prefMatch = intern.preferences.some(pref => 
          project.company.toLowerCase().includes(pref.toLowerCase()) ||
          project.title.toLowerCase().includes(pref.toLowerCase())
        ) ? 0.3 : 0;
        
        // Calculate experience match (using duration as a proxy for complexity)
        const expMatch = intern.experience >= 1 ? 0.2 : 0;
        
        const totalScore = (skillMatch * 0.5) + prefMatch + expMatch;
        
        return {
          projectId: project.id,
          project,
          score: Math.min(totalScore, 1) * 100,
        };
      })
      .filter(match => match.score >= 40)
      .sort((a, b) => b.score - a.score)
      .slice(0, 3);

    if (matchingProjects.length > 0) {
      recommendations.push({
        intern,
        project: matchingProjects[0].project,
        matchScore: matchingProjects[0].score,
        confidence: Math.max(...matchingProjects.map(p => p.score)),
        reasons: [`Best match based on ${matchingProjects[0].score >= 80 ? 'excellent' : 'good'} skill alignment`],
        concerns: matchingProjects[0].score < 60 ? ['Low skill match score'] : [],
      });
    }
  });
  
  return recommendations.sort((a, b) => b.confidence - a.confidence);
}

// Draggable Intern Card Component
function DraggableInternCard({ intern, isOverlay = false }: { intern: Intern; isOverlay?: boolean }) {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging,
  } = useSortable({ id: intern.id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
  };

  return (
    <motion.div
      ref={setNodeRef}
      style={style}
      {...attributes}
      {...listeners}
      className={cn(
        "p-4 bg-white rounded-xl border-2 border-gray-100 shadow-sm cursor-grab active:cursor-grabbing",
        "hover:shadow-lg hover:border-blue-200 transition-all duration-200",
        isDragging && "opacity-50 scale-95",
        isOverlay && "shadow-2xl border-blue-300"
      )}
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
    >
      <div className="flex items-start justify-between mb-3">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-semibold">
            {intern.name.split(' ').map(n => n[0]).join('')}
          </div>
          <div>
            <h4 className="font-semibold text-gray-900">{intern.name}</h4>
            <p className="text-sm text-gray-600">{intern.university}</p>
          </div>
        </div>
        <div className={cn(
          "px-2 py-1 rounded-full text-xs font-medium",
          getStatusColor(intern.status)
        )}>
          {intern.status}
        </div>
      </div>
      
      <div className="space-y-2">
        <div className="flex items-center text-sm text-gray-600">
          <Award className="w-4 h-4 mr-2" />
          {intern.gpa} GPA • {intern.experience} years exp
        </div>
        
        <div className="flex flex-wrap gap-1">
          {intern.skills.slice(0, 3).map((skill, index) => (
            <span key={index} className="px-2 py-1 bg-blue-50 text-blue-700 rounded-full text-xs">
              {typeof skill === 'string' ? skill : skill.name}
            </span>
          ))}
          {intern.skills.length > 3 && (
            <span className="px-2 py-1 bg-gray-100 text-gray-600 rounded-full text-xs">
              +{intern.skills.length - 3}
            </span>
          )}
        </div>
      </div>
    </motion.div>
  );
}

// Droppable Project Card Component
function DroppableProjectCard({ 
  project, 
  allocatedInterns, 
  isOver 
}: { 
  project: Project; 
  allocatedInterns: Intern[];
  isOver: boolean;
}) {
  const [isExpanded, setIsExpanded] = useState(false);
  
  return (
    <motion.div
      className={cn(
        "p-6 bg-white rounded-xl border-2 transition-all duration-200",
        isOver ? "border-green-300 bg-green-50" : "border-gray-100",
        "hover:shadow-lg"
      )}
      layout
      whileHover={{ scale: 1.01 }}
    >
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <div className="flex items-center space-x-2 mb-2">
            <Briefcase className="w-5 h-5 text-blue-600" />
            <h3 className="font-semibold text-gray-900">{project.title}</h3>
          </div>
          <p className="text-sm text-gray-600 mb-2">{project.company}</p>
          <div className="flex items-center space-x-4 text-sm text-gray-500">
            <span>Duration: {project.duration} weeks</span>
            <span>Type: {project.type}</span>
          </div>
        </div>
        
        <div className="text-right">
          <div className="text-sm font-medium text-gray-900">
            {allocatedInterns.length}/{project.maxInterns}
          </div>
          <div className="text-xs text-gray-500">Allocated</div>
        </div>
      </div>

      {/* Required Skills */}
      <div className="mb-4">
        <h4 className="text-sm font-medium text-gray-700 mb-2">Required Skills:</h4>
        <div className="flex flex-wrap gap-1">
          {project.requiredSkills.map((skill, index) => (
            <span key={index} className="px-2 py-1 bg-purple-50 text-purple-700 rounded-full text-xs">
              {typeof skill === 'string' ? skill : skill.name}
            </span>
          ))}
        </div>
      </div>

      {/* Allocated Interns */}
      {allocatedInterns.length > 0 && (
        <div className="mb-4">
          <h4 className="text-sm font-medium text-gray-700 mb-2">Allocated Interns:</h4>
          <div className="space-y-2">
            {allocatedInterns.slice(0, isExpanded ? undefined : 2).map((intern) => (
              <div key={intern.id} className="flex items-center justify-between p-2 bg-green-50 rounded-lg">
                <div className="flex items-center space-x-2">
                  <div className="w-6 h-6 bg-green-500 rounded-full flex items-center justify-center text-white text-xs font-medium">
                    {intern.name.split(' ').map(n => n[0]).join('')}
                  </div>
                  <span className="text-sm font-medium">{intern.name}</span>
                </div>
                <button
                  onClick={() => toast.success(`Removed ${intern.name} from ${project.title}`)}
                  className="text-red-500 hover:text-red-700 p-1"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>
            ))}
            {allocatedInterns.length > 2 && (
              <button
                onClick={() => setIsExpanded(!isExpanded)}
                className="flex items-center space-x-1 text-blue-600 hover:text-blue-800 text-sm"
              >
                {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                <span>{isExpanded ? 'Show Less' : `Show ${allocatedInterns.length - 2} More`}</span>
              </button>
            )}
          </div>
        </div>
      )}

      {/* Project Description */}
      {isExpanded && (
        <motion.div
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: 'auto' }}
          exit={{ opacity: 0, height: 0 }}
          className="border-t pt-4"
        >
          <p className="text-sm text-gray-600">{project.description}</p>
        </motion.div>
      )}
    </motion.div>
  );
}

// AI Recommendation Panel
function AIRecommendationPanel({ 
  recommendations, 
  onApplyRecommendation 
}: { 
  recommendations: AllocationRecommendation[];
  onApplyRecommendation: (recommendation: AllocationRecommendation) => void;
}) {
  return (
    <div className="bg-gradient-to-br from-purple-50 to-blue-50 rounded-xl p-6 border border-purple-100">
      <div className="flex items-center space-x-2 mb-4">
        <Brain className="w-6 h-6 text-purple-600" />
        <h3 className="text-lg font-semibold text-gray-900">AI Recommendations</h3>
        <span className="px-2 py-1 bg-purple-100 text-purple-700 rounded-full text-xs font-medium">
          {recommendations.length} available
        </span>
      </div>

      <div className="space-y-4 max-h-96 overflow-y-auto">
        {recommendations.slice(0, 5).map((rec) => (
          <motion.div
            key={`rec-${rec.intern.id}`}
            className="bg-white rounded-lg p-4 border border-gray-100"
            whileHover={{ scale: 1.01 }}
          >
            <div className="flex items-start justify-between mb-3">
              <div className="flex items-center space-x-3">
                <div className="w-8 h-8 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white text-sm font-semibold">
                  {rec.intern.name.split(' ').map(n => n[0]).join('')}
                </div>
                <div>
                  <h4 className="font-medium text-gray-900">{rec.intern.name}</h4>
                  <p className="text-sm text-gray-600">{rec.intern.university}</p>
                </div>
              </div>
              
              <div className="flex items-center space-x-2">
                <div className="flex items-center space-x-1">
                  <Star className="w-4 h-4 text-yellow-500" />
                  <span className="text-sm font-medium">{Math.round(rec.confidence)}%</span>
                </div>
                <button
                  onClick={() => onApplyRecommendation(rec)}
                  className="px-3 py-1 bg-green-500 text-white rounded-full text-xs font-medium hover:bg-green-600 transition-colors"
                >
                  Apply
                </button>
              </div>
            </div>

            <div className="space-y-2">
              <p className="text-sm text-gray-600">{rec.reasons[0]}</p>
              
              <div className="space-y-1">
                <div className="flex items-center justify-between p-2 bg-gray-50 rounded">
                  <span className="text-sm font-medium">{rec.project.title}</span>
                  <div className="flex items-center space-x-1">
                    <div className="w-12 bg-gray-200 rounded-full h-2">
                      <div 
                        className="bg-green-500 h-2 rounded-full transition-all duration-500"
                        style={{ width: `${rec.matchScore}%` }}
                      />
                    </div>
                    <span className="text-xs text-gray-600">{Math.round(rec.matchScore)}%</span>
                  </div>
                </div>
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  );
}

export default function WorldClassSmartAllocation() {
  const [interns] = useState(() => generateMockInterns(50));
  const [projects] = useState(() => generateMockProjects(30));
  const [allocations, setAllocations] = useState<Allocation[]>(() => generateMockAllocations(interns, projects));
  const [activeId, setActiveId] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [skillFilter, setSkillFilter] = useState<string>('all');

  const sensors = useSensors(
    useSensor(PointerSensor),
    useSensor(KeyboardSensor, {
      coordinateGetter: sortableKeyboardCoordinates,
    })
  );

  // Generate AI recommendations
  const recommendations = useMemo(() => {
    const unallocatedInterns = interns.filter(intern => 
      !allocations.some(allocation => allocation.internId === intern.id)
    );
    return generateRecommendations(unallocatedInterns, projects);
  }, [interns, projects, allocations]);

  // Filter interns
  const filteredInterns = useMemo(() => {
    return interns.filter(intern => {
      const matchesSearch = intern.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          intern.university.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          intern.skills.some(skill => 
                            (typeof skill === 'string' ? skill : skill.name).toLowerCase().includes(searchTerm.toLowerCase())
                          );
      
      const matchesStatus = statusFilter === 'all' || intern.status === statusFilter;
      
      const matchesSkill = skillFilter === 'all' || intern.skills.some(skill => 
        (typeof skill === 'string' ? skill : skill.name) === skillFilter
      );
      
      const isUnallocated = !allocations.some(allocation => allocation.internId === intern.id);
      
      return matchesSearch && matchesStatus && matchesSkill && isUnallocated;
    });
  }, [interns, searchTerm, statusFilter, skillFilter, allocations]);

  // Get allocated interns for each project
  const getProjectAllocations = useCallback((projectId: string) => {
    const projectAllocations = allocations.filter(allocation => allocation.projectId === projectId);
    return projectAllocations.map(allocation => 
      interns.find(intern => intern.id === allocation.internId)!
    ).filter(Boolean);
  }, [allocations, interns]);

  const handleDragStart = (event: DragStartEvent) => {
    setActiveId(event.active.id as string);
  };

  const handleDragEnd = (event: DragEndEvent) => {
    const { active, over } = event;
    
    if (!over) {
      setActiveId(null);
      return;
    }

    const internId = active.id as string;
    const projectId = over.id as string;
    
    // Check if dropping on a project
    const targetProject = projects.find(p => p.id === projectId);
    if (targetProject) {
      const currentAllocations = getProjectAllocations(projectId);
      
      if (currentAllocations.length >= targetProject.maxInterns) {
        toast.error(`${targetProject.title} is at capacity (${targetProject.maxInterns} interns)`);
        setActiveId(null);
        return;
      }

      // Create new allocation
      const newAllocation: Allocation = {
        id: `alloc-${Date.now()}`,
        internId,
        projectId,
        allocatedAt: new Date(),
        allocatedBy: 'Manual Assignment',
        status: 'approved',
        matchScore: Math.random() * 30 + 70, // Random score between 70-100
        confidence: Math.random() * 20 + 80, // Random confidence between 80-100
        reasons: ['Manual drag-and-drop allocation'],
      };

      setAllocations(prev => [...prev, newAllocation]);
      
      const intern = interns.find(i => i.id === internId);
      toast.success(`Successfully allocated ${intern?.name} to ${targetProject.title}!`);
    }
    
    setActiveId(null);
  };

  const handleApplyRecommendation = (recommendation: AllocationRecommendation) => {
    const targetProject = recommendation.project;
    if (!targetProject) return;

    const currentAllocations = getProjectAllocations(targetProject.id);
    if (currentAllocations.length >= targetProject.maxInterns) {
      toast.error(`${targetProject.title} is at capacity`);
      return;
    }

    const newAllocation: Allocation = {
      id: `alloc-${Date.now()}`,
      internId: recommendation.intern.id,
      projectId: targetProject.id,
      allocatedAt: new Date(),
      allocatedBy: 'AI System',
      status: 'approved',
      matchScore: recommendation.matchScore,
      confidence: recommendation.confidence,
      reasons: recommendation.reasons,
    };

    setAllocations(prev => [...prev, newAllocation]);
    toast.success(`Applied AI recommendation: ${recommendation.intern.name} → ${targetProject.title}`);
  };

  const uniqueSkills = Array.from(new Set(interns.flatMap(intern => 
    intern.skills.map(skill => typeof skill === 'string' ? skill : skill.name)
  ))).sort();

  const draggedIntern = activeId ? interns.find(intern => intern.id === activeId) : null;

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-pink-50 to-blue-50 p-6 relative overflow-hidden">
      {/* Background Pattern */}
      <div className="absolute inset-0 opacity-20">
        <div className="absolute top-20 left-20 w-72 h-72 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse" />
        <div className="absolute top-40 right-20 w-72 h-72 bg-yellow-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse animation-delay-2000" />
        <div className="absolute -bottom-8 left-1/2 w-72 h-72 bg-pink-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse animation-delay-4000" />
      </div>
      
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="relative max-w-7xl mx-auto"
      >
        {/* Smart Allocation Header - Unique Purple Theme */}
        <div className="bg-gradient-to-r from-purple-600 via-pink-600 to-indigo-600 rounded-2xl p-8 mb-8 text-white relative overflow-hidden">
          <div className="absolute inset-0">
            <div className="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full -translate-y-32 translate-x-32" />
            <div className="absolute bottom-0 left-0 w-48 h-48 bg-white/5 rounded-full translate-y-24 -translate-x-24" />
          </div>
          <div className="relative">
            <div className="flex items-center space-x-4 mb-4">
              <div className="p-4 bg-white/20 backdrop-blur-sm rounded-2xl">
                <Target className="w-10 h-10 text-white" />
              </div>
              <div>
                <h1 className="text-4xl font-bold mb-2">Smart Allocation Engine</h1>
                <p className="text-purple-100 text-lg">AI-powered intern-project matching with drag-and-drop interface</p>
              </div>
            </div>

            {/* Stats Bar */}
            <div className="grid grid-cols-4 gap-4 mb-6">
              <div className="bg-white/10 backdrop-blur-sm rounded-xl p-4">
                <div className="flex items-center space-x-2">
                  <Users className="w-5 h-5 text-white" />
                  <span className="text-sm text-purple-100">Available Interns</span>
                </div>
                <div className="text-2xl font-bold text-white">{filteredInterns.length}</div>
              </div>
              <div className="bg-white/10 backdrop-blur-sm rounded-xl p-4">
                <div className="flex items-center space-x-2">
                  <Briefcase className="w-5 h-5 text-white" />
                  <span className="text-sm text-purple-100">Active Projects</span>
                </div>
                <div className="text-2xl font-bold text-white">{projects.length}</div>
              </div>
              <div className="bg-white/10 backdrop-blur-sm rounded-xl p-4">
                <div className="flex items-center space-x-2">
                  <UserCheck className="w-5 h-5 text-white" />
                  <span className="text-sm text-purple-100">Allocations Made</span>
                </div>
                <div className="text-2xl font-bold text-white">{allocations.length}</div>
              </div>
              <div className="bg-white/10 backdrop-blur-sm rounded-xl p-4">
                <div className="flex items-center space-x-2">
                  <Sparkles className="w-5 h-5 text-white" />
                  <span className="text-sm text-purple-100">AI Recommendations</span>
                </div>
                <div className="text-2xl font-bold text-white">{recommendations.length}</div>
              </div>
            </div>
          </div>

          {/* Filters */}
          <div className="flex flex-wrap gap-4 bg-white/10 backdrop-blur-sm rounded-xl p-4">
            <div className="flex-1 min-w-64">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                <input
                  type="text"
                  placeholder="Search interns by name, university, or skills..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 bg-white/20 border border-white/30 rounded-lg focus:ring-2 focus:ring-white focus:border-white text-white placeholder-purple-200"
                />
              </div>
            </div>
            
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              className="px-4 py-2 bg-white/20 border border-white/30 rounded-lg focus:ring-2 focus:ring-white text-white"
            >
              <option value="all">All Status</option>
              <option value="available">Available</option>
              <option value="pending">Pending</option>
              <option value="allocated">Allocated</option>
            </select>

            <select
              value={skillFilter}
              onChange={(e) => setSkillFilter(e.target.value)}
              className="px-4 py-2 bg-white/20 border border-white/30 rounded-lg focus:ring-2 focus:ring-white text-white"
            >
              <option value="all">All Skills</option>
              {uniqueSkills.slice(0, 10).map(skill => (
                <option key={skill} value={skill}>{skill}</option>
              ))}
            </select>
          </div>
        </div>

        <DndContext
          sensors={sensors}
          collisionDetection={closestCenter}
          onDragStart={handleDragStart}
          onDragEnd={handleDragEnd}
        >
          <div className="grid grid-cols-12 gap-6">
            {/* AI Recommendations Sidebar */}
            <div className="col-span-3">
              <AIRecommendationPanel
                recommendations={recommendations}
                onApplyRecommendation={handleApplyRecommendation}
              />
            </div>

            {/* Available Interns */}
            <div className="col-span-4">
              <div className="bg-white rounded-xl p-6 border border-gray-100">
                <div className="flex items-center space-x-2 mb-4">
                  <Users className="w-5 h-5 text-blue-600" />
                  <h2 className="text-lg font-semibold text-gray-900">Available Interns</h2>
                  <span className="px-2 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-medium">
                    {filteredInterns.length}
                  </span>
                </div>

                <SortableContext items={filteredInterns.map(i => i.id)} strategy={verticalListSortingStrategy}>
                  <div className="space-y-3 max-h-[calc(100vh-300px)] overflow-y-auto">
                    {filteredInterns.map((intern) => (
                      <DraggableInternCard key={intern.id} intern={intern} />
                    ))}
                  </div>
                </SortableContext>
              </div>
            </div>

            {/* Projects */}
            <div className="col-span-5">
              <div className="bg-white rounded-xl p-6 border border-gray-100">
                <div className="flex items-center space-x-2 mb-4">
                  <Briefcase className="w-5 h-5 text-green-600" />
                  <h2 className="text-lg font-semibold text-gray-900">Projects</h2>
                  <span className="px-2 py-1 bg-green-100 text-green-700 rounded-full text-xs font-medium">
                    {projects.length}
                  </span>
                </div>

                <SortableContext items={projects.map(p => p.id)} strategy={verticalListSortingStrategy}>
                  <div className="space-y-4 max-h-[calc(100vh-300px)] overflow-y-auto">
                    {projects.map((project) => (
                      <DroppableProjectCard
                        key={project.id}
                        project={project}
                        allocatedInterns={getProjectAllocations(project.id)}
                        isOver={activeId !== null}
                      />
                    ))}
                  </div>
                </SortableContext>
              </div>
            </div>
          </div>

          <DragOverlay>
            {draggedIntern ? <DraggableInternCard intern={draggedIntern} isOverlay /> : null}
          </DragOverlay>
        </DndContext>
      </motion.div>
    </div>
  );
}