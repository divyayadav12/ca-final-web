import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_block = """              <div className="space-y-4 flex-1">
                {[
                  `Complete pending syllabus in ${weakest.id} on priority.`,
                  `Start structured revision, especially for ${sortedSubjects[sortedSubjects.length-2]?.id || 'weaker subjects'}.`,
                  `Solve and analyse PYQs, RTPs and MTPs regularly.`,
                  `Give at least 2 timed mocks in the next 15 days.`,
                  `Follow a fixed study plan and track your daily targets.`
                ].map((step, i) => (
                  <div key={i} className="flex items-start">
                    <div className="w-6 h-6 rounded-full bg-[#e51c24] text-white flex items-center justify-center text-xs font-bold mr-3 shrink-0 mt-0.5">
                      {i + 1}
                    </div>
                    <p className="text-sm text-gray-700 font-medium leading-relaxed">{step}</p>
                  </div>
                ))}
              </div>"""

new_block = """              <div className="space-y-4 flex-1">
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
              </div>"""

code = code.replace(old_block, new_block)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
