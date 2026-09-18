with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_handle = """  const handleDownload = async () => {
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

      let renderWidth = pdfWidth;
      let renderHeight = (canvas.height * pdfWidth) / canvas.width;

      // If height slightly exceeds 1 page (up to 30%), scale down to fit cleanly on 1 single page!
      if (renderHeight > pageHeight && renderHeight <= pageHeight * 1.30) {
        const scaleFactor = pageHeight / renderHeight;
        renderWidth = renderWidth * scaleFactor;
        renderHeight = pageHeight;
        const xOffset = (pdfWidth - renderWidth) / 2;
        pdf.addImage(imgData, 'JPEG', xOffset, 0, renderWidth, renderHeight);
      } else if (renderHeight <= pageHeight) {
        pdf.addImage(imgData, 'JPEG', 0, 0, renderWidth, renderHeight);
      } else {
        // Multi-page only if substantial content (>40mm) remains
        let heightLeft = renderHeight;
        let position = 0;
        pdf.addImage(imgData, 'JPEG', 0, position, renderWidth, renderHeight);
        heightLeft -= pageHeight;

        while (heightLeft > 40) {
          position -= pageHeight;
          pdf.addPage();
          pdf.addImage(imgData, 'JPEG', 0, position, renderWidth, renderHeight);
          heightLeft -= pageHeight;
        }
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

assert old_handle in code, "old_handle not found in App.jsx"
code = code.replace(old_handle, new_handle)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated PDF generation to eliminate extra blank page!")
