const fs = require('fs');
let code = fs.readFileSync('src/App.jsx', 'utf8');
let lines = code.split('\n');

for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes('text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>')) {
        console.log("Fixing line " + i);
        // Using string concatenation to avoid any escaping madness
        let p1 = '            <button type="submit" disabled={isSubmitting} className={lex-1 ";
        let p3 = ' text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>';
        lines[i] = p1 + p2 + p3;
    }
}

fs.writeFileSync('src/App.jsx', lines.join('\n'));
