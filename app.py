# app.py
from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calcola_gist_score(scores):
    """Calcola il GIST Score usando la formula completa della tesi."""
    pesi = {'fisica': 0.18, 'architetturale': 0.32, 'sicurezza': 0.28, 'conformita': 0.22}
    gamma = 0.95
    
    punteggio_finale = sum(pesi[c] * (s ** gamma) for c, s in scores.items())
        
    return round(punteggio_finale, 2)

def determina_livello_maturita(score):
    """Determina il livello di maturità in base al punteggio."""
    if score <= 25:
        return "Iniziale"
    elif score <= 50:
        return "In Sviluppo"
    elif score <= 75:
        return "Avanzato"
    else:
        return "Ottimizzato"

@app.route('/')
def index():
    """Mostra la pagina iniziale con valori di default."""
    return render_template('index.html')

# La rotta deve essere esattamente "/calcola" e deve accettare il metodo 'POST'
# app.py (solo la funzione 'calcola' modificata)

@app.route('/calcola', methods=['POST'])
def calcola():
    """Riceve i dati, calcola e mostra i risultati."""
    try:
        punteggi = {
            'fisica': int(request.form['fisica']),
            'architetturale': int(request.form['architetturale']),
            'sicurezza': int(request.form['sicurezza']),
            'conformita': int(request.form['conformita'])
        }
        
        score_calcolato = calcola_gist_score(punteggi)
        livello = determina_livello_maturita(score_calcolato)
        punteggi_per_grafico = list(punteggi.values())

        # --- NOVITÀ: Definiamo i dati per il nostro benchmark ---
        # Questi valori rappresentano un'organizzazione "ottimizzata" (Livello Avanzato/Ottimizzato)
        benchmark_target = [85, 88, 82, 86]

        return render_template('index.html', 
                               risultato=score_calcolato, 
                               livello_maturita=livello,
                               valori_inseriti=punteggi,
                               dati_grafico=punteggi_per_grafico,
                               dati_benchmark=benchmark_target) # Passiamo i nuovi dati!
    except (ValueError, KeyError):
        return "Errore nei dati inseriti. Assicurati di compilare tutti i campi con numeri.", 400

# Questa parte non è strettamente necessaria per Render, ma è utile per testare in locale
if __name__ == '__main__':
    app.run(debug=True)