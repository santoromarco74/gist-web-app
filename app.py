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
        
       <div style="display: flex; gap: 20px; margin-top: 20px;">
        <a href="/assessment" class="btn">📊 Inizia Assessment →</a>
        <a href="/demo" class="btn" style="background: #6b7280;">📈 Demo JSON</a>
    </div>
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
    <title>GIST Assessment - Valutazione Maturità Digitale GDO</title>
    <style>
        body { 
            font-family: -apple-system, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container { 
            background: white; 
            border-radius: 20px; 
            padding: 40px; 
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        h1 { color: #1f2937; margin-bottom: 10px; }
        .subtitle { color: #6b7280; margin-bottom: 30px; }
        
        .section-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: #4f46e5;
            margin: 30px 0 20px 0;
            padding: 10px;
            background: #f0f9ff;
            border-radius: 8px;
        }
        
        .question { 
            margin: 20px 0; 
            padding: 20px; 
            background: #f9fafb; 
            border-radius: 12px;
            border: 1px solid #e5e7eb;
        }
        .question h3 { 
            margin: 0 0 15px 0; 
            color: #374151;
            font-size: 1rem;
        }
        
        .radio-group {
            display: grid;
            gap: 10px;
        }
        
        .radio-option {
            display: flex;
            align-items: center;
            padding: 12px;
            background: white;
            border: 2px solid #e5e7eb;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .radio-option:hover {
            border-color: #4f46e5;
            background: #f0f9ff;
        }
        
        .radio-option input[type="radio"] {
            margin-right: 12px;
        }
        
        .radio-option input[type="radio"]:checked + label {
            font-weight: 600;
            color: #4f46e5;
        }
        
        .btn-submit {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 16px 40px;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 30px;
            width: 100%;
            transition: transform 0.2s;
        }
        
        .btn-submit:hover {
            transform: translateY(-2px);
        }
        
        .progress {
            height: 10px;
            background: #e5e7eb;
            border-radius: 10px;
            margin: 30px 0;
            overflow: hidden;
        }
        
        .progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            width: 0%;
            transition: width 0.3s;
        }
    </style>
    <script>
        function updateProgress() {
            const total = document.querySelectorAll('input[type="radio"]').length / 4; // 4 opzioni per domanda
            const checked = document.querySelectorAll('input[type="radio"]:checked').length;
            const percent = (checked / total) * 100;
            document.querySelector('.progress-bar').style.width = percent + '%';
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>📊 GIST Assessment Tool</h1>
        <p class="subtitle">Valuta la maturità digitale della tua organizzazione GDO in 5 minuti</p>
        
        <div class="progress">
            <div class="progress-bar"></div>
        </div>
        
        <form method="POST" action="/calculate">
            
            <!-- COMPONENTE FISICA (18%) -->
            <div class="section-title">⚡ Infrastruttura Fisica (18%)</div>
            
            <div class="question">
                <h3>1. Quanti punti vendita gestisci?</h3>
                <div class="radio-group">
                    <div class="radio-option">
                        <input type="radio" name="pv_count" value="25" id="pv1" onchange="updateProgress()">
                        <label for="pv1">1-10 punti vendita</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="pv_count" value="50" id="pv2" onchange="updateProgress()">
                        <label for="pv2">11-50 punti vendita</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="pv_count" value="75" id="pv3" onchange="updateProgress()">
                        <label for="pv3">51-150 punti vendita</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="pv_count" value="100" id="pv4" onchange="updateProgress()">
                        <label for="pv4">Oltre 150 punti vendita</label>
                    </div>
                </div>
            </div>
            
            <div class="question">
                <h3>2. Sistema di backup energetico?</h3>
                <div class="radio-group">
                    <div class="radio-option">
                        <input type="radio" name="backup_power" value="0" id="bp1" onchange="updateProgress()">
                        <label for="bp1">Nessun backup</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="backup_power" value="40" id="bp2" onchange="updateProgress()">
                        <label for="bp2">UPS base (15-30 min)</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="backup_power" value="70" id="bp3" onchange="updateProgress()">
                        <label for="bp3">UPS ridondante (1+ ore)</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="backup_power" value="100" id="bp4" onchange="updateProgress()">
                        <label for="bp4">UPS + Generatore</label>
                    </div>
                </div>
            </div>
            
            <div class="question">
                <h3>3. Connettività principale?</h3>
                <div class="radio-group">
                    <div class="radio-option">
                        <input type="radio" name="connectivity" value="25" id="cn1" onchange="updateProgress()">
                        <label for="cn1">ADSL/4G</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="connectivity" value="50" id="cn2" onchange="updateProgress()">
                        <label for="cn2">Mix ADSL/Fibra</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="connectivity" value="75" id="cn3" onchange="updateProgress()">
                        <label for="cn3">Fibra maggioranza PdV</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="connectivity" value="100" id="cn4" onchange="updateProgress()">
                        <label for="cn4">Fibra + backup 5G</label>
                    </div>
                </div>
            </div>
            
            <!-- COMPONENTE ARCHITETTURALE (32%) -->
            <div class="section-title">☁️ Architettura IT (32%)</div>
            
            <div class="question">
                <h3>4. Percentuale servizi in cloud?</h3>
                <div class="radio-group">
                    <div class="radio-option">
                        <input type="radio" name="cloud_percent" value="25" id="cl1" onchange="updateProgress()">
                        <label for="cl1">0-25% (Mostly on-premise)</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="cloud_percent" value="50" id="cl2" onchange="updateProgress()">
                        <label for="cl2">26-50% (Hybrid)</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="cloud_percent" value="75" id="cl3" onchange="updateProgress()">
                        <label for="cl3">51-75% (Cloud-first)</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="cloud_percent" value="100" id="cl4" onchange="updateProgress()">
                        <label for="cl4">76-100% (Cloud-native)</label>
                    </div>
                </div>
            </div>
            
            <div class="question">
                <h3>5. Livello di automazione deployment?</h3>
                <div class="radio-group">
                    <div class="radio-option">
                        <input type="radio" name="automation" value="0" id="au1" onchange="updateProgress()">
                        <label for="au1">Manuale</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="automation" value="40" id="au2" onchange="updateProgress()">
                        <label for="au2">Script base</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="automation" value="70" id="au3" onchange="updateProgress()">
                        <label for="au3">CI/CD parziale</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" name="automation" value="100" id="au4" onchange="updateProgress()">
                        <label for="au4">Full DevOps</label>
                    </div>
                </div>
            </div>
            
            <!-- Aggiungi altre domande per Security e Compliance... -->
            
            <button type="submit" class="btn-submit">
                Calcola il tuo GIST Score →
            </button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/assessment')
def assessment():
    return render_template_string(ASSESSMENT_TEMPLATE)

# Aggiungi questo RESULTS_TEMPLATE prima della funzione calculate
RESULTS_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GIST Score - I tuoi risultati</title>
    <style>
        body { 
            font-family: -apple-system, sans-serif; 
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container { 
            max-width: 900px;
            margin: 0 auto;
            background: white; 
            border-radius: 20px; 
            padding: 40px; 
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        
        .score-header {
            text-align: center;
            padding: 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            color: white;
            margin-bottom: 30px;
        }
        
        .score-value {
            font-size: 72px;
            font-weight: bold;
            margin: 20px 0;
        }
        
        .score-label {
            font-size: 24px;
            opacity: 0.9;
        }
        
        .maturity-badge {
            display: inline-block;
            padding: 10px 30px;
            background: rgba(255,255,255,0.2);
            border-radius: 50px;
            font-size: 18px;
            margin-top: 10px;
        }
        
        .components-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin: 30px 0;
        }
        
        .component-card {
            padding: 20px;
            border-radius: 12px;
            border: 2px solid #e5e7eb;
            position: relative;
            overflow: hidden;
        }
        
        .component-card h3 {
            margin: 0 0 10px 0;
            color: #374151;
            font-size: 16px;
        }
        
        .component-score {
            font-size: 32px;
            font-weight: bold;
            color: #4f46e5;
        }
        
        .component-bar {
            height: 8px;
            background: #e5e7eb;
            border-radius: 4px;
            margin-top: 10px;
            overflow: hidden;
        }
        
        .component-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 4px;
            transition: width 1s ease-out;
        }
        
        .recommendations {
            background: #f0f9ff;
            border-radius: 12px;
            padding: 25px;
            margin-top: 30px;
        }
        
        .recommendations h2 {
            color: #1e40af;
            margin-bottom: 15px;
        }
        
        .recommendation-item {
            background: white;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            border-left: 4px solid #3b82f6;
        }
        
        .priority-high { border-left-color: #ef4444; }
        .priority-medium { border-left-color: #f59e0b; }
        .priority-low { border-left-color: #10b981; }
        
        .actions {
            margin-top: 30px;
            text-align: center;
        }
        
        .btn {
            display: inline-block;
            padding: 14px 30px;
            margin: 0 10px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: transform 0.2s;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        .btn-secondary {
            background: white;
            color: #4f46e5;
            border: 2px solid #4f46e5;
        }
        
        .btn:hover {
            transform: translateY(-2px);
        }
        
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .animate {
            animation: slideUp 0.6s ease-out;
        }
    </style>
</head>
<body>
    <div class="container animate">
        <div class="score-header">
            <div class="score-label">Il tuo GIST Score</div>
            <div class="score-value">{{ "%.1f"|format(score) }}</div>
            <div class="maturity-badge">{{ maturity_level }}</div>
        </div>
        
        <div class="components-grid">
            <div class="component-card">
                <h3>⚡ Infrastruttura Fisica (18%)</h3>
                <div class="component-score">{{ "%.0f"|format(physical) }}/100</div>
                <div class="component-bar">
                    <div class="component-fill" style="width: {{ physical }}%"></div>
                </div>
            </div>
            
            <div class="component-card">
                <h3>☁️ Architettura IT (32%)</h3>
                <div class="component-score">{{ "%.0f"|format(architectural) }}/100</div>
                <div class="component-bar">
                    <div class="component-fill" style="width: {{ architectural }}%"></div>
                </div>
            </div>
            
            <div class="component-card">
                <h3>🔒 Sicurezza (28%)</h3>
                <div class="component-score">{{ "%.0f"|format(security) }}/100</div>
                <div class="component-bar">
                    <div class="component-fill" style="width: {{ security }}%"></div>
                </div>
            </div>
            
            <div class="component-card">
                <h3>📋 Conformità (22%)</h3>
                <div class="component-score">{{ "%.0f"|format(compliance) }}/100</div>
                <div class="component-bar">
                    <div class="component-fill" style="width: {{ compliance }}%"></div>
                </div>
            </div>
        </div>
        
        <div class="recommendations">
            <h2>🎯 Raccomandazioni Prioritarie</h2>
            {% for rec in recommendations %}
            <div class="recommendation-item {{ rec.priority }}">
                <strong>{{ rec.title }}</strong><br>
                {{ rec.description }}
            </div>
            {% endfor %}
        </div>
        
        <div class="actions">
            <a href="/" class="btn btn-secondary">← Torna alla Home</a>
            <a href="/assessment" class="btn btn-primary">Rifai Assessment</a>
        </div>
    </div>
    
    <script>
        // Anima le barre dopo il caricamento
        window.onload = function() {
            document.querySelectorAll('.component-fill').forEach(function(bar) {
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(function() {
                    bar.style.width = width;
                }, 100);
            });
        }
    </script>
</body>
</html>
"""

# Funzione calculate completa
@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Calcola il GIST Score basato sulle risposte del questionario
    """
    # Raccogli tutte le risposte dal form
    answers = request.form.to_dict()
    
    # Lista delle domande per componente (aggiungi tutte le tue domande qui)
    physical_questions = ['pv_count', 'backup_power', 'connectivity', 'hardware_age', 'datacenter']
    architectural_questions = ['cloud_percent', 'automation', 'scalability', 'microservices', 'recovery_time']
    security_questions = ['mfa_coverage', 'patch_frequency', 'incident_response', 'network_segmentation', 'backup_test']
    compliance_questions = ['gdpr_ready', 'pci_compliance', 'audit_frequency', 'training_hours', 'documentation']
    
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
    security = calculate_average(security_questions, answers)
    compliance = calculate_average(compliance_questions, answers)
    
    # Se alcune componenti non hanno domande, usa valori default
    if physical == 0:
        physical = 45  # Default per demo
    if architectural == 0:
        architectural = 40
    if security == 0:
        security = 50
    if compliance == 0:
        compliance = 55
    
    # Applica la formula GIST con i pesi corretti
    gamma = 0.95
    gist_score = (
        0.18 * (physical ** gamma) +
        0.32 * (architectural ** gamma) +
        0.28 * (security ** gamma) +
        0.22 * (compliance ** gamma)
    )
    
    # Determina il livello di maturità
    if gist_score < 25:
        maturity_level = "Iniziale"
        maturity_description = "Infrastruttura legacy con ampi margini di miglioramento"
    elif gist_score < 50:
        maturity_level = "In Sviluppo"
        maturity_description = "Modernizzazione in corso, buone basi per crescita"
    elif gist_score < 75:
        maturity_level = "Avanzato"
        maturity_description = "Infrastruttura moderna con ottime performance"
    else:
        maturity_level = "Ottimizzato"
        maturity_description = "Best-in-class, leader digitale nel settore"
    
    # Genera raccomandazioni basate sui punteggi
    recommendations = []
    
    # Trova la componente più debole per priorità
    components = {
        'Infrastruttura Fisica': physical,
        'Architettura IT': architectural,
        'Sicurezza': security,
        'Conformità': compliance
    }
    
    # Ordina per punteggio (dal più basso)
    sorted_components = sorted(components.items(), key=lambda x: x[1])
    
    # Raccomandazioni per la componente più debole
    weakest_component, weakest_score = sorted_components[0]
    
    if weakest_component == 'Infrastruttura Fisica' and weakest_score < 60:
        recommendations.append({
            'title': '🔴 Priorità Alta: Potenzia l\'infrastruttura fisica',
            'description': 'Investi in UPS ridondanti, migliora la connettività a fibra ottica e aggiorna l\'hardware obsoleto.',
            'priority': 'priority-high'
        })
    elif weakest_component == 'Architettura IT' and weakest_score < 60:
        recommendations.append({
            'title': '🔴 Priorità Alta: Modernizza l\'architettura IT',
            'description': 'Migra verso il cloud, implementa CI/CD e adotta microservizi per maggiore agilità.',
            'priority': 'priority-high'
        })
    elif weakest_component == 'Sicurezza' and weakest_score < 60:
        recommendations.append({
            'title': '🔴 Priorità Alta: Rafforza la sicurezza',
            'description': 'Implementa MFA, aumenta la frequenza di patching e adotta un approccio Zero Trust.',
            'priority': 'priority-high'
        })
    elif weakest_component == 'Conformità' and weakest_score < 60:
        recommendations.append({
            'title': '🔴 Priorità Alta: Migliora la conformità',
            'description': 'Assicura compliance GDPR/PCI-DSS, aumenta la formazione e documenta i processi.',
            'priority': 'priority-high'
        })
    
    # Raccomandazioni generali basate sul punteggio totale
    if gist_score < 50:
        recommendations.append({
            'title': '🟡 Quick Win: Automazione dei processi',
            'description': 'Inizia con l\'automazione dei backup e del patching per ridurre rischi e costi operativi.',
            'priority': 'priority-medium'
        })
        recommendations.append({
            'title': '🟢 Formazione del personale',
            'description': 'Investi in formazione cybersecurity per ridurre il rischio umano del 60%.',
            'priority': 'priority-low'
        })
    elif gist_score < 75:
        recommendations.append({
            'title': '🟡 Ottimizzazione Cloud',
            'description': 'Ottimizza i costi cloud con reserved instances e auto-scaling intelligente.',
            'priority': 'priority-medium'
        })
        recommendations.append({
            'title': '🟢 Implementa DevSecOps',
            'description': 'Integra la sicurezza nel ciclo di sviluppo per prevenire vulnerabilità.',
            'priority': 'priority-low'
        })
    else:
        recommendations.append({
            'title': '🟢 Mantieni l\'eccellenza',
            'description': 'Continua con audit regolari e resta aggiornato sulle best practice emergenti.',
            'priority': 'priority-low'
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