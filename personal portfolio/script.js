// Theme Switcher (Light / Dark Mode)
const themeBtn = document.getElementById('themeToggle');
const htmlElement = document.documentElement;

// Check if user previously saved a theme preference in localStorage
const savedTheme = localStorage.getItem('userTheme');
if (savedTheme) {
htmlElement.setAttribute('data-theme', savedTheme);
}

function toggleTheme() {
const currentTheme = htmlElement.getAttribute('data-theme');
const newTheme = currentTheme === 'light' ? 'dark' : 'light';

  // Set theme on <html> and save choice so it persists across pages
htmlElement.setAttribute('data-theme', newTheme);
localStorage.setItem('userTheme', newTheme);
}

themeBtn.addEventListener('click', toggleTheme);