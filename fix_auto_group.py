with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# ─────────────────────────────────────────────
# 1. Remove selectedGroups state + toggleGroup from UserInfoForm
# ─────────────────────────────────────────────
old_uf_state = """  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });
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

new_uf_state = "  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });"
code = code.replace(old_uf_state, new_uf_state)

# ─────────────────────────────────────────────
# 2. Remove selectedGroups from submit call in UserInfoForm
# ─────────────────────────────────────────────
code = code.replace(
    "      onSubmit({ ...formData, selectedGroups });",
    "      onSubmit(formData);"
)

# ─────────────────────────────────────────────
# 3. Remove Group Selection UI block from UserInfoForm
# ─────────────────────────────────────────────
old_group_ui = """
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
          """
new_group_ui = "\n          "
code = code.replace(old_group_ui, new_group_ui)

# ─────────────────────────────────────────────
# 4. Remove selectedGroups from App state
# ─────────────────────────────────────────────
code = code.replace(
    "  const [selectedGroups, setSelectedGroups] = useState([1, 2]);\n",
    ""
)

# ─────────────────────────────────────────────
# 5. Fix App's onSubmit to not extract selectedGroups
# ─────────────────────────────────────────────
old_app_submit = """          onSubmit={(data) => {
            const { selectedGroups: grps, ...rest } = data;
            setUserData(rest);
            setSelectedGroups(grps || [1, 2]);
            setStep('assessment');
          }}"""
new_app_submit = """          onSubmit={(data) => {
            setUserData(data);
            setStep('assessment');
          }}"""
code = code.replace(old_app_submit, new_app_submit)

# ─────────────────────────────────────────────
# 6. Remove selectedGroups prop from Assessment in App
# ─────────────────────────────────────────────
old_assessment_tag = """        <Assessment 
          selectedGroups={selectedGroups}
          onComplete={(data) => {
            setAnswers(data);
            setStep('result');
          }} 
        />"""
new_assessment_tag = """        <Assessment 
          onComplete={(data) => {
            setAnswers(data);
            setStep('result');
          }} 
        />"""
code = code.replace(old_assessment_tag, new_assessment_tag)

# ─────────────────────────────────────────────
# 7. Fix Assessment component - remove selectedGroups prop + activeSubjects
# ─────────────────────────────────────────────
code = code.replace(
    "const Assessment = ({ onComplete, selectedGroups }) => {",
    "const Assessment = ({ onComplete }) => {"
)

old_active_subjects = """  // Only show subjects from selected groups
  const activeSubjects = SUBJECTS.filter(s => selectedGroups.includes(s.group));"""
code = code.replace(old_active_subjects, "")

# ─────────────────────────────────────────────
# 8. Fix canProceed - auto-detect: at least one group fully answered
# ─────────────────────────────────────────────
old_can_proceed = """  const canProceed = () => {
    const qAns = answers[question.id];
    if (question.type === 'matrix') {
      if (!qAns) return false;
      return activeSubjects.every(s => qAns[s.id] !== undefined);
    } else {
      return qAns !== undefined;
    }
  };"""

new_can_proceed = """  const canProceed = () => {
    const qAns = answers[question.id];
    if (question.type === 'matrix') {
      if (!qAns) return false;
      const g1Done = GROUP1_SUBJECTS.every(s => qAns[s.id] !== undefined);
      const g2Done = GROUP2_SUBJECTS.every(s => qAns[s.id] !== undefined);
      return g1Done || g2Done;
    } else {
      return qAns !== undefined;
    }
  };"""
code = code.replace(old_can_proceed, new_can_proceed)

# ─────────────────────────────────────────────
# 9. Fix tbody - always show all 6 subjects with group separators, no selectedGroups filtering
# ─────────────────────────────────────────────
old_tbody = """                <tbody>
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

new_tbody = """                <tbody>
                  {[1, 2].map(grp => {
                    const grpSubjects = SUBJECTS.filter(s => s.group === grp);
                    const grpDone = grpSubjects.every(s => answers[question.id]?.[s.id] !== undefined);
                    return (
                      <React.Fragment key={grp}>
                        <tr className={`${grpDone ? 'bg-green-700' : 'bg-[#1a2b4b]'} transition-colors`}>
                          <td colSpan={question.options.length + 1} className="px-3 py-1.5 text-[10px] md:text-xs font-bold text-white uppercase tracking-widest">
                            Group {grp} — {grp === 1 ? 'FR · AFM · Audit' : 'DT · IDT · IBS'}
                            {grpDone && <span className="ml-2 normal-case font-normal opacity-80">✓ Complete</span>}
                          </td>
                        </tr>
                        {grpSubjects.map((subject) => (
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
                      </React.Fragment>
                    );
                  })}
                </tbody>"""

code = code.replace(old_tbody, new_tbody)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done!")
