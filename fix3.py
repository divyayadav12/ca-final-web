import re

with open('src/App.jsx', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Replace any className={...lex-1...} with the correct string interpolation.
# The issue is the form feed character \x0c
text = re.sub(
    r'className=\{\x0clex-1.*?shadow-red-500/20\}>',
    'className={lex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>',
    text
)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(text)
