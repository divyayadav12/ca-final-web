with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# ─────────────────────────────────────────────
# 1. Fix subjectScores — only include subjects that were actually answered
# ─────────────────────────────────────────────
old_subject_scores = """  // Calculate average per subject
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
  });"""

new_subject_scores = """  // Determine which subjects were actually answered by the candidate
  const answeredSubjectIds = new Set();
  QUESTIONS.forEach(q => {
    if (q.type === 'matrix' && answers[q.id]) {
      Object.keys(answers[q.id]).forEach(id => answeredSubjectIds.add(id));
    }
  });

  // Calculate average per subject — only for answered subjects
  const subjectScores = SUBJECTS.filter(s => answeredSubjectIds.has(s.id)).map(sub => {
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
  });"""

code = code.replace(old_subject_scores, new_subject_scores)

# ─────────────────────────────────────────────
# 2. Add "Connect with FAST" section right after "Next Steps" block closing div (line ~893)
# Replace the closing of next steps card to include FAST CTA card below it
# ─────────────────────────────────────────────
old_end = """              <button className="w-full bg-[#e51c24] hover:bg-red-700 text-white font-bold py-4 rounded-xl flex items-center justify-center transition-colors shadow-lg shadow-red-500/20">
                Keep Going, You Can Do This! <span className="ml-2">→</span>
              </button>
            </div>

          </div>
        </div>
      </main>
    </div>
  );
};"""

new_end = """              <button className="w-full bg-[#e51c24] hover:bg-red-700 text-white font-bold py-4 rounded-xl flex items-center justify-center transition-colors shadow-lg shadow-red-500/20">
                Keep Going, You Can Do This! <span className="ml-2">→</span>
              </button>
            </div>

            {/* Connect with FAST */}
            <div className="bg-[#111] rounded-2xl shadow-sm border border-gray-800 p-6 mt-0">
              <div className="flex items-center mb-5">
                <FastLogo className="max-w-[100px]" />
                <div className="ml-4">
                  <div className="text-white font-black text-lg leading-tight">Your Next Step</div>
                  <div className="text-gray-400 text-sm font-medium">Connect with F.A.S.T. and get expert guidance</div>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-5">
                <a href="tel:+919584510000" className="flex items-center bg-gray-900 border border-gray-700 rounded-xl p-4 hover:border-[#e51c24] transition-colors group">
                  <div className="w-10 h-10 rounded-full bg-[#e51c24] flex items-center justify-center mr-3 shrink-0">
                    <Phone className="w-5 h-5 text-white" />
                  </div>
                  <div>
                    <div className="text-gray-400 text-xs font-medium mb-0.5">Call Us</div>
                    <div className="text-white font-bold text-sm group-hover:text-[#e51c24] transition-colors">+91 9584510000</div>
                  </div>
                </a>

                <a href="mailto:faststudentcare@gmail.com" className="flex items-center bg-gray-900 border border-gray-700 rounded-xl p-4 hover:border-[#e51c24] transition-colors group">
                  <div className="w-10 h-10 rounded-full bg-[#e51c24] flex items-center justify-center mr-3 shrink-0">
                    <Mail className="w-5 h-5 text-white" />
                  </div>
                  <div>
                    <div className="text-gray-400 text-xs font-medium mb-0.5">Email Us</div>
                    <div className="text-white font-bold text-sm group-hover:text-[#e51c24] transition-colors">faststudentcare@gmail.com</div>
                  </div>
                </a>

                <a href="https://www.fast.edu.in/" target="_blank" rel="noreferrer" className="flex items-center bg-gray-900 border border-gray-700 rounded-xl p-4 hover:border-[#e51c24] transition-colors group">
                  <div className="w-10 h-10 rounded-full bg-[#e51c24] flex items-center justify-center mr-3 shrink-0">
                    <Globe className="w-5 h-5 text-white" />
                  </div>
                  <div>
                    <div className="text-gray-400 text-xs font-medium mb-0.5">Website</div>
                    <div className="text-white font-bold text-sm group-hover:text-[#e51c24] transition-colors">www.fast.edu.in</div>
                  </div>
                </a>

                <div className="flex items-center bg-gray-900 border border-gray-700 rounded-xl p-4">
                  <div className="w-10 h-10 rounded-full bg-[#e51c24] flex items-center justify-center mr-3 shrink-0">
                    <MapPin className="w-5 h-5 text-white" />
                  </div>
                  <div>
                    <div className="text-gray-400 text-xs font-medium mb-0.5">Address</div>
                    <div className="text-white text-xs leading-snug">M1 Trade Center, South Tukoganj,<br/>Indore, 452001 MP</div>
                  </div>
                </div>
              </div>

              <a href="https://www.fast.edu.in/" target="_blank" rel="noreferrer" className="block w-full bg-[#e51c24] hover:bg-red-700 text-white font-bold py-4 rounded-xl text-center transition-colors shadow-lg shadow-red-500/20 text-base">
                Visit F.A.S.T. Website →
              </a>
            </div>

          </div>
        </div>
      </main>
    </div>
  );
};"""

code = code.replace(old_end, new_end)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done!")
