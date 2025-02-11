// script.js

// Función para alternar el tema
function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    const currentTheme = body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('theme', currentTheme);
}

// Evento para el botón de cambio de tema
document.getElementById('toggle-theme').addEventListener('click', toggleTheme);

// Verificar el tema guardado en localStorage al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }
});