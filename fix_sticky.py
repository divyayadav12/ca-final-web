with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_sticky = 'className="absolute top-36 md:top-52 right-4 md:right-12 xl:right-24 bg-[#e8e4d9] text-gray-900 font-handwriting text-lg md:text-xl p-4 shadow-2xl rotate-[3deg] hidden lg:flex flex-col items-center justify-center w-36 h-36 md:w-40 md:h-40 rounded-sm"'
new_sticky = 'className="absolute top-auto bottom-20 md:bottom-32 right-4 md:right-12 xl:right-24 bg-[#e8e4d9] text-gray-900 font-handwriting text-lg md:text-xl p-4 shadow-2xl rotate-[3deg] hidden lg:flex flex-col items-center justify-center w-36 h-36 md:w-40 md:h-40 rounded-sm"'

code = code.replace(old_sticky, new_sticky)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
