import React, { useState, useEffect } from 'react';
import { Bell, X, CheckCircle, AlertTriangle, Info, Clock, ArrowRight, Settings, Filter, Search } from 'lucide-react';
import { Card } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Input } from './ui/input';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from './ui/tooltip';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from './ui/dialog';

interface Notification {
  id: string;
  type: 'success' | 'warning' | 'info' | 'alert';
  title: string;
  message: string;
  timestamp: Date;
  isRead: boolean;
  priority: 'high' | 'medium' | 'low';
  category: 'allocation' | 'system' | 'application' | 'deadline' | 'approval';
  actionable?: boolean;
  actionText?: string;
  actionUrl?: string;
  relatedData?: any;
}

export const NotificationSystem = () => {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [filter, setFilter] = useState<string>('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [showSettings, setShowSettings] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);

  useEffect(() => {
    // Generate mock notifications
    const mockNotifications: Notification[] = [
      {
        id: '1',
        type: 'success',
        title: 'Allocation Completed',
        message: '25 candidates successfully allocated to internship positions',
        timestamp: new Date(Date.now() - 5 * 60 * 1000),
        isRead: false,
        priority: 'high',
        category: 'allocation',
        actionable: true,
        actionText: 'View Results',
        actionUrl: '/allocations'
      },
      {
        id: '2',
        type: 'warning',
        title: 'Pending Approvals',
        message: '12 allocations require supervisor approval',
        timestamp: new Date(Date.now() - 15 * 60 * 1000),
        isRead: false,
        priority: 'high',
        category: 'approval',
        actionable: true,
        actionText: 'Review',
        actionUrl: '/approvals'
      },
      {
        id: '3',
        type: 'info',
        title: 'New Applications',
        message: '8 new internship applications received',
        timestamp: new Date(Date.now() - 30 * 60 * 1000),
        isRead: true,
        priority: 'medium',
        category: 'application',
        actionable: true,
        actionText: 'View Applications',
        actionUrl: '/applications'
      },
      {
        id: '4',
        type: 'alert',
        title: 'System Update Required',
        message: 'Maintenance window scheduled for tonight 11 PM - 2 AM',
        timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000),
        isRead: false,
        priority: 'medium',
        category: 'system',
        actionable: false
      },
      {
        id: '5',
        type: 'warning',
        title: 'Application Deadline',
        message: 'Summer internship applications close in 3 days',
        timestamp: new Date(Date.now() - 4 * 60 * 60 * 1000),
        isRead: true,
        priority: 'high',
        category: 'deadline',
        actionable: true,
        actionText: 'View Details',
        actionUrl: '/deadlines'
      },
      {
        id: '6',
        type: 'success',
        title: 'Performance Report',
        message: 'Monthly allocation report generated successfully',
        timestamp: new Date(Date.now() - 6 * 60 * 60 * 1000),
        isRead: true,
        priority: 'low',
        category: 'system',
        actionable: true,
        actionText: 'Download',
        actionUrl: '/reports'
      }
    ];

    setNotifications(mockNotifications);

    // Simulate real-time notifications
    const interval = setInterval(() => {
      const newNotification: Notification = {
        id: Date.now().toString(),
        type: ['success', 'warning', 'info', 'alert'][Math.floor(Math.random() * 4)] as any,
        title: 'Real-time Update',
        message: `New activity detected at ${new Date().toLocaleTimeString()}`,
        timestamp: new Date(),
        isRead: false,
        priority: 'medium',
        category: 'system',
        actionable: false
      };

      setNotifications(prev => [newNotification, ...prev.slice(0, 9)]); // Keep only 10 notifications
    }, 30000); // New notification every 30 seconds

    return () => clearInterval(interval);
  }, []);

  const getNotificationIcon = (type: string) => {
    switch (type) {
      case 'success': return <CheckCircle className="w-5 h-5 text-green-600" />;
      case 'warning': return <AlertTriangle className="w-5 h-5 text-yellow-600" />;
      case 'alert': return <AlertTriangle className="w-5 h-5 text-red-600" />;
      case 'info': return <Info className="w-5 h-5 text-blue-600" />;
      default: return <Bell className="w-5 h-5 text-gray-600" />;
    }
  };

  const getNotificationColor = (type: string) => {
    switch (type) {
      case 'success': return 'border-green-200 bg-green-50';
      case 'warning': return 'border-yellow-200 bg-yellow-50';
      case 'alert': return 'border-red-200 bg-red-50';
      case 'info': return 'border-blue-200 bg-blue-50';
      default: return 'border-gray-200 bg-gray-50';
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

  const formatTimestamp = (timestamp: Date) => {
    const now = new Date();
    const diffMs = now.getTime() - timestamp.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMins / 60);
    const diffDays = Math.floor(diffHours / 24);

    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins}m ago`;
    if (diffHours < 24) return `${diffHours}h ago`;
    return `${diffDays}d ago`;
  };

  const markAsRead = (id: string) => {
    setNotifications(prev =>
      prev.map(notification =>
        notification.id === id ? { ...notification, isRead: true } : notification
      )
    );
  };

  const deleteNotification = (id: string) => {
    setNotifications(prev => prev.filter(notification => notification.id !== id));
  };

  const markAllAsRead = () => {
    setNotifications(prev =>
      prev.map(notification => ({ ...notification, isRead: true }))
    );
  };

  const filteredNotifications = notifications.filter(notification => {
    const matchesFilter = filter === 'all' || notification.category === filter || 
                         (filter === 'unread' && !notification.isRead);
    const matchesSearch = notification.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         notification.message.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesFilter && matchesSearch;
  });

  const unreadCount = notifications.filter(n => !n.isRead).length;

  const NotificationItem = ({ notification, isCompact = false }: { notification: Notification, isCompact?: boolean }) => (
    <div
      className={`p-4 border rounded-xl transition-all duration-300 hover:shadow-lg ${
        notification.isRead ? 'bg-white border-gray-200' : getNotificationColor(notification.type)
      } ${isCompact ? 'p-3' : ''}`}
    >
      <div className="flex items-start justify-between gap-3">
        <div className="flex items-start gap-3 flex-1">
          <div className="flex-shrink-0 mt-0.5">
            {getNotificationIcon(notification.type)}
          </div>
          <div className="flex-1 min-w-0">
            <div className="flex items-center gap-2 mb-1">
              <h4 className={`font-semibold text-gray-900 ${isCompact ? 'text-sm' : 'text-base'}`}>
                {notification.title}
              </h4>
              <Badge className={`${getPriorityColor(notification.priority)} text-xs`}>
                {notification.priority}
              </Badge>
              {!notification.isRead && (
                <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
              )}
            </div>
            <p className={`text-gray-600 ${isCompact ? 'text-xs' : 'text-sm'} mb-2`}>
              {notification.message}
            </p>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2 text-xs text-gray-500">
                <Clock className="w-3 h-3" />
                {formatTimestamp(notification.timestamp)}
                <Badge className="bg-gray-100 text-gray-700 capitalize text-xs">
                  {notification.category}
                </Badge>
              </div>
              {notification.actionable && (
                <Button
                  size="sm"
                  variant="outline"
                  className="text-xs hover:bg-blue-50 hover:border-blue-300"
                >
                  {notification.actionText}
                  <ArrowRight className="w-3 h-3 ml-1" />
                </Button>
              )}
            </div>
          </div>
        </div>
        <div className="flex items-center gap-1">
          {!notification.isRead && (
            <Tooltip>
              <TooltipTrigger asChild>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() => markAsRead(notification.id)}
                  className="w-8 h-8 p-0 hover:bg-blue-100"
                >
                  <CheckCircle className="w-4 h-4 text-blue-600" />
                </Button>
              </TooltipTrigger>
              <TooltipContent>
                <p>Mark as read</p>
              </TooltipContent>
            </Tooltip>
          )}
          <Tooltip>
            <TooltipTrigger asChild>
              <Button
                size="sm"
                variant="ghost"
                onClick={() => deleteNotification(notification.id)}
                className="w-8 h-8 p-0 hover:bg-red-100"
              >
                <X className="w-4 h-4 text-red-600" />
              </Button>
            </TooltipTrigger>
            <TooltipContent>
              <p>Dismiss</p>
            </TooltipContent>
          </Tooltip>
        </div>
      </div>
    </div>
  );

  return (
    <TooltipProvider>
      <div className="space-y-6 animate-fadeIn">
        {/* Compact Notification Bell for Header */}
        <div className="fixed top-4 right-4 z-50">
          <Tooltip>
            <TooltipTrigger asChild>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setIsExpanded(!isExpanded)}
                className="relative modern-card shadow-lg hover:shadow-xl transition-all duration-300"
              >
                <Bell className="w-5 h-5" />
                {unreadCount > 0 && (
                  <span className="absolute -top-2 -right-2 w-5 h-5 bg-red-500 text-white text-xs rounded-full flex items-center justify-center animate-pulse">
                    {unreadCount > 9 ? '9+' : unreadCount}
                  </span>
                )}
              </Button>
            </TooltipTrigger>
            <TooltipContent>
              <p>{unreadCount} unread notifications</p>
            </TooltipContent>
          </Tooltip>
        </div>

        {/* Expanded Notification Panel */}
        {isExpanded && (
          <Card className="fixed top-16 right-4 w-96 max-h-96 overflow-hidden z-40 modern-card shadow-2xl animate-slideInRight">
            <div className="p-4 border-b">
              <div className="flex items-center justify-between">
                <h3 className="font-semibold text-gray-900">Notifications</h3>
                <div className="flex items-center gap-2">
                  <Button size="sm" variant="ghost" onClick={markAllAsRead}>
                    Mark all read
                  </Button>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() => setIsExpanded(false)}
                  >
                    <X className="w-4 h-4" />
                  </Button>
                </div>
              </div>
            </div>
            <div className="max-h-80 overflow-y-auto p-2">
              {filteredNotifications.slice(0, 5).map(notification => (
                <div key={notification.id} className="mb-2">
                  <NotificationItem notification={notification} isCompact={true} />
                </div>
              ))}
              {filteredNotifications.length === 0 && (
                <div className="text-center py-8 text-gray-500">
                  <Bell className="w-8 h-8 mx-auto mb-2 opacity-50" />
                  <p>No notifications found</p>
                </div>
              )}
            </div>
            <div className="p-3 border-t bg-gray-50">
              <Button
                size="sm"
                variant="outline"
                className="w-full"
                onClick={() => setIsExpanded(false)}
              >
                View All Notifications
              </Button>
            </div>
          </Card>
        )}

        {/* Full Notification Dashboard */}
        <div className="animate-slideInUp">
          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6 mb-8">
            <div>
              <div className="flex items-center space-x-3 mb-2">
                <div className="p-3 bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl shadow-lg">
                  <Bell className="w-8 h-8 text-white" />
                </div>
                <div>
                  <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                    Notification Center
                  </h1>
                  <p className="text-gray-600 text-lg">Stay updated with real-time system alerts and updates</p>
                </div>
              </div>
            </div>
            
            <div className="flex items-center gap-3">
              <Dialog open={showSettings} onOpenChange={setShowSettings}>
                <DialogTrigger asChild>
                  <Button variant="outline" size="sm" className="modern-card">
                    <Settings className="w-4 h-4 mr-2" />
                    Settings
                  </Button>
                </DialogTrigger>
                <DialogContent>
                  <DialogHeader>
                    <DialogTitle>Notification Settings</DialogTitle>
                  </DialogHeader>
                  <div className="space-y-4 py-4">
                    <div className="space-y-2">
                      <label className="text-sm font-medium">Email Notifications</label>
                      <div className="space-y-2">
                        <label className="flex items-center space-x-2">
                          <input type="checkbox" defaultChecked className="rounded" />
                          <span className="text-sm">Allocation updates</span>
                        </label>
                        <label className="flex items-center space-x-2">
                          <input type="checkbox" defaultChecked className="rounded" />
                          <span className="text-sm">System alerts</span>
                        </label>
                        <label className="flex items-center space-x-2">
                          <input type="checkbox" className="rounded" />
                          <span className="text-sm">Weekly reports</span>
                        </label>
                      </div>
                    </div>
                  </div>
                </DialogContent>
              </Dialog>
              <Button onClick={markAllAsRead} className="gradient-button">
                Mark All Read
              </Button>
            </div>
          </div>

          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
            <Card className="modern-card interactive-hover">
              <div className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-gray-600">Total Notifications</p>
                    <p className="text-2xl font-bold text-gray-900">{notifications.length}</p>
                  </div>
                  <Bell className="w-8 h-8 text-blue-600" />
                </div>
              </div>
            </Card>
            <Card className="modern-card interactive-hover">
              <div className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-gray-600">Unread</p>
                    <p className="text-2xl font-bold text-red-600">{unreadCount}</p>
                  </div>
                  <div className="w-8 h-8 bg-red-100 rounded-full flex items-center justify-center">
                    <AlertTriangle className="w-5 h-5 text-red-600" />
                  </div>
                </div>
              </div>
            </Card>
            <Card className="modern-card interactive-hover">
              <div className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-gray-600">High Priority</p>
                    <p className="text-2xl font-bold text-orange-600">
                      {notifications.filter(n => n.priority === 'high').length}
                    </p>
                  </div>
                  <div className="w-8 h-8 bg-orange-100 rounded-full flex items-center justify-center">
                    <AlertTriangle className="w-5 h-5 text-orange-600" />
                  </div>
                </div>
              </div>
            </Card>
            <Card className="modern-card interactive-hover">
              <div className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-gray-600">Actionable</p>
                    <p className="text-2xl font-bold text-green-600">
                      {notifications.filter(n => n.actionable).length}
                    </p>
                  </div>
                  <div className="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                    <CheckCircle className="w-5 h-5 text-green-600" />
                  </div>
                </div>
              </div>
            </Card>
          </div>

          {/* Filters and Search */}
          <Card className="modern-card mb-6">
            <div className="p-6">
              <div className="flex flex-col lg:flex-row gap-4">
                <div className="flex-1">
                  <div className="relative">
                    <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                    <Input
                      placeholder="Search notifications..."
                      value={searchTerm}
                      onChange={(e) => setSearchTerm(e.target.value)}
                      className="pl-10"
                    />
                  </div>
                </div>
                <div className="flex gap-2">
                  {['all', 'unread', 'allocation', 'system', 'approval', 'deadline'].map((filterOption) => (
                    <Button
                      key={filterOption}
                      variant={filter === filterOption ? "default" : "outline"}
                      size="sm"
                      onClick={() => setFilter(filterOption)}
                      className={`capitalize ${filter === filterOption ? 'gradient-button' : 'modern-card'}`}
                    >
                      <Filter className="w-3 h-3 mr-1" />
                      {filterOption}
                    </Button>
                  ))}
                </div>
              </div>
            </div>
          </Card>

          {/* Notifications List */}
          <div className="space-y-4">
            {filteredNotifications.map((notification, index) => (
              <div key={notification.id} className="animate-slideInUp" style={{ animationDelay: `${index * 50}ms` }}>
                <NotificationItem notification={notification} />
              </div>
            ))}
            
            {filteredNotifications.length === 0 && (
              <Card className="modern-card text-center py-12">
                <Bell className="w-16 h-16 mx-auto mb-4 text-gray-300" />
                <h3 className="text-xl font-semibold text-gray-900 mb-2">No notifications found</h3>
                <p className="text-gray-600">Try adjusting your filters or search terms</p>
              </Card>
            )}
          </div>
        </div>
      </div>
    </TooltipProvider>
  );
};