import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Add useEffect to Assessment
pattern = r'const Assessment = \(\{ onComplete \}\) => \{\s*const \[currentStep, setCurrentStep\] = useState\(1\);'
replacement = r'''const Assessment = ({ onComplete }) => {
  const [currentStep, setCurrentStep] = useState(1);
  
  React.useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'instant' });
  }, [currentStep]);'''
code = re.sub(pattern, replacement, code)

# Let's also do it for UserInfoForm if needed
pattern_userinfo = r'const UserInfoForm = \(\{ onSubmit, onBack \}\) => \{\s*const \[formData, setFormData\]'
replacement_userinfo = r'''const UserInfoForm = ({ onSubmit, onBack }) => {
  React.useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'instant' });
  }, []);
  const [formData, setFormData]'''
code = re.sub(pattern_userinfo, replacement_userinfo, code)


with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
