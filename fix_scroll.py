with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace(
    'className="min-h-screen text-white flex flex-col font-sans relative overflow-hidden bg-black"',
    'className="h-screen text-white flex flex-col font-sans relative overflow-hidden bg-black"'
)
code = code.replace('text-3xl md:text-5xl font-bold', 'text-2xl md:text-4xl font-bold')
code = code.replace('text-5xl md:text-8xl font-black', 'text-4xl md:text-6xl font-black')
code = code.replace('text-base md:text-2xl text-gray-200 mb-6', 'text-sm md:text-xl text-gray-200 mb-4 md:mb-6')

code = code.replace('mb-6 max-w-4xl w-full', 'mb-4 md:mb-6 max-w-4xl w-full')
code = code.replace(
    'w-12 h-12 rounded-full border-2 border-white/20 flex items-center justify-center mb-3 bg-white/5 backdrop-blur-sm',
    'w-10 h-10 md:w-12 md:h-12 rounded-full border-2 border-white/20 flex items-center justify-center mb-2 bg-white/5 backdrop-blur-sm'
)

code = code.replace('px-4 pb-12 text-center mt-2 md:mt-6', 'px-4 pb-2 md:pb-4 text-center mt-2 md:mt-4')

code = code.replace('top-48 right-10 md:right-24 bg-[#e8e4d9]', 'top-24 right-4 md:right-12 xl:right-24 bg-[#e8e4d9]')

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
