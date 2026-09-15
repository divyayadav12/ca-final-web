import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_form_code = '''const UserInfoForm = ({ onSubmit, onBack }) => {
  const [formData, setFormData] = useState({ name: '', phone: '', email: '' });

  const handleSubmit = (e) => {
    e.preventDefault();
    // Simulate saving to Google Sheets/Database
    console.log("Saving to Excel Database:", formData);
    onSubmit(formData);
  };'''

new_form_code = '''const UserInfoForm = ({ onSubmit, onBack }) => {
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
  };'''

code = code.replace(old_form_code, new_form_code)

# Update the submit button to show loading state
old_button = '''<button type="submit" className="flex-1 bg-[#e51c24] hover:bg-red-700 text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20">Start Test →</button>'''
new_button = '''<button type="submit" disabled={isSubmitting} className={lex-1  text-white font-bold py-3 rounded-lg transition-colors shadow-lg shadow-red-500/20}>
              {isSubmitting ? 'Starting...' : 'Start Test →'}
            </button>'''

code = code.replace(old_button, new_button)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
