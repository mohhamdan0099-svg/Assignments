// Step 1: Select the root <html> element
const htmlElement = document.documentElement;
// Step 2: Check if the user previously saved a theme preference
const savedTheme = localStorage.getItem('userTheme');

if (savedTheme) {
  htmlElement.setAttribute('data-theme', savedTheme);
}


// Step 3: Function called directly by onclick="handleThemeClick()" in HTML
function handleThemeClick() {
  const currentTheme = htmlElement.getAttribute('data-theme');

  if (currentTheme === 'light') {
    htmlElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('userTheme', 'dark');
  } else {
    htmlElement.setAttribute('data-theme', 'light');
    localStorage.setItem('userTheme', 'light');
  }
}