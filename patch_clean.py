import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_form = '''const UserInfoForm = ({ onSubmit, onBack }) => {
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
};'''

new_form = '''const UserInfoForm = ({ onSubmit, onBack }) => {
  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    const scriptURL = 'https://script.google.com/macros/s/AKfycbyKVpT1goIoymf2reDW_a5zs0ZfmQ1CdVEqCWzXUWWqSX-W3kRvjkdYZpiQp13cEScm/exec';
    
    fetch(scriptURL, {
      method: 'POST',
      mode: 'no-cors',
      headers: {
        'Content-Type': 'text/plain',
      },
      body: JSON.stringify(formData)
    })
    .then(() => {
      setIsSubmitting(false);
      onSubmit(formData);
    })
    .catch(error => {
      console.error('Error saving to sheets:', error);
      setIsSubmitting(false);
      onSubmit(formData); // Proceed to test even if tracking fails
    });
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
            <button type="submit" disabled={isSubmitting} className={lex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>
              {isSubmitting ? 'Starting...' : 'Start Test →'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};'''

if old_form in code:
    code = code.replace(old_form, new_form)
    with open('src/App.jsx', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Success")
else:
    print("Old form not found exactly as written.")
