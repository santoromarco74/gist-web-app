from flask import Flask, render_template, request

app = Flask(__name__)

# --- Logica di Calcolo GIST (invariata) ---
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

def genera_raccomandazione(scores):
    if all(score >= 75 for score in scores.values()):
        return "Ottimo lavoro! La tua infrastruttura è a un livello di maturità elevato. Continua a monitorare e ottimizzare costantemente per mantenere l'eccellenza."
    area_piu_debole = min(scores, key=scores.get)
    consigli = {
        'fisica': "L'area più critica è l'Infrastruttura Fisica. Concentrati sul potenziamento dei sistemi di alimentazione (UPS) e di raffreddamento, e valuta un upgrade della connettività di rete per garantire le fondamenta della resilienza. (Rif. Capitolo 3)",
        'architetturale': "L'area più critica è l'Architettura. È il momento di accelerare la modernizzazione. Valuta la migrazione verso un modello Cloud Ibrido e l'adozione di architetture a Microservizi per aumentare agilità e scalabilità. (Rif. Capitolo 3)",
        'sicurezza': "L'area più critica è la Sicurezza. Implementa un approccio Zero Trust per ridurre la superficie di attacco. Rafforza il monitoraggio con un SIEM e automatizza la risposta agli incidenti per migliorare le metriche temporali. (Rif. Capitolo 2)",
        'conformita': "L'area più critica è la Conformità. Adotta un framework di conformità integrata per armonizzare i controlli di GDPR, PCI-DSS e NIS2. L'automazione dei controlli può ridurre i costi e l'effort manuale fino al 40%. (Rif. Capitolo 4)"
    }
    return consigli[area_piu_debole]

# --- NOVITÀ: Logica per calcolare i punteggi dal questionario ---
def calcola_punteggi_da_questionario(risposte):
    punteggi = {}
    
    # Dimensione Fisica (Max 55 punti)
    punti_fisica = int(risposte.get('alimentazione', 0)) + int(risposte.get('connettivita', 0)) + int(risposte.get('monitoraggio_fisico', 0))
    punteggi['fisica'] = round((punti_fisica / 55) * 100)
    
    # Dimensione Architetturale (Max 60 punti)
    punti_arch = int(risposte.get('arch_core', 0)) + int(risposte.get('disaster_recovery', 0)) + int(risposte.get('deployment', 0))
    punteggi['architetturale'] = round((punti_arch / 60) * 100)
    
    # Dimensione Sicurezza (Max 70 punti)
    punti_sicurezza = int(risposte.get('modello_sicurezza', 0)) + int(risposte.get('iam', 0)) + int(risposte.get('incident_response', 0))
    punteggi['sicurezza'] = round((punti_sicurezza / 70) * 100)

    # Dimensione Conformità (Max 70 punti)
    punti_conf = int(risposte.get('approccio_conf', 0)) + int(risposte.get('audit', 0)) + int(risposte.get('data_gov', 0))
    punteggi['conformita'] = round((punti_conf / 70) * 100)
    
    return punteggi

# La rotta principale ora mostra il questionario
@app.route('/')
def questionario():
    return render_template('questionario.html')

# La rotta '/calcola' ora processa le risposte del questionario
@app.route('/calcola', methods=['POST'])
def calcola():
    try:
        risposte = request.form
        punteggi = calcola_punteggi_da_questionario(risposte)
        
        score_calcolato = calcola_gist_score(punteggi)
        livello = determina_livello_maturita(score_calcolato)
        raccomandazione = genera_raccomandazione(punteggi)
        
        punteggi_per_grafico = list(punteggi.values())
        benchmark_target = [85, 88, 82, 86]

        return render_template('risultati.html', 
                               risultato=score_calcolato, 
                               livello_maturita=livello,
                               dati_grafico=punteggi_per_grafico,
                               dati_benchmark=benchmark_target,
                               raccomandazione=raccomandazione)
    except Exception as e:
        print(f"Errore durante il calcolo: {e}")
        return "Si è verificato un errore durante l'elaborazione del questionario. Assicurati di aver risposto a tutte le domande.", 400

if __name__ == '__main__':
    app.run(debug=True)
