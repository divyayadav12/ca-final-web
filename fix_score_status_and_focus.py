with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update getStatus function
old_get_status = """  const getStatus = (perc) => {
    if (perc >= 75) return { text: "Good", color: "text-[#16a34a]" };
    if (perc >= 50) return { text: "Needs Work", color: "text-[#e51c24]" };
    return { text: "Needs Correction", color: "text-[#e51c24]" };
  };"""

new_get_status = """  const getStatus = (perc) => {
    if (perc >= 90) return { text: "Excellent", color: "text-[#16a34a]", bg: "bg-green-50", border: "border-green-200" };
    if (perc >= 80) return { text: "Better", color: "text-[#059669]", bg: "bg-emerald-50", border: "border-emerald-200" };
    if (perc >= 65) return { text: "Good", color: "text-[#0284c7]", bg: "bg-sky-50", border: "border-sky-200" };
    if (perc >= 50) return { text: "Average", color: "text-[#d97706]", bg: "bg-amber-50", border: "border-amber-200" };
    return { text: "Below Average", color: "text-[#e51c24]", bg: "bg-red-50", border: "border-red-200" };
  };"""

assert old_get_status in code, "old_get_status not found!"
code = code.replace(old_get_status, new_get_status)

# 2. Update the Category Wise Score rendering to use the dynamic colors
old_cat_score = """                    const stat = getStatus(cat.score);
                    return (
                      <div key={i} className="flex flex-col items-center text-center p-3 border border-gray-100 rounded-xl hover:shadow-md transition-shadow">
                        <cat.icon className={`w-8 h-8 mb-2 ${stat.color === 'text-[#16a34a]' ? 'text-[#16a34a]' : 'text-[#e51c24]'}`} strokeWidth={1.5} />
                        <div className="text-xs font-semibold text-gray-500 whitespace-pre-line leading-tight mb-2 h-8">{cat.label}</div>
                        <div className="text-xl font-black text-[#1a2b4b] mb-1">{cat.score}%</div>
                        <div className={`text-[10px] font-bold uppercase tracking-wider ${stat.color} bg-gray-50 px-2 py-1 rounded w-full border border-gray-100`}>
                          {stat.text}
                        </div>
                      </div>
                    )"""

new_cat_score = """                    const stat = getStatus(cat.score);
                    return (
                      <div key={i} className="flex flex-col items-center text-center p-3 border border-gray-100 rounded-xl hover:shadow-md transition-shadow">
                        <cat.icon className={`w-8 h-8 mb-2 ${stat.color}`} strokeWidth={1.5} />
                        <div className="text-xs font-semibold text-gray-500 whitespace-pre-line leading-tight mb-2 h-8">{cat.label}</div>
                        <div className="text-xl font-black text-[#1a2b4b] mb-1">{cat.score}%</div>
                        <div className={`text-[10px] font-bold uppercase tracking-wider ${stat.color} ${stat.bg} px-2 py-1 rounded w-full border ${stat.border}`}>
                          {stat.text}
                        </div>
                      </div>
                    )"""

assert old_cat_score in code, "old_cat_score not found!"
code = code.replace(old_cat_score, new_cat_score)

# 3. Update Strongest and Weakest calculation & rendering
old_strongest_weakest_calc = """  // Strongest / Weakest
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
  }"""

new_strongest_weakest_calc = """  // Strongest / Weakest
  const sortedSubjects = [...subjectScores].sort((a, b) => b.score - a.score);
  const strongest = sortedSubjects[0] || { score: 0, name: '-' };
  const weakest = sortedSubjects[sortedSubjects.length - 1] || { score: 0, name: '-' };
  
  const highestScore = strongest.score;
  const lowestScore = weakest.score;
  const isAllTie = (highestScore === lowestScore);

  const strongestList = sortedSubjects.filter(s => s.score === highestScore);
  let strongestName = strongestList[0]?.name.split(' (')[0] || '-';
  if (isAllTie && sortedSubjects.length > 1) {
    strongestName = 'All Subjects (Tie)';
  } else if (strongestList.length > 1) {
    strongestName = strongestName + ' & ' + (strongestList.length - 1) + ' more';
  }

  const weakestList = sortedSubjects.filter(s => s.score === lowestScore);
  let weakestName = weakestList[0]?.name.split(' (')[0] || '-';
  if (isAllTie && sortedSubjects.length > 1) {
    weakestName = 'All Subjects (Tie)';
  } else if (weakestList.length > 1) {
    weakestName = weakestName + ' & ' + (weakestList.length - 1) + ' more';
  }"""

assert old_strongest_weakest_calc in code, "old_strongest_weakest_calc not found!"
code = code.replace(old_strongest_weakest_calc, new_strongest_weakest_calc)

# 4. Update Area of Focus / Weakest card rendering
old_focus_card = """                {weakest.score >= 3.5 ? (
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
                )}"""

new_focus_card = """                {isAllTie && highestScore === 4 ? (
                  <div className="bg-white p-5 rounded-2xl shadow-sm border border-gray-200 flex items-start border-l-4 border-l-[#16a34a]">
                    <div className="bg-green-100 p-3 rounded-xl mr-4 text-[#16a34a]">
                      <CheckCircle2 className="w-8 h-8" />
                    </div>
                    <div>
                      <div className="text-xs font-bold text-gray-500 mb-1">Area of Focus</div>
                      <div className="text-xl font-bold text-[#1a2b4b] mb-1">All Subjects Strong!</div>
                      <div className="text-sm text-gray-600 mb-2">You have 100% readiness across all subjects.</div>
                      <div className="text-sm font-semibold text-[#16a34a]">Keep revising consistently.</div>
                    </div>
                  </div>
                ) : (
                  <div className={`bg-white p-5 rounded-2xl shadow-sm border border-gray-200 flex items-start border-l-4 ${weakest.score >= 3.0 ? 'border-l-[#f59e0b]' : 'border-l-[#e51c24]'}`}>
                    <div className={`p-3 rounded-xl mr-4 ${weakest.score >= 3.0 ? 'bg-amber-100 text-[#f59e0b]' : 'bg-red-100 text-[#e51c24]'}`}>
                      {weakest.score >= 3.0 ? <AlertCircle className="w-8 h-8" /> : <AlertTriangle className="w-8 h-8" />}
                    </div>
                    <div>
                      <div className="text-xs font-bold text-gray-500 mb-1">
                        {weakest.score >= 3.0 ? 'Subject Needing Focus' : 'Your Biggest Gap'}
                      </div>
                      <div className="text-xl font-bold text-[#1a2b4b] mb-1">{weakestName}</div>
                      <div className="text-sm text-gray-600 mb-2">({Math.round((weakest.score / 4) * 100)}% overall readiness)</div>
                      <div className={`text-sm font-semibold ${weakest.score >= 3.0 ? 'text-[#f59e0b]' : 'text-[#e51c24]'}`}>
                        {weakest.score >= 3.0 
                          ? 'Prioritise this subject to secure 60+ exemption.' 
                          : 'Prioritise this subject in your next 30 days.'}
                      </div>
                    </div>
                  </div>
                )}"""

assert old_focus_card in code, "old_focus_card not found!"
code = code.replace(old_focus_card, new_focus_card)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated score statuses and lowest subject focus!")
