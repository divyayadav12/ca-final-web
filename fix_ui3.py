import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix 1: submit logic
old_submit_pattern = r'const handleSubmit = \(e\) => \{[\s\S]*?e\.preventDefault\(\);\s*setIsSubmitting\(true\);\s*const scriptURL = \'.*?\';[\s\S]*?fetch\(scriptURL[\s\S]*?\.catch[\s\S]*?\}\);?\s*\};'
new_submit = r"""const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!/^\d{10}$/.test(formData.phone)) {
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
  };"""

code = re.sub(old_submit_pattern, lambda m: new_submit, code)

# Fix 2: inputs
code = code.replace(
    '<input type="tel" required className="w-full bg-[#0a0a0a] border border-gray-800 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-red-500 transition-colors"',
    '<input type="tel" required pattern="[0-9]{10}" maxLength="10" title="10-digit mobile number" className="w-full bg-[#0a0a0a] border border-gray-800 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-red-500 transition-colors"'
)

code = code.replace(
    '<input type="text" required className="w-full bg-[#0a0a0a] border border-gray-800 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-red-500 transition-colors" value={formData.email}',
    '<input type="email" required className="w-full bg-[#0a0a0a] border border-gray-800 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-red-500 transition-colors" value={formData.email}'
)

# Fix 3: table headers text size
code = code.replace(
    'className="px-1 sm:px-2 py-2 sm:py-4 text-center text-[10px] md:text-sm font-semibold text-[#1a2b4b] leading-tight w-16',
    'className="px-0 sm:px-2 py-2 sm:py-4 text-center text-[8px] md:text-sm font-bold text-[#1a2b4b] leading-none whitespace-nowrap w-auto sm:w-16'
)

# Fix 4: footer card pushing up
code = code.replace(
    'className="mt-16 sm:mt-24 w-full max-w-sm mx-auto"',
    'className="mt-4 sm:mt-24 w-full max-w-sm mx-auto z-10 relative"'
)
code = code.replace(
    'className="relative min-h-[500px] flex items-center justify-center pt-8 sm:pt-12 pb-24"',
    'className="relative min-h-[500px] flex items-center justify-center pt-8 sm:pt-12 pb-12 sm:pb-24"'
)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
