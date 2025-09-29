import { useState } from 'react';
import { Search, Filter, Plus, MapPin, Calendar, Users, Clock, Building } from 'lucide-react';
import { Card } from './ui/card';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Badge } from './ui/badge';
import { mockInternships } from '../data/mockData';
import { formatDate } from '../lib/utils';

export const Internships = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedFilter, setSelectedFilter] = useState('all');

  const filteredInternships = mockInternships.filter(internship => {
    const matchesSearch = internship.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         internship.companyName.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         internship.requiredSkills.some(skill => skill.toLowerCase().includes(searchTerm.toLowerCase()));
    
    if (selectedFilter === 'all') return matchesSearch;
    if (selectedFilter === 'active') return matchesSearch && new Date(internship.applicationDeadline) > new Date();
    if (selectedFilter === 'expired') return matchesSearch && new Date(internship.applicationDeadline) <= new Date();
    return matchesSearch;
  });

  const filters = [
    { id: 'all', label: 'All Positions', count: mockInternships.length },
    { id: 'active', label: 'Active', count: mockInternships.filter(i => new Date(i.applicationDeadline) > new Date()).length },
    { id: 'expired', label: 'Expired', count: mockInternships.filter(i => new Date(i.applicationDeadline) <= new Date()).length }
  ];

  const getSectorColor = (sector: string) => {
    const colors = {
      'Technology': 'bg-blue-100 text-blue-800',
      'Healthcare': 'bg-green-100 text-green-800',
      'Finance': 'bg-purple-100 text-purple-800',
      'Manufacturing': 'bg-orange-100 text-orange-800',
      'Education': 'bg-yellow-100 text-yellow-800',
      'Government': 'bg-gray-100 text-gray-800'
    };
    return colors[sector as keyof typeof colors] || 'bg-gray-100 text-gray-800';
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Internship Positions</h1>
          <p className="text-gray-600 mt-2">Manage available internship opportunities</p>
        </div>
        <Button className="flex items-center space-x-2">
          <Plus className="w-4 h-4" />
          <span>Add Position</span>
        </Button>
      </div>

      {/* Search and Filters */}
      <div className="flex flex-col sm:flex-row gap-4">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          <Input
            type="text"
            placeholder="Search internships by title, organization, or skills..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="pl-10"
          />
        </div>
        <div className="flex space-x-2">
          {filters.map((filter) => (
            <Button
              key={filter.id}
              variant={selectedFilter === filter.id ? "default" : "outline"}
              onClick={() => setSelectedFilter(filter.id)}
              className="flex items-center space-x-2"
            >
              <Filter className="w-4 h-4" />
              <span>{filter.label}</span>
              <Badge variant="secondary">{filter.count}</Badge>
            </Button>
          ))}
        </div>
      </div>

      {/* Internships Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {filteredInternships.map((internship) => {
          const isExpired = new Date(internship.applicationDeadline) <= new Date();
          
          return (
            <Card key={internship.id} className="p-6 hover:shadow-md transition-shadow">
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-start space-x-3">
                  <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                    <Building className="w-6 h-6 text-blue-600" />
                  </div>
                  <div className="flex-1">
                    <h3 className="font-semibold text-gray-900 text-lg">{internship.title}</h3>
                    <p className="text-gray-600">{internship.companyName}</p>
                    <div className="flex items-center space-x-2 mt-1">
                      <Badge className={getSectorColor(internship.sector)}>
                        {internship.sector}
                      </Badge>
                      <Badge variant={isExpired ? 'destructive' : 'default'}>
                        {isExpired ? 'Expired' : 'Active'}
                      </Badge>
                    </div>
                  </div>
                </div>
              </div>

              {/* Key Details */}
              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="flex items-center space-x-2 text-sm text-gray-600">
                  <MapPin className="w-4 h-4" />
                  <span>{internship.location.district}, {internship.location.state}</span>
                </div>
                <div className="flex items-center space-x-2 text-sm text-gray-600">
                  <Clock className="w-4 h-4" />
                  <span>{internship.duration} months</span>
                </div>
                <div className="flex items-center space-x-2 text-sm text-gray-600">
                  <Calendar className="w-4 h-4" />
                  <span>Apply by {formatDate(internship.applicationDeadline)}</span>
                </div>
                <div className="flex items-center space-x-2 text-sm text-gray-600">
                  <Users className="w-4 h-4" />
                  <span>{internship.capacity} positions</span>
                </div>
              </div>

              {/* Description */}
              <div className="mb-4">
                <p className="text-sm text-gray-700 line-clamp-3">
                  {internship.description}
                </p>
              </div>

              {/* Required Skills */}
              <div className="mb-4">
                <p className="text-sm font-medium text-gray-700 mb-2">Required Skills</p>
                <div className="flex flex-wrap gap-2">
                  {internship.requiredSkills.slice(0, 4).map((skill, index) => (
                    <Badge key={index} variant="outline" className="text-xs">
                      {skill}
                    </Badge>
                  ))}
                  {internship.requiredSkills.length > 4 && (
                    <Badge variant="outline" className="text-xs">
                      +{internship.requiredSkills.length - 4} more
                    </Badge>
                  )}
                </div>
              </div>

              {/* Stipend */}
              <div className="mb-4">
                <div className="flex items-center justify-between">
                  <span className="text-sm font-medium text-gray-700">Stipend</span>
                  <span className="text-lg font-semibold text-green-600">
                    ₹{internship.stipend.toLocaleString('en-IN')}/month
                  </span>
                </div>
              </div>

              {/* Actions */}
              <div className="flex space-x-2">
                <Button size="sm" className="flex-1" disabled={isExpired}>
                  View Details
                </Button>
                <Button size="sm" variant="outline" className="flex-1">
                  Edit Position
                </Button>
              </div>
            </Card>
          );
        })}
      </div>

      {filteredInternships.length === 0 && (
        <div className="text-center py-12">
          <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <Search className="w-8 h-8 text-gray-400" />
          </div>
          <h3 className="text-lg font-medium text-gray-900 mb-2">No internships found</h3>
          <p className="text-gray-600">Try adjusting your search criteria or filters.</p>
        </div>
      )}
    </div>
  );
};