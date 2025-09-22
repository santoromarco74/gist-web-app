// static/js/app.js
document.getElementById('gist-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Raccogli tutte le risposte
    const formData = new FormData(this);
    const answers = {};
    
    for (let [key, value] of formData.entries()) {
        answers[key] = parseInt(value);
    }
    
    // Mostra loading
    document.getElementById('results').style.display = 'none';
    // ... loading spinner ...
    
    try {
        // Calcola GIST Score
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(answers)
        });
        
        const result = await response.json();
        
        // Mostra risultati
        document.getElementById('gist-score').textContent = result.score.toFixed(1);
        document.getElementById('maturity-level').textContent = result.maturity_level;
        document.getElementById('results').style.display = 'block';
        
    } catch (error) {
        alert('Errore nel calcolo. Riprova.');
    }
});