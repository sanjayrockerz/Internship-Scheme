import { useState } from 'react';
import { Settings, BarChart3, Users, Target, RefreshCw, Zap, Brain, CheckCircle, XCircle, Clock, ArrowRight } from 'lucide-react';
import { Card } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Progress } from './ui/progress';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from './ui/tooltip';
import { mockCandidates, mockInternships } from '../data/mockData';
import { calculateMatchScore } from '../lib/utils';

interface AllocationResult {
  id: string;
  candidate: any;
  bestMatch: any;
  score: number;
  status: 'allocated' | 'waitlisted' | 'not-matched' | 'pending' | 'approved' | 'rejected';
  reasoning: string[];
}

export const SmartAllocation = () => {
  const [isRunning, setIsRunning] = useState(false);
  const [allocationProgress, setAllocationProgress] = useState(0);
  const [results, setResults] = useState<AllocationResult[]>([]);
  const [selectedFilter, setSelectedFilter] = useState('all');
  const [isDragMode, setIsDragMode] = useState(false);
  const [pendingApprovals, setPendingApprovals] = useState<AllocationResult[]>([]);

  const runAllocation = async () => {
    setIsRunning(true);
    setAllocationProgress(0);
    setResults([]);

    const totalSteps = mockCandidates.length;
    const newResults: AllocationResult[] = [];

    for (let i = 0; i < totalSteps; i++) {
      await new Promise(resolve => setTimeout(resolve, 150));
      
      const candidate = mockCandidates[i];
      const scores = mockInternships.map(internship => ({
        internship,
        score: calculateMatchScore(candidate, internship)
      })).sort((a, b) => b.score - a.score);

      const bestMatch = scores[0];
      const status = bestMatch.score >= 70 ? 'pending' : 
                   bestMatch.score >= 50 ? 'waitlisted' : 'not-matched';
      
      const reasoning = generateReasoning(candidate, bestMatch.internship, bestMatch.score);
      
      const result: AllocationResult = {
        id: `allocation-${i}`,
        candidate,
        bestMatch: bestMatch.internship,
        score: bestMatch.score,
        status,
        reasoning
      };

      newResults.push(result);
      setAllocationProgress(((i + 1) / totalSteps) * 100);
      setResults([...newResults]);
    }

    const pending = newResults.filter(r => r.status === 'pending');
    setPendingApprovals(pending);
    setIsRunning(false);
  };

  const generateReasoning = (candidate: any, internship: any, score: number): string[] => {
    const reasons = [];
    
    if (score >= 90) {
      reasons.push("🎯 Perfect skills alignment");
      reasons.push("📍 Ideal location match");
    } else if (score >= 70) {
      reasons.push("✨ Strong skills compatibility");
      reasons.push("🏢 Good organizational fit");
    } else {
      reasons.push("⚠️ Limited skills overlap");
      reasons.push("📚 Requires additional training");
    }
    
    reasons.push(`💼 ${internship.sector} sector experience`);
    reasons.push(`🎓 ${candidate.education.degree} background`);
    
    return reasons;
  };

  const handleApproval = (resultId: string, approved: boolean) => {
    setResults(prev => prev.map(result => 
      result.id === resultId 
        ? { ...result, status: approved ? 'approved' : 'rejected' }
        : result
    ));
    setPendingApprovals(prev => prev.filter(p => p.id !== resultId));
  };



  const filteredResults = results.filter(result => {
    if (selectedFilter === 'all') return true;
    return result.status === selectedFilter;
  });

  const allocationStats = {
    total: results.length,
    allocated: results.filter(r => r.status === 'approved').length,
    pending: results.filter(r => r.status === 'pending').length,
    waitlisted: results.filter(r => r.status === 'waitlisted').length,
    rejected: results.filter(r => r.status === 'rejected').length,
    notMatched: results.filter(r => r.status === 'not-matched').length,
    averageScore: results.length > 0 ? Math.round(results.reduce((sum, r) => sum + r.score, 0) / results.length) : 0
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'approved': return 'bg-green-100 text-green-800 border-green-200';
      case 'pending': return 'bg-blue-100 text-blue-800 border-blue-200';
      case 'waitlisted': return 'bg-yellow-100 text-yellow-800 border-yellow-200';
      case 'rejected': return 'bg-red-100 text-red-800 border-red-200';
      case 'not-matched': return 'bg-gray-100 text-gray-800 border-gray-200';
      default: return 'bg-gray-100 text-gray-800 border-gray-200';
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'approved': return <CheckCircle className="w-4 h-4" />;
      case 'pending': return <Clock className="w-4 h-4" />;
      case 'waitlisted': return <Clock className="w-4 h-4" />;
      case 'rejected': return <XCircle className="w-4 h-4" />;
      default: return <Target className="w-4 h-4" />;
    }
  };

  return (
    <TooltipProvider>
      <div className="space-y-8 animate-fadeIn">
        {/* Header with Enhanced Controls */}
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
          <div className="animate-slideInUp">
            <div className="flex items-center space-x-3 mb-2">
              <div className="p-3 bg-gradient-to-r from-purple-500 to-blue-600 rounded-2xl shadow-lg">
                <Brain className="w-8 h-8 text-white" />
              </div>
              <div>
                <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
                  Smart Allocation Engine
                </h1>
                <p className="text-gray-600 text-lg">AI-powered matching system for optimal candidate-internship allocation</p>
              </div>
            </div>
          </div>
          
          <div className="flex items-center gap-3 animate-slideInRight">
            <Tooltip>
              <TooltipTrigger asChild>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => setIsDragMode(!isDragMode)}
                  className={`modern-card transition-all duration-300 ${isDragMode ? 'bg-blue-50 border-blue-300' : ''}`}
                >
                  <Target className="w-4 h-4 mr-2" />
                  {isDragMode ? 'Exit Drag Mode' : 'Manual Mode'}
                </Button>
              </TooltipTrigger>
              <TooltipContent>
                <p>Toggle manual drag-and-drop allocation</p>
              </TooltipContent>
            </Tooltip>

            <Button variant="outline" size="sm" className="modern-card hover:shadow-lg">
              <Settings className="w-4 h-4 mr-2" />
              Configure AI
            </Button>

            <Button 
              onClick={runAllocation} 
              disabled={isRunning}
              className="gradient-button shadow-lg hover:shadow-xl transition-all duration-300 px-6"
            >
              {isRunning ? (
                <>
                  <RefreshCw className="w-5 h-5 mr-2 animate-spin" />
                  Processing...
                </>
              ) : (
                <>
                  <Zap className="w-5 h-5 mr-2" />
                  Run AI Allocation
                </>
              )}
            </Button>
          </div>
        </div>

        {/* Algorithm Overview Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          {[
            { title: 'Skills Analysis', icon: Target, color: 'from-blue-500 to-blue-600', weight: '40%', desc: 'NLP-based skill compatibility' },
            { title: 'Location Match', icon: Users, color: 'from-green-500 to-green-600', weight: '20%', desc: 'Geographic preferences' },
            { title: 'Experience Level', icon: BarChart3, color: 'from-purple-500 to-purple-600', weight: '20%', desc: 'Background alignment' },
            { title: 'Availability', icon: Settings, color: 'from-orange-500 to-orange-600', weight: '20%', desc: 'Duration compatibility' }
          ].map((item, index) => {
            const Icon = item.icon;
            return (
              <Card key={index} className="modern-card interactive-hover animate-bounceIn" style={{ animationDelay: `${index * 100}ms` }}>
                <div className="p-6 text-center">
                  <div className={`w-16 h-16 bg-gradient-to-br ${item.color} rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg`}>
                    <Icon className="w-8 h-8 text-white" />
                  </div>
                  <h3 className="text-lg font-semibold text-gray-900 mb-2">{item.title}</h3>
                  <Badge className="bg-gray-100 text-gray-800 mb-2">{item.weight} weight</Badge>
                  <p className="text-sm text-gray-600">{item.desc}</p>
                </div>
              </Card>
            );
          })}
        </div>

        {/* Progress and Stats */}
        {isRunning && (
          <Card className="modern-card animate-slideInUp">
            <div className="p-6">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center space-x-3">
                  <div className="p-2 bg-blue-100 rounded-lg">
                    <Brain className="w-6 h-6 text-blue-600 animate-pulse" />
                  </div>
                  <div>
                    <h3 className="text-xl font-semibold text-gray-900">AI Processing</h3>
                    <p className="text-gray-600">Analyzing {mockCandidates.length} candidates...</p>
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-3xl font-bold text-blue-600">{Math.round(allocationProgress)}%</div>
                  <div className="text-sm text-gray-500">Complete</div>
                </div>
              </div>
              <Progress value={allocationProgress} className="w-full h-3 mb-4" />
              <div className="grid grid-cols-3 gap-4 text-center">
                <div>
                  <div className="text-lg font-semibold text-green-600">{results.filter(r => r.status === 'pending').length}</div>
                  <div className="text-xs text-gray-500">Matches Found</div>
                </div>
                <div>
                  <div className="text-lg font-semibold text-yellow-600">{results.filter(r => r.status === 'waitlisted').length}</div>
                  <div className="text-xs text-gray-500">Waitlisted</div>
                </div>
                <div>
                  <div className="text-lg font-semibold text-gray-600">{results.filter(r => r.status === 'not-matched').length}</div>
                  <div className="text-xs text-gray-500">No Match</div>
                </div>
              </div>
            </div>
          </Card>
        )}

        {/* Results Summary */}
        {results.length > 0 && (
          <Card className="modern-card animate-slideInUp">
            <div className="p-6">
              <div className="flex items-center justify-between mb-6">
                <h3 className="text-2xl font-semibold text-gray-900">Allocation Results</h3>
                <div className="flex space-x-2">
                  {['all', 'pending', 'approved', 'waitlisted', 'rejected'].map((filter) => (
                    <Button
                      key={filter}
                      variant={selectedFilter === filter ? "default" : "outline"}
                      size="sm"
                      onClick={() => setSelectedFilter(filter)}
                      className="capitalize"
                    >
                      {filter} ({filter === 'all' ? results.length : results.filter(r => r.status === filter).length})
                    </Button>
                  ))}
                </div>
              </div>
              
              <div className="grid grid-cols-2 md:grid-cols-6 gap-4 mb-6">
                <div className="text-center p-4 bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl">
                  <div className="text-2xl font-bold text-blue-600">{allocationStats.total}</div>
                  <div className="text-sm text-gray-600">Total Processed</div>
                </div>
                <div className="text-center p-4 bg-gradient-to-br from-green-50 to-green-100 rounded-xl">
                  <div className="text-2xl font-bold text-green-600">{allocationStats.allocated}</div>
                  <div className="text-sm text-gray-600">Approved</div>
                </div>
                <div className="text-center p-4 bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl">
                  <div className="text-2xl font-bold text-blue-600">{allocationStats.pending}</div>
                  <div className="text-sm text-gray-600">Pending</div>
                </div>
                <div className="text-center p-4 bg-gradient-to-br from-yellow-50 to-yellow-100 rounded-xl">
                  <div className="text-2xl font-bold text-yellow-600">{allocationStats.waitlisted}</div>
                  <div className="text-sm text-gray-600">Waitlisted</div>
                </div>
                <div className="text-center p-4 bg-gradient-to-br from-red-50 to-red-100 rounded-xl">
                  <div className="text-2xl font-bold text-red-600">{allocationStats.rejected}</div>
                  <div className="text-sm text-gray-600">Rejected</div>
                </div>
                <div className="text-center p-4 bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl">
                  <div className="text-2xl font-bold text-purple-600">{allocationStats.averageScore}%</div>
                  <div className="text-sm text-gray-600">Avg Score</div>
                </div>
              </div>
            </div>
          </Card>
        )}

        {/* Allocation Results Grid */}
        {filteredResults.length > 0 && (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {filteredResults.slice(0, 8).map((result, index) => (
              <Card key={result.id} className="modern-card interactive-hover animate-slideInUp" style={{ animationDelay: `${index * 50}ms` }}>
                <div className="p-6">
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex items-center space-x-4">
                      <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-semibold shadow-lg">
                        {result.candidate.name.split(' ').map((n: string) => n[0]).join('').substring(0, 2)}
                      </div>
                      <div>
                        <h4 className="font-semibold text-gray-900">{result.candidate.name}</h4>
                        <p className="text-sm text-gray-600">{result.candidate.education.degree}</p>
                      </div>
                    </div>
                    <div className="text-right">
                      <div className={`text-2xl font-bold ${result.score >= 90 ? 'text-green-600' : result.score >= 70 ? 'text-blue-600' : 'text-orange-600'}`}>
                        {result.score}%
                      </div>
                      <div className="text-xs text-gray-500">Match Score</div>
                    </div>
                  </div>

                  <div className="flex items-center space-x-2 mb-4">
                    <ArrowRight className="w-4 h-4 text-gray-400" />
                    <div className="flex-1">
                      <p className="font-medium text-gray-900">{result.bestMatch.title}</p>
                      <p className="text-sm text-gray-600">{result.bestMatch.companyName}</p>
                    </div>
                  </div>

                  <div className="space-y-2 mb-4">
                    {result.reasoning.slice(0, 2).map((reason, idx) => (
                      <div key={idx} className="text-xs text-gray-600 bg-gray-50 px-2 py-1 rounded-lg">
                        {reason}
                      </div>
                    ))}
                  </div>

                  <div className="flex items-center justify-between">
                    <Badge className={`${getStatusColor(result.status)} flex items-center space-x-1`}>
                      {getStatusIcon(result.status)}
                      <span className="capitalize">{result.status}</span>
                    </Badge>

                    {result.status === 'pending' && (
                      <div className="flex space-x-2">
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Button
                              size="sm"
                              variant="outline"
                              onClick={() => handleApproval(result.id, false)}
                              className="text-red-600 hover:bg-red-50"
                            >
                              <XCircle className="w-4 h-4" />
                            </Button>
                          </TooltipTrigger>
                          <TooltipContent>
                            <p>Reject allocation</p>
                          </TooltipContent>
                        </Tooltip>
                        
                        <Tooltip>
                          <TooltipTrigger asChild>
                            <Button
                              size="sm"
                              onClick={() => handleApproval(result.id, true)}
                              className="gradient-button"
                            >
                              <CheckCircle className="w-4 h-4" />
                            </Button>
                          </TooltipTrigger>
                          <TooltipContent>
                            <p>Approve allocation</p>
                          </TooltipContent>
                        </Tooltip>
                      </div>
                    )}
                  </div>
                </div>
              </Card>
            ))}
          </div>
        )}

        {/* Getting Started State */}
        {results.length === 0 && !isRunning && (
          <Card className="modern-card text-center animate-bounceIn">
            <div className="p-12">
              <div className="w-24 h-24 bg-gradient-to-br from-purple-500 to-blue-600 rounded-full flex items-center justify-center mx-auto mb-6 shadow-2xl">
                <Brain className="w-12 h-12 text-white" />
              </div>
              <h3 className="text-2xl font-semibold text-gray-900 mb-4">Ready to Run Smart Allocation</h3>
              <p className="text-gray-600 mb-8 max-w-2xl mx-auto text-lg">
                Our advanced AI system will analyze <span className="font-semibold text-blue-600">{mockCandidates.length} candidates</span> against <span className="font-semibold text-purple-600">{mockInternships.length} internship positions</span> using machine learning algorithms to find optimal matches based on skills, location, experience, and availability.
              </p>
              
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div className="text-center">
                  <div className="w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mx-auto mb-3">
                    <Target className="w-8 h-8 text-blue-600" />
                  </div>
                  <h4 className="font-semibold text-gray-900 mb-2">Intelligent Matching</h4>
                  <p className="text-sm text-gray-600">AI-powered analysis of candidate profiles and position requirements</p>
                </div>
                <div className="text-center">
                  <div className="w-16 h-16 bg-green-100 rounded-2xl flex items-center justify-center mx-auto mb-3">
                    <Users className="w-8 h-8 text-green-600" />
                  </div>
                  <h4 className="font-semibold text-gray-900 mb-2">Bulk Processing</h4>
                  <p className="text-sm text-gray-600">Process hundreds of candidates simultaneously with real-time progress</p>
                </div>
                <div className="text-center">
                  <div className="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mx-auto mb-3">
                    <BarChart3 className="w-8 h-8 text-purple-600" />
                  </div>
                  <h4 className="font-semibold text-gray-900 mb-2">Smart Analytics</h4>
                  <p className="text-sm text-gray-600">Detailed scoring and reasoning for every allocation decision</p>
                </div>
              </div>
              
              <Button onClick={runAllocation} size="lg" className="gradient-button text-lg px-8 py-3 shadow-xl hover:shadow-2xl transition-all duration-300">
                <Zap className="w-6 h-6 mr-3" />
                Start AI Allocation Process
              </Button>
            </div>
          </Card>
        )}

        {/* Pending Approvals Summary */}
        {pendingApprovals.length > 0 && (
          <Card className="modern-card border-blue-200 bg-blue-50">
            <div className="p-6">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  <Clock className="w-6 h-6 text-blue-600" />
                  <div>
                    <h3 className="text-lg font-semibold text-blue-900">Pending Approvals</h3>
                    <p className="text-blue-700">{pendingApprovals.length} allocations require your review</p>
                  </div>
                </div>
                <Button className="gradient-button">
                  Review All ({pendingApprovals.length})
                </Button>
              </div>
            </div>
          </Card>
        )}
      </div>
    </TooltipProvider>
  );
};