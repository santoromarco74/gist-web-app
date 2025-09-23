from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Template HTML inline per ora
HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GIST Assessment Tool</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f3f4f6;
        }
        .container {
            background: white;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        h1 {
            color: #1f2937;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #6b7280;
            font-size: 1.2rem;
            margin-bottom: 30px;
        }
        .status {
            display: inline-block;
            background: #10b981;
            color: white;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 500;
        }
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .info-card {
            background: #f9fafb;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
        }
        .info-card h3 {
            margin: 0 0 10px 0;
            color: #374151;
        }
        .btn {
            display: inline-block;
            background: #3b82f6;
            color: white;
            padding: 12px 24px;
            border-radius: 6px;
            text-decoration: none;
            margin-top: 20px;
            font-weight: 500;
        }
        .btn:hover {
            background: #2563eb;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 GIST Web Assessment</h1>
        <p class="subtitle">Framework per la Valutazione della Maturità Digitale GDO</p>
        <span class="status">✅ App Live su Render!</span>
        
        <div class="info-grid">
            <div class="info-card">
                <h3>📊 GIST Score</h3>
                <p>Valutazione quantitativa della maturità digitale basata su 4 componenti</p>
            </div>
            <div class="info-card">
                <h3>🔒 Security (28%)</h3>
                <p>Zero Trust, ASSA-GDO, incident response</p>
            </div>
            <div class="info-card">
                <h3>☁️ Architecture (32%)</h3>
                <p>Cloud-hybrid, microservizi, automazione</p>
            </div>
            <div class="info-card">
                <h3>⚡ Physical (18%)</h3>
                <p>Infrastruttura, connettività, resilienza</p>
            </div>
            <div class="info-card">
                <h3>📋 Compliance (22%)</h3>
                <p>GDPR, PCI-DSS, NIS2 integrati</p>
            </div>
            <div class="info-card">
                <h3>🎯 Target</h3>
                <p>PMI della GDO italiana (20-200 PdV)</p>
            </div>
        </div>
        
        <a href="/demo" class="btn">Prova Demo Assessment →</a>
    </div>
</body>
</html>
"""



@app.route('/')
def index():
    return render_template_string(HOME_TEMPLATE)

@app.route('/demo')
def demo():
    return jsonify({
        "message": "Demo assessment coming soon!",
        "components": {
            "physical": "18%",
            "architectural": "32%",
            "security": "28%",
            "compliance": "22%"
        },
        "sample_score": 67.5
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"})


# Aggiungi questo al tuo app.py

ASSESSMENT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GIST Assessment - Valutazione</title>
    <style>
        /* Stesso stile base */
        body { font-family: -apple-system, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f3f4f6; }
        .container { background: white; border-radius: 12px; padding: 40px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        h1 { color: #1f2937; }
        
        .question { margin: 20px 0; padding: 20px; background: #f9fafb; border-radius: 8px; }
        .question h3 { margin: 0 0 10px 0; color: #374151; }
        .options { display: flex; gap: 10px; flex-wrap: wrap; }
        .option { padding: 10px 20px; border: 2px solid #e5e7eb; border-radius: 6px; cursor: pointer; background: white; }
        .option:hover { border-color: #3b82f6; }
        .option.selected { background: #3b82f6; color: white; border-color: #3b82f6; }
        .progress { height: 8px; background: #e5e7eb; border-radius: 4px; margin: 20px 0; }
        .progress-fill { height: 100%; background: #3b82f6; border-radius: 4px; transition: width 0.3s; }
        .btn-submit { background: #10b981; color: white; padding: 12px 40px; border: none; border-radius: 6px; font-size: 16px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Assessment GIST</h1>
        <div class="progress"><div class="progress-fill" style="width: 25%"></div></div>
        
        <form method="POST" action="/calculate">
            <!-- FISICA (18%) -->
            <div class="question">
                <h3>1. Quanti punti vendita gestisci?</h3>
                <div class="options">
                    <label class="option"><input type="radio" name="q1" value="10"> 1-10</label>
                    <label class="option"><input type="radio" name="q1" value="30"> 11-50</label>
                    <label class="option"><input type="radio" name="q1" value="60"> 51-100</label>
                    <label class="option"><input type="radio" name="q1" value="80"> 100+</label>
                </div>
            </div>
            
            <div class="question">
                <h3>2. Quale tipo di backup energetico hai?</h3>
                <div class="options">
                    <label class="option"><input type="radio" name="q2" value="0"> Nessuno</label>
                    <label class="option"><input type="radio" name="q2" value="40"> UPS base (15 min)</label>
                    <label class="option"><input type="radio" name="q2" value="70"> UPS ridondante (1h+)</label>
                    <label class="option"><input type="radio" name="q2" value="100"> Generatore + UPS</label>
                </div>
            </div>
            
            <!-- Aggiungi altre domande... -->
            
            <button type="submit" class="btn-submit">Calcola GIST Score →</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/assessment')
def assessment():
    return render_template_string(ASSESSMENT_TEMPLATE)

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Calcola il GIST Score basato sulle risposte del questionario
    """
    # Raccogli tutte le risposte dal form
    answers = request.form.to_dict()
    
    # Liste delle domande per componente
    physical_questions = ['pv_count', 'backup_power', 'connectivity']
    architectural_questions = ['cloud_percent', 'automation']
    security_questions = []  # Aggiungeremo dopo
    compliance_questions = []  # Aggiungeremo dopo
    
    # Funzione helper per calcolare media sicura
    def calculate_average(questions, answers):
        scores = []
        for q in questions:
            if q in answers:
                try:
                    scores.append(float(answers[q]))
                except (ValueError, TypeError):
                    scores.append(0)
        return sum(scores) / len(scores) if scores else 0
    
    # Calcola i punteggi per ogni componente
    physical = calculate_average(physical_questions, answers)
    architectural = calculate_average(architectural_questions, answers)
    
    # Per demo, usa valori fissi per security e compliance se non ci sono domande
    if not security_questions:
        # Usa un valore medio-alto per demo
        security = 65  
    else:
        security = calculate_average(security_questions, answers)
        
    if not compliance_questions:
        # Usa un valore medio-alto per demo
        compliance = 70
    else:
        compliance = calculate_average(compliance_questions, answers)
    
    # Se non ci sono risposte, usa valori demo
    if physical == 0:
        physical = 60
    if architectural == 0:
        architectural = 55
    
    # FORMULA GIST CORRETTA CON NORMALIZZAZIONE
    gamma = 0.95
    weights = {
        'physical': 0.18,
        'architectural': 0.32,
        'security': 0.28,
        'compliance': 0.22
    }
    
    # Calcolo del GIST Score raw
    gist_score_raw = (
        weights['physical'] * (physical ** gamma) +
        weights['architectural'] * (architectural ** gamma) +
        weights['security'] * (security ** gamma) +
        weights['compliance'] * (compliance ** gamma)
    )
    
    # NORMALIZZAZIONE: Il massimo teorico con tutti 100 è ~79.43
    # Quindi normalizziamo per avere 100 come massimo
    MAX_THEORETICAL_SCORE = (
        weights['physical'] * (100 ** gamma) +
        weights['architectural'] * (100 ** gamma) +
        weights['security'] * (100 ** gamma) +
        weights['compliance'] * (100 ** gamma)
    )
    
    # Score normalizzato 0-100
    gist_score = (gist_score_raw / MAX_THEORETICAL_SCORE) * 100
    
    # Ora i livelli di maturità hanno più senso
    if gist_score < 25:
        maturity_level = "Iniziale"
        maturity_description = "Infrastruttura legacy, necessita trasformazione urgente"
    elif gist_score < 50:
        maturity_level = "In Sviluppo"
        maturity_description = "Modernizzazione in corso, sulla strada giusta"
    elif gist_score < 75:
        maturity_level = "Avanzato"
        maturity_description = "Infrastruttura moderna e competitiva"
    else:
        maturity_level = "Ottimizzato"
        maturity_description = "🏆 Eccellenza digitale! Best-in-class nel settore GDO"
    
    # Come raggiungere l'eccellenza - raccomandazioni specifiche
    recommendations = []
    
    # Calcola gap dall'eccellenza per ogni componente
    gaps = {
        'Infrastruttura Fisica': (100 - physical, physical),
        'Architettura IT': (100 - architectural, architectural),
        'Sicurezza': (100 - security, security),
        'Conformità': (100 - compliance, compliance)
    }
    
    # Ordina per gap maggiore (maggior potenziale di miglioramento)
    sorted_gaps = sorted(gaps.items(), key=lambda x: x[1][0], reverse=True)
    
    # Raccomandazioni per raggiungere l'eccellenza
    for component_name, (gap, current_score) in sorted_gaps[:3]:
        if gap > 30:  # Solo se c'è un gap significativo
            if component_name == 'Infrastruttura Fisica':
                if current_score < 70:
                    recommendations.append({
                        'title': f'⚡ Potenzia Infrastruttura (attuale: {current_score:.0f}/100)',
                        'description': 'Per l\'eccellenza: Data center Tier III+, fibra 100% PdV, UPS+generatori ridondanti, edge computing distribuito',
                        'priority': 'priority-high' if gap > 50 else 'priority-medium'
                    })
            elif component_name == 'Architettura IT':
                if current_score < 70:
                    recommendations.append({
                        'title': f'☁️ Modernizza Architettura (attuale: {current_score:.0f}/100)',
                        'description': 'Per l\'eccellenza: 100% cloud-native, microservizi, CI/CD completo, IaC, auto-scaling, multi-cloud orchestration',
                        'priority': 'priority-high' if gap > 50 else 'priority-medium'
                    })
            elif component_name == 'Sicurezza':
                if current_score < 70:
                    recommendations.append({
                        'title': f'🔒 Rafforza Sicurezza (attuale: {current_score:.0f}/100)',
                        'description': 'Per l\'eccellenza: Zero Trust completo, SOC 24/7 con AI, patch 0-day automatiche, pen-test mensili',
                        'priority': 'priority-high' if gap > 50 else 'priority-medium'
                    })
            elif component_name == 'Conformità':
                if current_score < 70:
                    recommendations.append({
                        'title': f'📋 Perfeziona Conformità (attuale: {current_score:.0f}/100)',
                        'description': 'Per l\'eccellenza: Compliance-as-code, audit continui automatizzati, certificazioni multiple (ISO 27001, SOC2)',
                        'priority': 'priority-high' if gap > 50 else 'priority-medium'
                    })
    
    # Se il punteggio è già alto, dai consigli per mantenere l'eccellenza
    if gist_score >= 75:
        recommendations.append({
            'title': '🏆 Mantieni l\'Eccellenza',
            'description': 'Sei nel top 5% del settore! Focus su: innovazione continua, AI/ML adoption, quantum-ready security',
            'priority': 'priority-low'
        })
        recommendations.append({
            'title': '🚀 Diventa un Leader',
            'description': 'Condividi best practices, partecipa a conferenze, ottieni certificazioni avanzate, mentora altre aziende',
            'priority': 'priority-low'
        })
    
    # Aggiungi sempre un consiglio su come migliorare il punteggio
    potential_improvement = min(100 - gist_score, 25)  # Max 25 punti di miglioramento suggerito
    if gist_score < 90:
        recommendations.append({
            'title': f'📈 Potenziale: +{potential_improvement:.0f} punti',
            'description': f'Con investimenti mirati puoi raggiungere un GIST Score di {min(gist_score + potential_improvement, 100):.0f}/100',
            'priority': 'priority-medium'
        })
    
    # Renderizza il template con tutti i dati
    return render_template_string(
        RESULTS_TEMPLATE,
        score=gist_score,
        maturity_level=maturity_level,
        maturity_description=maturity_description,
        physical=physical,
        architectural=architectural,
        security=security,
        compliance=compliance,
        recommendations=recommendations
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)