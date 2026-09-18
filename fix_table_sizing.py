import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix subject column width
old_subject_th = r'<th className="bg-\[#f8fafc\] text-left p-2 md:p-4 rounded-tl-lg font-bold text-\[#1a2b4b\] border-b border-gray-200 w-\[35%\] text-\[10px\] md:text-sm leading-tight">Subject</th>'
new_subject_th = r'<th className="bg-[#f8fafc] text-left p-1 md:p-4 rounded-tl-lg font-bold text-[#1a2b4b] border-b border-gray-200 w-[28%] text-[8px] md:text-sm leading-tight">Subject</th>'
code = re.sub(old_subject_th, new_subject_th, code)

# Fix options wrapping & size
old_opt_th = r'className=\{\`bg-\[#f8fafc\] p-1 md:p-2 lg:p-4 font-bold text-\[#1a2b4b\] text-center border-b border-gray-200 text-\[8px\] md:text-xs lg:text-sm break-words \$\{i === question\.options\.length - 1 \? \'rounded-tr-lg\' : \'\'\}\`\}'
new_opt_th = r'className={`bg-[#f8fafc] p-1 md:p-2 lg:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 text-[6.5px] min-[375px]:text-[7.5px] sm:text-[9px] md:text-xs lg:text-sm whitespace-nowrap tracking-tighter ${i === question.options.length - 1 ? \'rounded-tr-lg\' : \'\'}`}'
code = re.sub(old_opt_th, new_opt_th, code)

# Also update the Subject text in the TD to be slightly smaller on mobile to fit the narrower column
old_subject_td = r'<td className="p-2 md:p-4 text-\[10px\] md:text-sm font-medium text-gray-800 border-b border-gray-100">'
new_subject_td = r'<td className="p-2 md:p-4 text-[9px] min-[375px]:text-[10px] md:text-sm font-medium text-gray-800 border-b border-gray-100">'
code = re.sub(old_subject_td, new_subject_td, code)


with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
