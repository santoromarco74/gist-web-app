# app.py (versione completa e aggiornata)

from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Le funzioni 'calcola_gist_score' e 'determina_livello_maturita' restano invariate
def calcola_gist_score(scores):
    pesi = {'fisica': 0.18, 'architetturale': 0.32, 'sicurezza': 0.28, 'conformita': 0.22}
    gamma = 0.95
    punteggio_finale = sum(pesi[c] * (s ** gamma) for c, s in scores.items())
    return round(punteggio_finale, 2)

def determina_livello_maturita(score):
    if score <= 25: return "Iniziale"
    if score <= 50: return "In Sviluppo"
    if score <= 75: return "Avanzato"
    return "Ottimizzato"

# --- NOVITÀ: La funzione che genera i consigli ---
def genera_raccomandazione(scores):
    """
    Analizza i punteggi e restituisce un consiglio basato sull'area più debole.
    I consigli sono ispirati ai capitoli della tua tesi!
    """
    # Controlla se tutti i punteggi sono alti per un messaggio di congratulazioni
    if all(score >= 75 for score in scores.values()):
        return "Ottimo lavoro! La tua infrastruttura è a un livello di maturità elevato. Continua a monitorare e ottimizzare costantemente per mantenere l'eccellenza."

    # Trova la dimensione con il punteggio più basso
    area_piu_debole = min(scores, key=scores.get)
    
    # Dizionario delle raccomandazioni
    consigli = {
        'fisica': "L'area più critica è l'Infrastruttura Fisica. Concentrati sul potenziamento dei sistemi di alimentazione (UPS) e di raffreddamento, e valuta un upgrade della connettività di rete per garantire le fondamenta della resilienza. (Rif. Capitolo 3)",
        'architetturale': "L'area più critica è l'Architettura. È il momento di accelerare la modernizzazione. Valuta la migrazione verso un modello Cloud Ibrido e l'adozione di architetture a Microservizi per aumentare agilità e scalabilità. (Rif. Capitolo 3)",
        'sicurezza': "L'area più critica è la Sicurezza. Implementa un approccio Zero Trust per ridurre la superficie di attacco. Rafforza il monitoraggio con un SIEM e automatizza la risposta agli incidenti per migliorare le metriche temporali. (Rif. Capitolo 2)",
        'conformita': "L'area più critica è la Conformità. Adotta un framework di conformità integrata per armonizzare i controlli di GDPR, PCI-DSS e NIS2. L'automazione dei controlli può ridurre i costi e l'effort manuale fino al 40%. (Rif. Capitolo 4)"
    }
    
    return consigli[area_piu_debole]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcola', methods=['POST'])
def calcola():
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
        benchmark_target = [85, 88, 82, 86]
        
        # --- NOVITÀ: Chiamiamo la nuova funzione e passiamo il risultato ---
        raccomandazione_generata = genera_raccomandazione(punteggi)

        return render_template('index.html', 
                               risultato=score_calcolato, 
                               livello_maturita=livello,
                               valori_inseriti=punteggi,
                               dati_grafico=punteggi_per_grafico,
                               dati_benchmark=benchmark_target,
                               raccomandazione=raccomandazione_generata) # Passiamo la raccomandazione!
    except (ValueError, KeyError):
        return "Errore nei dati inseriti. Assicurati di compilare tutti i campi con numeri.", 400

# Questa parte non è strettamente necessaria per Render, ma è utile per testare in locale
if __name__ == '__main__':
    app.run(debug=True)