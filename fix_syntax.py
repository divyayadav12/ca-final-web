import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace actual newlines inside the strings with \n
code = code.replace('text: "Know Your\nCurrent Position"', r'text: "Know Your\nCurrent Position"')
code = code.replace('text: "Identify Your\nWeak Areas"', r'text: "Identify Your\nWeak Areas"')
code = code.replace('text: "Get Subject-wise\nAnalysis"', r'text: "Get Subject-wise\nAnalysis"')
code = code.replace('text: "Start Your\nAction Plan"', r'text: "Start Your\nAction Plan"')

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
