import React, { useState, useMemo, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
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
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  ComposedChart
} from 'recharts';
import {
  BarChart3,
  TrendingUp,
  Users,
  Globe,
  Award,
  Target,
  Brain,
  Download,
  Clock,
  MapPin,
  Star,
  Activity,
  ArrowUpRight,
  ArrowDownRight,
  Play,
  Pause,
  Maximize2
} from 'lucide-react';
import { generateMockInterns } from '../data/mockDataGenerator';
import { cn } from '../lib/utils';

const PREMIUM_COLORS = {
  gradient: ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe', '#00f2fe', '#ff9a9e', '#fecfef']
};

interface AnalyticsData {
  interns?: any[];
  projects?: any[];
}

export const AnalyticsDashboard = ({ interns = [], projects = [] }: AnalyticsData) => {
  const [viewMode, setViewMode] = useState<'executive' | 'detailed' | 'realtime'>('executive');
  const [isRealtime, setIsRealtime] = useState(false);
  const [realtimeData, setRealtimeData] = useState<any[]>([]);

  useEffect(() => {
    // Process mock data to generate analytics
    const processAnalytics = () => {
      const skills: { [key: string]: number } = {};
      const locations: { [key: string]: number } = {};
      const sectors: { [key: string]: number } = {};
      const experience: { [key: string]: number } = {};
      const education: { [key: string]: number } = {};

      // Process candidates data
      mockCandidates.forEach(candidate => {
        candidate.skills.forEach((skill: string) => {
          skills[skill] = (skills[skill] || 0) + 1;
        });
        
        const locationKey = typeof candidate.location === 'string' ? candidate.location : `${candidate.location.state}, ${candidate.location.district}`;
        locations[locationKey] = (locations[locationKey] || 0) + 1;
        education[candidate.education.degree] = (education[candidate.education.degree] || 0) + 1;
        
        const workExp = (candidate as any).workExperience || [];
        const expLevel = workExp.length === 0 ? 'Entry Level' :
                        workExp.length <= 2 ? 'Junior' :
                        workExp.length <= 5 ? 'Mid-Level' : 'Senior';
        experience[expLevel] = (experience[expLevel] || 0) + 1;
      });

      // Process internships data
      mockInternships.forEach(internship => {
        sectors[internship.sector] = (sectors[internship.sector] || 0) + 1;
      });

      // Generate mock allocation trends
      const allocationTrends = [
        { month: 'Jan', allocated: 85, applied: 120 },
        { month: 'Feb', allocated: 92, applied: 135 },
        { month: 'Mar', allocated: 78, applied: 110 },
        { month: 'Apr', allocated: 88, applied: 125 },
        { month: 'May', allocated: 95, applied: 140 },
        { month: 'Jun', allocated: 102, applied: 150 }
      ];

      const successRates = {
        'Technology': 92,
        'Healthcare': 88,
        'Finance': 85,
        'Education': 90,
        'Manufacturing': 82,
        'Retail': 78
      };

      setAnalyticsData({
        skillsDistribution: skills,
        locationDistribution: locations,
        sectorDistribution: sectors,
        experienceDistribution: experience,
        educationDistribution: education,
        allocationTrends,
        successRates
      });
    };

    processAnalytics();
  }, []);

  if (!analyticsData) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  const skillsChartData = {
    labels: Object.keys(analyticsData.skillsDistribution).slice(0, 10),
    datasets: [{
      label: 'Candidates',
      data: Object.values(analyticsData.skillsDistribution).slice(0, 10),
      backgroundColor: [
        'rgba(59, 130, 246, 0.8)',
        'rgba(147, 51, 234, 0.8)',
        'rgba(239, 68, 68, 0.8)',
        'rgba(34, 197, 94, 0.8)',
        'rgba(251, 191, 36, 0.8)',
        'rgba(168, 85, 247, 0.8)',
        'rgba(236, 72, 153, 0.8)',
        'rgba(20, 184, 166, 0.8)',
        'rgba(245, 101, 101, 0.8)',
        'rgba(129, 140, 248, 0.8)'
      ],
      borderColor: [
        'rgba(59, 130, 246, 1)',
        'rgba(147, 51, 234, 1)',
        'rgba(239, 68, 68, 1)',
        'rgba(34, 197, 94, 1)',
        'rgba(251, 191, 36, 1)',
        'rgba(168, 85, 247, 1)',
        'rgba(236, 72, 153, 1)',
        'rgba(20, 184, 166, 1)',
        'rgba(245, 101, 101, 1)',
        'rgba(129, 140, 248, 1)'
      ],
      borderWidth: 2,
      borderRadius: 8,
      borderSkipped: false,
    }]
  };

  const locationPieData = {
    labels: Object.keys(analyticsData.locationDistribution),
    datasets: [{
      data: Object.values(analyticsData.locationDistribution),
      backgroundColor: [
        'rgba(59, 130, 246, 0.8)',
        'rgba(147, 51, 234, 0.8)',
        'rgba(239, 68, 68, 0.8)',
        'rgba(34, 197, 94, 0.8)',
        'rgba(251, 191, 36, 0.8)',
        'rgba(168, 85, 247, 0.8)',
      ],
      borderColor: [
        'rgba(59, 130, 246, 1)',
        'rgba(147, 51, 234, 1)',
        'rgba(239, 68, 68, 1)',
        'rgba(34, 197, 94, 1)',
        'rgba(251, 191, 36, 1)',
        'rgba(168, 85, 247, 1)',
      ],
      borderWidth: 3,
    }]
  };

  const trendLineData = {
    labels: analyticsData.allocationTrends.map(d => d.month),
    datasets: [
      {
        label: 'Applications',
        data: analyticsData.allocationTrends.map(d => d.applied),
        borderColor: 'rgba(147, 51, 234, 1)',
        backgroundColor: 'rgba(147, 51, 234, 0.1)',
        fill: true,
        tension: 0.4,
        pointRadius: 6,
        pointHoverRadius: 8,
        pointBackgroundColor: 'rgba(147, 51, 234, 1)',
        pointBorderColor: '#fff',
        pointBorderWidth: 2,
      },
      {
        label: 'Successful Allocations',
        data: analyticsData.allocationTrends.map(d => d.allocated),
        borderColor: 'rgba(34, 197, 94, 1)',
        backgroundColor: 'rgba(34, 197, 94, 0.1)',
        fill: true,
        tension: 0.4,
        pointRadius: 6,
        pointHoverRadius: 8,
        pointBackgroundColor: 'rgba(34, 197, 94, 1)',
        pointBorderColor: '#fff',
        pointBorderWidth: 2,
      }
    ]
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top' as const,
        labels: {
          padding: 20,
          font: {
            size: 12,
            weight: 500
          }
        }
      },
      tooltip: {
        backgroundColor: 'rgba(17, 24, 39, 0.95)',
        titleColor: '#fff',
        bodyColor: '#fff',
        borderColor: 'rgba(59, 130, 246, 0.5)',
        borderWidth: 1,
        cornerRadius: 12,
        padding: 12,
        displayColors: true,
        boxPadding: 4,
      }
    },
    scales: {
      x: {
        grid: {
          display: false
        },
        ticks: {
          font: {
            size: 12
          }
        }
      },
      y: {
        grid: {
          color: 'rgba(156, 163, 175, 0.2)'
        },
        ticks: {
          font: {
            size: 12
          }
        }
      }
    }
  };

  const pieOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'right' as const,
        labels: {
          padding: 20,
          font: {
            size: 12,
            weight: 500
          }
        }
      },
      tooltip: {
        backgroundColor: 'rgba(17, 24, 39, 0.95)',
        titleColor: '#fff',
        bodyColor: '#fff',
        borderColor: 'rgba(59, 130, 246, 0.5)',
        borderWidth: 1,
        cornerRadius: 12,
        padding: 12,
      }
    }
  };

  const analyticsStats = [
    {
      title: 'Total Candidates',
      value: mockCandidates.length,
      icon: Users,
      color: 'from-blue-500 to-blue-600',
      change: '+12%',
      changeType: 'positive'
    },
    {
      title: 'Available Positions',
      value: mockInternships.length,
      icon: Target,
      color: 'from-green-500 to-green-600',
      change: '+8%',
      changeType: 'positive'
    },
    {
      title: 'Success Rate',
      value: '87%',
      icon: Award,
      color: 'from-purple-500 to-purple-600',
      change: '+5%',
      changeType: 'positive'
    },
    {
      title: 'Avg. Processing Time',
      value: '2.3h',
      icon: Clock,
      color: 'from-orange-500 to-orange-600',
      change: '-15%',
      changeType: 'positive'
    }
  ];

  return (
    <TooltipProvider>
      <div className="space-y-8 animate-fadeIn">
        {/* Header */}
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
          <div className="animate-slideInUp">
            <div className="flex items-center space-x-3 mb-2">
              <div className="p-3 bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl shadow-lg">
                <BarChart3 className="w-8 h-8 text-white" />
              </div>
              <div>
                <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                  Analytics Dashboard
                </h1>
                <p className="text-gray-600 text-lg">Comprehensive insights and performance metrics</p>
              </div>
            </div>
          </div>
          
          <div className="flex items-center gap-3 animate-slideInRight">
            <Button variant="outline" size="sm" className="modern-card">
              Export Report
            </Button>
            <Button className="gradient-button">
              <TrendingUp className="w-4 h-4 mr-2" />
              Generate Insights
            </Button>
          </div>
        </div>

        {/* Stats Overview */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          {analyticsStats.map((stat, index) => {
            const Icon = stat.icon;
            return (
              <Card key={index} className="modern-card interactive-hover animate-bounceIn" style={{ animationDelay: `${index * 100}ms` }}>
                <div className="p-6">
                  <div className="flex items-center justify-between mb-4">
                    <div className={`w-12 h-12 bg-gradient-to-br ${stat.color} rounded-xl flex items-center justify-center shadow-lg`}>
                      <Icon className="w-6 h-6 text-white" />
                    </div>
                    <Badge className={`${stat.changeType === 'positive' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                      {stat.change}
                    </Badge>
                  </div>
                  <h3 className="text-2xl font-bold text-gray-900 mb-1">{stat.value}</h3>
                  <p className="text-sm text-gray-600">{stat.title}</p>
                </div>
              </Card>
            );
          })}
        </div>

        {/* Chart Navigation */}
        <div className="flex flex-wrap gap-3">
          {[
            { id: 'overview', label: 'Overview', icon: BarChart3 },
            { id: 'skills', label: 'Skills Analysis', icon: Target },
            { id: 'locations', label: 'Location Distribution', icon: MapPin },
            { id: 'sectors', label: 'Sector Breakdown', icon: Building },
            { id: 'trends', label: 'Allocation Trends', icon: TrendingUp },
            { id: 'education', label: 'Education Levels', icon: BookOpen }
          ].map((chart) => {
            const Icon = chart.icon;
            return (
              <Button
                key={chart.id}
                variant={selectedChart === chart.id ? "default" : "outline"}
                onClick={() => setSelectedChart(chart.id)}
                className={`flex items-center space-x-2 ${selectedChart === chart.id ? 'gradient-button' : 'modern-card hover:shadow-lg'} transition-all duration-300`}
              >
                <Icon className="w-4 h-4" />
                <span>{chart.label}</span>
              </Button>
            );
          })}
        </div>

        {/* Charts Section */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Skills Distribution Chart */}
          {(selectedChart === 'overview' || selectedChart === 'skills') && (
            <Card className="modern-card animate-slideInUp">
              <div className="p-6">
                <div className="flex items-center justify-between mb-6">
                  <h3 className="text-xl font-semibold text-gray-900 flex items-center">
                    <Target className="w-5 h-5 mr-2 text-blue-600" />
                    Top Skills in Demand
                  </h3>
                  <Tooltip>
                    <TooltipTrigger asChild>
                      <Button variant="outline" size="sm">
                        View All
                      </Button>
                    </TooltipTrigger>
                    <TooltipContent>
                      <p>View complete skills breakdown</p>
                    </TooltipContent>
                  </Tooltip>
                </div>
                <div className="h-80">
                  <Bar data={skillsChartData} options={chartOptions} />
                </div>
              </div>
            </Card>
          )}

          {/* Location Distribution Chart */}
          {(selectedChart === 'overview' || selectedChart === 'locations') && (
            <Card className="modern-card animate-slideInUp">
              <div className="p-6">
                <div className="flex items-center justify-between mb-6">
                  <h3 className="text-xl font-semibold text-gray-900 flex items-center">
                    <MapPin className="w-5 h-5 mr-2 text-green-600" />
                    Geographic Distribution
                  </h3>
                  <Badge className="bg-green-100 text-green-800">
                    {Object.keys(analyticsData.locationDistribution).length} Cities
                  </Badge>
                </div>
                <div className="h-80">
                  <Pie data={locationPieData} options={pieOptions} />
                </div>
              </div>
            </Card>
          )}

          {/* Allocation Trends */}
          {(selectedChart === 'overview' || selectedChart === 'trends') && (
            <Card className="modern-card animate-slideInUp lg:col-span-2">
              <div className="p-6">
                <div className="flex items-center justify-between mb-6">
                  <h3 className="text-xl font-semibold text-gray-900 flex items-center">
                    <TrendingUp className="w-5 h-5 mr-2 text-purple-600" />
                    Allocation Trends (6 Months)
                  </h3>
                  <div className="flex items-center space-x-4">
                    <Badge className="bg-purple-100 text-purple-800">Monthly View</Badge>
                    <Button variant="outline" size="sm">
                      Export Data
                    </Button>
                  </div>
                </div>
                <div className="h-80">
                  <Line data={trendLineData} options={chartOptions} />
                </div>
              </div>
            </Card>
          )}
        </div>

        {/* Success Rates by Sector */}
        <Card className="modern-card animate-slideInUp">
          <div className="p-6">
            <h3 className="text-xl font-semibold text-gray-900 mb-6 flex items-center">
              <Award className="w-5 h-5 mr-2 text-orange-600" />
              Success Rates by Sector
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {Object.entries(analyticsData.successRates).map(([sector, rate], index) => (
                <div key={sector} className="animate-bounceIn" style={{ animationDelay: `${index * 100}ms` }}>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm font-medium text-gray-900">{sector}</span>
                    <span className="text-sm font-semibold text-gray-600">{rate}%</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-3 mb-3">
                    <div 
                      className="bg-gradient-to-r from-blue-500 to-purple-600 h-3 rounded-full transition-all duration-1000 ease-out"
                      style={{ width: `${rate}%` }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </Card>

        {/* Insights and Recommendations */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <Card className="modern-card animate-slideInUp">
            <div className="p-6">
              <h3 className="text-xl font-semibold text-gray-900 mb-4 flex items-center">
                <Target className="w-5 h-5 mr-2 text-blue-600" />
                Key Insights
              </h3>
              <div className="space-y-4">
                <div className="flex items-start space-x-3">
                  <div className="w-2 h-2 bg-blue-500 rounded-full mt-2"></div>
                  <p className="text-sm text-gray-700">
                    <span className="font-semibold">High Demand:</span> JavaScript and React skills show 40% higher placement rates
                  </p>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="w-2 h-2 bg-green-500 rounded-full mt-2"></div>
                  <p className="text-sm text-gray-700">
                    <span className="font-semibold">Location Trends:</span> Remote positions have increased by 65% this quarter
                  </p>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="w-2 h-2 bg-purple-500 rounded-full mt-2"></div>
                  <p className="text-sm text-gray-700">
                    <span className="font-semibold">Sector Growth:</span> Technology sector leads with 35% of total allocations
                  </p>
                </div>
              </div>
            </div>
          </Card>

          <Card className="modern-card animate-slideInUp">
            <div className="p-6">
              <h3 className="text-xl font-semibold text-gray-900 mb-4 flex items-center">
                <TrendingUp className="w-5 h-5 mr-2 text-green-600" />
                Recommendations
              </h3>
              <div className="space-y-4">
                <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                  <p className="text-sm text-blue-800">
                    <span className="font-semibold">Skill Focus:</span> Increase training programs for cloud technologies and data science
                  </p>
                </div>
                <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                  <p className="text-sm text-green-800">
                    <span className="font-semibold">Partnership Opportunity:</span> Expand relationships with tech companies in tier-2 cities
                  </p>
                </div>
                <div className="p-4 bg-purple-50 rounded-lg border border-purple-200">
                  <p className="text-sm text-purple-800">
                    <span className="font-semibold">Process Improvement:</span> Automate initial screening to reduce processing time by 30%
                  </p>
                </div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </TooltipProvider>
  );
};