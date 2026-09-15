const fs = require('fs');
let code = fs.readFileSync('src/App.jsx', 'utf8');

// The file might contain multiple weird variations of lex-1. Let's just find the whole line and nuke it.
let lines = code.split('\n');
for(let i=0; i<lines.length; i++) {
    if(lines[i].includes('lex-1')) {
        console.log("Found lex-1 on line " + i);
        lines[i] = '            <button type="submit" disabled={isSubmitting} className={lex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>';
    }
}
fs.writeFileSync('src/App.jsx', lines.join('\n'));
