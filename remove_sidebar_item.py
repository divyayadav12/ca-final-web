import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Original string:
#             { name: 'Your Action Plan', active: false },
#             { name: 'Download Report', active: false }
#           ].map((item, idx) => (

code = re.sub(r",\s*\{\s*name:\s*'Download Report',\s*active:\s*false\s*\}", "", code)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
