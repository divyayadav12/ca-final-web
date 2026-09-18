import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_nav = """        <nav className="flex-1 py-6 space-y-1">
          {[
            { name: 'Your Result', active: true },
            { name: 'Subject-wise Analysis', active: false },
            { name: 'Detailed Insights', active: false },
            { name: 'Your Action Plan', active: false }
          ].map((item, idx) => (
            <a key={idx} href="#" className={`flex items-center px-6 py-4 font-medium transition-colors ${
              item.active ? 'bg-[#e51c24] text-white' : 'text-gray-400 hover:text-white hover:bg-gray-800'
            }`}>
              {item.name}
            </a>
          ))}
        </nav>"""

# Replace it with an empty flex-1 div to maintain spacing for the quote at the bottom
new_nav = """        <div className="flex-1"></div>"""

code = code.replace(old_nav, new_nav)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
