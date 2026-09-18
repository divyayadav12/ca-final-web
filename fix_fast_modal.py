with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# ─────────────────────────────────────────────
# 1. Remove the broken "Connect with FAST" inline section
# ─────────────────────────────────────────────
old_fast_section = """
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

new_fast_section = """

          </div>
        </div>
      </main>

      {/* Floating "Connect with FAST" button */}
      <button
        onClick={() => setShowFastModal(true)}
        className="fixed bottom-6 right-6 z-50 bg-[#e51c24] hover:bg-red-700 text-white font-bold px-5 py-3 rounded-full shadow-2xl shadow-red-500/40 flex items-center gap-2 transition-all hover:scale-105 active:scale-95"
      >
        <Globe className="w-4 h-4" />
        Connect with FAST
      </button>

      {/* FAST Connect Modal */}
      {showFastModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm" onClick={() => setShowFastModal(false)}>
          <div className="bg-[#111] border border-gray-700 rounded-2xl w-full max-w-sm shadow-2xl relative overflow-hidden" onClick={e => e.stopPropagation()}>
            {/* Header */}
            <div className="bg-[#e51c24] p-5 flex items-center justify-between">
              <div>
                <div className="text-white font-black text-xl leading-tight">Your Next Step</div>
                <div className="text-red-100 text-xs font-medium mt-0.5">Connect with F.A.S.T. and get expert guidance</div>
              </div>
              <button onClick={() => setShowFastModal(false)} className="text-white/80 hover:text-white text-2xl font-bold leading-none ml-4 shrink-0">✕</button>
            </div>

            {/* Logo area */}
            <div className="flex justify-center pt-5 pb-3 border-b border-gray-800">
              <FastLogo className="max-w-[130px]" />
            </div>

            {/* Contact Cards */}
            <div className="p-5 space-y-3">
              <a href="tel:+919584510000" className="flex items-center bg-gray-900 border border-gray-700 rounded-xl p-4 hover:border-[#e51c24] transition-colors group">
                <div className="w-10 h-10 rounded-full bg-[#e51c24] flex items-center justify-center mr-3 shrink-0">
                  <Phone className="w-5 h-5 text-white" />
                </div>
                <div>
                  <div className="text-gray-400 text-[10px] font-medium mb-0.5 uppercase tracking-wider">Call Us</div>
                  <div className="text-white font-bold text-sm group-hover:text-[#e51c24] transition-colors">+91 9584510000</div>
                </div>
              </a>

              <a href="mailto:faststudentcare@gmail.com" className="flex items-center bg-gray-900 border border-gray-700 rounded-xl p-4 hover:border-[#e51c24] transition-colors group">
                <div className="w-10 h-10 rounded-full bg-[#e51c24] flex items-center justify-center mr-3 shrink-0">
                  <Mail className="w-5 h-5 text-white" />
                </div>
                <div>
                  <div className="text-gray-400 text-[10px] font-medium mb-0.5 uppercase tracking-wider">Email Us</div>
                  <div className="text-white font-bold text-xs group-hover:text-[#e51c24] transition-colors break-all">faststudentcare@gmail.com</div>
                </div>
              </a>

              <div className="flex items-center bg-gray-900 border border-gray-700 rounded-xl p-4">
                <div className="w-10 h-10 rounded-full bg-[#e51c24] flex items-center justify-center mr-3 shrink-0">
                  <MapPin className="w-5 h-5 text-white" />
                </div>
                <div>
                  <div className="text-gray-400 text-[10px] font-medium mb-0.5 uppercase tracking-wider">Address</div>
                  <div className="text-white text-xs leading-snug">M1 Trade Center, South Tukoganj,<br/>Opp. Samavsharan Jain Temple,<br/>Indore, 452001 MP</div>
                </div>
              </div>

              <a
                href="https://www.fast.edu.in/"
                target="_blank"
                rel="noreferrer"
                className="flex items-center justify-center w-full bg-[#e51c24] hover:bg-red-700 text-white font-bold py-4 rounded-xl transition-colors shadow-lg shadow-red-500/20 text-base gap-2"
              >
                <Globe className="w-5 h-5" />
                Visit F.A.S.T. Website
              </a>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};"""

code = code.replace(old_fast_section, new_fast_section)

# ─────────────────────────────────────────────
# 2. Add showFastModal state to Result component
# ─────────────────────────────────────────────
code = code.replace(
    "  const [activeTab, setActiveTab] = useState('Overview');",
    "  const [activeTab, setActiveTab] = useState('Overview');\n  const [showFastModal, setShowFastModal] = useState(false);"
)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done!")
