const fs = require('fs');
let code = fs.readFileSync('src/App.jsx', 'utf8');
code = code.replace(/\\'rounded-tr-lg\\'/g, "'rounded-tr-lg'");
code = code.replace(/\\'\\'/g, "''");
fs.writeFileSync('src/App.jsx', code);
