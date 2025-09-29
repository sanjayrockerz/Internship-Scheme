import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  BarChart, 
  Bar, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  LineChart,
  Line,
  Area,
  AreaChart
} from 'recharts';
import { 
  Users, 
  TrendingUp, 
  MapPin, 
  Star, 
  Clock, 
  Award,
  Globe,
  Zap,
  Target
} from 'lucide-react';
import { Card } from './ui/card';
import { Progress } from './ui/progress';
import { Badge } from './ui/badge';
import { Button } from './ui/button';
import { cn, formatNumber, formatPercentage } from '../lib/utils';
import { generateMockInterns } from '../data/mockDataGenerator';

interface WorldClassDashboardProps {
  stats?: any;
  interns?: any[];
  projects?: any[];
  uiState?: any;
  updateUIState?: (updates: any) => void;
}

export function WorldClassDashboard({ stats, interns = [], projects = [] }: WorldClassDashboardProps) {
  const [selectedMetric, setSelectedMetric] = useState('overview');
  const [isLoading, setIsLoading] = useState(false);

  // Calculate diversity statistics from mock data
  const mockCandidates = generateMockInterns(100);
  const diversityStats = {
    countries: new Set(mockCandidates.map(intern => intern.location.split(',')[1]?.trim() || intern.location)).size,
    universities: new Set(mockCandidates.map(intern => intern.university)).size,
    totalCandidates: mockCandidates.length,
    skillCategories: new Set(mockCandidates.flatMap(intern => intern.skills.map(skill => typeof skill === 'string' ? skill : skill.category))).size,
    averageGPA: (mockCandidates.reduce((sum, intern) => sum + intern.gpa, 0) / mockCandidates.length).toFixed(1)
  };
  
  // Get diverse statistics from our enhanced mock data
  const mockInterns = generateMockInterns(100);

  // Mock data for charts
  const allocationTrends = [
    { month: 'Jan', allocations: 45, applications: 120, success: 85 },
    { month: 'Feb', allocations: 52, applications: 135, success: 88 },
    { month: 'Mar', allocations: 68, applications: 150, success: 92 },
    { month: 'Apr', allocations: 73, applications: 145, success: 89 },
    { month: 'May', allocations: 85, applications: 160, success: 94 },
    { month: 'Jun', allocations: 92, applications: 175, success: 96 },
  ];

  const skillsDistribution = [
    { name: 'JavaScript', value: 35, color: '#3B82F6', candidates: 156 },
    { name: 'Python', value: 28, color: '#10B981', candidates: 124 },
    { name: 'React', value: 22, color: '#8B5CF6', candidates: 98 },
    { name: 'Data Science', value: 15, color: '#F59E0B', candidates: 67 },
  ];

  const performanceMetrics = [
    { 
      id: 'interns',
      title: 'Total Interns', 
      value: formatNumber(interns.length || 1234), 
      change: '+12%', 
      changeType: 'positive',
      icon: '👥',
      color: 'from-blue-500 to-blue-600',
      bgColor: 'bg-blue-50',
      description: 'Registered candidates'
    },
    { 
      id: 'projects',
      title: 'Active Projects', 
      value: formatNumber(projects.filter(p => p?.status === 'open').length || 89), 
      change: '+8%',
      changeType: 'positive', 
      icon: '🚀',
      color: 'from-green-500 to-green-600',
      bgColor: 'bg-green-50',
      description: 'Open positions'
    },
    { 
      id: 'matches',
      title: 'Match Success', 
      value: '95.2%', 
      change: '+2.1%',
      changeType: 'positive', 
      icon: '🎯',
      color: 'from-purple-500 to-purple-600',
      bgColor: 'bg-purple-50',
      description: 'AI accuracy rate'
    },
    { 
      id: 'efficiency',
      title: 'Time Efficiency', 
      value: '2.3hrs', 
      change: '-15%',
      changeType: 'positive', 
      icon: '⚡',
      color: 'from-orange-500 to-orange-600',
      bgColor: 'bg-orange-50',
      description: 'Avg processing time'
    },
  ];

  // Generate diverse activities from different candidates
  const activityCandidates = generateMockInterns(20);
  const recentActivities = [
    { 
      id: 1,
      action: `${activityCandidates[0]?.name || 'Aarav Sharma'} allocated to Google AI Research Project`, 
      user: activityCandidates[0]?.location || 'Bangalore, India', 
      time: '2 minutes ago', 
      type: 'allocation',
      avatar: '🎯',
      priority: 'high'
    },
    { 
      id: 2,
      action: `${activityCandidates[1]?.name || 'Sofia Martinez'} completed Machine Learning certification`, 
      user: activityCandidates[1]?.location || 'Barcelona, Spain', 
      time: '8 minutes ago', 
      type: 'achievement',
      avatar: '🏆',
      priority: 'medium'
    },
    { 
      id: 3,
      action: `${activityCandidates[2]?.name || 'Chen Wei'} joined Meta VR internship program`, 
      user: activityCandidates[2]?.location || 'Singapore', 
      time: '15 minutes ago', 
      type: 'allocation',
      avatar: '🥽',
      priority: 'high'
    },
    { 
      id: 4,
      action: `${activityCandidates[3]?.name || 'Aisha Hassan'} portfolio featured in top 10 designs`, 
      user: activityCandidates[3]?.location || 'Dubai, UAE', 
      time: '25 minutes ago', 
      type: 'achievement',
      avatar: '✨',
      priority: 'medium'
    },
    { 
      id: 5,
      action: `${activityCandidates[4]?.name || 'Lucas Silva'} scheduled for Tesla interview`, 
      user: activityCandidates[4]?.location || 'São Paulo, Brazil', 
      time: '35 minutes ago', 
      type: 'interview',
      avatar: '🚗',
      priority: 'high'
    },
    { 
      id: 6,
      action: `${activityCandidates[5]?.name || 'Yuki Tanaka'} AI project achieved 96% accuracy`, 
      user: activityCandidates[5]?.location || 'Tokyo, Japan', 
      time: '45 minutes ago', 
      type: 'project',
      avatar: '🤖',
      priority: 'high'
    },
    { 
      id: 7,
      action: 'New blockchain internship posted by Coinbase', 
      user: 'System Notification', 
      time: '1 hour ago', 
      type: 'system',
      avatar: '💎',
      priority: 'medium'
    },
  ];

  const handleMetricClick = (metricId: string) => {
    setSelectedMetric(metricId);
    // Add haptic feedback if supported
    if (navigator.vibrate) {
      navigator.vibrate(50);
    }
  };

  const handleRefresh = async () => {
    setIsLoading(true);
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1500));
    setIsLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
      <div className="max-w-7xl mx-auto p-6 space-y-8">
        {/* Hero Header */}
        <motion.div 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center py-8"
        >
          <div className="inline-flex items-center justify-center w-20 h-20 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 mb-6">
            <span className="text-3xl">🎯</span>
          </div>
          <h1 className="text-5xl font-bold bg-gradient-to-r from-gray-900 via-blue-800 to-purple-800 bg-clip-text text-transparent mb-4">
            Smart Allocation Engine
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            AI-powered internship matching with real-time analytics and intelligent automation
          </p>
        </motion.div>

        {/* Action Bar */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="flex flex-wrap justify-center gap-4 mb-8"
        >
          <Button 
            onClick={handleRefresh}
            disabled={isLoading}
            className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white shadow-lg hover:shadow-xl transition-all duration-300"
          >
            {isLoading ? (
              <>
                <motion.div 
                  animate={{ rotate: 360 }}
                  transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                  className="w-4 h-4 border-2 border-white border-t-transparent rounded-full mr-2"
                />
                Refreshing...
              </>
            ) : (
              <>
                🔄 Refresh Data
              </>
            )}
          </Button>
          <Button variant="outline" className="bg-white/80 backdrop-blur-sm">
            📊 Generate Report
          </Button>
          <Button variant="outline" className="bg-white/80 backdrop-blur-sm">
            🚀 New Allocation
          </Button>
          <Button variant="outline" className="bg-white/80 backdrop-blur-sm">
            ⚙️ AI Settings
          </Button>
        </motion.div>

        {/* Global Diversity Stats */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8"
        >
          <Card className="p-6 bg-gradient-to-r from-blue-50 to-purple-50 border-0 shadow-lg">
            <div className="flex items-center justify-between mb-4">
              <div>
                <h3 className="text-xl font-bold text-gray-900">Global Talent Diversity</h3>
                <p className="text-sm text-gray-600">Worldwide reach and inclusive opportunities</p>
              </div>
              <Globe className="w-8 h-8 text-blue-500" />
            </div>
            
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
              <div className="text-center">
                <div className="text-2xl font-bold text-blue-600">{diversityStats.countries}</div>
                <div className="text-xs text-gray-600">Countries</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-green-600">{diversityStats.universities}</div>
                <div className="text-xs text-gray-600">Universities</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-purple-600">{diversityStats.totalCandidates}</div>
                <div className="text-xs text-gray-600">Candidates</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-orange-600">{diversityStats.skillCategories}+</div>
                <div className="text-xs text-gray-600">Skill Areas</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-red-600">{diversityStats.averageGPA}</div>
                <div className="text-xs text-gray-600">Avg GPA</div>
              </div>
            </div>
          </Card>
        </motion.div>

        {/* Performance Metrics Grid */}
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6"
        >
          {performanceMetrics.map((metric, index) => (
            <motion.div
              key={metric.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.1 * index }}
              whileHover={{ scale: 1.02, y: -5 }}
              whileTap={{ scale: 0.98 }}
              className="cursor-pointer"
              onClick={() => handleMetricClick(metric.id)}
            >
              <Card className={cn(
                "relative overflow-hidden border-0 shadow-lg hover:shadow-2xl transition-all duration-500",
                metric.bgColor,
                selectedMetric === metric.id && "ring-2 ring-blue-500 ring-offset-2"
              )}>
                {/* Animated Background */}
                <div className={cn(
                  "absolute top-0 right-0 w-32 h-32 opacity-10 rounded-full transform translate-x-16 -translate-y-16 transition-transform duration-700 hover:scale-110",
                  `bg-gradient-to-br ${metric.color}`
                )} />
                
                {/* Glow Effect */}
                <div className={cn(
                  "absolute inset-0 opacity-0 hover:opacity-20 transition-opacity duration-300",
                  `bg-gradient-to-br ${metric.color}`
                )} />
                
                <div className="relative p-6">
                  <div className="flex items-start justify-between mb-4">
                    <div className="space-y-1">
                      <p className="text-sm font-semibold text-gray-600 uppercase tracking-wider">{metric.title}</p>
                      <p className="text-3xl font-bold text-gray-900">{metric.value}</p>
                    </div>
                    <div className="text-3xl transform transition-transform duration-300 hover:scale-110">
                      {metric.icon}
                    </div>
                  </div>
                  
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                      <span className={cn(
                        "text-sm font-semibold",
                        metric.changeType === 'positive' ? 'text-green-600' : 'text-red-600'
                      )}>
                        {metric.change}
                      </span>
                      <span className="text-xs text-gray-500">vs last month</span>
                    </div>
                  </div>
                  
                  <p className="text-xs text-gray-500 mt-2">{metric.description}</p>
                </div>
              </Card>
            </motion.div>
          ))}
        </motion.div>

        {/* Advanced Analytics Section */}
        <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">
          {/* Allocation Trends - Advanced Chart */}
          <motion.div 
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.3 }}
            className="xl:col-span-2"
          >
            <Card className="p-6 bg-white/90 backdrop-blur-sm border-0 shadow-lg">
              <div className="flex items-center justify-between mb-6">
                <div>
                  <h3 className="text-xl font-bold text-gray-900">Allocation Performance</h3>
                  <p className="text-sm text-gray-600">Real-time allocation trends and success rates</p>
                </div>
                <div className="flex space-x-2">
                  <Badge variant="secondary" className="bg-blue-100 text-blue-800">
                    Live Data
                  </Badge>
                  <Badge variant="outline">6 Months</Badge>
                </div>
              </div>
              <div className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={allocationTrends}>
                    <defs>
                      <linearGradient id="successGradient" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#10B981" stopOpacity={0.4}/>
                        <stop offset="95%" stopColor="#10B981" stopOpacity={0.1}/>
                      </linearGradient>
                      <linearGradient id="allocationsGradient" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#3B82F6" stopOpacity={0.4}/>
                        <stop offset="95%" stopColor="#3B82F6" stopOpacity={0.1}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" opacity={0.5} />
                    <XAxis 
                      dataKey="month" 
                      stroke="#6B7280" 
                      fontSize={12}
                      tickLine={false}
                    />
                    <YAxis 
                      stroke="#6B7280" 
                      fontSize={12}
                      tickLine={false}
                      axisLine={false}
                    />
                    <Tooltip 
                      contentStyle={{
                        backgroundColor: 'rgba(255, 255, 255, 0.95)',
                        border: 'none',
                        borderRadius: '12px',
                        boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1)',
                        backdropFilter: 'blur(10px)'
                      }}
                    />
                    <Area
                      type="monotone"
                      dataKey="success"
                      stroke="#10B981"
                      strokeWidth={3}
                      fillOpacity={1}
                      fill="url(#successGradient)"
                    />
                    <Area
                      type="monotone"
                      dataKey="allocations"
                      stroke="#3B82F6"
                      strokeWidth={3}
                      fillOpacity={1}
                      fill="url(#allocationsGradient)"
                    />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </Card>
          </motion.div>
          
          {/* Skills Distribution - Interactive Pie Chart */}
          <motion.div 
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.4 }}
          >
            <Card className="p-6 bg-white/90 backdrop-blur-sm border-0 shadow-lg">
              <div className="flex items-center justify-between mb-6">
                <h3 className="text-xl font-bold text-gray-900">Skills Distribution</h3>
                <Badge variant="outline" className="text-xs">Top Skills</Badge>
              </div>
              <div className="h-60 mb-6">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie
                      data={skillsDistribution}
                      cx="50%"
                      cy="50%"
                      outerRadius={70}
                      innerRadius={35}
                      paddingAngle={3}
                      dataKey="value"
                    >
                      {skillsDistribution.map((entry, index) => (
                        <Cell 
                          key={`cell-${index}`} 
                          fill={entry.color}
                          stroke="white"
                          strokeWidth={2}
                        />
                      ))}
                    </Pie>
                    <Tooltip 
                      formatter={(value: any, name: any, props: any) => [
                        `${value}% (${props.payload.candidates} candidates)`,
                        name
                      ]}
                    />
                  </PieChart>
                </ResponsiveContainer>
              </div>
              <div className="space-y-3">
                {skillsDistribution.map((skill, index) => (
                  <motion.div 
                    key={skill.name}
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: 0.1 * index }}
                    className="flex items-center justify-between p-2 rounded-lg hover:bg-gray-50 transition-colors"
                  >
                    <div className="flex items-center space-x-3">
                      <div 
                        className="w-3 h-3 rounded-full shadow-sm" 
                        style={{ backgroundColor: skill.color }}
                      />
                      <span className="text-sm font-medium text-gray-700">{skill.name}</span>
                    </div>
                    <div className="text-right">
                      <span className="text-sm font-semibold text-gray-900">{skill.value}%</span>
                      <p className="text-xs text-gray-500">{skill.candidates} candidates</p>
                    </div>
                  </motion.div>
                ))}
              </div>
            </Card>
          </motion.div>
        </div>

        {/* Featured Candidates Showcase */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
        >
          <Card className="p-6 bg-white/90 backdrop-blur-sm border-0 shadow-lg">
            <div className="flex items-center justify-between mb-6">
              <div>
                <h3 className="text-xl font-bold text-gray-900">Featured Candidates</h3>
                <p className="text-sm text-gray-600">Top performing interns from around the world</p>
              </div>
              <div className="flex items-center space-x-2">
                <Globe className="w-4 h-4 text-blue-500" />
                <span className="text-sm font-medium text-blue-600">Global Talent</span>
              </div>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {generateMockInterns(8).slice(0, 6).map((intern, index) => {
                const gradients = [
                  'from-blue-500 to-purple-600',
                  'from-green-500 to-teal-600',
                  'from-pink-500 to-rose-600',
                  'from-yellow-500 to-orange-600',
                  'from-indigo-500 to-blue-600',
                  'from-red-500 to-pink-600'
                ];
                
                return (
                  <motion.div
                    key={intern.id}
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: index * 0.1 }}
                    className="group relative overflow-hidden bg-gradient-to-br from-white to-gray-50 rounded-xl border border-gray-100 hover:border-blue-200 hover:shadow-lg transition-all duration-300 cursor-pointer p-4"
                    whileHover={{ y: -4 }}
                  >
                    <div className="flex items-start space-x-4">
                      <div className="relative">
                        <img
                          src={intern.avatar}
                          alt={intern.name}
                          className="w-14 h-14 rounded-full border-3 border-white shadow-lg"
                        />
                        <div className={cn(
                          "absolute -bottom-1 -right-1 w-5 h-5 rounded-full border-2 border-white flex items-center justify-center",
                          intern.status === 'available' ? 'bg-green-500' :
                          intern.status === 'allocated' ? 'bg-blue-500' : 'bg-gray-400'
                        )}>
                          <div className="w-2 h-2 bg-white rounded-full" />
                        </div>
                      </div>
                      
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center justify-between mb-1">
                          <h4 className="font-bold text-gray-900 truncate">{intern.name}</h4>
                          <div className="flex items-center space-x-1">
                            <Star className="w-3 h-3 text-yellow-500 fill-current" />
                            <span className="text-sm font-medium text-gray-700">{intern.gpa}</span>
                          </div>
                        </div>
                        
                        <p className="text-sm text-gray-600 truncate mb-2">{intern.university}</p>
                        
                        <div className="flex items-center space-x-2 mb-3">
                          <MapPin className="w-3 h-3 text-gray-400" />
                          <span className="text-xs text-gray-500 truncate">{intern.location}</span>
                          <div className="mx-1 w-1 h-1 bg-gray-300 rounded-full" />
                          <Clock className="w-3 h-3 text-gray-400" />
                          <span className="text-xs text-gray-500">{intern.experience}y exp</span>
                        </div>
                        
                        <div className="flex flex-wrap gap-1 mb-3">
                          {intern.skills.slice(0, 3).map((skill, skillIndex) => (
                            <span
                              key={skillIndex}
                              className={cn(
                                "px-2 py-1 rounded-full text-xs font-medium",
                                skillIndex === 0 ? 'bg-blue-100 text-blue-700' :
                                skillIndex === 1 ? 'bg-green-100 text-green-700' :
                                'bg-purple-100 text-purple-700'
                              )}
                            >
                              {typeof skill === 'string' ? skill : skill.name}
                            </span>
                          ))}
                          {intern.skills.length > 3 && (
                            <span className="px-2 py-1 bg-gray-100 text-gray-600 rounded-full text-xs font-medium">
                              +{intern.skills.length - 3}
                            </span>
                          )}
                        </div>
                        
                        <div className="flex items-center justify-between">
                          <div className={cn(
                            "px-2 py-1 rounded-full text-xs font-medium",
                            intern.status === 'available' ? 'bg-green-100 text-green-700' :
                            intern.status === 'allocated' ? 'bg-blue-100 text-blue-700' :
                            'bg-gray-100 text-gray-700'
                          )}>
                            {intern.status}
                          </div>
                          
                          <div className="flex items-center space-x-1">
                            <TrendingUp className="w-3 h-3 text-green-500" />
                            <span className="text-xs font-bold text-green-600">{intern.matchScore}%</span>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    {/* Hover overlay */}
                    <div className="absolute inset-0 bg-gradient-to-r from-blue-500/10 to-purple-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-xl" />
                  </motion.div>
                );
              })}
            </div>
            
            <div className="mt-6 text-center">
              <Button variant="outline" className="group">
                <Users className="w-4 h-4 mr-2 group-hover:scale-110 transition-transform" />
                View All Candidates
                <span className="ml-2 px-2 py-0.5 bg-blue-100 text-blue-700 rounded-full text-xs font-medium">
                  {generateMockInterns(100).length}
                </span>
              </Button>
            </div>
          </Card>
        </motion.div>

        {/* Real-time Activity Feed */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5 }}
        >
          <Card className="p-6 bg-white/90 backdrop-blur-sm border-0 shadow-lg">
            <div className="flex items-center justify-between mb-6">
              <div>
                <h3 className="text-xl font-bold text-gray-900">Live Activity Feed</h3>
                <p className="text-sm text-gray-600">Real-time system events and notifications</p>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
                <span className="text-xs text-green-600 font-medium">Live</span>
              </div>
            </div>
            <div className="space-y-4 max-h-80 overflow-y-auto">
              {recentActivities.map((activity, index) => (
                <motion.div
                  key={activity.id}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.1 * index }}
                  className="flex items-start space-x-4 p-4 rounded-xl bg-gradient-to-r from-gray-50 to-white hover:from-blue-50 hover:to-white transition-all duration-300 cursor-pointer group border border-gray-100 hover:border-blue-200"
                >
                  <div className="flex-shrink-0">
                    <div className={cn(
                      "w-10 h-10 rounded-full flex items-center justify-center text-lg",
                      activity.type === 'system' ? 'bg-gradient-to-r from-blue-500 to-blue-600' : 
                      activity.type === 'allocation' ? 'bg-gradient-to-r from-green-500 to-green-600' : 
                      'bg-gradient-to-r from-purple-500 to-purple-600'
                    )}>
                      <span className="text-white">{activity.avatar}</span>
                    </div>
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-gray-900 group-hover:text-blue-900 transition-colors">
                      {activity.action}
                    </p>
                    <div className="flex items-center justify-between mt-1">
                      <div className="flex items-center space-x-1">
                        <MapPin className="w-3 h-3 text-gray-400" />
                        <p className="text-xs text-gray-500">{activity.user}</p>
                      </div>
                      <div className="flex items-center space-x-2">
                        <Badge 
                          variant={activity.priority === 'high' ? 'destructive' : 'secondary'}
                          className="text-xs"
                        >
                          {activity.priority}
                        </Badge>
                        <span className="text-xs text-gray-400">{activity.time}</span>
                      </div>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </Card>
        </motion.div>
      </div>
    </div>
  );
}

export default WorldClassDashboard;