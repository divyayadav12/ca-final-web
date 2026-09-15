import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add UserInfoForm component above App
user_info_form = '''
const UserInfoForm = ({ onSubmit, onBack }) => {
  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });

  const handleSubmit = (e) => {
    e.preventDefault();
    // Simulate saving to Google Sheets/Database
    console.log("Saving to Excel Database:", formData);
    onSubmit(formData);
  };

  return (
    <div className="min-h-screen bg-[#111] text-white flex flex-col items-center justify-center p-6 font-sans relative overflow-hidden">
      <div className="bg-gray-900 border border-gray-800 p-6 md:p-8 rounded-2xl w-full max-w-md relative z-10 shadow-2xl">
        <FastLogo className="mb-8 scale-90 origin-left" />
        <h2 className="text-2xl font-bold mb-2">Student Details</h2>
        <p className="text-gray-400 mb-6 text-sm">Please enter your details to start the Reality Check. Your report will be saved to our database.</p>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">Full Name</label>
            <input required type="text" value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none transition-colors" placeholder="e.g. Rahul Kumar" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">Contact Number</label>
            <input required type="tel" value={formData.phone} onChange={e => setFormData({...formData, phone: e.target.value})} className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none transition-colors" placeholder="+91 99999 99999" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">Email Address</label>
            <input required type="email" value={formData.email} onChange={e => setFormData({...formData, email: e.target.value})} className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none transition-colors" placeholder="student@example.com" />
          </div>
          
          <div className="pt-4 flex gap-4">
            <button type="button" onClick={onBack} className="flex-1 bg-gray-800 hover:bg-gray-700 text-white font-bold py-3 rounded-lg transition-colors">Back</button>
            <button type="submit" className="flex-1 bg-[#e51c24] hover:bg-red-700 text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20">Start Test →</button>
          </div>
        </form>
      </div>
    </div>
  );
};
'''
code = code.replace('// --- APP WRAPPER ---', user_info_form + '\n// --- APP WRAPPER ---')

# 2. Update App Router
old_app = '''export default function App() {
  const [step, setStep] = useState('landing');
  const [answers, setAnswers] = useState(null);

  return (
    <>
      {step === 'landing' && <Landing onStart={() => setStep('assessment')} onNav={setStep} />}
      {step === 'Home' && <Home onNav={setStep} />}
      {step === 'CA Final' && <CAFinal onNav={setStep} />}
      {step === 'About' && <About onNav={setStep} />}
      {step === 'Contact' && <Contact onNav={setStep} />}
      {step === 'assessment' && (
        <Assessment 
          onComplete={(data) => {
            setAnswers(data);
            setStep('result');
          }} 
        />
      )}
      {step === 'result' && <Result answers={answers} onRetake={() => setStep('landing')} />}
    </>
  );
}'''

new_app = '''export default function App() {
  const [step, setStep] = useState('landing');
  const [answers, setAnswers] = useState(null);
  const [userData, setUserData] = useState(null);

  return (
    <>
      {step === 'landing' && <Landing onStart={() => setStep('userForm')} onNav={setStep} />}
      {step === 'Home' && <Home onNav={setStep} />}
      {step === 'CA Final' && <CAFinal onNav={setStep} />}
      {step === 'About' && <About onNav={setStep} />}
      {step === 'Contact' && <Contact onNav={setStep} />}
      
      {step === 'userForm' && (
        <UserInfoForm 
          onBack={() => setStep('landing')}
          onSubmit={(data) => {
            setUserData(data);
            setStep('assessment');
          }} 
        />
      )}

      {step === 'assessment' && (
        <Assessment 
          onComplete={(data) => {
            setAnswers(data);
            setStep('result');
          }} 
        />
      )}
      
      {step === 'result' && <Result answers={answers} userData={userData} onRetake={() => setStep('landing')} />}
    </>
  );
}'''
code = code.replace(old_app, new_app)

# 3. Fix Landing Page text (remove "No personal info required")
code = code.replace('''<div className="flex items-center text-gray-400 mt-4 text-xs md:text-sm font-medium relative z-20">
          <Lock className="w-3 h-3 mr-2" />
          No personal information required
        </div>''', '''<div className="flex items-center text-gray-400 mt-4 text-xs md:text-sm font-medium relative z-20">
          <Lock className="w-3 h-3 mr-2" />
          Secure & Private Assessment
        </div>''')

# 4. Fix Table Mobile view (Assessment Component)
old_table = '''<table className="w-full min-w-[600px] border-collapse">
                  <thead>
                    <tr>
                      <th className="bg-[#f8fafc] text-left p-4 rounded-tl-lg font-bold text-[#1a2b4b] border-b border-gray-200 w-1/3">Subject</th>
                      {question.options.map((opt, i) => (
                        <th key={i} className={g-[#f8fafc] p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 }>
                          {opt.text}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {SUBJECTS.map((subject, sIdx) => (
                      <tr key={subject.id} className="border-b border-gray-100 hover:bg-gray-50/50 transition-colors">
                        <td className="p-4 font-medium text-[#1a2b4b] text-sm">{subject.name}</td>
                        {question.options.map((opt, oIdx) => {
                          const isSelected = answers[question.id]?.[subject.id] === opt.value;
                          return (
                            <td key={oIdx} className="p-4 text-center">
                              <input 
                                type="radio" 
                                name={${question.id}-}
                                className="custom-radio"
                                checked={isSelected}
                                onChange={() => handleMatrixChange(subject.id, opt.value)}
                              />
                            </td>
                          );
                        })}
                      </tr>
                    ))}
                  </tbody>
                </table>'''

new_table = '''<table className="w-full border-collapse table-fixed">
                  <thead>
                    <tr>
                      <th className="bg-[#f8fafc] text-left p-2 md:p-4 rounded-tl-lg font-bold text-[#1a2b4b] border-b border-gray-200 w-1/3 md:w-1/4 text-[10px] md:text-sm leading-tight">Subject</th>
                      {question.options.map((opt, i) => (
                        <th key={i} className={g-[#f8fafc] p-1 md:p-4 font-bold text-[#1a2b4b] text-center border-b border-gray-200 text-[10px] md:text-sm leading-tight }>
                          {opt.text}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {SUBJECTS.map((subject, sIdx) => (
                      <tr key={subject.id} className="border-b border-gray-100 hover:bg-gray-50/50 transition-colors">
                        <td className="p-2 md:p-4 font-medium text-[#1a2b4b] text-[10px] md:text-sm leading-tight pr-1">
                          {/* Show abbreviation on very small screens if needed, else full name */}
                          <span className="hidden sm:inline">{subject.name}</span>
                          <span className="sm:hidden">{subject.name.split(' (')[0]}</span>
                        </td>
                        {question.options.map((opt, oIdx) => {
                          const isSelected = answers[question.id]?.[subject.id] === opt.value;
                          return (
                            <td key={oIdx} className="p-1 md:p-4 text-center">
                              <input 
                                type="radio" 
                                name={${question.id}-}
                                className="custom-radio transform scale-75 md:scale-100"
                                checked={isSelected}
                                onChange={() => handleMatrixChange(subject.id, opt.value)}
                              />
                            </td>
                          );
                        })}
                      </tr>
                    ))}
                  </tbody>
                </table>'''
code = code.replace(old_table, new_table)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Tasks Complete!")
