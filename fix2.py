with open('src/App.jsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'lex-1  text-white' in line:
        lines[i] = '            <button type="submit" disabled={isSubmitting} className={lex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>\n'
        print('Fixed line:', i)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.writelines(lines)
