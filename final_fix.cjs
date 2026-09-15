const fs = require('fs');
let code = fs.readFileSync('src/App.jsx', 'utf8');

// Fix 1: The backslashes in useState
code = code.replace(/useState\(\\'Overview\\'\)/g, "useState('Overview')");

// Fix 2: The weird lex-1 interpolation syntax error
let corruptString = "className={\x0clex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>";
let fixedString = "className={lex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>";

if (code.includes(corruptString)) {
    code = code.replace(corruptString, fixedString);
    console.log("Found and replaced corrupt string!");
} else {
    console.log("Could not find the corrupt string exact match, trying regex...");
    code = code.replace(/className=\{.*?lex-1.*?shadow-red-500\/20\}>/g, fixedString);
}

fs.writeFileSync('src/App.jsx', code);
