with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Result component parameter to accept userData
old_result_sig = "const Result = ({ answers, onRetake }) => {"
new_result_sig = "const Result = ({ answers, userData, onRetake }) => {"
assert old_result_sig in code, "old_result_sig not found"
code = code.replace(old_result_sig, new_result_sig)

# 2. Update handleDownload to handle multi-page PDFs, CORS, and proper naming
old_handle_download = """  const handleDownload = async () => {
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
  };"""

new_handle_download = """  const handleDownload = async () => {
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

assert old_handle_download in code, "old_handle_download not found"
code = code.replace(old_handle_download, new_handle_download)

# 3. Update top area of dashboardRef to include official FAST branding & student details
old_top_area = """          {/* Mobile logo bar - only visible when sidebar is hidden */}
          <div className="flex items-center mb-6 lg:hidden">
            <FastLogo className="max-w-[120px]" />
            <div className="ml-4 font-bold text-[#1a2b4b] text-base leading-tight">
              CA Final Nov 26<br/>
              <span className="text-gray-500 text-xs font-semibold">Reality Check</span>
            </div>
          </div>

          <div className="flex justify-between items-center mb-8 flex-wrap gap-4">
            <div>
              <h1 className="text-3xl font-bold text-[#1a2b4b]">Your CA Final Reality Check Result</h1>
              <p className="text-gray-500 font-medium mt-1">Here's your complete preparation analysis based on your responses.</p>
            </div>
            <div className="flex gap-4">
              <button onClick={onRetake} className="px-5 py-2.5 bg-white border border-gray-300 rounded-lg text-gray-700 font-bold hover:bg-gray-50 flex items-center">
                <RefreshCw className="w-4 h-4 mr-2" /> Retake Test
              </button>
              <button onClick={handleDownload} className="px-5 py-2.5 bg-[#e51c24] rounded-lg text-white font-bold hover:bg-red-700 flex items-center shadow-md">
                Download My Report
              </button>
            </div>
          </div>"""

new_top_area = """          {/* Official Report Header Banner - Always captured in PDF & Dashboard */}
          <div className="bg-white p-5 md:p-6 rounded-2xl shadow-sm border border-gray-200 mb-6 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
            <div className="flex items-center gap-4">
              <FastLogo className="max-w-[130px] md:max-w-[150px]" />
              <div className="border-l-2 border-gray-200 pl-4">
                <div className="text-[10px] md:text-xs font-bold text-[#e51c24] uppercase tracking-wider">Official Assessment Report</div>
                <div className="text-lg md:text-2xl font-black text-[#1a2b4b] leading-tight">CA Final Nov 26 Reality Check</div>
                <div className="text-[11px] md:text-xs text-gray-500 font-medium">Detailed Preparation & Strategic Advisory Report</div>
              </div>
            </div>

            {userData?.name && (
              <div className="bg-[#f8fafc] border border-gray-200 rounded-xl px-4 py-2.5 text-xs text-gray-600 w-full sm:w-auto">
                <div className="font-bold text-[#1a2b4b] text-sm">{userData.name}</div>
                {userData.phone && <div className="text-gray-500 mt-0.5">📞 {userData.phone}</div>}
                {userData.email && <div className="text-gray-500">✉️ {userData.email}</div>}
              </div>
            )}
          </div>

          <div className="flex justify-between items-center mb-8 flex-wrap gap-4">
            <div>
              <h1 className="text-2xl md:text-3xl font-bold text-[#1a2b4b]">Performance Overview</h1>
              <p className="text-gray-500 font-medium mt-1 text-sm">Here is your complete preparation analysis and subject-wise score breakdown.</p>
            </div>
            <div className="flex gap-4" data-html2canvas-ignore="true">
              <button onClick={onRetake} className="px-5 py-2.5 bg-white border border-gray-300 rounded-lg text-gray-700 font-bold hover:bg-gray-50 flex items-center text-sm shadow-sm cursor-pointer">
                <RefreshCw className="w-4 h-4 mr-2" /> Retake Test
              </button>
              <button onClick={handleDownload} className="px-5 py-2.5 bg-[#e51c24] rounded-lg text-white font-bold hover:bg-red-700 flex items-center shadow-md text-sm cursor-pointer">
                <FileText className="w-4 h-4 mr-2" /> Download My Report
              </button>
            </div>
          </div>"""

assert old_top_area in code, "old_top_area not found"
code = code.replace(old_top_area, new_top_area)

# 4. Add official FAST Footer inside dashboardRef before the closing </div></div></main>
old_bottom_area = """              <button 
                onClick={() => setShowFastModal(true)}
                className="w-full bg-[#e51c24] hover:bg-red-700 text-white font-bold py-4 rounded-xl flex items-center justify-center transition-colors shadow-lg shadow-red-500/20 text-base gap-2 cursor-pointer"
              >
                Now What Next? Connect with F.A.S.T. <span>→</span>
              </button>
            </div>


          </div>
        </div>
      </main>"""

new_bottom_area = """              <button 
                onClick={() => setShowFastModal(true)}
                className="w-full bg-[#e51c24] hover:bg-red-700 text-white font-bold py-4 rounded-xl flex items-center justify-center transition-colors shadow-lg shadow-red-500/20 text-base gap-2 cursor-pointer"
              >
                Now What Next? Connect with F.A.S.T. <span>→</span>
              </button>
            </div>

            {/* Official FAST Footer Banner - Captured in PDF & Dashboard */}
            <div className="mt-8 bg-white rounded-2xl border border-gray-200 shadow-sm p-6 overflow-hidden">
              <div className="flex flex-col md:flex-row items-center justify-between gap-4 pb-5 border-b border-gray-100">
                <div className="flex items-center gap-4">
                  <FastLogo className="max-w-[130px]" />
                  <div>
                    <div className="font-black text-[#1a2b4b] text-base leading-tight">First Attempt Success Tutorials (F.A.S.T.)</div>
                    <div className="text-xs text-gray-500 font-medium mt-0.5">India's Leading CA Coaching & Mentorship Institute</div>
                  </div>
                </div>
                <div className="text-xs font-semibold text-gray-500 italic text-center md:text-right">
                  "Same Effort. Better Direction. Stronger You."
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 pt-5 text-xs text-gray-600">
                <div className="flex items-start gap-2.5">
                  <Globe className="w-4 h-4 text-[#e51c24] shrink-0 mt-0.5" />
                  <div>
                    <div className="font-bold text-gray-400 uppercase tracking-wider text-[10px]">Official Website</div>
                    <a href="https://www.fast.edu.in/" target="_blank" rel="noreferrer" className="text-[#1a2b4b] font-bold hover:text-[#e51c24] underline">
                      www.fast.edu.in
                    </a>
                  </div>
                </div>

                <div className="flex items-start gap-2.5">
                  <Phone className="w-4 h-4 text-[#e51c24] shrink-0 mt-0.5" />
                  <div>
                    <div className="font-bold text-gray-400 uppercase tracking-wider text-[10px]">Helpline</div>
                    <a href="tel:+919584510000" className="text-[#1a2b4b] font-bold hover:text-[#e51c24]">
                      +91 9584510000
                    </a>
                  </div>
                </div>

                <div className="flex items-start gap-2.5">
                  <Mail className="w-4 h-4 text-[#e51c24] shrink-0 mt-0.5" />
                  <div>
                    <div className="font-bold text-gray-400 uppercase tracking-wider text-[10px]">Student Support</div>
                    <a href="mailto:faststudentcare@gmail.com" className="text-[#1a2b4b] font-bold hover:text-[#e51c24] break-all">
                      faststudentcare@gmail.com
                    </a>
                  </div>
                </div>

                <div className="flex items-start gap-2.5">
                  <MapPin className="w-4 h-4 text-[#e51c24] shrink-0 mt-0.5" />
                  <div>
                    <div className="font-bold text-gray-400 uppercase tracking-wider text-[10px]">Head Office</div>
                    <div className="text-gray-700 leading-tight">
                      M1 Trade Center, South Tukoganj, Indore (MP) - 452001
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </main>"""

assert old_bottom_area in code, "old_bottom_area not found"
code = code.replace(old_bottom_area, new_bottom_area)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated PDF header and footer with FAST details and logo!")
