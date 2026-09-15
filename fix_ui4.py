with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix matrix headers
old_th = "className={`bg-[#f8fafc] p-1 md:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 text-[9px] md:text-sm break-words ${i === question.options.length - 1 ? 'rounded-tr-lg' : ''}`}"
new_th = "className={`bg-[#f8fafc] p-0 md:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 text-[8px] md:text-sm whitespace-nowrap ${i === question.options.length - 1 ? 'rounded-tr-lg' : ''}`}"
code = code.replace(old_th, new_th)

# Fix footer pill
old_pill = '<div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 w-full max-w-2xl px-4 z-20">'
new_pill = '<div className="relative mt-8 mb-4 w-full max-w-2xl px-4 z-20 mx-auto">'
code = code.replace(old_pill, new_pill)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
