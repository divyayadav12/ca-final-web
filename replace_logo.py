import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_logo = """const FastLogo = ({ className = "" }) => (
  <div className={`flex flex-col items-center bg-[#e51c24] border border-[#a81319] rounded-[2px] p-1 w-fit ${className}`}>
    <div className="text-white font-black italic text-2xl md:text-3xl tracking-widest leading-none px-2">F.A.S.T</div>
    <div className="bg-black text-white text-[6px] md:text-[8px] uppercase font-bold tracking-[0.1em] px-2 py-0.5 mt-0.5 w-full text-center border border-gray-600">
      first attempt success tutorials
    </div>
  </div>
);"""

new_logo = """const FastLogo = ({ className = "" }) => (
  <img 
    src="/fast-logo.png" 
    alt="F.A.S.T. First Attempt Success Tutorials" 
    className={`max-w-[140px] md:max-w-[180px] h-auto object-contain ${className}`} 
  />
);"""

code = code.replace(old_logo, new_logo)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
