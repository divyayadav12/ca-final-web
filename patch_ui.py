import sys
import re

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Landing Page Margins
    content = content.replace(
        'className="flex-1 flex flex-col items-center justify-center relative z-10 px-4 pb-24 text-center mt-8 md:mt-12"',
        'className="flex-1 flex flex-col items-center justify-center relative z-10 px-4 pb-12 text-center mt-2 md:mt-6"'
    )
    content = content.replace(
        'className="text-6xl md:text-8xl font-black italic mb-6 flex flex-wrap justify-center gap-4"',
        'className="text-5xl md:text-8xl font-black italic mb-3 flex flex-wrap justify-center gap-4"'
    )
    content = content.replace(
        'className="text-lg md:text-2xl text-gray-200 mb-12 font-medium max-w-2xl drop-shadow-md"',
        'className="text-base md:text-2xl text-gray-200 mb-6 font-medium max-w-2xl drop-shadow-md"'
    )
    content = content.replace(
        'className="grid grid-cols-2 md:grid-cols-4 gap-6 md:gap-12 mb-12 max-w-4xl w-full"',
        'className="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-12 mb-6 max-w-4xl w-full"'
    )
    
    # CTA button scale
    content = content.replace(
        'className="bg-[#e51c24] hover:bg-red-700 text-white text-xl md:text-2xl font-bold py-4 px-12 md:px-20 rounded-xl flex items-center transition-all shadow-[0_0_30px_rgba(229,28,36,0.5)] relative z-20"',
        'className="bg-[#e51c24] hover:bg-red-700 text-white text-lg md:text-2xl font-bold py-3 md:py-4 px-10 md:px-20 rounded-xl flex items-center transition-all shadow-[0_0_30px_rgba(229,28,36,0.5)] relative z-20"'
    )

    # 2. Matrix Table mobile responsiveness
    content = content.replace(
        '<table className="w-full min-w-[600px] border-collapse">',
        '<table className="w-full table-fixed border-collapse max-w-full">'
    )
    # Subject Header
    content = content.replace(
        '<th className="bg-[#f8fafc] text-left p-4 rounded-tl-lg font-bold text-[#1a2b4b] border-b border-gray-200 w-1/3">Subject</th>',
        '<th className="bg-[#f8fafc] text-left p-2 md:p-4 rounded-tl-lg font-bold text-[#1a2b4b] border-b border-gray-200 w-[35%] text-[10px] md:text-sm leading-tight">Subject</th>'
    )
    # Options Headers
    content = re.sub(
        r'<th key=\{i\} className={`bg-\[#f8fafc\] p-4 font-bold text-\[#1a2b4b\] text-center border-b border-gray-200 \$\{i === question\.options\.length - 1 \? \'rounded-tr-lg\' : \'\'\}`\}',
        r'<th key={i} className={`bg-[#f8fafc] p-1 md:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 text-[9px] md:text-sm break-words ${i === question.options.length - 1 ? \'rounded-tr-lg\' : \'\'}`}',
        content
    )
    
    # Row Data
    content = content.replace(
        '<td className="p-4 font-medium text-[#1a2b4b] text-sm">{subject.name}</td>',
        '<td className="p-2 md:p-4 font-medium text-[#1a2b4b] text-[10px] md:text-sm leading-tight">{subject.name}</td>'
    )
    content = content.replace(
        '<td key={oIdx} className="p-4 text-center">',
        '<td key={oIdx} className="p-1 md:p-4 text-center">'
    )
    
    content = content.replace(
        'className="custom-radio"',
        'className="custom-radio scale-75 md:scale-100"'
    )

    # 3. Assessment container bottom spacing
    content = content.replace(
        '<main className="flex-1 bg-white rounded-xl shadow-sm border border-gray-200 p-6 md:p-10">',
        '<main className="flex-1 bg-white md:rounded-xl shadow-sm border border-gray-200 p-4 md:p-10 flex flex-col min-h-[50vh]">'
    )
    
    content = content.replace(
        '<div className="overflow-x-auto pb-4">',
        '<div className="w-full pb-2 md:pb-4 overflow-hidden">'
    )

    content = content.replace(
        '<div className="mt-8 pt-6 border-t border-gray-100 flex justify-between items-center">',
        '<div className="mt-4 md:mt-8 pt-4 md:pt-6 border-t border-gray-100 flex justify-between items-center mt-auto">'
    )
    
    content = content.replace(
        'className={`flex items-center px-6 py-3 rounded-lg font-bold transition-colors ${',
        'className={`flex items-center px-4 md:px-6 py-2 md:py-3 rounded-lg font-bold text-sm md:text-base transition-colors ${'
    )
    content = content.replace(
        'className={`flex items-center px-8 py-3 rounded-lg font-bold transition-all shadow-md ${',
        'className={`flex items-center px-6 md:px-8 py-2 md:py-3 rounded-lg font-bold text-sm md:text-base transition-all shadow-md ${'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
patch_file('src/App.jsx')
print("Patched!")
