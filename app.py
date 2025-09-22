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
        
        <a href="/assessment" class="btn">Prova Demo Assessment →</a>
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
    # Raccogli le risposte
    answers = request.form.to_dict()
    
    # Calcolo semplificato per MVP
    total = sum([int(v) for v in answers.values() if v.isdigit()])
    num_questions = len(answers)
    score = (total / (num_questions * 100)) * 100 if num_questions > 0 else 0
    
    # Determina livello maturità
    if score < 25:
        maturity = "Iniziale"
    elif score < 50:
        maturity = "In Sviluppo"  
    elif score < 75:
        maturity = "Avanzato"
    else:
        maturity = "Ottimizzato"
    
    return f"""
    <html>
        <head><title>GIST Score - Risultato</title></head>
        <body style="font-family: sans-serif; max-width: 600px; margin: 50px auto; text-align: center;">
            <h1>Il tuo GIST Score: {score:.1f}/100</h1>
            <h2>Livello: {maturity}</h2>
            <a href="/">← Torna alla Home</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)