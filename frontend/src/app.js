document.getElementById('reportForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const description = document.getElementById('description').value;
  const recipientsRaw = document.getElementById('recipients').value;
  const recipients = recipientsRaw
    .split(',')
    .map((s) => s.trim())
    .filter(Boolean);
  const status = document.getElementById('status');
  try {
    const id = Date.now();
    const response = await fetch('/reports', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, description, recipients }),
    });
    if (response.ok) {
      status.textContent = 'Segnalazione inviata';
    } else {
      status.textContent = 'Errore durante l\'invio';
    }
  } catch (err) {
    status.textContent = 'Errore durante l\'invio';
  }
});
