import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# ─────────────────────────────────────────────
# 1. UPDATE SUBJECTS with group info
# ─────────────────────────────────────────────
old_subjects = """const SUBJECTS = [
  { id: 'FR', name: 'Financial Reporting (FR)' },
  { id: 'AFM', name: 'Advanced Financial Management (AFM)' },
  { id: 'Audit', name: 'Audit' },
  { id: 'DT', name: 'Direct Tax (DT)' },
  { id: 'IDT', name: 'Indirect Tax (IDT)' },
  { id: 'IBS', name: 'International Business & Economics (IBS)' }
];"""

new_subjects = """const SUBJECTS = [
  { id: 'FR',    name: 'Financial Reporting (FR)',                  group: 1 },
  { id: 'AFM',   name: 'Advanced Financial Management (AFM)',       group: 1 },
  { id: 'Audit', name: 'Audit',                                     group: 1 },
  { id: 'DT',    name: 'Direct Tax (DT)',                           group: 2 },
  { id: 'IDT',   name: 'Indirect Tax (IDT)',                        group: 2 },
  { id: 'IBS',   name: 'International Business & Economics (IBS)',  group: 2 },
];

const GROUP1_SUBJECTS = SUBJECTS.filter(s => s.group === 1);
const GROUP2_SUBJECTS = SUBJECTS.filter(s => s.group === 2);"""

code = code.replace(old_subjects, new_subjects)

# ─────────────────────────────────────────────
# 2. UPDATE QUESTIONS with meaningful options
# ─────────────────────────────────────────────
old_questions = """const QUESTIONS = [
  {
    id: 1,
    title: 'Your Syllabus Completion',
    subtitle: 'How much syllabus have you completed in each subject?\\n(Select one option for each subject)',
    sidebarTitle: 'Syllabus Status',
    type: 'matrix',
    icon: BookOpen,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: \"Real students face gaps. Winners fix them.\"
  },
  {
    id: 2,
    title: 'Your Revision Status',
    subtitle: 'How many revisions have you completed for each subject?\\n(Select one option for each subject)',
    sidebarTitle: 'Revision Status',
    type: 'matrix',
    icon: RefreshCw,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: \"Progress is a result of honest self-assessment, not wishful thinking.\"
  },
  {
    id: 3,
    title: 'Your Last Mock/Test Performance',
    subtitle: 'What was your most recent mock or test score in each subject?\\n(Select one option for each subject)',
    sidebarTitle: 'Mock/Test Performance',
    type: 'matrix',
    icon: BarChart2,
    options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Below Average)', value: 1 }
    ],
    quote: \"Tests don't define you. They show you what to work on.\"
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
    quote: \"Identifying the leak is the first step to fixing the pipe.\"
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
    quote: \"Exam conditions reveal what casual study conceals.\"
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
    quote: \"Memory is a muscle. Active recall is the workout.\"
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
    quote: \"Don't let yesterday take up too much of today.\"
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
    quote: \"A goal without a plan is just a wish.\"
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
    quote: \"Execution eats strategy for breakfast.\"
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
    quote: \"Confidence comes from discipline and training.\"
  }
];"""

new_questions = """const QUESTIONS = [
  {
    id: 1,
    title: 'Your Syllabus Completion',
    subtitle: 'How much syllabus have you completed in each subject?\\n(Select one option per subject)',
    sidebarTitle: 'Syllabus Status',
    type: 'matrix',
    icon: BookOpen,
    options: [
      { text: 'A  90%+ Done', value: 4 },
      { text: 'B  60–90%', value: 3 },
      { text: 'C  30–60%', value: 2 },
      { text: 'D  <30% Done', value: 1 }
    ],
    quote: \"Real students face gaps. Winners fix them.\"
  },
  {
    id: 2,
    title: 'Your Revision Status',
    subtitle: 'How many full revisions have you completed per subject?\\n(Select one option per subject)',
    sidebarTitle: 'Revision Status',
    type: 'matrix',
    icon: RefreshCw,
    options: [
      { text: 'A  3+ Revisions', value: 4 },
      { text: 'B  2 Revisions', value: 3 },
      { text: 'C  1 Revision', value: 2 },
      { text: 'D  Not Yet', value: 1 }
    ],
    quote: \"Progress is a result of honest self-assessment, not wishful thinking.\"
  },
  {
    id: 3,
    title: 'Your Last Mock / Test Score',
    subtitle: 'What percentage did you score in your most recent mock per subject?\\n(Select one option per subject)',
    sidebarTitle: 'Mock/Test Performance',
    type: 'matrix',
    icon: BarChart2,
    options: [
      { text: 'A  60%+', value: 4 },
      { text: 'B  45–60%', value: 3 },
      { text: 'C  30–45%', value: 2 },
      { text: 'D  <30%', value: 1 }
    ],
    quote: \"Tests don't define you. They show you what to work on.\"
  },
  {
    id: 4,
    title: 'Marks Loss Analysis',
    subtitle: 'Approximately what % of marks do you lose per subject in mocks?\\n(Select one option per subject)',
    sidebarTitle: 'Marks Loss',
    type: 'matrix',
    icon: AlertCircle,
    options: [
      { text: 'A  Rarely (<5%)', value: 4 },
      { text: 'B  Sometimes (5–15%)', value: 3 },
      { text: 'C  Often (15–30%)', value: 2 },
      { text: 'D  Heavily (>30%)', value: 1 }
    ],
    quote: \"Identifying the leak is the first step to fixing the pipe.\"
  },
  {
    id: 5,
    title: 'PYQs, RTPs & MTPs',
    subtitle: 'How much of past papers and ICAI mock series have you solved?\\n(Select one option per subject)',
    sidebarTitle: 'PYQs, RTPs & MTPs',
    type: 'matrix',
    icon: FileText,
    options: [
      { text: 'A  All Done', value: 4 },
      { text: 'B  >50% Done', value: 3 },
      { text: 'C  Just Started', value: 2 },
      { text: 'D  Not Started', value: 1 }
    ],
    quote: \"Exam conditions reveal what casual study conceals.\"
  },
  {
    id: 6,
    title: 'Recall Ability',
    subtitle: 'How easily can you recall key concepts without looking at notes?\\n(Select one option per subject)',
    sidebarTitle: 'Recall Ability',
    type: 'matrix',
    icon: Activity,
    options: [
      { text: 'A  Without Book', value: 4 },
      { text: 'B  Minor Hints', value: 3 },
      { text: 'C  Need Notes', value: 2 },
      { text: 'D  Struggle to Recall', value: 1 }
    ],
    quote: \"Memory is a muscle. Active recall is the workout.\"
  },
  {
    id: 7,
    title: 'Backlog Analysis',
    subtitle: 'How much pending backlog (unfinished chapters) do you have?\\n(Select one option per subject)',
    sidebarTitle: 'Backlog Analysis',
    type: 'matrix',
    icon: AlertTriangle,
    options: [
      { text: 'A  No Backlog', value: 4 },
      { text: 'B  Minor (1–2 ch)', value: 3 },
      { text: 'C  Moderate (3–5 ch)', value: 2 },
      { text: 'D  Heavy (5+ ch)', value: 1 }
    ],
    quote: \"Don't let yesterday take up too much of today.\"
  },
  {
    id: 8,
    title: 'Next 7–10 Days Planning',
    subtitle: 'How clear and detailed is your study plan for the next 7–10 days?',
    sidebarTitle: 'Next 7-10 Days',
    type: 'single',
    icon: Target,
    options: [
      { text: 'A  Full clear daily plan', value: 4 },
      { text: 'B  Rough plan ready', value: 3 },
      { text: 'C  Partially planned', value: 2 },
      { text: 'D  No plan yet', value: 1 }
    ],
    quote: \"A goal without a plan is just a wish.\"
  },
  {
    id: 9,
    title: 'Study Execution',
    subtitle: 'How much of your planned daily study time do you actually complete?',
    sidebarTitle: 'Study Execution',
    type: 'single',
    icon: Play,
    options: [
      { text: 'A  Achieving 80%+ of target', value: 4 },
      { text: 'B  Achieving 60–80%', value: 3 },
      { text: 'C  Achieving 40–60%', value: 2 },
      { text: 'D  Achieving less than 40%', value: 1 }
    ],
    quote: \"Execution eats strategy for breakfast.\"
  },
  {
    id: 10,
    title: 'November Readiness',
    subtitle: 'If the CA Final exam were tomorrow, how ready would you feel overall?',
    sidebarTitle: 'November Readiness',
    type: 'single',
    icon: CheckCircle2,
    options: [
      { text: 'A  Very confident, fully ready', value: 4 },
      { text: 'B  Mostly ready, minor gaps', value: 3 },
      { text: 'C  Some major gaps remain', value: 2 },
      { text: 'D  Not ready at all', value: 1 }
    ],
    quote: \"Confidence comes from discipline and training.\"
  }
];"""

code = code.replace(old_questions, new_questions)

# ─────────────────────────────────────────────
# 3. UPDATE Assessment component signature to accept selectedGroups
# ─────────────────────────────────────────────
code = code.replace(
    "const Assessment = ({ onComplete }) => {",
    "const Assessment = ({ onComplete, selectedGroups }) => {"
)

# ─────────────────────────────────────────────
# 4. Add activeSubjects derived variable right after useState in Assessment
# ─────────────────────────────────────────────
code = code.replace(
    "  const [answers, setAnswers] = useState({}); // { qId: { FR: val, AFM: val... } or single value }",
    """  const [answers, setAnswers] = useState({}); // { qId: { FR: val, AFM: val... } or single value }

  // Only show subjects from selected groups
  const activeSubjects = SUBJECTS.filter(s => selectedGroups.includes(s.group));"""
)

# ─────────────────────────────────────────────
# 5. Fix canProceed to use activeSubjects
# ─────────────────────────────────────────────
code = code.replace(
    "      return SUBJECTS.every(s => qAns[s.id] !== undefined);",
    "      return activeSubjects.every(s => qAns[s.id] !== undefined);"
)

# ─────────────────────────────────────────────
# 6. Fix tbody to use grouped subject rendering with group headers
# ─────────────────────────────────────────────
old_tbody = """                <tbody>
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
                </tbody>"""

new_tbody = """                <tbody>
                  {(() => {
                    const rows = [];
                    const showBoth = selectedGroups.includes(1) && selectedGroups.includes(2);
                    [1, 2].forEach(grp => {
                      if (!selectedGroups.includes(grp)) return;
                      if (showBoth) {
                        rows.push(
                          <tr key={`grp-header-${grp}`} className="bg-[#1a2b4b]">
                            <td colSpan={question.options.length + 1} className="px-3 py-1.5 text-[10px] md:text-xs font-bold text-white uppercase tracking-widest">
                              Group {grp} — {grp === 1 ? 'FR · AFM · Audit' : 'DT · IDT · IBS'}
                            </td>
                          </tr>
                        );
                      }
                      SUBJECTS.filter(s => s.group === grp).forEach((subject) => {
                        const row = (
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
                        );
                        rows.push(row);
                      });
                    });
                    return rows;
                  })()}
                </tbody>"""

code = code.replace(old_tbody, new_tbody)

# ─────────────────────────────────────────────
# 7. Add group selection to UserInfoForm  
# ─────────────────────────────────────────────
# Find the UserInfoForm component and update it to include group selection
old_userform_state = "  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });"
new_userform_state = """  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });
  const [selectedGroups, setSelectedGroups] = useState([1, 2]);

  const toggleGroup = (grp) => {
    setSelectedGroups(prev => {
      if (prev.includes(grp)) {
        if (prev.length === 1) return prev; // must have at least one
        return prev.filter(g => g !== grp);
      }
      return [...prev, grp].sort();
    });
  };"""

code = code.replace(old_userform_state, new_userform_state)

# Fix UserInfoForm signature to also pass selectedGroups on submit  
old_userform_submit = "    onSubmit(formData);"
new_userform_submit = "    onSubmit({ ...formData, selectedGroups });"
code = code.replace(old_userform_submit, new_userform_submit)

# Add the group picker UI inside UserInfoForm after email field, before submit buttons
old_email_div_end = """          </div>
          
          <div className="pt-4 flex gap-4">"""

new_email_div_end = """          </div>

          {/* Group Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">Which CA Final Group are you appearing for?</label>
            <div className="flex gap-3">
              {[1, 2].map(grp => (
                <button
                  key={grp}
                  type="button"
                  onClick={() => toggleGroup(grp)}
                  className={`flex-1 py-3 px-4 rounded-lg border-2 font-bold text-sm transition-all ${
                    selectedGroups.includes(grp)
                      ? 'border-[#e51c24] bg-[#e51c24] text-white'
                      : 'border-gray-600 bg-gray-800 text-gray-300 hover:border-gray-400'
                  }`}
                >
                  Group {grp}
                  <div className="text-[10px] font-normal mt-0.5 opacity-80">
                    {grp === 1 ? 'FR · AFM · Audit' : 'DT · IDT · IBS'}
                  </div>
                </button>
              ))}
            </div>
            <p className="text-gray-500 text-xs mt-1.5">Select one or both groups. You can fill only your selected group(s).</p>
          </div>
          
          <div className="pt-4 flex gap-4">"""

code = code.replace(old_email_div_end, new_email_div_end)

# ─────────────────────────────────────────────
# 8. Pass selectedGroups from App → Assessment
# ─────────────────────────────────────────────
old_app_state = """  const [step, setStep] = useState('landing');
  const [answers, setAnswers] = useState(null);
  const [userData, setUserData] = useState(null);"""

new_app_state = """  const [step, setStep] = useState('landing');
  const [answers, setAnswers] = useState(null);
  const [userData, setUserData] = useState(null);
  const [selectedGroups, setSelectedGroups] = useState([1, 2]);"""

code = code.replace(old_app_state, new_app_state)

old_userform_onsubmit = """          onSubmit={(data) => {
            setUserData(data);
            setStep('assessment');
          }}"""
new_userform_onsubmit = """          onSubmit={(data) => {
            const { selectedGroups: grps, ...rest } = data;
            setUserData(rest);
            setSelectedGroups(grps || [1, 2]);
            setStep('assessment');
          }}"""
code = code.replace(old_userform_onsubmit, new_userform_onsubmit)

old_assessment_tag = """        <Assessment 
          onComplete={(data) => {
            setAnswers(data);
            setStep('result');
          }} 
        />"""
new_assessment_tag = """        <Assessment 
          selectedGroups={selectedGroups}
          onComplete={(data) => {
            setAnswers(data);
            setStep('result');
          }} 
        />"""
code = code.replace(old_assessment_tag, new_assessment_tag)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done! All changes applied.")
