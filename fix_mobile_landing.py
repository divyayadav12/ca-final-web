import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

landing_component = """const Landing = ({ onStart, onNav }) => {
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
            { icon: Target, text: "Know Your\\nCurrent Position" },
            { icon: BarChart2, text: "Identify Your\\nWeak Areas" },
            { icon: ClipboardList, text: "Get Subject-wise\\nAnalysis" },
            { icon: Rocket, text: "Start Your\\nAction Plan" }
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
};"""

code = re.sub(r'const Landing = \(\{ onStart, onNav \}\) => \{.*?^\};\s*$', landing_component, code, flags=re.MULTILINE|re.DOTALL)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
