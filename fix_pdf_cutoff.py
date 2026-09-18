with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update handleDownload
old_handle = """  const handleDownload = async () => {
    if (!dashboardRef.current) return;
    try {
      const canvas = await html2canvas(dashboardRef.current, {
        scale: 2,
        useCORS: true,
        logging: false,
        backgroundColor: '#f8fafc'
      });
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jsPDF('p', 'mm', 'a4');
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = (canvas.height * pdfWidth) / canvas.width;
      const pageHeight = pdf.internal.pageSize.getHeight();

      let heightLeft = pdfHeight;
      let position = 0;

      pdf.addImage(imgData, 'PNG', 0, position, pdfWidth, pdfHeight);
      heightLeft -= pageHeight;

      while (heightLeft > 0) {
        position = heightLeft - pdfHeight;
        pdf.addPage();
        pdf.addImage(imgData, 'PNG', 0, position, pdfWidth, pdfHeight);
        heightLeft -= pageHeight;
      }

      const fileName = userData?.name
        ? `CA_Final_Reality_Check_${userData.name.trim().replace(/\\s+/g, '_')}.pdf`
        : 'CA_Final_Reality_Check_Report.pdf';
      pdf.save(fileName);
    } catch (e) {
      console.error(e);
      alert('Failed to download report. Please try on a desktop.');
    }
  };"""

new_handle = """  const handleDownload = async () => {
    if (!dashboardRef.current) return;
    try {
      const element = dashboardRef.current;
      const canvas = await html2canvas(element, {
        scale: 2,
        useCORS: true,
        logging: false,
        backgroundColor: '#f8fafc',
        windowWidth: 1280
      });
      const imgData = canvas.toDataURL('image/jpeg', 0.98);
      const pdf = new jsPDF('p', 'mm', 'a4');
      const pdfWidth = pdf.internal.pageSize.getWidth(); // 210 mm
      const pageHeight = pdf.internal.pageSize.getHeight(); // 297 mm
      const imgHeight = (canvas.height * pdfWidth) / canvas.width;

      let heightLeft = imgHeight;
      let position = 0;

      // Add page 1
      pdf.addImage(imgData, 'JPEG', 0, position, pdfWidth, imgHeight);
      heightLeft -= pageHeight;

      // Add subsequent pages for complete report without cutting off
      while (heightLeft > 5) {
        position -= pageHeight;
        pdf.addPage();
        pdf.addImage(imgData, 'JPEG', 0, position, pdfWidth, imgHeight);
        heightLeft -= pageHeight;
      }

      const fileName = userData?.name
        ? `CA_Final_Reality_Check_${userData.name.trim().replace(/\\s+/g, '_')}.pdf`
        : 'CA_Final_Reality_Check_Report.pdf';
      pdf.save(fileName);
    } catch (e) {
      console.error(e);
      alert('Failed to download report. Please try on a desktop.');
    }
  };"""

assert old_handle in code, "old_handle not found"
code = code.replace(old_handle, new_handle)

# 2. Move dashboardRef from <main> to the inner content <div>
old_main = """      {/* Main Dashboard */}
      <main ref={dashboardRef} className="flex-1 bg-[#f8fafc] lg:rounded-l-2xl overflow-hidden flex flex-col h-screen overflow-y-auto relative">
        <div className="p-6 md:p-8">"""

new_main = """      {/* Main Dashboard */}
      <main className="flex-1 bg-[#f8fafc] lg:rounded-l-2xl overflow-hidden flex flex-col h-screen overflow-y-auto relative">
        <div ref={dashboardRef} className="p-6 md:p-8">"""

assert old_main in code, "old_main not found"
code = code.replace(old_main, new_main)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully fixed PDF full content capture and pagination!")
