import React, { useState, useRef } from 'react';
import html2canvas from 'html2canvas';
import { jsPDF } from 'jspdf';
import { Target, BarChart2, ClipboardList, Rocket, Lock, BookOpen, RefreshCw, AlertCircle, Trophy, FileText, Activity, CheckCircle2, AlertTriangle, Play } from 'lucide-react';

// --- DATA ---
const SUBJECTS = [
  { id: 'FR', name: 'Financial Reporting (FR)' },
  { id: 'AFM', name: 'Advanced Financial Management (AFM)' },
  { id: 'Audit', name: 'Audit' },
  { id: 'DT', name: 'Direct Tax (DT)' },
  { id: 'IDT', name: 'Indirect Tax (IDT)' },
  { id: 'IBS', name: 'International Business & Economics (IBS)' }
];

const QUESTIONS = [
  {
    id: 1,
    title: 'Your Syllabus Completion',
    subtitle: 'How much syllabus have you completed in each subject?\n(Select one option for each subject)',
    sidebarTitle: 'Syllabus Status',
    type: 'matrix',
    icon: BookOpen,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "Real students face gaps. Winners fix them."
  },
  {
    id: 2,
    title: 'Your Revision Status',
    subtitle: 'How many revisions have you completed for each subject?\n(Select one option for each subject)',
    sidebarTitle: 'Revision Status',
    type: 'matrix',
    icon: RefreshCw,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "Progress is a result of honest self-assessment, not wishful thinking."
  },
  {
    id: 3,
    title: 'Your Last Mock/Test Performance',
    subtitle: 'What was your most recent mock or test score in each subject?\n(Select one option for each subject)',
    sidebarTitle: 'Mock/Test Performance',
    type: 'matrix',
    icon: BarChart2,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "Tests don't define you. They show you what to work on."
  },
  {
    id: 4,
    title: 'Marks Loss Analysis',
    subtitle: 'Where do you lose maximum marks in each subject?',
    sidebarTitle: 'Marks Loss',
    type: 'matrix',
    icon: AlertCircle,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "Identifying the leak is the first step to fixing the pipe."
  },
  {
    id: 5,
    title: 'PYQs, RTPs & MTPs',
    subtitle: 'How much of past papers and mock series have you solved?',
    sidebarTitle: 'PYQs, RTPs & MTPs',
    type: 'matrix',
    icon: FileText,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "Exam conditions reveal what casual study conceals."
  },
  {
    id: 6,
    title: 'Recall Ability',
    subtitle: 'How easily can you recall concepts without looking at the book?',
    sidebarTitle: 'Recall Ability',
    type: 'matrix',
    icon: Activity,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "Memory is a muscle. Active recall is the workout."
  },
  {
    id: 7,
    title: 'Backlog Analysis',
    subtitle: 'What is the status of your backlog in each subject?',
    sidebarTitle: 'Backlog Analysis',
    type: 'matrix',
    icon: AlertTriangle,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "Don't let yesterday take up too much of today."
  },
  {
    id: 8,
    title: 'Next 7-10 Days Planning',
    subtitle: 'How clear is your study plan for the next week?',
    sidebarTitle: 'Next 7-10 Days',
    type: 'single',
    icon: Target,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "A goal without a plan is just a wish."
  },
  {
    id: 9,
    title: 'Study Execution',
    subtitle: 'How much of your planned daily study time do you actually achieve?',
    sidebarTitle: 'Study Execution',
    type: 'single',
    icon: Play,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "Execution eats strategy for breakfast."
  },
  {
    id: 10,
    title: 'November Readiness',
    subtitle: 'If the exam were tomorrow, how ready do you feel?',
    sidebarTitle: 'November Readiness',
    type: 'single',
    icon: CheckCircle2,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: "Confidence comes from discipline and training."
  }
];

// --- COMPONENTS ---

const FastLogo = ({ className = "" }) => (
  <div className={`flex flex-col items-center bg-[#e51c24] border border-[#a81319] rounded-[2px] p-1 w-fit ${className}`}>
    <div className="text-white font-black italic text-2xl md:text-3xl tracking-widest leading-none px-2">F.A.S.T</div>
    <div className="bg-black text-white text-[6px] md:text-[8px] uppercase font-bold tracking-[0.1em] px-2 py-0.5 mt-0.5 w-full text-center border border-gray-600">
      first attempt success tutorials
    </div>
  </div>
);

const Landing = ({ onStart, onNav }) => {
  return (
    <div 
      className="h-[100dvh] text-white flex flex-col font-sans relative overflow-hidden bg-black"
      style={{
        backgroundImage: "url('https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=1920&auto=format&fit=crop')",
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundBlendMode: 'overlay',
        backgroundColor: 'rgba(10, 10, 10, 0.85)' // Dark overlay
      }}
    >
      {/* Navbar */}
      <nav className="flex justify-between items-center px-4 md:px-12 py-3 md:py-4 z-10 relative">
        <FastLogo />
        <div className="hidden md:flex space-x-10 text-sm font-medium text-gray-300">
          <button onClick={() => onNav('Home')} className="hover:text-white transition-colors">Home</button>
          <button onClick={() => onNav('CA Final')} className="hover:text-white flex items-center transition-colors">CA Final <span className="ml-1 text-[10px]">▼</span></button>
          <button onClick={() => onNav('About')} className="hover:text-white transition-colors">About</button>
          <button onClick={() => onNav('Contact')} className="hover:text-white transition-colors">Contact</button>
        </div>
      </nav>

      {/* Main Content */}
      <div className="flex-1 flex flex-col items-center justify-center relative z-10 px-4 pb-16 md:pb-20 text-center w-full max-w-full">
        
        <h2 className="text-2xl md:text-3xl font-bold tracking-wide mb-2 uppercase text-gray-100">CA Final Nov 26</h2>
        <h1 className="text-[2.75rem] leading-[1.1] md:text-6xl font-black italic mb-3 flex flex-wrap justify-center gap-x-3 gap-y-1 w-full">
          <span className="text-white drop-shadow-lg">REALITY</span>
          <span className="text-[#e51c24] drop-shadow-lg">CHECK</span>
        </h1>
        <p className="text-base md:text-lg text-gray-200 mb-6 font-medium max-w-2xl drop-shadow-md">
          A 10-Question Self-Assessment<br/>for a Clearer, Stronger You.
        </p>

        {/* Features */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-y-6 gap-x-4 md:gap-6 mb-8 max-w-4xl w-full px-2">
          {[
            { icon: Target, text: "Know Your\nCurrent Position" },
            { icon: BarChart2, text: "Identify Your\nWeak Areas" },
            { icon: ClipboardList, text: "Get Subject-wise\nAnalysis" },
            { icon: Rocket, text: "Start Your\nAction Plan" }
          ].map((feat, idx) => (
            <div key={idx} className="flex flex-col items-center text-center">
              <div className="w-11 h-11 md:w-12 md:h-12 rounded-full border-2 border-white/20 flex items-center justify-center mb-3 bg-white/5 backdrop-blur-sm">
                <feat.icon className="w-5 h-5 md:w-5 md:h-5 text-white" strokeWidth={2} />
              </div>
              <p className="text-xs md:text-[13px] text-gray-300 whitespace-pre-line font-medium leading-tight">{feat.text}</p>
            </div>
          ))}
        </div>

        {/* CTA */}
        <button 
          onClick={onStart}
          className="bg-[#e51c24] hover:bg-red-700 text-white text-lg md:text-xl font-bold py-3.5 md:py-4 px-8 md:px-16 w-[90%] sm:w-auto rounded-xl flex items-center justify-center transition-all shadow-[0_0_30px_rgba(229,28,36,0.5)] relative z-20"
        >
          Start Reality Check <span className="ml-2">→</span>
        </button>
        <div className="flex items-center text-gray-400 mt-4 text-[11px] md:text-xs font-medium relative z-20">
          <Lock className="w-3.5 h-3.5 mr-1" />
          Secure & Private Assessment
        </div>

        {/* Floating Texts & Decor */}
        {/* Top Right Red Text */}
        <div className="absolute top-4 md:top-16 right-4 md:right-16 xl:right-32 text-[#e51c24] font-handwriting text-xl md:text-3xl rotate-[-5deg] leading-tight hidden md:block drop-shadow-md text-right">
          Be Honest.<br/>Know Your Gaps.<br/>Plan Better.
          <div className="h-1 w-full bg-[#e51c24] rounded-full mt-1 opacity-80 transform -rotate-2"></div>
        </div>

        {/* Sticky Note */}
        <div className="absolute top-auto bottom-6 md:bottom-12 right-4 md:right-12 xl:right-24 bg-[#e8e4d9] text-gray-900 font-handwriting text-lg md:text-xl p-4 shadow-2xl rotate-[3deg] hidden lg:flex flex-col items-center justify-center w-36 h-36 md:w-40 md:h-40 rounded-sm">
          <div className="absolute top-[-8px] w-12 h-4 bg-white/40 shadow-sm rotate-[-2deg]"></div>
          Discipline<br/>Creates<br/>Freedom
        </div>

        {/* Left Hoodie Text */}
        <div className="absolute bottom-28 md:bottom-32 left-4 md:left-12 xl:left-24 text-gray-300 font-handwriting text-2xl md:text-3xl rotate-[-8deg] leading-tight hidden lg:block opacity-80 drop-shadow-lg text-left">
          Same<br/>Student<br/>Different<br/>Result!
        </div>

        {/* Bottom Pill Quote */}
        <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 w-[95%] max-w-2xl px-2 md:px-4 z-20">
           <div className="bg-white/10 backdrop-blur-md rounded-xl md:rounded-2xl py-3.5 px-5 md:py-4 md:px-8 text-gray-300 italic text-[11px] sm:text-xs md:text-sm border border-white/10 shadow-2xl flex justify-between items-center">
              <span className="leading-snug">"Clarity today, a better result tomorrow."</span> 
              <span className="font-semibold not-italic text-gray-400 ml-2 whitespace-nowrap">— Team FAST</span>
           </div>
        </div>
      </div>
    </div>
  );
};
const Assessment = ({ onComplete }) => {
  const [currentStep, setCurrentStep] = useState(1);
  
  React.useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'instant' });
  }, [currentStep]);
  const [answers, setAnswers] = useState({}); // { qId: { FR: val, AFM: val... } or single value }

  const question = QUESTIONS[currentStep - 1];

  const handleMatrixChange = (subjectId, value) => {
    setAnswers(prev => ({
      ...prev,
      [question.id]: {
        ...(prev[question.id] || {}),
        [subjectId]: value
      }
    }));
  };

  const handleSingleChange = (value) => {
    setAnswers(prev => ({
      ...prev,
      [question.id]: value
    }));
  };

  const canProceed = () => {
    const qAns = answers[question.id];
    if (question.type === 'matrix') {
      if (!qAns) return false;
      return SUBJECTS.every(s => qAns[s.id] !== undefined);
    } else {
      return qAns !== undefined;
    }
  };

  const handleNext = () => {
    if (currentStep < QUESTIONS.length) {
      setCurrentStep(prev => prev + 1);
    } else {
      onComplete(answers);
    }
  };

  return (
    <div className="min-h-screen bg-[#f3f4f6] flex flex-col font-sans">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 px-3 sm:px-6 py-3 flex justify-between items-center shadow-sm z-20 sticky top-0">
        <div className="flex items-center space-x-3 sm:space-x-6 scale-[0.80] origin-left sm:scale-100">
          <FastLogo />
          <div className="font-bold text-[#1a2b4b] text-lg hidden sm:block">
            CA Final Nov 26<br/>
            <span className="text-gray-600 text-sm font-semibold">Reality Check</span>
          </div>
        </div>
        <div className="flex flex-col items-end w-32 sm:w-48">
          <div className="flex justify-between w-full text-sm font-bold text-[#1a2b4b] mb-1">
            <span>Q {currentStep} of {QUESTIONS.length}</span>
            <span>{Math.round((currentStep / QUESTIONS.length) * 100)}%</span>
          </div>
          <div className="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
            <div 
              className="bg-[#e51c24] h-full transition-all duration-300"
              style={{ width: `${(currentStep / QUESTIONS.length) * 100}%` }}
            ></div>
          </div>
        </div>
      </header>

      <div className="flex flex-1 max-w-7xl mx-auto w-full p-4 md:p-6 gap-6 items-start">
        {/* Sidebar */}
        <aside className="hidden md:flex flex-col w-64 shrink-0 bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden sticky top-24">
          <div className="py-2">
            {QUESTIONS.map((q, idx) => {
              const stepNum = idx + 1;
              const isActive = stepNum === currentStep;
              const isPast = stepNum < currentStep;
              
              return (
                <div 
                  key={q.id}
                  className={`flex items-center px-4 py-3 cursor-default transition-colors ${
                    isActive ? 'bg-[#fff1f2] border-l-4 border-[#e51c24]' : 'border-l-4 border-transparent hover:bg-gray-50'
                  }`}
                >
                  <div className={`w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold mr-3 shrink-0 ${
                    isActive ? 'bg-black text-white' : 
                    isPast ? 'bg-black text-white' : 'border-2 border-gray-300 text-gray-400 bg-white'
                  }`}>
                    {stepNum}
                  </div>
                  <span className={`text-sm font-medium ${isActive ? 'text-[#e51c24] font-bold' : isPast ? 'text-gray-800' : 'text-gray-500'}`}>
                    {q.sidebarTitle}
                  </span>
                </div>
              );
            })}
          </div>
          <div className="mt-auto p-6 bg-[#fff7ed]">
            <p className="text-[#c2410c] font-medium text-sm leading-relaxed italic">
              {question.quote}
            </p>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 bg-white md:rounded-xl shadow-sm border border-gray-200 p-4 md:p-10 flex flex-col min-h-[50vh]">
          <div className="flex items-start mb-8">
            <div className="bg-[#fff1f2] p-3 rounded-xl text-[#e51c24] mr-4 shrink-0">
              <question.icon className="w-8 h-8" />
            </div>
            <div>
              <h2 className="text-2xl font-bold text-[#1a2b4b] mb-2">{question.title}</h2>
              <p className="text-gray-500 font-medium whitespace-pre-line leading-relaxed">{question.subtitle}</p>
            </div>
          </div>

          <div className="w-full pb-2 md:pb-4 overflow-hidden">
            {question.type === 'matrix' ? (
              <table className="w-full table-fixed border-collapse max-w-full">
                <thead>
                  <tr>
                    <th className="bg-[#f8fafc] text-left p-1 md:p-4 rounded-tl-lg font-bold text-[#1a2b4b] border-b border-gray-200 w-[28%] text-[8px] md:text-sm leading-tight">Subject</th>
                    {question.options.map((opt, i) => (
                      <th key={i} className={`bg-[#f8fafc] p-1 md:p-2 lg:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 text-[6.5px] min-[375px]:text-[7.5px] sm:text-[9px] md:text-xs lg:text-sm whitespace-nowrap tracking-tighter ${i === question.options.length - 1 ? 'rounded-tr-lg' : ''}`}>
                        {opt.text}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {SUBJECTS.map((subject, sIdx) => (
                    <tr key={subject.id} className="border-b border-gray-100 hover:bg-gray-50/50 transition-colors">
                      <td className="p-2 md:p-4 font-medium text-[#1a2b4b] text-[10px] md:text-sm leading-tight">{subject.name}</td>
                      {question.options.map((opt, oIdx) => {
                        const isSelected = answers[question.id]?.[subject.id] === opt.value;
                        return (
                          <td key={oIdx} className="p-1 md:p-4 text-center">
                            <input 
                              type="radio" 
                              name={`${question.id}-${subject.id}`}
                              className="custom-radio scale-75 md:scale-100"
                              checked={isSelected}
                              onChange={() => handleMatrixChange(subject.id, opt.value)}
                            />
                          </td>
                        );
                      })}
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div className="space-y-3 max-w-2xl">
                {question.options.map((opt, oIdx) => {
                  const isSelected = answers[question.id] === opt.value;
                  return (
                    <label key={oIdx} className={`flex items-center p-5 rounded-xl border-2 cursor-pointer transition-all ${
                      isSelected ? 'border-[#e51c24] bg-[#fff1f2]' : 'border-gray-200 hover:border-gray-300 bg-white'
                    }`}>
                      <input 
                        type="radio"
                        name={`q-${question.id}`}
                        className="custom-radio mr-4"
                        checked={isSelected}
                        onChange={() => handleSingleChange(opt.value)}
                      />
                      <span className={`font-semibold text-lg ${isSelected ? 'text-[#e51c24]' : 'text-[#1a2b4b]'}`}>
                        {opt.text}
                      </span>
                    </label>
                  )
                })}
              </div>
            )}
          </div>

          {/* Footer Actions */}
          <div className="mt-4 md:mt-8 pt-4 md:pt-6 border-t border-gray-100 flex justify-between items-center mt-auto">
            <button 
              onClick={() => setCurrentStep(prev => Math.max(1, prev - 1))}
              disabled={currentStep === 1}
              className={`flex items-center px-4 md:px-6 py-2 md:py-3 rounded-lg font-bold text-sm md:text-base transition-colors ${
                currentStep === 1 ? 'text-gray-300 cursor-not-allowed bg-gray-50' : 'text-gray-600 bg-gray-100 hover:bg-gray-200'
              }`}
            >
              <span className="mr-2">←</span> Back
            </button>
            <button 
              onClick={handleNext}
              disabled={!canProceed()}
              className={`flex items-center px-6 md:px-8 py-2 md:py-3 rounded-lg font-bold text-sm md:text-base transition-all shadow-md ${
                !canProceed() ? 'bg-gray-300 text-white cursor-not-allowed shadow-none' : 'bg-[#e51c24] hover:bg-red-700 text-white'
              }`}
            >
              {currentStep === QUESTIONS.length ? 'Show Results' : 'Next'} <span className="ml-2">→</span>
            </button>
          </div>
        </main>
      </div>
    </div>
  );
};

const Result = ({ answers, onRetake }) => {
  const [activeTab, setActiveTab] = useState('Overview');
  const dashboardRef = useRef(null);
  const handleDownload = async () => {
    if(!dashboardRef.current) return;
    try {
      const canvas = await html2canvas(dashboardRef.current, { scale: 2 });
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jsPDF('p', 'mm', 'a4');
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = (canvas.height * pdfWidth) / canvas.width;
      pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
      pdf.save('CA_Final_Reality_Check_Report.pdf');
    } catch (e) {
      console.error(e);
      alert('Failed to download report. Please try on a desktop.');
    }
  };
  // Logic to calculate scores based on answers
  // Max possible per subject per question is generally 4 (value).
  // Some matrix questions have 4 options (1-4).
  
  // Calculate average per subject
  const subjectScores = SUBJECTS.map(sub => {
    let subTotal = 0;
    let count = 0;
    
    // Q1, Q2, Q3, Q4, Q5, Q6, Q7 are matrices
    QUESTIONS.forEach(q => {
      if (q.type === 'matrix' && answers[q.id] && answers[q.id][sub.id] !== undefined) {
        subTotal += answers[q.id][sub.id];
        count++;
      }
    });
    
    return {
      ...sub,
      score: count > 0 ? (subTotal / count) : 0, // avg out of 4
      syl: answers[1]?.[sub.id] || 0,
      rev: answers[2]?.[sub.id] || 0,
      mock: answers[3]?.[sub.id] || 0,
      prac: answers[5]?.[sub.id] || 0,
    };
  });

  // Category wise percentages
  // Syl = Q1 average, Rev = Q2 average, Prac = Q5 average, Exec = Q9 (single), Read = Q10 (single)
  const calcMatrixAvg = (qId) => {
    if (!answers[qId]) return 0;
    const vals = Object.values(answers[qId]);
    if (vals.length === 0) return 0;
    const avg = vals.reduce((a, b) => a + b, 0) / vals.length;
    return Math.round((avg / 4) * 100);
  };
  
  const sylCov = calcMatrixAvg(1);
  const revStat = calcMatrixAvg(2);
  const examPrac = calcMatrixAvg(3);
  const execution = answers[9] ? Math.round((answers[9] / 4) * 100) : 0;
  const readiness = answers[10] ? Math.round((answers[10] / 4) * 100) : 0;

  // Overall Score Out of 40 (based on image). If there are 10 questions, each average out of 4 = max 40.
  let totalScore = 0;
  QUESTIONS.forEach(q => {
    if (q.type === 'matrix') {
      const vals = Object.values(answers[q.id] || {});
      if (vals.length > 0) {
        totalScore += vals.reduce((a, b) => a + b, 0) / vals.length;
      }
    } else {
      totalScore += (answers[q.id] || 0);
    }
  });
  
  const finalScore = Math.round(totalScore);
  const finalPerc = Math.round((finalScore / 40) * 100);

  const overallStat = (() => {
    if (finalPerc >= 80) return {
      text: "EXCELLENT",
      color: "text-[#16a34a]",
      bg: "bg-green-50",
      border: "border-green-200",
      icon: CheckCircle2,
      desc: "Outstanding preparation! You are well on track for a great result.",
      quote: "Success is the sum of small efforts, repeated day in and day out."
    };
    if (finalPerc >= 50) return {
      text: "GOOD PROGRESS",
      color: "text-[#ca8a04]",
      bg: "bg-yellow-50",
      border: "border-yellow-200",
      icon: Activity,
      desc: "You are doing well, but there is room for improvement in some areas.",
      quote: "Good is not enough when better is expected."
    };
    return {
      text: "NEEDS CORRECTION",
      color: "text-[#e51c24]",
      bg: "bg-[#fff1f2]",
      border: "border-red-100",
      icon: AlertCircle,
      desc: "Good progress, but important gaps need attention. Now is the time to fix them and get on track.",
      quote: "You're not far, you just need a sharper plan."
    };
  })();

  // Strongest / Weakest
  const sortedSubjects = [...subjectScores].sort((a, b) => b.score - a.score);
  const strongest = sortedSubjects[0];
  const weakest = sortedSubjects[sortedSubjects.length - 1];
  
  const highestScore = strongest.score;
  const strongestList = sortedSubjects.filter(s => s.score === highestScore);
  let strongestName = strongestList[0].name.split(' (')[0];
  if (strongestList.length === sortedSubjects.length) {
    strongestName = 'All Subjects (Tie)';
  } else if (strongestList.length > 1) {
    strongestName = strongestName + ' & ' + (strongestList.length - 1) + ' more';
  }

  const lowestScore = weakest.score;
  const weakestList = sortedSubjects.filter(s => s.score === lowestScore);
  let weakestName = weakestList[0].name.split(' (')[0];
  if (weakestList.length === sortedSubjects.length) {
    weakestName = 'All Subjects (Tie)';
  } else if (weakestList.length > 1) {
    weakestName = weakestName + ' & ' + (weakestList.length - 1) + ' more';
  }

  const getStatus = (perc) => {
    if (perc >= 75) return { text: "Good", color: "text-[#16a34a]" };
    if (perc >= 50) return { text: "Needs Work", color: "text-[#e51c24]" };
    return { text: "Needs Correction", color: "text-[#e51c24]" };
  };

  const mapOptText = (qId, val) => {
    const q = QUESTIONS.find(q => q.id === qId);
    const opt = q.options.find(o => o.value === val);
    return opt ? opt.text : '-';
  };

  const getReadinessDot = (score) => {
    if (score >= 3.5) return <span className="flex items-center text-sm"><span className="w-2.5 h-2.5 rounded-full bg-[#16a34a] mr-2"></span> Ready</span>;
    if (score >= 2.5) return <span className="flex items-center text-sm"><span className="w-2.5 h-2.5 rounded-full bg-[#f59e0b] mr-2"></span> Almost Ready</span>;
    return <span className="flex items-center text-sm"><span className="w-2.5 h-2.5 rounded-full bg-[#e51c24] mr-2"></span> Needs Work</span>;
  };

  return (
    <div className="min-h-screen bg-[#111] flex font-sans">
      
      {/* Sidebar */}
      <aside className="w-64 bg-[#111] text-white flex flex-col border-r border-gray-800 shrink-0 hidden lg:flex">
        <div className="p-6 border-b border-gray-800">
          <FastLogo />
          <div className="mt-6 font-bold text-lg text-white">
            CA Final Nov 26<br/>
            <span className="text-gray-400 text-sm font-semibold">Reality Check</span>
          </div>
        </div>
        
        <div className="flex-1"></div>

        <div className="p-6 relative">
          <div className="font-handwriting text-2xl text-gray-400 rotate-[-5deg] leading-tight">
            Same Effort.<br/>Better Direction.<br/>Stronger You.
          </div>
          <BarChart2 className="w-12 h-12 text-gray-700 mt-4 rotate-[15deg]" />
        </div>
      </aside>

      {/* Main Dashboard */}
      <main ref={dashboardRef} className="flex-1 bg-[#f8fafc] lg:rounded-l-2xl overflow-hidden flex flex-col h-screen overflow-y-auto relative">
        <div className="p-6 md:p-8">
          
          <div className="flex justify-between items-center mb-8 flex-wrap gap-4">
            <div>
              <h1 className="text-3xl font-bold text-[#1a2b4b]">Your CA Final Reality Check Result</h1>
              <p className="text-gray-500 font-medium mt-1">Here's your complete preparation analysis based on your responses.</p>
            </div>
            <div className="flex gap-4">
              <button onClick={onRetake} className="px-5 py-2.5 bg-white border border-gray-300 rounded-lg text-gray-700 font-bold hover:bg-gray-50 flex items-center">
                <RefreshCw className="w-4 h-4 mr-2" /> Retake Test
              </button>
              <button onClick={handleDownload} className="px-5 py-2.5 bg-[#e51c24] rounded-lg text-white font-bold hover:bg-red-700 flex items-center shadow-md">
                Download My Report
              </button>
            </div>
          </div>

          {/* Top Cards Row */}
          <div className="grid grid-cols-1 md:grid-cols-12 gap-6 mb-6">
            
            {/* Overall Score */}
            <div className={`md:col-span-4 bg-white p-6 rounded-2xl shadow-sm border flex flex-col relative overflow-hidden ${overallStat.border}`}>
              <div className="text-sm font-bold text-[#1a2b4b] mb-2">Overall Score</div>
              <div className="flex items-baseline mb-2">
                <span className={`text-5xl font-black ${overallStat.color}`}>{finalScore}</span>
                <span className="text-2xl font-bold text-gray-400 ml-1">/ 40</span>
              </div>
              <div className="flex items-center gap-4 mb-4">
                <div className={`flex-1 ${overallStat.bg} h-2.5 rounded-full overflow-hidden`}>
                  <div className={`h-full ${overallStat.color === 'text-[#16a34a]' ? 'bg-[#16a34a]' : overallStat.color === 'text-[#ca8a04]' ? 'bg-[#ca8a04]' : 'bg-[#e51c24]'}`} style={{ width: `${finalPerc}%` }}></div>
                </div>
                <span className={`font-bold ${overallStat.color} text-sm`}>{finalPerc}%</span>
              </div>
              <div className={`${overallStat.bg} ${overallStat.color} text-sm font-bold px-3 py-1.5 rounded w-fit mb-4 flex items-center border ${overallStat.border}`}>
                <overallStat.icon className="w-4 h-4 mr-1.5" /> {overallStat.text}
              </div>
              <p className="text-gray-600 text-sm leading-relaxed mb-4 flex-1">
                {overallStat.desc}
              </p>
              <p className="text-xs text-gray-400 italic">"{overallStat.quote}" <br/><span className="float-right">— Team FAST</span></p>
            </div>

            {/* Category Scores & Highlights */}
            <div className="md:col-span-8 flex flex-col gap-6">
              
              {/* Category Wise Score */}
              <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-200">
                <h3 className="text-sm font-bold text-[#1a2b4b] mb-4">Category Wise Score</h3>
                <div className="grid grid-cols-2 sm:grid-cols-5 gap-4">
                  {[
                    { icon: BookOpen, label: 'Syllabus\nCoverage', score: sylCov },
                    { icon: RefreshCw, label: 'Revision\nStatus', score: revStat },
                    { icon: FileText, label: 'Exam\nPractice', score: examPrac },
                    { icon: Play, label: 'Execution\n', score: execution },
                    { icon: Target, label: 'Readiness\n', score: readiness },
                  ].map((cat, i) => {
                    const stat = getStatus(cat.score);
                    return (
                      <div key={i} className="flex flex-col items-center text-center p-3 border border-gray-100 rounded-xl hover:shadow-md transition-shadow">
                        <cat.icon className={`w-8 h-8 mb-2 ${stat.color === 'text-[#16a34a]' ? 'text-[#16a34a]' : 'text-[#e51c24]'}`} strokeWidth={1.5} />
                        <div className="text-xs font-semibold text-gray-500 whitespace-pre-line leading-tight mb-2 h-8">{cat.label}</div>
                        <div className="text-xl font-black text-[#1a2b4b] mb-1">{cat.score}%</div>
                        <div className={`text-[10px] font-bold uppercase tracking-wider ${stat.color} bg-gray-50 px-2 py-1 rounded w-full border border-gray-100`}>
                          {stat.text}
                        </div>
                      </div>
                    )
                  })}
                </div>
              </div>

              {/* Highlights */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 flex-1">
                <div className="bg-white p-5 rounded-2xl shadow-sm border border-gray-200 flex items-start border-l-4 border-l-[#16a34a]">
                  <div className="bg-green-100 p-3 rounded-xl mr-4 text-[#16a34a]">
                    <Trophy className="w-8 h-8" />
                  </div>
                  <div>
                    <div className="text-xs font-bold text-gray-500 mb-1">Your Strongest Subject</div>
                    <div className="text-xl font-bold text-[#1a2b4b] mb-1">{strongestName}</div>
                    <div className="text-sm text-gray-600 mb-2">({Math.round((strongest.score / 4)*100)}% overall readiness)</div>
                    <div className="text-sm font-semibold text-[#16a34a]">Keep the momentum!</div>
                  </div>
                </div>
                
                {weakest.score >= 3.5 ? (
                  <div className="bg-white p-5 rounded-2xl shadow-sm border border-gray-200 flex items-start border-l-4 border-l-[#16a34a]">
                    <div className="bg-green-100 p-3 rounded-xl mr-4 text-[#16a34a]">
                      <CheckCircle2 className="w-8 h-8" />
                    </div>
                    <div>
                      <div className="text-xs font-bold text-gray-500 mb-1">Area of Focus</div>
                      <div className="text-xl font-bold text-[#1a2b4b] mb-1">All Subjects Strong!</div>
                      <div className="text-sm text-gray-600 mb-2">You have excellent readiness across the board.</div>
                      <div className="text-sm font-semibold text-[#16a34a]">Keep revising consistently.</div>
                    </div>
                  </div>
                ) : (
                  <div className="bg-white p-5 rounded-2xl shadow-sm border border-gray-200 flex items-start border-l-4 border-l-[#e51c24]">
                    <div className="bg-red-100 p-3 rounded-xl mr-4 text-[#e51c24]">
                      <AlertTriangle className="w-8 h-8" />
                    </div>
                    <div>
                      <div className="text-xs font-bold text-gray-500 mb-1">Your Biggest Gap</div>
                      <div className="text-xl font-bold text-[#1a2b4b] mb-1">{weakestName}</div>
                      <div className="text-sm text-gray-600 mb-2">Needs immediate action</div>
                      <div className="text-sm font-semibold text-[#e51c24]">Prioritise this subject in your next 30 days.</div>
                    </div>
                  </div>
                )}
              </div>

            </div>
          </div>

          {/* Bottom Row */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            {/* Table */}
            <div className="lg:col-span-2 bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
              <div className="p-5 border-b border-gray-100">
                <h3 className="font-bold text-[#1a2b4b]">Subject-wise Summary</h3>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full text-sm text-left">
                  <thead className="bg-[#f8fafc] text-xs uppercase font-bold text-gray-500">
                    <tr>
                      <th className="px-5 py-4">Subject</th>
                      <th className="px-5 py-4">Syllabus<br/>Completion</th>
                      <th className="px-5 py-4">Revision<br/>Status</th>
                      <th className="px-5 py-4">Last Mock<br/>Score</th>
                      <th className="px-5 py-4">PYQs/RTPs/MTPs</th>
                      <th className="px-5 py-4">Readiness</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-100">
                    {subjectScores.map((sub, i) => (
                      <tr key={i} className="hover:bg-gray-50 transition-colors">
                        <td className="px-5 py-4 font-semibold text-[#1a2b4b] whitespace-nowrap">{sub.name}</td>
                        <td className="px-5 py-4 text-gray-600 font-medium">{mapOptText(1, sub.syl)}</td>
                        <td className="px-5 py-4 text-gray-600 font-medium">{mapOptText(2, sub.rev)}</td>
                        <td className="px-5 py-4 text-gray-600 font-medium">{mapOptText(3, sub.mock)}</td>
                        <td className="px-5 py-4 text-gray-600 font-medium">{mapOptText(5, sub.prac)}</td>
                        <td className="px-5 py-4 font-bold">{getReadinessDot(sub.score)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Next Steps */}
            <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 flex flex-col">
              <h3 className="font-bold text-[#1a2b4b] mb-6 flex items-center">
                <Activity className="w-5 h-5 mr-2 text-[#1a2b4b]" /> Your Next Steps
              </h3>
              
              <div className="space-y-4 flex-1">
                {(() => {
                  const w1 = weakest.id || 'your weaker subjects';
                  const w2 = sortedSubjects[sortedSubjects.length - 2]?.id || 'other subjects';
                  let steps = [];
                  if (finalPerc >= 80) {
                    steps = [
                      "Excellent preparation! Focus entirely on maintaining your momentum.",
                      `Keep revising ${w1} and ${w2} to ensure no minor gaps remain.`,
                      "Focus strictly on past exam papers (PYQs) and recent RTPs.",
                      "Attempt full-syllabus timed mocks to master time management.",
                      "Avoid starting any new heavy materials; trust your current notes."
                    ];
                  } else if (finalPerc >= 50) {
                    steps = [
                      `Address specific conceptual gaps in ${w1} and ${w2} on priority.`,
                      "Consolidate your revision rather than reading new heavy materials.",
                      "Solve at least 3-4 past papers specifically for your weaker subjects.",
                      "Give sectional mocks to build confidence before jumping to full mocks.",
                      "Follow a strict daily timetable to cover remaining topics efficiently."
                    ];
                  } else {
                    steps = [
                      `Complete your pending syllabus for ${w1} on utmost priority.`,
                      `Start a structured, aggressive revision for ${w2}.`,
                      "Focus on high-weightage chapters first; don't rush 100% coverage blindly.",
                      "Do not jump to full mocks yet; solve chapter-wise questions to build a base.",
                      "Maintain a fixed daily study plan and track your targets strictly."
                    ];
                  }
                  return steps.map((step, i) => (
                    <div key={i} className="flex items-start">
                      <div className="w-6 h-6 rounded-full bg-[#e51c24] text-white flex items-center justify-center text-xs font-bold mr-3 shrink-0 mt-0.5">
                        {i + 1}
                      </div>
                      <p className="text-sm text-gray-700 font-medium leading-relaxed">{step}</p>
                    </div>
                  ));
                })()}
              </div>

              <div className="mt-6 p-4 bg-[#f8fafc] rounded-xl border border-gray-100 italic text-sm text-gray-500 text-center mb-6">
                "Discipline today, a better result tomorrow." <span className="font-bold not-italic">— Team FAST</span>
              </div>

              <button className="w-full bg-[#e51c24] hover:bg-red-700 text-white font-bold py-4 rounded-xl flex items-center justify-center transition-colors shadow-lg shadow-red-500/20">
                Keep Going, You Can Do This! <span className="ml-2">→</span>
              </button>
            </div>

          </div>
        </div>
      </main>
    </div>
  );
};

const Nav = ({ current, onNav }) => (
  <nav className="flex justify-between items-center px-6 md:px-12 py-4 border-b border-gray-800 z-10 relative bg-[#111]">
    <FastLogo />
    <div className="hidden md:flex space-x-10 text-sm font-medium text-gray-300">
      <button onClick={() => onNav('Home')} className={`hover:text-white transition-colors ${current === 'Home' ? 'text-white font-bold' : ''}`}>Home</button>
      <button onClick={() => onNav('CA Final')} className={`hover:text-white flex items-center transition-colors ${current === 'CA Final' ? 'text-white font-bold' : ''}`}>CA Final <span className="ml-1 text-[10px]">▼</span></button>
      <button onClick={() => onNav('About')} className={`hover:text-white transition-colors ${current === 'About' ? 'text-white font-bold' : ''}`}>About</button>
      <button onClick={() => onNav('Contact')} className={`hover:text-white transition-colors ${current === 'Contact' ? 'text-white font-bold' : ''}`}>Contact</button>
    </div>
  </nav>
);

const Home = ({ onNav }) => (
  <div className="min-h-screen bg-[#111] text-white flex flex-col font-sans relative">
    <Nav current="Home" onNav={onNav} />
    <div className="flex-1 flex flex-col items-center justify-center p-6 text-center">
      <h2 className="text-xl text-gray-400 mb-2 uppercase tracking-widest mt-12">Welcome to</h2>
      <h1 className="text-5xl md:text-7xl font-black italic mb-8">
        FIRST ATTEMPT <span className="text-[#e51c24]">SUCCESS</span>
      </h1>
      <p className="text-lg md:text-xl text-gray-300 mb-12 max-w-2xl leading-relaxed">
        Premium video classes, comprehensive books, and structured test series for CA Final & Inter.
      </p>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl w-full mb-16">
        <div className="bg-gray-900 border border-gray-800 p-8 rounded-xl hover:border-gray-600 transition-colors">
          <BookOpen className="w-10 h-10 text-[#e51c24] mx-auto mb-4" />
          <h3 className="text-xl font-bold mb-2">Concept Books</h3>
          <p className="text-gray-400 text-sm">Colored summary books with multi-colored memory techniques.</p>
        </div>
        <div className="bg-gray-900 border border-gray-800 p-8 rounded-xl hover:border-gray-600 transition-colors">
          <Play className="w-10 h-10 text-[#e51c24] mx-auto mb-4" />
          <h3 className="text-xl font-bold mb-2">Video Lectures</h3>
          <p className="text-gray-400 text-sm">Exam-oriented fast track and regular batches.</p>
        </div>
        <div className="bg-gray-900 border border-gray-800 p-8 rounded-xl hover:border-gray-600 transition-colors">
          <CheckCircle2 className="w-10 h-10 text-[#e51c24] mx-auto mb-4" />
          <h3 className="text-xl font-bold mb-2">Test Series</h3>
          <p className="text-gray-400 text-sm">Detailed evaluation by qualified CAs within 48 hours.</p>
        </div>
      </div>

      <button 
        onClick={() => onNav('landing')}
        className="px-8 py-4 bg-[#e51c24] text-white font-bold rounded-xl hover:bg-red-700 transition-colors shadow-lg flex items-center mb-12"
      >
        Take the CA Final Reality Check <span className="ml-2">→</span>
      </button>
    </div>
  </div>
);

const CAFinal = ({ onNav }) => (
  <div className="min-h-screen bg-[#111] text-white flex flex-col font-sans relative">
    <Nav current="CA Final" onNav={onNav} />
    <div className="max-w-6xl mx-auto w-full p-8 py-16">
      <div className="flex flex-col md:flex-row justify-between md:items-end mb-12 border-b border-gray-800 pb-6 gap-4">
        <div>
          <h1 className="text-4xl font-bold text-gray-100 mb-2">CA Final Resources</h1>
          <p className="text-gray-400">Everything you need for the Nov 26 attempt.</p>
        </div>
        <button onClick={() => onNav('landing')} className="bg-[#e51c24] px-6 py-3 rounded-lg font-bold text-sm hover:bg-red-700 transition-colors">Reality Check Assessment</button>
      </div>
      
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {['Financial Reporting (FR)', 'Adv. Financial Management (AFM)', 'Advanced Auditing', 'Direct Tax Laws (DT)', 'Indirect Tax Laws (IDT)', 'IBS (Paper 6)'].map((sub, i) => (
          <div key={i} className="bg-gray-900 border border-gray-800 rounded-xl p-6 hover:border-[#e51c24] transition-colors cursor-pointer group">
            <h3 className="text-lg font-bold text-gray-200 group-hover:text-white mb-4">{sub}</h3>
            <div className="flex gap-3 mt-4">
              <span className="text-xs bg-black px-3 py-1 rounded text-gray-400 border border-gray-800">Lectures</span>
              <span className="text-xs bg-black px-3 py-1 rounded text-gray-400 border border-gray-800">Books</span>
              <span className="text-xs bg-black px-3 py-1 rounded text-gray-400 border border-gray-800">Test Series</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  </div>
);

const About = ({ onNav }) => (
  <div className="min-h-screen bg-[#111] text-white flex flex-col font-sans relative">
    <Nav current="About" onNav={onNav} />
    <div className="flex-1 max-w-4xl mx-auto w-full p-8 py-20 text-center">
      <FastLogo className="mx-auto mb-8 scale-110" />
      <h1 className="text-4xl font-bold mb-6">Empowering CA Students</h1>
      <p className="text-lg text-gray-300 leading-relaxed mb-12">
        At F.A.S.T (First Attempt Success Tutorials), our core mission is simple yet powerful: To ensure every dedicated CA student clears their exams on their very first attempt. 
        We provide meticulously designed study materials, strategic planning, and unwavering mentorship to turn this goal into reality.
      </p>
      
      <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center border-t border-gray-800 pt-12">
        <div>
          <div className="text-4xl font-black text-[#e51c24] mb-2">50K+</div>
          <div className="text-gray-400 text-sm">Students Guided</div>
        </div>
        <div>
          <div className="text-4xl font-black text-[#e51c24] mb-2">100+</div>
          <div className="text-gray-400 text-sm">All India Ranks</div>
        </div>
        <div>
          <div className="text-4xl font-black text-[#e51c24] mb-2">12+</div>
          <div className="text-gray-400 text-sm">Years Experience</div>
        </div>
        <div>
          <div className="text-4xl font-black text-[#e51c24] mb-2">95%</div>
          <div className="text-gray-400 text-sm">Success Rate</div>
        </div>
      </div>
    </div>
  </div>
);

const Contact = ({ onNav }) => (
  <div className="min-h-screen bg-[#111] text-white flex flex-col font-sans relative">
    <Nav current="Contact" onNav={onNav} />
    <div className="flex-1 max-w-5xl mx-auto w-full p-8 py-16 flex flex-col md:flex-row gap-12">
      <div className="flex-1">
        <h1 className="text-4xl font-bold mb-4">Get in Touch</h1>
        <p className="text-gray-400 mb-8">We're here to help you with your CA journey. Reach out to our support team for any queries regarding classes, books, or test series.</p>
        
        <div className="space-y-6">
          <div className="flex items-center">
             <div className="w-12 h-12 bg-gray-900 rounded-full flex items-center justify-center mr-4 text-[#e51c24]">📞</div>
             <div>
               <div className="text-sm text-gray-500">Phone Support</div>
               <div className="font-bold">+91 99999 99999</div>
             </div>
          </div>
          <div className="flex items-center">
             <div className="w-12 h-12 bg-gray-900 rounded-full flex items-center justify-center mr-4 text-[#e51c24]">✉️</div>
             <div>
               <div className="text-sm text-gray-500">Email Us</div>
               <div className="font-bold">support@fast.edu.in</div>
             </div>
          </div>
          <div className="flex items-center">
             <div className="w-12 h-12 bg-gray-900 rounded-full flex items-center justify-center mr-4 text-[#e51c24]">📍</div>
             <div>
               <div className="text-sm text-gray-500">Head Office</div>
               <div className="font-bold text-sm">F.A.S.T Education, Center Point, India</div>
             </div>
          </div>
        </div>
      </div>
      
      <div className="flex-1 bg-gray-900 border border-gray-800 p-8 rounded-xl">
        <h2 className="text-2xl font-bold mb-6">Send a Message</h2>
        <form className="space-y-4" onSubmit={e => e.preventDefault()}>
          <input type="text" placeholder="Your Name" className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none" />
          <input type="email" placeholder="Email Address" className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none" />
          <textarea placeholder="How can we help?" rows="4" className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none"></textarea>
          <button className="w-full bg-[#e51c24] text-white font-bold py-3 rounded-lg hover:bg-red-700 transition-colors">Send Message</button>
        </form>
      </div>
    </div>
  </div>
);


const UserInfoForm = ({ onSubmit, onBack }) => {
  React.useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'instant' });
  }, []);
  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!/^\d{10}$/.test(formData.phone)) {
      alert('Please enter a valid 10-digit mobile number.');
      return;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formData.email)) {
      alert('Please enter a valid email address.');
      return;
    }

    setIsSubmitting(true);
    const scriptURL = 'https://script.google.com/macros/s/AKfycbzlK48p9oZf2f8Y0l437bU9cproU3f3y1Pm8Y8tfHnMxfXMVKbx2cSQNfqu0t7Un23b/exec';
    
    fetch(scriptURL, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain' },
      body: JSON.stringify(formData)
    }).catch(err => console.error(err));
    
    setTimeout(() => {
      setIsSubmitting(false);
      onSubmit(formData);
    }, 400);
  };

  return (
    <div className="min-h-screen bg-[#111] text-white flex flex-col items-center justify-center p-6 font-sans relative overflow-hidden">
      <div className="bg-gray-900 border border-gray-800 p-6 md:p-8 rounded-2xl w-full max-w-md relative z-10 shadow-2xl">
        <FastLogo className="mb-8 scale-90 origin-left" />
        <h2 className="text-2xl font-bold mb-2">Student Details</h2>
        <p className="text-gray-400 mb-6 text-sm">Please enter your details to start the Reality Check. Your report will be saved to our database.</p>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">Full Name</label>
            <input required type="text" value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none transition-colors" placeholder="e.g. Rahul Kumar" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">Contact Number</label>
            <input required type="tel" value={formData.phone} onChange={e => setFormData({...formData, phone: e.target.value})} className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none transition-colors" placeholder="+91 99999 99999" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">Email Address</label>
            <input required type="email" value={formData.email} onChange={e => setFormData({...formData, email: e.target.value})} className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none transition-colors" placeholder="student@example.com" />
          </div>
          
          <div className="pt-4 flex gap-4">
            <button type="button" onClick={onBack} className="flex-1 bg-gray-800 hover:bg-gray-700 text-white font-bold py-3 rounded-lg transition-colors">Back</button>
            <button type="submit" disabled={isSubmitting} className={`flex-1 ${isSubmitting ? 'bg-red-900 cursor-not-allowed' : 'bg-[#e51c24] hover:bg-red-700'} text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20`}>
              {isSubmitting ? 'Starting...' : 'Start Test →'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

// --- APP WRAPPER ---

export default function App() {
  const [step, setStep] = useState('landing');
  const [answers, setAnswers] = useState(null);
  const [userData, setUserData] = useState(null);

  return (
    <>
      {step === 'landing' && <Landing onStart={() => setStep('userForm')} onNav={setStep} />}
      {step === 'Home' && <Home onNav={setStep} />}
      {step === 'CA Final' && <CAFinal onNav={setStep} />}
      {step === 'About' && <About onNav={setStep} />}
      {step === 'Contact' && <Contact onNav={setStep} />}
      
      {step === 'userForm' && (
        <UserInfoForm 
          onBack={() => setStep('landing')}
          onSubmit={(data) => {
            setUserData(data);
            setStep('assessment');
          }} 
        />
      )}

      {step === 'assessment' && (
        <Assessment 
          onComplete={(data) => {
            setAnswers(data);
            setStep('result');
          }} 
        />
      )}
      
      {step === 'result' && <Result answers={answers} userData={userData} onRetake={() => setStep('landing')} />}
    </>
  );
}
