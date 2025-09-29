import { useState } from 'react';
import { Users, Building, Target, TrendingUp, Bell, RefreshCw, Eye, Download, Filter, Zap, AlertCircle } from 'lucide-react';
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
import { Card } from './ui/card';
import { mockCandidates as candidates, mockInternships as internships } from '../data/mockData';
import { calculateMatchScore } from '../lib/utils';

export const Dashboard = () => {
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

  const stats = [
    {
      title: 'Total Candidates',
      value: candidates.length,
      icon: Users,
      color: 'text-blue-600',
      bg: 'bg-blue-50'
    },
    {
      title: 'Available Positions',
      value: internships.length,
      icon: Building,
      color: 'text-green-600',
      bg: 'bg-green-50'
    },
    {
      title: 'High Matches (70%+)',
      value: totalMatches,
      icon: Target,
      color: 'text-purple-600',
      bg: 'bg-purple-50'
    },
    {
      title: 'Avg Match Score',
      value: `${avgMatchScore}%`,
      icon: TrendingUp,
      color: 'text-orange-600',
      bg: 'bg-orange-50'
    }
  ];

  const recentActivity = [
    { action: 'New candidate registered', name: 'Priya Sharma', time: '2 hours ago' },
    { action: 'Internship position added', name: 'Data Science Intern', time: '4 hours ago' },
    { action: 'Match found (95%)', name: 'Rahul Kumar → Tech Lead', time: '6 hours ago' },
    { action: 'Application submitted', name: 'Anita Patel', time: '1 day ago' }
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-600 mt-2">PM Internship Allocation System Overview</p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, index) => {
          const Icon = stat.icon;
          return (
            <Card key={index} className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600">{stat.title}</p>
                  <p className="text-2xl font-bold text-gray-900 mt-2">{stat.value}</p>
                </div>
                <div className={`p-3 rounded-full ${stat.bg}`}>
                  <Icon className={`w-6 h-6 ${stat.color}`} />
                </div>
              </div>
            </Card>
          );
        })}
      </div>

      {/* Recent Activity */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card className="p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Recent Activity</h3>
          <div className="space-y-4">
            {recentActivity.map((activity, index) => (
              <div key={index} className="flex items-start space-x-3">
                <div className="w-2 h-2 bg-blue-500 rounded-full mt-2"></div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm text-gray-900">
                    <span className="font-medium">{activity.action}:</span> {activity.name}
                  </p>
                  <p className="text-xs text-gray-500">{activity.time}</p>
                </div>
              </div>
            ))}
          </div>
        </Card>

        <Card className="p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Top Matches Today</h3>
          <div className="space-y-3">
            {candidates.slice(0, 4).map((candidate, index) => {
              const bestMatch = internships.reduce((best, current) => {
                const currentScore = calculateMatchScore(candidate, current);
                const bestScore = calculateMatchScore(candidate, best);
                return currentScore > bestScore ? current : best;
              });
              
              const score = calculateMatchScore(candidate, bestMatch);
              
              return (
                <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <div>
                    <p className="font-medium text-gray-900">{candidate.name}</p>
                    <p className="text-sm text-gray-600">{bestMatch.title}</p>
                  </div>
                  <div className="text-right">
                    <p className="font-semibold text-green-600">{score}%</p>
                    <p className="text-xs text-gray-500">match</p>
                  </div>
                </div>
              );
            })}
          </div>
        </Card>
      </div>
    </div>
  );
};