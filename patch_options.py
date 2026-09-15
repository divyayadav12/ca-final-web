import re

def patch():
    with open('src/App.jsx', 'r', encoding='utf-8') as f:
        code = f.read()
    
    # We want to replace options: [...] ONLY inside the QUESTIONS array.
    # The QUESTIONS array starts at `const QUESTIONS = [` and ends at `]; // End of QUESTIONS` or something.
    
    # Actually, we can just find all occurrences of `options: [\n ... \n    ],` and replace them.
    # But let's be safe.
    
    standard_options = """options: [
      { text: 'D (Needs Improvement 🔴)', value: 1 },
      { text: 'C (Average)', value: 2 },
      { text: 'B (Good / Better)', value: 3 },
      { text: 'A (Excellent 🟢)', value: 4 }
    ]"""
    
    new_code = re.sub(r'options:\s*\[[\s\S]*?\]', standard_options, code)
    
    with open('src/App.jsx', 'w', encoding='utf-8') as f:
        f.write(new_code)

patch()
