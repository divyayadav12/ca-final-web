with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix 1: Matrix header text wrapping (Needs Improvement cutoff)
old_th = "className={`bg-[#f8fafc] p-0 md:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 text-[8px] md:text-sm whitespace-nowrap ${i === question.options.length - 1 ? 'rounded-tr-lg' : ''}`}"
new_th = "className={`bg-[#f8fafc] p-1 md:p-2 lg:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 text-[8px] md:text-xs lg:text-sm break-words ${i === question.options.length - 1 ? 'rounded-tr-lg' : ''}`}"
code = code.replace(old_th, new_th)

# Fix 2: Bottom pill cutoff on desktop (Give container more bottom padding & margin)
old_main_container = 'className="flex-1 flex flex-col items-center justify-center relative z-10 px-4 pb-2 md:pb-4 text-center mt-2 md:mt-4"'
new_main_container = 'className="flex-1 flex flex-col items-center justify-center relative z-10 px-4 pb-6 md:pb-12 text-center mt-2 md:mt-4"'
code = code.replace(old_main_container, new_main_container)

old_pill = 'className="relative mt-8 mb-4 w-full max-w-2xl px-4 z-20 mx-auto"'
new_pill = 'className="relative mt-4 md:mt-8 mb-8 md:mb-16 w-full max-w-2xl px-4 z-20 mx-auto"'
code = code.replace(old_pill, new_pill)

# Fix 3: Sticky note overlap (Move down and scale down)
old_sticky = 'className="absolute top-24 right-4 md:right-12 xl:right-24 bg-[#e8e4d9] text-gray-900 font-handwriting text-2xl p-6 shadow-2xl rotate-[3deg] hidden lg:flex flex-col items-center justify-center w-48 h-48 rounded-sm"'
new_sticky = 'className="absolute top-40 md:top-48 right-4 md:right-12 xl:right-24 bg-[#e8e4d9] text-gray-900 font-handwriting text-xl p-4 shadow-2xl rotate-[3deg] hidden lg:flex flex-col items-center justify-center w-40 h-40 rounded-sm"'
code = code.replace(old_sticky, new_sticky)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
