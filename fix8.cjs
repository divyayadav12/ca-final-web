const fs = require('fs');
let code = fs.readFileSync('src/App.jsx', 'utf8');

code = code.replace(/useState\(\\'Overview\\'\)/g, "useState('Overview')");

let lines = code.split('\n');
for(let i=0; i<lines.length; i++) {
    if(lines[i].includes('text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>')) {
        console.log("Found corrupted line at " + i);
        lines[i] = '            <button type="submit" disabled={isSubmitting} className={lex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>';
    }
}
fs.writeFileSync('src/App.jsx', lines.join('\n'));
