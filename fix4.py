import io
with io.open('src/App.jsx', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.read().split('\n')

for i, line in enumerate(lines):
    if 'lex-1' in line:
        lines[i] = '            <button type="submit" disabled={isSubmitting} className={lex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>'
        print('Fixed line', i)

with io.open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
