with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace(r"\'rounded-tr-lg\'", "'rounded-tr-lg'")
code = code.replace(r"\'\'", "''")

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
