const form = document.getElementById('todo-form');
const input = document.getElementById('new-task');
const list = document.getElementById('todo-list');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (input.value.trim() !== '') {
        const li = document.createElement('li');
        li.textContent = input.value;
        li.addEventListener('click', () => li.remove());
        list.appendChild(li);
        input.value = '';
    }
});

const toggle = document.getElementById('theme-toggle');
toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});
