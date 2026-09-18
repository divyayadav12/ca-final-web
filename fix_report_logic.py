import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Insert overallStat computation right before "// Strongest / Weakest"
stat_logic = """  const finalPerc = Math.round((finalScore / 40) * 100);

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

  // Strongest / Weakest"""
code = code.replace("  const finalPerc = Math.round((finalScore / 40) * 100);\n\n  // Strongest / Weakest", stat_logic)


# 2. Replace the Overall Score render block
old_overall_html = """            {/* Overall Score */}
            <div className="md:col-span-4 bg-white p-6 rounded-2xl shadow-sm border border-gray-200 flex flex-col relative overflow-hidden">
              <div className="text-sm font-bold text-[#1a2b4b] mb-2">Overall Score</div>
              <div className="flex items-baseline mb-2">
                <span className="text-5xl font-black text-[#e51c24]">{finalScore}</span>
                <span className="text-2xl font-bold text-gray-400 ml-1">/ 40</span>
              </div>
              <div className="flex items-center gap-4 mb-4">
                <div className="flex-1 bg-red-100 h-2.5 rounded-full overflow-hidden">
                  <div className="bg-[#e51c24] h-full" style={{ width: `${finalPerc}%` }}></div>
                </div>
                <span className="font-bold text-[#e51c24] text-sm">{finalPerc}%</span>
              </div>
              <div className="bg-[#fff1f2] text-[#e51c24] text-sm font-bold px-3 py-1.5 rounded w-fit mb-4 flex items-center border border-red-100">
                <AlertCircle className="w-4 h-4 mr-1.5" /> NEEDS CORRECTION
              </div>
              <p className="text-gray-600 text-sm leading-relaxed mb-4 flex-1">
                Good progress, but important gaps need attention. Now is the time to fix them and get on track.
              </p>
              <p className="text-xs text-gray-400 italic">"You're not far, you just need<br/>a sharper plan." <span className="float-right">— Team FAST</span></p>
            </div>"""

new_overall_html = """            {/* Overall Score */}
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
            </div>"""

code = code.replace(old_overall_html, new_overall_html)


# 3. Replace the Highlights render block
old_highlights_html = """              {/* Highlights */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 flex-1">
                <div className="bg-white p-5 rounded-2xl shadow-sm border border-gray-200 flex items-start">
                  <div className="bg-green-100 p-3 rounded-xl mr-4 text-[#16a34a]">
                    <Trophy className="w-8 h-8" />
                  </div>
                  <div>
                    <div className="text-xs font-bold text-gray-500 mb-1">Your Strongest Subject</div>
                    <div className="text-xl font-bold text-[#1a2b4b] mb-1">{strongest.name.split(' (')[0]}</div>
                    <div className="text-sm text-gray-600 mb-2">({Math.round((strongest.score / 4)*100)}% overall readiness)</div>
                    <div className="text-sm font-semibold text-[#16a34a]">Keep the momentum!</div>
                  </div>
                </div>
                
                <div className="bg-white p-5 rounded-2xl shadow-sm border border-gray-200 flex items-start border-l-4 border-l-[#e51c24]">
                  <div className="bg-red-100 p-3 rounded-xl mr-4 text-[#e51c24]">
                    <AlertTriangle className="w-8 h-8" />
                  </div>
                  <div>
                    <div className="text-xs font-bold text-gray-500 mb-1">Your Biggest Gap</div>
                    <div className="text-xl font-bold text-[#1a2b4b] mb-1">{weakest.name}</div>
                    <div className="text-sm text-gray-600 mb-2">Needs immediate action</div>
                    <div className="text-sm font-semibold text-[#e51c24]">Prioritise this subject in your next 30 days.</div>
                  </div>
                </div>
              </div>"""

new_highlights_html = """              {/* Highlights */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 flex-1">
                <div className="bg-white p-5 rounded-2xl shadow-sm border border-gray-200 flex items-start border-l-4 border-l-[#16a34a]">
                  <div className="bg-green-100 p-3 rounded-xl mr-4 text-[#16a34a]">
                    <Trophy className="w-8 h-8" />
                  </div>
                  <div>
                    <div className="text-xs font-bold text-gray-500 mb-1">Your Strongest Subject</div>
                    <div className="text-xl font-bold text-[#1a2b4b] mb-1">{strongest.name.split(' (')[0]}</div>
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
                      <div className="text-xl font-bold text-[#1a2b4b] mb-1">{weakest.name}</div>
                      <div className="text-sm text-gray-600 mb-2">Needs immediate action</div>
                      <div className="text-sm font-semibold text-[#e51c24]">Prioritise this subject in your next 30 days.</div>
                    </div>
                  </div>
                )}
              </div>"""

code = code.replace(old_highlights_html, new_highlights_html)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
