import { useState } from 'react';
import { Play, Settings, BarChart3, Users, Target, RefreshCw } from 'lucide-react';
import { Card } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Progress } from './ui/progress';
import { mockCandidates, mockInternships } from '../data/mockData';
import { calculateMatchScore } from '../lib/utils';

export const SmartAllocation = () => {
  const [isRunning, setIsRunning] = useState(false);
  const [allocationProgress, setAllocationProgress] = useState(0);
  const [results, setResults] = useState<any[]>([]);

  const runAllocation = async () => {
    setIsRunning(true);
    setAllocationProgress(0);
    setResults([]);

    // Simulate allocation process
    const totalSteps = mockCandidates.length;
    const newResults: any[] = [];

    for (let i = 0; i < totalSteps; i++) {
      await new Promise(resolve => setTimeout(resolve, 100)); // Simulate processing
      
      const candidate = mockCandidates[i];
      const scores = mockInternships.map(internship => ({
        internship,
        score: calculateMatchScore(candidate, internship)
      })).sort((a, b) => b.score - a.score);

      const bestMatch = scores[0];
      
      newResults.push({
        candidate,
        bestMatch: bestMatch.internship,
        score: bestMatch.score,
        status: bestMatch.score >= 70 ? 'allocated' : bestMatch.score >= 50 ? 'waitlisted' : 'not-matched'
      });

      setAllocationProgress(((i + 1) / totalSteps) * 100);
      setResults([...newResults]);
    }

    setIsRunning(false);
  };

  const allocationStats = {
    total: results.length,
    allocated: results.filter(r => r.status === 'allocated').length,
    waitlisted: results.filter(r => r.status === 'waitlisted').length,
    notMatched: results.filter(r => r.status === 'not-matched').length,
    averageScore: results.length > 0 ? Math.round(results.reduce((sum, r) => sum + r.score, 0) / results.length) : 0
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'allocated': return 'bg-green-100 text-green-800';
      case 'waitlisted': return 'bg-yellow-100 text-yellow-800';
      case 'not-matched': return 'bg-red-100 text-red-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const getStatusLabel = (status: string) => {
    switch (status) {
      case 'allocated': return 'Allocated';
      case 'waitlisted': return 'Waitlisted';
      case 'not-matched': return 'Not Matched';
      default: return 'Unknown';
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Smart Allocation Engine</h1>
          <p className="text-gray-600 mt-2">AI-powered matching system for optimal candidate-internship allocation</p>
        </div>
        <div className="flex space-x-3">
          <Button variant="outline" className="flex items-center space-x-2">
            <Settings className="w-4 h-4" />
            <span>Configure</span>
          </Button>
          <Button 
            onClick={runAllocation} 
            disabled={isRunning}
            className="flex items-center space-x-2"
          >
            {isRunning ? (
              <RefreshCw className="w-4 h-4 animate-spin" />
            ) : (
              <Play className="w-4 h-4" />
            )}
            <span>{isRunning ? 'Running...' : 'Run Allocation'}</span>
          </Button>
        </div>
      </div>

      {/* Algorithm Overview */}
      <Card className="p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Allocation Algorithm</h3>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="text-center p-4 bg-blue-50 rounded-lg">
            <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-2">
              <Target className="w-6 h-6 text-blue-600" />
            </div>
            <h4 className="font-medium text-blue-900">Skills Match</h4>
            <p className="text-sm text-blue-700 mt-1">40% weight</p>
          </div>
          <div className="text-center p-4 bg-green-50 rounded-lg">
            <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-2">
              <Users className="w-6 h-6 text-green-600" />
            </div>
            <h4 className="font-medium text-green-900">Location Match</h4>
            <p className="text-sm text-green-700 mt-1">20% weight</p>
          </div>
          <div className="text-center p-4 bg-purple-50 rounded-lg">
            <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-2">
              <BarChart3 className="w-6 h-6 text-purple-600" />
            </div>
            <h4 className="font-medium text-purple-900">Experience Level</h4>
            <p className="text-sm text-purple-700 mt-1">20% weight</p>
          </div>
          <div className="text-center p-4 bg-orange-50 rounded-lg">
            <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-2">
              <Settings className="w-6 h-6 text-orange-600" />
            </div>
            <h4 className="font-medium text-orange-900">Availability</h4>
            <p className="text-sm text-orange-700 mt-1">20% weight</p>
          </div>
        </div>
      </Card>

      {/* Progress */}
      {isRunning && (
        <Card className="p-6">
          <div className="flex items-center justify-between mb-2">
            <h3 className="text-lg font-semibold text-gray-900">Allocation Progress</h3>
            <span className="text-sm text-gray-600">{Math.round(allocationProgress)}%</span>
          </div>
          <Progress value={allocationProgress} className="w-full" />
          <p className="text-sm text-gray-600 mt-2">
            Processing {results.length} of {mockCandidates.length} candidates...
          </p>
        </Card>
      )}

      {/* Results Summary */}
      {results.length > 0 && (
        <Card className="p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Allocation Summary</h3>
          <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-6">
            <div className="text-center">
              <div className="text-2xl font-bold text-gray-900">{allocationStats.total}</div>
              <div className="text-sm text-gray-600">Total Processed</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-green-600">{allocationStats.allocated}</div>
              <div className="text-sm text-gray-600">Allocated</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-yellow-600">{allocationStats.waitlisted}</div>
              <div className="text-sm text-gray-600">Waitlisted</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-red-600">{allocationStats.notMatched}</div>
              <div className="text-sm text-gray-600">Not Matched</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-blue-600">{allocationStats.averageScore}%</div>
              <div className="text-sm text-gray-600">Avg Score</div>
            </div>
          </div>
        </Card>
      )}

      {/* Results Table */}
      {results.length > 0 && (
        <Card className="p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Allocation Results</h3>
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Candidate
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Best Match
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Match Score
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Status
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {results.slice(0, 10).map((result, index) => (
                  <tr key={index} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="flex items-center">
                        <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-3">
                          <span className="text-blue-600 font-medium text-sm">
                            {result.candidate.name.split(' ').map((n: string) => n[0]).join('').substring(0, 2)}
                          </span>
                        </div>
                        <div>
                          <div className="text-sm font-medium text-gray-900">{result.candidate.name}</div>
                          <div className="text-sm text-gray-500">{result.candidate.location.district}</div>
                        </div>
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="text-sm text-gray-900">{result.bestMatch.title}</div>
                      <div className="text-sm text-gray-500">{result.bestMatch.companyName}</div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="flex items-center">
                        <div className="text-sm font-medium text-gray-900 mr-2">{result.score}%</div>
                        <div className="w-16 bg-gray-200 rounded-full h-2">
                          <div 
                            className="bg-blue-600 h-2 rounded-full" 
                            style={{ width: `${result.score}%` }}
                          ></div>
                        </div>
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <Badge className={getStatusColor(result.status)}>
                        {getStatusLabel(result.status)}
                      </Badge>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          {results.length > 10 && (
            <div className="mt-4 text-center">
              <Button variant="outline">
                View All {results.length} Results
              </Button>
            </div>
          )}
        </Card>
      )}

      {/* Getting Started */}
      {results.length === 0 && !isRunning && (
        <Card className="p-12 text-center">
          <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <Target className="w-8 h-8 text-blue-600" />
          </div>
          <h3 className="text-lg font-medium text-gray-900 mb-2">Ready to Run Smart Allocation</h3>
          <p className="text-gray-600 mb-6 max-w-md mx-auto">
            Our AI-powered matching system will analyze {mockCandidates.length} candidates against {mockInternships.length} internship positions to find optimal matches.
          </p>
          <Button onClick={runAllocation} size="lg" className="flex items-center space-x-2">
            <Play className="w-5 h-5" />
            <span>Start Allocation Process</span>
          </Button>
        </Card>
      )}
    </div>
  );
};