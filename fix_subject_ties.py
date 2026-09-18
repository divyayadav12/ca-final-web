import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_sort = """  // Strongest / Weakest
  const sortedSubjects = [...subjectScores].sort((a, b) => b.score - a.score);
  const strongest = sortedSubjects[0];
  const weakest = sortedSubjects[sortedSubjects.length - 1];"""

new_sort = """  // Strongest / Weakest
  const sortedSubjects = [...subjectScores].sort((a, b) => b.score - a.score);
  const strongest = sortedSubjects[0];
  const weakest = sortedSubjects[sortedSubjects.length - 1];
  
  const highestScore = strongest.score;
  const strongestList = sortedSubjects.filter(s => s.score === highestScore);
  let strongestName = strongestList[0].name.split(' (')[0];
  if (strongestList.length === sortedSubjects.length) {
    strongestName = 'All Subjects (Tie)';
  } else if (strongestList.length > 1) {
    strongestName = strongestName + ' & ' + (strongestList.length - 1) + ' more';
  }

  const lowestScore = weakest.score;
  const weakestList = sortedSubjects.filter(s => s.score === lowestScore);
  let weakestName = weakestList[0].name.split(' (')[0];
  if (weakestList.length === sortedSubjects.length) {
    weakestName = 'All Subjects (Tie)';
  } else if (weakestList.length > 1) {
    weakestName = weakestName + ' & ' + (weakestList.length - 1) + ' more';
  }"""

code = code.replace(old_sort, new_sort)
code = code.replace("{strongest.name.split(' (')[0]}", "{strongestName}")
code = code.replace("{weakest.name}", "{weakestName}")

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(code)
