import { useState } from 'react';
import { Users, Building, Target, TrendingUp, Bell, RefreshCw, Eye, Download, Filter, Zap, AlertCircle, BarChart3 } from 'lucide-react';
import { Card } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from './ui/dialog';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from './ui/tooltip';
import { mockCandidates as candidates, mockInternships as internships } from '../data/mockData';
import { calculateMatchScore } from '../lib/utils';

export const Dashboard = () => {
  const [selectedCard, setSelectedCard] = useState<string | null>(null);
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [notifications] = useState([
    { id: 1, message: "New candidate registered: Priya Sharma", time: "2 mins ago", type: "info" as const },
    { id: 2, message: "High match found (95%): Rahul → Tech Lead", time: "5 mins ago", type: "success" as const },
    { id: 3, message: "Allocation pending approval", time: "10 mins ago", type: "warning" as const }
  ]);

  const totalMatches = candidates.reduce((total, candidate) => {
    return total + internships.filter(internship => 
      calculateMatchScore(candidate, internship) >= 70
    ).length;
  }, 0);

  const avgMatchScore = Math.round(
    candidates.reduce((total, candidate) => {
      const scores = internships.map(internship => calculateMatchScore(candidate, internship));
      return total + Math.max(...scores);
    }, 0) / candidates.length
  );

  const handleRefresh = async () => {
    setIsRefreshing(true);
    await new Promise(resolve => setTimeout(resolve, 2000));
    setIsRefreshing(false);
  };

  const handleCardClick = (cardType: string) => {
    setSelectedCard(cardType);
  };

  const stats = [
    {
      title: 'Total Candidates',
      value: candidates.length,
      icon: Users,
      color: 'from-blue-500 to-blue-600',
      textColor: 'text-blue-600',
      bgColor: 'bg-blue-50',
      change: '+12%',
      changeType: 'positive' as const
    },
    {
      title: 'Available Positions',
      value: internships.length,
      icon: Building,
      color: 'from-green-500 to-green-600',
      textColor: 'text-green-600',
      bgColor: 'bg-green-50',
      change: '+8%',
      changeType: 'positive' as const
    },
    {
      title: 'High Matches (70%+)',
      value: totalMatches,
      icon: Target,
      color: 'from-purple-500 to-purple-600',
      textColor: 'text-purple-600',
      bgColor: 'bg-purple-50',
      change: '+24%',
      changeType: 'positive' as const
    },
    {
      title: 'Avg Match Score',
      value: `${avgMatchScore}%`,
      icon: TrendingUp,
      color: 'from-orange-500 to-orange-600',
      textColor: 'text-orange-600',
      bgColor: 'bg-orange-50',
      change: '+5%',
      changeType: 'positive' as const
    }
  ];

  const recentActivity = [
    { 
      id: 1,
      action: 'New candidate registered', 
      name: 'Priya Sharma', 
      time: '2 hours ago',
      type: 'candidate' as const,
      priority: 'medium' as const
    },
    { 
      id: 2,
      action: 'Internship position added', 
      name: 'Data Science Intern', 
      time: '4 hours ago',
      type: 'position' as const,
      priority: 'high' as const
    },
    { 
      id: 3,
      action: 'Match found (95%)', 
      name: 'Rahul Kumar → Tech Lead', 
      time: '6 hours ago',
      type: 'match' as const,
      priority: 'high' as const
    },
    { 
      id: 4,
      action: 'Application submitted', 
      name: 'Anita Patel', 
      time: '1 day ago',
      type: 'application' as const,
      priority: 'low' as const
    }
  ];

  const getNotificationColor = (type: string) => {
    switch (type) {
      case 'success': return 'bg-green-100 text-green-800 border-green-200';
      case 'warning': return 'bg-yellow-100 text-yellow-800 border-yellow-200';
      case 'info': return 'bg-blue-100 text-blue-800 border-blue-200';
      default: return 'bg-gray-100 text-gray-800 border-gray-200';
    }
  };

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'high': return 'bg-red-100 text-red-800';
      case 'medium': return 'bg-yellow-100 text-yellow-800';
      case 'low': return 'bg-green-100 text-green-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <TooltipProvider>
      <div className="space-y-8 animate-fadeIn">
        {/* Header Section with Actions */}
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          <div className="animate-slideInUp">
            <h1 className="text-4xl font-bold bg-gradient-to-r from-gray-900 to-gray-600 bg-clip-text text-transparent">
              Dashboard
            </h1>
            <p className="text-gray-600 mt-2 text-lg">PM Internship Allocation System Overview</p>
          </div>
          
          <div className="flex items-center gap-3 animate-slideInRight">
            <Tooltip>
              <TooltipTrigger asChild>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={handleRefresh}
                  disabled={isRefreshing}
                  className="modern-card hover:shadow-lg transition-all duration-300"
                >
                  <RefreshCw className={`w-4 h-4 mr-2 ${isRefreshing ? 'animate-spin' : ''}`} />
                  Refresh
                </Button>
              </TooltipTrigger>
              <TooltipContent>
                <p>Refresh dashboard data</p>
              </TooltipContent>
            </Tooltip>

            <Dialog>
              <DialogTrigger asChild>
                <Button variant="outline" size="sm" className="modern-card hover:shadow-lg">
                  <Bell className="w-4 h-4 mr-2" />
                  Notifications
                  <Badge className="ml-2 bg-red-500">{notifications.length}</Badge>
                </Button>
              </DialogTrigger>
              <DialogContent className="max-w-md">
                <DialogHeader>
                  <DialogTitle>Recent Notifications</DialogTitle>
                </DialogHeader>
                <div className="space-y-3">
                  {notifications.map((notification) => (
                    <div
                      key={notification.id}
                      className={`p-3 rounded-lg border ${getNotificationColor(notification.type)}`}
                    >
                      <p className="text-sm font-medium">{notification.message}</p>
                      <p className="text-xs opacity-70 mt-1">{notification.time}</p>
                    </div>
                  ))}
                </div>
              </DialogContent>
            </Dialog>

            <Button className="gradient-button shadow-lg hover:shadow-xl transition-all duration-300">
              <Download className="w-4 h-4 mr-2" />
              Export Report
            </Button>
          </div>
        </div>

        {/* Stats Grid with Enhanced Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {stats.map((stat, index) => {
            const Icon = stat.icon;
            return (
              <Card 
                key={index} 
                className="modern-card interactive-hover cursor-pointer overflow-hidden animate-bounceIn"
                style={{ animationDelay: `${index * 100}ms` }}
                onClick={() => handleCardClick(stat.title)}
              >
                <div className="p-6 relative">
                  {/* Background Gradient */}
                  <div className={`absolute top-0 right-0 w-20 h-20 bg-gradient-to-br ${stat.color} opacity-10 rounded-full transform translate-x-6 -translate-y-6`} />
                  
                  <div className="flex items-center justify-between relative z-10">
                    <div className="space-y-2">
                      <p className="text-sm font-medium text-gray-600">{stat.title}</p>
                      <div className="flex items-baseline space-x-2">
                        <p className="text-3xl font-bold text-gray-900">{stat.value}</p>
                        <Badge className={`${getPriorityColor('low')} text-xs`}>
                          {stat.change}
                        </Badge>
                      </div>
                    </div>
                    <div className={`p-4 rounded-2xl ${stat.bgColor} shadow-lg`}>
                      <Icon className={`w-8 h-8 ${stat.textColor}`} />
                    </div>
                  </div>
                  
                  {/* Interactive Elements */}
                  <div className="mt-4 flex items-center text-xs text-gray-500">
                    <TrendingUp className="w-3 h-3 mr-1" />
                    <span>vs last month</span>
                  </div>
                </div>
              </Card>
            );
          })}
        </div>

        {/* Activity & Analytics Section */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Recent Activity with Enhanced UI */}
          <Card className="modern-card animate-slideInUp">
            <div className="p-6">
              <div className="flex items-center justify-between mb-6">
                <div className="flex items-center space-x-2">
                  <div className="p-2 bg-blue-100 rounded-lg">
                    <BarChart3 className="w-5 h-5 text-blue-600" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900">Recent Activity</h3>
                </div>
                <Button variant="ghost" size="sm">
                  <Eye className="w-4 h-4 mr-2" />
                  View All
                </Button>
              </div>
              
              <div className="space-y-4">
                {recentActivity.map((activity, index) => (
                  <div key={activity.id} className="flex items-start space-x-4 p-3 rounded-xl hover:bg-gray-50 transition-colors">
                    <div className="flex-shrink-0">
                      <div className={`w-2 h-2 rounded-full mt-2 animate-pulse ${
                        activity.priority === 'high' ? 'bg-red-500' : 
                        activity.priority === 'medium' ? 'bg-yellow-500' : 'bg-green-500'
                      }`} />
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between">
                        <p className="text-sm font-medium text-gray-900">
                          {activity.action}
                        </p>
                        <Badge className={`${getPriorityColor(activity.priority)} text-xs`}>
                          {activity.priority}
                        </Badge>
                      </div>
                      <p className="text-sm text-gray-600 mt-1">{activity.name}</p>
                      <p className="text-xs text-gray-500 mt-1">{activity.time}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </Card>

          {/* Quick Actions & Top Matches */}
          <Card className="modern-card animate-slideInUp" style={{ animationDelay: '200ms' }}>
            <div className="p-6">
              <div className="flex items-center space-x-2 mb-6">
                <div className="p-2 bg-purple-100 rounded-lg">
                  <Zap className="w-5 h-5 text-purple-600" />
                </div>
                <h3 className="text-xl font-semibold text-gray-900">Quick Actions</h3>
              </div>
              
              {/* Action Buttons */}
              <div className="grid grid-cols-2 gap-3 mb-6">
                <Button className="gradient-button h-16 flex-col">
                  <Target className="w-6 h-6 mb-1" />
                  <span className="text-sm">Run AI Match</span>
                </Button>
                <Button variant="outline" className="h-16 flex-col modern-card">
                  <Filter className="w-6 h-6 mb-1" />
                  <span className="text-sm">Filter Data</span>
                </Button>
              </div>

              {/* Top Matches Preview */}
              <div className="space-y-3">
                <h4 className="font-medium text-gray-900 flex items-center">
                  <AlertCircle className="w-4 h-4 mr-2 text-orange-500" />
                  Top Matches Today
                </h4>
                {candidates.slice(0, 3).map((candidate, index) => {
                  const bestMatch = internships.reduce((best, current) => {
                    const currentScore = calculateMatchScore(candidate, current);
                    const bestScore = calculateMatchScore(candidate, best);
                    return currentScore > bestScore ? current : best;
                  });
                  
                  const score = calculateMatchScore(candidate, bestMatch);
                  
                  return (
                    <div key={index} className="flex items-center justify-between p-3 bg-gradient-to-r from-gray-50 to-gray-100 rounded-xl hover:shadow-md transition-all cursor-pointer">
                      <div className="flex items-center space-x-3">
                        <div className="w-8 h-8 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white text-sm font-semibold">
                          {candidate.name.split(' ').map(n => n[0]).join('').substring(0, 2)}
                        </div>
                        <div>
                          <p className="font-medium text-gray-900 text-sm">{candidate.name}</p>
                          <p className="text-xs text-gray-600">{bestMatch.title}</p>
                        </div>
                      </div>
                      <div className="text-right">
                        <div className={`font-bold text-lg ${score >= 90 ? 'text-green-600' : score >= 80 ? 'text-blue-600' : 'text-orange-600'}`}>
                          {score}%
                        </div>
                        <p className="text-xs text-gray-500">match</p>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </Card>
        </div>
      </div>
    </TooltipProvider>
  );
};