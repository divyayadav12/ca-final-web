import sys
import re

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Import useRef
    if 'useRef' not in code:
        code = code.replace("import React, { useState } from 'react';", "import React, { useState, useRef } from 'react';")

    # 2. Add handleDownload to Result component
    if 'const handleDownload = async () =>' not in code:
        inject_marker = "const [activeTab, setActiveTab] = useState('Overview');\n"
        download_func = """  const dashboardRef = useRef(null);
  const handleDownload = async () => {
    if(!dashboardRef.current) return;
    try {
      const canvas = await html2canvas(dashboardRef.current, { scale: 2 });
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jsPDF('p', 'mm', 'a4');
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = (canvas.height * pdfWidth) / canvas.width;
      pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
      pdf.save('CA_Final_Reality_Check_Report.pdf');
    } catch (e) {
      console.error(e);
      alert('Failed to download report. Please try on a desktop.');
    }
  };
"""
        code = code.replace(inject_marker, inject_marker + download_func)

    # 3. Attach ref to the main dashboard container
    code = code.replace(
        '<main className="flex-1 bg-[#f8fafc] lg:rounded-l-2xl overflow-hidden flex flex-col h-screen overflow-y-auto relative">', 
        '<main ref={dashboardRef} className="flex-1 bg-[#f8fafc] lg:rounded-l-2xl overflow-hidden flex flex-col h-screen overflow-y-auto relative">'
    )

    # 4. Attach onClick to Download button
    old_btn = '<button className="px-5 py-2.5 bg-[#e51c24] rounded-lg text-white font-bold hover:bg-red-700 flex items-center shadow-md">\n                Download My Report'
    new_btn = '<button onClick={handleDownload} className="px-5 py-2.5 bg-[#e51c24] rounded-lg text-white font-bold hover:bg-red-700 flex items-center shadow-md">\n                Download My Report'
    code = code.replace(old_btn, new_btn)

    # Alternate match in case there's no newline
    code = re.sub(
        r'<button className="px-5 py-2\.5 bg-\[#e51c24\] rounded-lg text-white font-bold hover:bg-red-700 flex items-center shadow-md">\s*Download My Report', 
        r'<button onClick={handleDownload} className="px-5 py-2.5 bg-[#e51c24] rounded-lg text-white font-bold hover:bg-red-700 flex items-center shadow-md">\n                Download My Report', 
        code
    )

    # 5. Fix Assessment header overlap
    code = code.replace(
        '<header className="bg-white border-b border-gray-200 px-6 py-3 flex justify-between items-center shadow-sm z-20 sticky top-0">', 
        '<header className="bg-white border-b border-gray-200 px-3 sm:px-6 py-3 flex justify-between items-center shadow-sm z-20 sticky top-0">'
    )
    code = code.replace(
        '<div className="flex items-center space-x-6">', 
        '<div className="flex items-center space-x-3 sm:space-x-6 scale-[0.80] origin-left sm:scale-100">'
    )
    code = code.replace(
        '<div className="flex flex-col items-end w-48">', 
        '<div className="flex flex-col items-end w-32 sm:w-48">'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)

patch_file('src/App.jsx')
print("Patched!")
