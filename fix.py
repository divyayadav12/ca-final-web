with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace("useState(\\\'Overview\\\')", "useState('Overview')")

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
