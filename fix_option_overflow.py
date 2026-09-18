with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Add shortText to every option in QUESTIONS
replacements = [
    # Q1
    ("      { text: 'A  90%+ Done', value: 4 },", "      { text: 'A  90%+ Done', shortText: 'A 90%+', value: 4 },"),
    ("      { text: 'B  60–90%', value: 3 },\n    ],\n    quote: \"Real students face gaps. Winners fix them.\"",
     "      { text: 'B  60–90%', shortText: 'B 60–90%', value: 3 },\n      { text: 'C  30–60%', shortText: 'C 30–60%', value: 2 },\n      { text: 'D  <30% Done', shortText: 'D <30%', value: 1 }\n    ],\n    quote: \"Real students face gaps. Winners fix them.\""),
    # Remove old C and D for Q1 since we replaced them above
    ("      { text: 'C  30–60%', value: 2 },\n      { text: 'D  <30% Done', value: 1 }\n    ],\n    quote: \"Real students face gaps. Winners fix them.\"", ""),

    # Q2
    ("      { text: 'A  3+ Revisions', value: 4 },", "      { text: 'A  3+ Revisions', shortText: 'A 3+ Rev', value: 4 },"),
    ("      { text: 'B  2 Revisions', value: 3 },\n    ],\n    quote: \"Progress is a result",
     "      { text: 'B  2 Revisions', shortText: 'B 2 Rev', value: 3 },\n      { text: 'C  1 Revision', shortText: 'C 1 Rev', value: 2 },\n      { text: 'D  Not Yet', shortText: 'D None', value: 1 }\n    ],\n    quote: \"Progress is a result"),
    ("      { text: 'C  1 Revision', value: 2 },\n      { text: 'D  Not Yet', value: 1 }\n    ],\n    quote: \"Progress is a result", ""),

    # Q3
    ("      { text: 'A  60%+', value: 4 },", "      { text: 'A  60%+', shortText: 'A 60%+', value: 4 },"),
    ("      { text: 'B  45–60%', value: 3 },\n    ],\n    quote: \"Tests don't define",
     "      { text: 'B  45–60%', shortText: 'B 45–60%', value: 3 },\n      { text: 'C  30–45%', shortText: 'C 30–45%', value: 2 },\n      { text: 'D  <30%', shortText: 'D <30%', value: 1 }\n    ],\n    quote: \"Tests don't define"),
    ("      { text: 'C  30–45%', value: 2 },\n      { text: 'D  <30%', value: 1 }\n    ],\n    quote: \"Tests don't define", ""),

    # Q4
    ("      { text: 'A  Rarely (<5%)', value: 4 },", "      { text: 'A  Rarely (<5%)', shortText: 'A Rarely', value: 4 },"),
    ("      { text: 'B  Sometimes (5–15%)', value: 3 },\n    ],\n    quote: \"Identifying",
     "      { text: 'B  Sometimes (5–15%)', shortText: 'B 5–15%', value: 3 },\n      { text: 'C  Often (15–30%)', shortText: 'C 15–30%', value: 2 },\n      { text: 'D  Heavily (>30%)', shortText: 'D >30%', value: 1 }\n    ],\n    quote: \"Identifying"),
    ("      { text: 'C  Often (15–30%)', value: 2 },\n      { text: 'D  Heavily (>30%)', value: 1 }\n    ],\n    quote: \"Identifying", ""),

    # Q5
    ("      { text: 'A  All Done', value: 4 },", "      { text: 'A  All Done', shortText: 'A All', value: 4 },"),
    ("      { text: 'B  >50% Done', value: 3 },\n    ],\n    quote: \"Exam conditions",
     "      { text: 'B  >50% Done', shortText: 'B >50%', value: 3 },\n      { text: 'C  Just Started', shortText: 'C Started', value: 2 },\n      { text: 'D  Not Started', shortText: 'D None', value: 1 }\n    ],\n    quote: \"Exam conditions"),
    ("      { text: 'C  Just Started', value: 2 },\n      { text: 'D  Not Started', value: 1 }\n    ],\n    quote: \"Exam conditions", ""),

    # Q6
    ("      { text: 'A  Without Book', value: 4 },", "      { text: 'A  Without Book', shortText: 'A No Book', value: 4 },"),
    ("      { text: 'B  Minor Hints', value: 3 },\n    ],\n    quote: \"Memory is",
     "      { text: 'B  Minor Hints', shortText: 'B Hints', value: 3 },\n      { text: 'C  Need Notes', shortText: 'C Notes', value: 2 },\n      { text: 'D  Struggle to Recall', shortText: 'D Struggle', value: 1 }\n    ],\n    quote: \"Memory is"),
    ("      { text: 'C  Need Notes', value: 2 },\n      { text: 'D  Struggle to Recall', value: 1 }\n    ],\n    quote: \"Memory is", ""),

    # Q7
    ("      { text: 'A  No Backlog', value: 4 },", "      { text: 'A  No Backlog', shortText: 'A None', value: 4 },"),
    ("      { text: 'B  Minor (1–2 ch)', value: 3 },\n    ],\n    quote: \"Don't let",
     "      { text: 'B  Minor (1–2 ch)', shortText: 'B 1–2 ch', value: 3 },\n      { text: 'C  Moderate (3–5 ch)', shortText: 'C 3–5 ch', value: 2 },\n      { text: 'D  Heavy (5+ ch)', shortText: 'D 5+ ch', value: 1 }\n    ],\n    quote: \"Don't let"),
    ("      { text: 'C  Moderate (3–5 ch)', value: 2 },\n      { text: 'D  Heavy (5+ ch)', value: 1 }\n    ],\n    quote: \"Don't let", ""),
]

for old, new in replacements:
    if old in code:
        code = code.replace(old, new)
    else:
        print(f"NOT FOUND: {old[:60]}")

# Fix th to use opt.shortText for mobile, opt.text for desktop
old_th = """                       <th key={i} className={`bg-[#f8fafc] p-1 md:p-2 lg:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 text-[6.5px] min-[375px]:text-[7.5px] sm:text-[9px] md:text-xs lg:text-sm whitespace-nowrap tracking-tighter ${i === question.options.length - 1 ? 'rounded-tr-lg' : ''}`}>
                         {opt.text}
                       </th>"""

new_th = """                       <th key={i} className={`bg-[#f8fafc] p-1 md:p-2 lg:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 whitespace-nowrap tracking-tight ${i === question.options.length - 1 ? 'rounded-tr-lg' : ''}`}>
                         <span className="hidden md:inline text-xs lg:text-sm">{opt.text}</span>
                         <span className="md:hidden text-[7px] min-[375px]:text-[8px] sm:text-[9px]">{opt.shortText || opt.text.split(' ')[0]}</span>
                       </th>"""

code = code.replace(old_th, new_th)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done!")
