data = open('src/App.jsx', 'rb').read()

dash = b'\xe2\x80\x93'  # UTF-8 en-dash –

replacements = [
    # Q1 - add shortText to B C D
    (b"      { text: 'B  60" + dash + b"90%', value: 3 },",
     b"      { text: 'B  60\xe2\x80\x9390%', shortText: 'B 60-90%', value: 3 },"),
    (b"      { text: 'C  30" + dash + b"60%', value: 2 },",
     b"      { text: 'C  30\xe2\x80\x9360%', shortText: 'C 30-60%', value: 2 },"),
    (b"      { text: 'D  <30% Done', value: 1 }\n    ],\n    quote: \"Real students",
     b"      { text: 'D  <30% Done', shortText: 'D <30%', value: 1 }\n    ],\n    quote: \"Real students"),
    # Q2
    (b"      { text: 'B  2 Revisions', value: 3 },",
     b"      { text: 'B  2 Revisions', shortText: 'B 2 Rev', value: 3 },"),
    (b"      { text: 'C  1 Revision', value: 2 },",
     b"      { text: 'C  1 Revision', shortText: 'C 1 Rev', value: 2 },"),
    (b"      { text: 'D  Not Yet', value: 1 }",
     b"      { text: 'D  Not Yet', shortText: 'D None', value: 1 }"),
    # Q3
    (b"      { text: 'B  45" + dash + b"60%', value: 3 },",
     b"      { text: 'B  45\xe2\x80\x9360%', shortText: 'B 45-60%', value: 3 },"),
    (b"      { text: 'C  30" + dash + b"45%', value: 2 },",
     b"      { text: 'C  30\xe2\x80\x9345%', shortText: 'C 30-45%', value: 2 },"),
    (b"      { text: 'D  <30%', value: 1 }\n    ],\n    quote: \"Tests don",
     b"      { text: 'D  <30%', shortText: 'D <30%', value: 1 }\n    ],\n    quote: \"Tests don"),
    # Q4
    (b"      { text: 'B  Sometimes (5" + dash + b"15%)', value: 3 },",
     b"      { text: 'B  Sometimes (5\xe2\x80\x9315%)', shortText: 'B 5-15%', value: 3 },"),
    (b"      { text: 'C  Often (15" + dash + b"30%)', value: 2 },",
     b"      { text: 'C  Often (15\xe2\x80\x9330%)', shortText: 'C 15-30%', value: 2 },"),
    (b"      { text: 'D  Heavily (>30%)', value: 1 }",
     b"      { text: 'D  Heavily (>30%)', shortText: 'D >30%', value: 1 }"),
    # Q5
    (b"      { text: 'B  >50% Done', value: 3 },",
     b"      { text: 'B  >50% Done', shortText: 'B >50%', value: 3 },"),
    (b"      { text: 'C  Just Started', value: 2 },",
     b"      { text: 'C  Just Started', shortText: 'C Started', value: 2 },"),
    (b"      { text: 'D  Not Started', value: 1 }",
     b"      { text: 'D  Not Started', shortText: 'D None', value: 1 }"),
    # Q6
    (b"      { text: 'B  Minor Hints', value: 3 },",
     b"      { text: 'B  Minor Hints', shortText: 'B Hints', value: 3 },"),
    (b"      { text: 'C  Need Notes', value: 2 },",
     b"      { text: 'C  Need Notes', shortText: 'C Notes', value: 2 },"),
    (b"      { text: 'D  Struggle to Recall', value: 1 }",
     b"      { text: 'D  Struggle to Recall', shortText: 'D Struggle', value: 1 }"),
    # Q7
    (b"      { text: 'B  Minor (1" + dash + b"2 ch)', value: 3 },",
     b"      { text: 'B  Minor (1\xe2\x80\x932 ch)', shortText: 'B 1-2 ch', value: 3 },"),
    (b"      { text: 'C  Moderate (3" + dash + b"5 ch)', value: 2 },",
     b"      { text: 'C  Moderate (3\xe2\x80\x935 ch)', shortText: 'C 3-5 ch', value: 2 },"),
    (b"      { text: 'D  Heavy (5+ ch)', value: 1 }",
     b"      { text: 'D  Heavy (5+ ch)', shortText: 'D 5+ ch', value: 1 }"),
]

for old, new in replacements:
    if old in data:
        data = data.replace(old, new)
    else:
        print(f"NOT FOUND: {repr(old[:50])}")

open('src/App.jsx', 'wb').write(data)
print("Done!")
