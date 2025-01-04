const themeToggle = document.getElementById('theme-toggle');
        
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
    themeToggle.checked = savedTheme === 'dark';
}

if (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.setAttribute('data-theme', 'dark');
    themeToggle.checked = true;
}

themeToggle.addEventListener('change', function(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    }
});

document.getElementById('image').addEventListener('change', function(e) {
    const fileName = e.target.files[0]?.name || 'Nenhum arquivo selecionado';
    const button = e.target.previousElementSibling;
    button.textContent = fileName;
});