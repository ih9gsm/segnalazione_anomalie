let count = 0;
const btn = document.getElementById('btn');
const counter = document.getElementById('count');
btn.addEventListener('click', () => {
  count++;
  counter.textContent = String(count);
});
