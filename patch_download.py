import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Add imports
if 'html2canvas' not in code:
    code = code.replace("import React, { useState } from 'react';", "import React, { useState } from 'react';\nimport html2canvas from 'html2canvas';\nimport { jsPDF } from 'jspdf';")

# Add handleDownload function inside Result component
download_func = '''
  const handleDownload = async () => {
    const element = document.getElementById('report-content');
    if (!element) return;
    
    // Save current tab, switch to Overview for printing
    const previousTab = activeTab;
    setActiveTab('Overview');
    
    // Allow React to re-render
    setTimeout(async () => {
      try {
        const canvas = await html2canvas(element, { scale: 2 });
        const imgData = canvas.toDataURL('image/png');
        const pdf = new jsPDF('p', 'mm', 'a4');
        const pdfWidth = pdf.internal.pageSize.getWidth();
        const pdfHeight = (canvas.height * pdfWidth) / canvas.width;
        
        pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
        pdf.save('CA-Final-FAST-Report.pdf');
      } catch (err) {
        console.error('Error generating PDF', err);
      } finally {
        setActiveTab(previousTab);
      }
    }, 300);
  };
'''

code = re.sub(
    r'(const \[activeTab, setActiveTab\] = useState\(\'Overview\'\);)',
    r'\1\n' + download_func,
    code
)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patched handleDownload successfully")
