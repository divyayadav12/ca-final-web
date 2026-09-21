with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_user_info_form = """const UserInfoForm = ({ onSubmit, onBack }) => {
  React.useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'instant' });
  }, []);
  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const digits = formData.phone.replace(/\\D/g, '');
    const phone10 = (digits.length === 12 && digits.startsWith('91')) ? digits.slice(2) : digits;
    
    if (!/^\\d{10}$/.test(phone10)) {
      alert('Please enter a valid 10-digit mobile number.');
      return;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formData.email)) {
      alert('Please enter a valid email address.');
      return;
    }

    setIsSubmitting(true);
    const scriptURL = 'https://script.google.com/macros/s/AKfycbzlK48p9oZf2f8Y0l437bU9cproU3f3y1Pm8Y8tfHnMxfXMVKbx2cSQNfqu0t7Un23b/exec';
    
    fetch(scriptURL, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain' },
      body: JSON.stringify(formData)
    }).catch(err => console.error(err));
    
    setTimeout(() => {
      setIsSubmitting(false);
      onSubmit(formData);
    }, 400);
  };

  return (
    <div className="min-h-screen bg-[#111] text-white flex flex-col items-center justify-center p-6 font-sans relative overflow-hidden">
      <div className="bg-gray-900 border border-gray-800 p-6 md:p-8 rounded-2xl w-full max-w-md relative z-10 shadow-2xl">
        <FastLogo className="mb-8 scale-90 origin-left" />
        <h2 className="text-2xl font-bold mb-2">Student Details</h2>
        <p className="text-gray-400 mb-6 text-sm">Please enter your details to start the Reality Check.</p>
        
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
            <button type="submit" disabled={isSubmitting} className={`flex-1 ${isSubmitting ? 'bg-red-900 cursor-not-allowed' : 'bg-[#e51c24] hover:bg-red-700'} text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20`}>
              {isSubmitting ? 'Starting...' : 'Start Test →'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};"""

new_user_info_form = """const UserInfoForm = ({ onSubmit, onBack }) => {
  React.useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'instant' });
  }, []);
  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');
  const [alreadyRegisteredModal, setAlreadyRegisteredModal] = useState({ show: false, email: '' });

  // Real Email & Mobile Verification logic
  const validateForm = () => {
    setErrorMsg('');

    // 1. Name Check
    if (!formData.name || formData.name.trim().length < 2) {
      setErrorMsg('Please enter your full name.');
      return null;
    }

    // 2. Mobile Verification
    const digits = formData.phone.replace(/\\D/g, '');
    const phone10 = (digits.length === 12 && digits.startsWith('91')) ? digits.slice(2) : digits;

    if (!/^[6-9]\\d{9}$/.test(phone10)) {
      setErrorMsg('Please enter a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9.');
      return null;
    }

    if (/^(\\d)\\1{9}$/.test(phone10)) {
      setErrorMsg('Please enter a genuine mobile number (repeated digits like 9999999999 not allowed).');
      return null;
    }

    const dummyPhones = ['9876543210', '9898989898', '9123456789', '9000000000', '6789012345', '7890123456', '8901234567'];
    if (dummyPhones.includes(phone10)) {
      setErrorMsg('Please enter a genuine mobile number.');
      return null;
    }

    // 3. Email Verification
    const cleanEmail = formData.email.trim().toLowerCase();
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,10}$/;
    if (!emailRegex.test(cleanEmail)) {
      setErrorMsg('Please enter a valid email address (e.g. yourname@gmail.com).');
      return null;
    }

    const parts = cleanEmail.split('@');
    if (parts.length !== 2) {
      setErrorMsg('Invalid email format.');
      return null;
    }
    const [userPart, domainPart] = parts;

    if (userPart.length < 3) {
      setErrorMsg('Email username must be at least 3 characters long.');
      return null;
    }

    const fakePrefixes = ['test', 'dummy', 'fake', 'asdf', 'sample', 'temp', 'admin', 'user', 'unknown', 'abcd', '1234', 'abc', 'xyz', 'demo'];
    if (fakePrefixes.includes(userPart) || /^\\d+$/.test(userPart)) {
      setErrorMsg('Please enter your genuine personal email address.');
      return null;
    }

    // Common domain typo auto-checks
    const typoDomains = {
      'gmil.com': 'gmail.com', 'gamil.com': 'gmail.com', 'gnail.com': 'gmail.com',
      'gmaill.com': 'gmail.com', 'gmai.com': 'gmail.com', 'gmial.com': 'gmail.com',
      'yaho.com': 'yahoo.com', 'yahooo.com': 'yahoo.com', 'hotmial.com': 'hotmail.com',
      'outlok.com': 'outlook.com', 'redif.com': 'rediffmail.com', 'rediff.com': 'rediffmail.com'
    };
    if (typoDomains[domainPart]) {
      setErrorMsg(`Did you mean @${typoDomains[domainPart]}? Please correct the email address.`);
      return null;
    }

    const disposableDomains = [
      'mailinator.com', 'tempmail.com', '10minutemail.com', 'guerrillamail.com',
      'yopmail.com', 'throwawaymail.com', 'sharklasers.com', 'dispostable.com',
      'getnada.com', 'mohmal.com', 'inboxkitten.com', 'fakeinbox.com'
    ];
    if (disposableDomains.includes(domainPart)) {
      setErrorMsg('Disposable or temporary email addresses are not allowed. Please enter your real email.');
      return null;
    }

    return {
      name: formData.name.trim(),
      phone: phone10,
      email: cleanEmail
    };
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const validated = validateForm();
    if (!validated) return;

    // Check if email already registered (Device / Local Storage check)
    let registeredEmails = [];
    try {
      registeredEmails = JSON.parse(localStorage.getItem('ca_final_registered_emails') || '[]');
    } catch (err) {
      registeredEmails = [];
    }

    if (registeredEmails.includes(validated.email)) {
      setAlreadyRegisteredModal({ show: true, email: validated.email });
      return;
    }

    setIsSubmitting(true);
    const scriptURL = 'https://script.google.com/macros/s/AKfycbzlK48p9oZf2f8Y0l437bU9cproU3f3y1Pm8Y8tfHnMxfXMVKbx2cSQNfqu0t7Un23b/exec';
    
    try {
      const response = await fetch(scriptURL, {
        method: 'POST',
        headers: { 'Content-Type': 'text/plain' },
        body: JSON.stringify({
          ...validated,
          action: 'register',
          timestamp: new Date().toISOString()
        })
      });

      try {
        const result = await response.json();
        if (result && (result.status === 'already_registered' || result.already_registered || result.error === 'already_registered')) {
          setIsSubmitting(false);
          setAlreadyRegisteredModal({ show: true, email: validated.email });
          if (!registeredEmails.includes(validated.email)) {
            registeredEmails.push(validated.email);
            localStorage.setItem('ca_final_registered_emails', JSON.stringify(registeredEmails));
          }
          return;
        }
      } catch (parseErr) {
        // if response is not JSON, proceed
      }
    } catch (err) {
      console.warn('Apps Script submission notice:', err);
    }

    // Save email in registered emails list so they cannot retake
    if (!registeredEmails.includes(validated.email)) {
      registeredEmails.push(validated.email);
      localStorage.setItem('ca_final_registered_emails', JSON.stringify(registeredEmails));
    }

    setTimeout(() => {
      setIsSubmitting(false);
      onSubmit(validated);
    }, 400);
  };

  return (
    <div className="min-h-screen bg-[#111] text-white flex flex-col items-center justify-center p-6 font-sans relative overflow-hidden">
      <div className="bg-gray-900 border border-gray-800 p-6 md:p-8 rounded-2xl w-full max-w-md relative z-10 shadow-2xl">
        <FastLogo className="mb-8 scale-90 origin-left" />
        <h2 className="text-2xl font-bold mb-2">Student Details</h2>
        <p className="text-gray-400 mb-6 text-sm">Please enter your details to start the Reality Check.</p>
        
        {errorMsg && (
          <div className="mb-5 p-3.5 bg-red-950/70 border border-red-500/40 rounded-xl text-red-200 text-xs flex items-start gap-2.5 animate-fadeIn">
            <AlertCircle className="w-4 h-4 text-[#e51c24] shrink-0 mt-0.5" />
            <span className="leading-relaxed">{errorMsg}</span>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">Full Name</label>
            <input 
              required 
              type="text" 
              value={formData.name} 
              onChange={e => { setFormData({...formData, name: e.target.value}); setErrorMsg(''); }} 
              className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none transition-colors" 
              placeholder="e.g. Rahul Kumar" 
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">Contact Number (10 Digits)</label>
            <input 
              required 
              type="tel" 
              value={formData.phone} 
              onChange={e => { setFormData({...formData, phone: e.target.value}); setErrorMsg(''); }} 
              className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none transition-colors" 
              placeholder="e.g. 9826012345" 
            />
            <div className="text-[11px] text-gray-500 mt-1">Enter valid Indian mobile number starting with 6, 7, 8, or 9</div>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-1">Email Address</label>
            <input 
              required 
              type="email" 
              value={formData.email} 
              onChange={e => { setFormData({...formData, email: e.target.value}); setErrorMsg(''); }} 
              className="w-full bg-black border border-gray-700 rounded-lg p-3 text-white focus:border-[#e51c24] outline-none transition-colors" 
              placeholder="e.g. rahul.kumar@gmail.com" 
            />
            <div className="text-[11px] text-gray-500 mt-1">Your report will be tied to this verified email address</div>
          </div>

          <div className="pt-4 flex gap-4">
            <button type="button" onClick={onBack} className="flex-1 bg-gray-800 hover:bg-gray-700 text-white font-bold py-3 rounded-lg transition-colors cursor-pointer">Back</button>
            <button type="submit" disabled={isSubmitting} className={`flex-1 ${isSubmitting ? 'bg-red-900 cursor-not-allowed' : 'bg-[#e51c24] hover:bg-red-700'} text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20 cursor-pointer`}>
              {isSubmitting ? 'Verifying...' : 'Start Test →'}
            </button>
          </div>
        </form>
      </div>

      {/* Email Already Registered Popup Modal */}
      {alreadyRegisteredModal.show && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm" onClick={() => setAlreadyRegisteredModal({ show: false, email: '' })}>
          <div className="bg-[#111] border border-gray-700 rounded-2xl w-full max-w-sm shadow-2xl relative overflow-hidden text-center p-6" onClick={e => e.stopPropagation()}>
            <div className="w-16 h-16 bg-red-950 border border-red-500/30 rounded-full flex items-center justify-center mx-auto mb-4 text-[#e51c24]">
              <AlertCircle className="w-8 h-8" />
            </div>
            <h3 className="text-xl font-bold text-white mb-2">Email is Already Registered</h3>
            <p className="text-gray-300 text-sm mb-4 leading-relaxed">
              The email address <span className="text-[#e51c24] font-semibold">{alreadyRegisteredModal.email}</span> has already been registered and used to take the CA Final Reality Check.
            </p>
            <div className="bg-gray-900 border border-gray-800 rounded-xl p-3 text-xs text-gray-400 mb-6 text-left space-y-1">
              <div>• Ek email address se <strong>sirf 1 baar</strong> test diya ja sakta hai.</div>
              <div>• Agar aap dobara guidance chahte hain, toh kripya FAST mentors se sampark karein.</div>
            </div>
            <div className="space-y-3">
              <button
                onClick={() => {
                  setAlreadyRegisteredModal({ show: false, email: '' });
                  setFormData(prev => ({ ...prev, email: '' }));
                }}
                className="w-full bg-[#e51c24] hover:bg-red-700 text-white font-bold py-3 rounded-xl transition-colors shadow-lg shadow-red-500/20 text-sm cursor-pointer"
              >
                Try With Another Email
              </button>
              <a
                href="https://www.fast.edu.in/"
                target="_blank"
                rel="noreferrer"
                className="block w-full bg-gray-800 hover:bg-gray-700 text-gray-200 font-semibold py-3 rounded-xl transition-colors text-sm"
              >
                Visit F.A.S.T. Website →
              </a>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};"""

assert old_user_info_form in code, "old_user_info_form not found!"
code = code.replace(old_user_info_form, new_user_info_form)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated UserInfoForm with strict email/mobile verification and duplicate email prevention modal!")
