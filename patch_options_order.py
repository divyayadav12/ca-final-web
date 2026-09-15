import re

def patch():
    with open('src/App.jsx', 'r', encoding='utf-8') as f:
        code = f.read()
    
    # We want to replace the current options array with the new one requested by the user.
    # Current options look something like this in the file:
    # options: [
    #   { text: 'D (Needs Improvement 🔴)', value: 1 },
    #   { text: 'C (Average)', value: 2 },
    #   { text: 'B (Good / Better)', value: 3 },
    #   { text: 'A (Excellent 🟢)', value: 4 }
    # ]
    
    standard_options = """options: [
      { text: 'A (Excellent)', value: 4 },
      { text: 'B (Better)', value: 3 },
      { text: 'C (Average)', value: 2 },
      { text: 'D (Needs Improvement)', value: 1 }
    ]"""
    
    # Replace all occurrences of options array with the new standard options
    new_code = re.sub(r'options:\s*\[[\s\S]*?\]', standard_options, code)
    
    with open('src/App.jsx', 'w', encoding='utf-8') as f:
        f.write(new_code)

patch()
