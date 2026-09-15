import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Add activeTab state to Result component
code = re.sub(
    r'(const Result = \(\{ answers, onRetake \}\) => \{)',
    r'\1\n  const [activeTab, setActiveTab] = useState(\'Overview\');',
    code
)

# Replace the sidebar buttons with active state logic
old_sidebar = '''<div className="flex-1 px-4 py-6 space-y-2">
            <button className="w-full text-left px-4 py-3 rounded-lg text-sm font-semibold bg-[#1a2b4b] text-white">Dashboard Overview</button>
            <button className="w-full text-left px-4 py-3 rounded-lg text-sm font-semibold text-gray-400 hover:text-white hover:bg-gray-800 transition-colors">Subject-wise Analysis</button>
            <button className="w-full text-left px-4 py-3 rounded-lg text-sm font-semibold text-gray-400 hover:text-white hover:bg-gray-800 transition-colors">Detailed Insights</button>
            <button className="w-full text-left px-4 py-3 rounded-lg text-sm font-semibold text-gray-400 hover:text-white hover:bg-gray-800 transition-colors">Your Action Plan</button>
          </div>'''

new_sidebar = '''<div className="flex-1 px-4 py-6 space-y-2">
            <button onClick={() => setActiveTab('Overview')} className={w-full text-left px-4 py-3 rounded-lg text-sm font-semibold transition-colors }>Dashboard Overview</button>
            <button onClick={() => setActiveTab('Subject-wise Analysis')} className={w-full text-left px-4 py-3 rounded-lg text-sm font-semibold transition-colors }>Subject-wise Analysis</button>
            <button onClick={() => setActiveTab('Detailed Insights')} className={w-full text-left px-4 py-3 rounded-lg text-sm font-semibold transition-colors }>Detailed Insights</button>
            <button onClick={() => setActiveTab('Your Action Plan')} className={w-full text-left px-4 py-3 rounded-lg text-sm font-semibold transition-colors }>Your Action Plan</button>
          </div>'''

code = code.replace(old_sidebar, new_sidebar)

# Add conditional rendering around the existing Dashboard Overview content
# The existing content is inside <div className="flex-1 flex flex-col gap-6">
# and starts with <!-- Top Row --> or similar. We need to wrap it.
content_area_match = re.search(r'(<div className="flex-1 flex flex-col gap-6">)(.*?)(?=</main>)', code, re.DOTALL)
if content_area_match:
    old_content = content_area_match.group(2)
    # Wrap the old content
    new_content = """
          {activeTab === 'Overview' && (
            <>
""" + old_content.strip() + """
            </>
          )}

          {activeTab === 'Subject-wise Analysis' && (
            <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 md:p-8">
              <h2 className="text-2xl font-bold text-[#1a2b4b] mb-6 border-b border-gray-100 pb-4">Subject-wise Analysis</h2>
              <div className="space-y-8">
                {subjectScores.map((sub, i) => (
                  <div key={i} className="border border-gray-100 rounded-xl p-6 bg-gray-50/50 hover:shadow-md transition-shadow">
                    <div className="flex justify-between items-center mb-4">
                      <h3 className="text-lg font-bold text-gray-800">{sub.name}</h3>
                      <div className="font-bold text-lg text-[#1a2b4b]">{Math.round((sub.score / 4) * 100)}%</div>
                    </div>
                    
                    {/* Progress Bar */}
                    <div className="w-full bg-gray-200 rounded-full h-3 mb-6">
                      <div className={h-3 rounded-full } style={{width: ${Math.round((sub.score / 4) * 100)}%}}></div>
                    </div>

                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                      <div className="bg-white p-3 rounded-lg border border-gray-100 shadow-sm text-center">
                        <div className="text-[10px] uppercase text-gray-500 font-bold mb-1">Syllabus</div>
                        <div className="text-sm font-semibold">{mapOptText(1, sub.syl)}</div>
                      </div>
                      <div className="bg-white p-3 rounded-lg border border-gray-100 shadow-sm text-center">
                        <div className="text-[10px] uppercase text-gray-500 font-bold mb-1">Revision</div>
                        <div className="text-sm font-semibold">{mapOptText(2, sub.rev)}</div>
                      </div>
                      <div className="bg-white p-3 rounded-lg border border-gray-100 shadow-sm text-center">
                        <div className="text-[10px] uppercase text-gray-500 font-bold mb-1">Last Mock</div>
                        <div className="text-sm font-semibold">{mapOptText(3, sub.mock)}</div>
                      </div>
                      <div className="bg-white p-3 rounded-lg border border-gray-100 shadow-sm text-center">
                        <div className="text-[10px] uppercase text-gray-500 font-bold mb-1">Practice</div>
                        <div className="text-sm font-semibold">{mapOptText(5, sub.prac)}</div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeTab === 'Detailed Insights' && (
            <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 md:p-8">
              <h2 className="text-2xl font-bold text-[#1a2b4b] mb-6 border-b border-gray-100 pb-4">Detailed Insights</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="bg-gray-50 p-6 rounded-xl border border-gray-100">
                  <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center"><Target className="w-5 h-5 mr-2 text-[#e51c24]"/> Overall Preparedness</h3>
                  <p className="text-gray-600 leading-relaxed mb-4">
                    Based on your self-assessment, your overall preparedness sits at <span className="font-bold text-[#1a2b4b]">{Math.round((totalScore / 40) * 100)}%</span>. 
                    Your strongest pillar is <b>{sylCov > examPrac ? "Syllabus Coverage" : "Exam Practice"}</b>.
                  </p>
                  <p className="text-gray-600 leading-relaxed">
                    You need to focus immediately on bringing your weaker subjects up to par, specifically <b>{weakest.name}</b>, which requires immediate attention to avoid cascading effects on your overall aggregate.
                  </p>
                </div>
                
                <div className="bg-gray-50 p-6 rounded-xl border border-gray-100">
                  <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center"><AlertTriangle className="w-5 h-5 mr-2 text-amber-500"/> Critical Gaps</h3>
                  <ul className="space-y-3">
                    <li className="flex items-start">
                      <div className="w-2 h-2 rounded-full bg-red-500 mt-2 mr-2"></div>
                      <p className="text-sm text-gray-600">Lack of mock tests given in the last 30 days for practical subjects.</p>
                    </li>
                    <li className="flex items-start">
                      <div className="w-2 h-2 rounded-full bg-red-500 mt-2 mr-2"></div>
                      <p className="text-sm text-gray-600">Revision backlog in Audit and DT.</p>
                    </li>
                    <li className="flex items-start">
                      <div className="w-2 h-2 rounded-full bg-amber-500 mt-2 mr-2"></div>
                      <p className="text-sm text-gray-600">PYQs and RTPs are only partially complete for Group 1.</p>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'Your Action Plan' && (
            <div className="bg-white rounded-2xl shadow-sm border border-gray-200 p-6 md:p-8">
              <h2 className="text-2xl font-bold text-[#1a2b4b] mb-6 border-b border-gray-100 pb-4">Your 30-Day Action Plan</h2>
              
              <div className="relative border-l-2 border-gray-200 ml-4 space-y-8 pb-4">
                
                <div className="relative pl-8">
                  <div className="absolute w-6 h-6 bg-[#1a2b4b] rounded-full left-[-13px] top-0 border-4 border-white flex items-center justify-center text-white text-[10px] font-bold">1</div>
                  <h3 className="text-lg font-bold text-gray-800 mb-2">Phase 1: Clear the Backlog (Days 1-10)</h3>
                  <ul className="text-sm text-gray-600 space-y-2 list-disc ml-4">
                    <li>Focus 70% of your time on <b>{weakest.name}</b>.</li>
                    <li>Complete all pending lectures and summarize notes.</li>
                    <li>Start a 1-hour daily cumulative revision for <b>{strongest.name.split(' (')[0]}</b> to keep it fresh.</li>
                  </ul>
                </div>

                <div className="relative pl-8">
                  <div className="absolute w-6 h-6 bg-amber-500 rounded-full left-[-13px] top-0 border-4 border-white flex items-center justify-center text-white text-[10px] font-bold">2</div>
                  <h3 className="text-lg font-bold text-gray-800 mb-2">Phase 2: Aggressive Practice (Days 11-20)</h3>
                  <ul className="text-sm text-gray-600 space-y-2 list-disc ml-4">
                    <li>Solve at least 2 full RTPs for every subject.</li>
                    <li>For practical subjects (FR, AFM), solve questions manually without looking at solutions.</li>
                    <li>Book your first full mock test series.</li>
                  </ul>
                </div>

                <div className="relative pl-8">
                  <div className="absolute w-6 h-6 bg-[#e51c24] rounded-full left-[-13px] top-0 border-4 border-white flex items-center justify-center text-white text-[10px] font-bold">3</div>
                  <h3 className="text-lg font-bold text-gray-800 mb-2">Phase 3: Mock & Analyze (Days 21-30)</h3>
                  <ul className="text-sm text-gray-600 space-y-2 list-disc ml-4">
                    <li>Give 1 mock test every alternate day.</li>
                    <li>Spend 3 hours analyzing each mock test to identify silly mistakes.</li>
                    <li>Review handwritten summary notes exclusively. Avoid opening main modules.</li>
                  </ul>
                </div>

              </div>
              
              <div className="mt-8 bg-gray-50 p-4 rounded-xl border border-gray-200 text-center">
                 <p className="italic text-gray-600">"Success in CA Final is not about reading everything, it's about remembering and executing what you've read."</p>
              </div>
            </div>
          )}
"""
    code = code.replace(content_area_match.group(0), content_area_match.group(1) + new_content)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patched successfully")
