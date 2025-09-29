// Demo showcase for the personalized matching system
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Target, 
  Star, 
  TrendingUp, 
  Users, 
  Code, 
  Award,
  ChevronRight,
  Play,
  Sparkles
} from 'lucide-react';

export function MatchingDemo() {
  const [currentStep, setCurrentStep] = useState(0);

  const demoSteps = [
    {
      title: "Enter Your Profile",
      description: "Add your name, skills, CGPA, and preferences",
      icon: Users,
      color: "from-blue-500 to-cyan-500"
    },
    {
      title: "AI Analysis",
      description: "Our algorithm analyzes your profile against 50+ internships",
      icon: Target,
      color: "from-purple-500 to-pink-500"
    },
    {
      title: "Perfect Matches",
      description: "Get personalized internship recommendations with match scores",
      icon: Star,
      color: "from-green-500 to-emerald-500"
    },
    {
      title: "Apply & Succeed",
      description: "Apply to top matches and land your dream internship",
      icon: Award,
      color: "from-yellow-500 to-orange-500"
    }
  ];

  const sampleMatches = [
    {
      title: "SDE Intern at TechCorp",
      match: 95,
      salary: "₹50K/month",
      skills: ["React", "JavaScript", "Node.js"]
    },
    {
      title: "Full Stack Developer at StartupXYZ", 
      match: 88,
      salary: "₹45K/month",
      skills: ["MERN Stack", "MongoDB", "Express"]
    },
    {
      title: "Frontend Developer at InnovateUI",
      match: 82,
      salary: "₹42K/month", 
      skills: ["React", "TypeScript", "Redux"]
    }
  ];

  return (
    <div className="bg-gradient-to-br from-slate-900 to-indigo-900 text-white p-8 rounded-3xl">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-12"
        >
          <div className="flex items-center justify-center mb-4">
            <Sparkles className="w-8 h-8 text-yellow-400 mr-3" />
            <h2 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
              How It Works
            </h2>
            <Sparkles className="w-8 h-8 text-yellow-400 ml-3" />
          </div>
          <p className="text-xl text-slate-300">
            Get perfectly matched internships in 4 simple steps
          </p>
        </motion.div>

        {/* Demo Steps */}
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 mb-12">
          {demoSteps.map((step, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.2 }}
              className={`relative p-6 rounded-2xl bg-gradient-to-br ${
                currentStep >= index ? step.color : 'from-slate-800 to-slate-700'
              } transition-all duration-500 cursor-pointer hover:scale-105`}
              onClick={() => setCurrentStep(index)}
            >
              <div className="text-center">
                <div className="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center mx-auto mb-4">
                  <step.icon className="w-8 h-8" />
                </div>
                <h3 className="text-lg font-bold mb-2">{step.title}</h3>
                <p className="text-sm opacity-90">{step.description}</p>
                
                {/* Step Number */}
                <div className="absolute -top-3 -right-3 w-8 h-8 bg-white text-black rounded-full flex items-center justify-center font-bold text-sm">
                  {index + 1}
                </div>
                
                {/* Arrow */}
                {index < demoSteps.length - 1 && (
                  <ChevronRight className="absolute -right-3 top-1/2 transform -translate-y-1/2 w-6 h-6 text-white/70 hidden lg:block" />
                )}
              </div>
            </motion.div>
          ))}
        </div>

        {/* Sample Results Preview */}
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.8 }}
          className="bg-white/10 backdrop-blur-sm rounded-2xl p-8"
        >
          <h3 className="text-2xl font-bold text-center mb-6">
            Sample Match Results for "React Developer"
          </h3>
          
          <div className="grid gap-4">
            {sampleMatches.map((match, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 1 + index * 0.1 }}
                className="bg-white/10 rounded-xl p-4 border border-white/20 hover:bg-white/20 transition-colors"
              >
                <div className="flex items-center justify-between">
                  <div className="flex-1">
                    <h4 className="font-semibold text-lg">{match.title}</h4>
                    <div className="flex items-center space-x-4 mt-2 text-sm text-slate-300">
                      <span>💰 {match.salary}</span>
                      <span>🔧 {match.skills.join(', ')}</span>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="flex items-center space-x-2">
                      <span className="text-2xl font-bold text-green-400">{match.match}%</span>
                      <span className="text-sm text-slate-300">Match</span>
                    </div>
                    <div className="flex items-center mt-1">
                      {[...Array(5)].map((_, i) => (
                        <Star 
                          key={i} 
                          className={`w-4 h-4 ${
                            i < Math.floor(match.match / 20) 
                              ? 'text-yellow-400 fill-current' 
                              : 'text-slate-500'
                          }`} 
                        />
                      ))}
                    </div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>

          {/* CTA */}
          <div className="text-center mt-8">
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl font-semibold shadow-xl hover:shadow-2xl transition-all"
            >
              <Play className="w-5 h-5 mr-2" />
              Try the Matching System Now
            </motion.button>
          </div>
        </motion.div>

        {/* Stats */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.2 }}
          className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12"
        >
          {[
            { label: "Internships Available", value: "50+", icon: Code },
            { label: "Average Match Accuracy", value: "94%", icon: Target },
            { label: "Successful Placements", value: "500+", icon: TrendingUp }
          ].map((stat, index) => (
            <div key={index} className="text-center">
              <stat.icon className="w-8 h-8 text-blue-400 mx-auto mb-2" />
              <div className="text-3xl font-bold text-white">{stat.value}</div>
              <div className="text-sm text-slate-400">{stat.label}</div>
            </div>
          ))}
        </motion.div>
      </div>
    </div>
  );
}