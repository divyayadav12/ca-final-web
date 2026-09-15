const fs = require('fs');
let code = fs.readFileSync('src/App.jsx', 'utf8');
// Target the exact problematic string
let target = 'className={\x0clex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>';
let replacement = 'className={lex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>';

if (code.includes(target)) {
    code = code.replace(target, replacement);
    fs.writeFileSync('src/App.jsx', code);
    console.log('Fixed successfully.');
} else {
    console.log('Target not found.');
    // Try regex as fallback
    let reg = /className=\{\x0clex-1.*?shadow-red-500\/20\}>/g;
    if (reg.test(code)) {
        code = code.replace(reg, replacement);
        fs.writeFileSync('src/App.jsx', code);
        console.log('Fixed via regex fallback.');
    }
}
