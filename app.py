# app.py - GIST Assessment Web Application
from flask import Flask, render_template, request, jsonify, send_file
from gist_calculator import GISTCalculator
from questionnaire import QUESTIONNAIRE, COMPONENT_LABELS
import json
from datetime import datetime
import io

app = Flask(__name__)
app.secret_key = 'gist-framework-2025-secure-key'

@app.route('/')
def home():
    """Homepage con introduzione al GIST Framework."""
    return render_template('index.html')

@app.route('/assessment')
def assessment():
    """
    Pagina assessment interattivo con questionario completo.
    """
    return render_template(
        'assessment.html', 
        questions=QUESTIONNAIRE,
        component_labels=COMPONENT_LABELS
    )

@app.route('/api/calculate', methods=['POST'])
def calculate_gist():
    """
    API endpoint per calcolo GIST Score.
    
    Request body:
    {
        "company_name": "Nome Azienda",
        "answers": {
            "physical": {"power_supply": 60, ...},
            "architectural": {...},
            "security": {...},
            "compliance": {...}
        }
    }
    """
    try:
        data = request.json
        company_name = data.get('company_name', 'Organizzazione')
        answers = data.get('answers', {})
        
        # Validazione base
        if not answers:
            return jsonify({'error': 'Nessuna risposta fornita'}), 400
        
        # Calcola GIST Score
        calculator = GISTCalculator(company_name)
        results = calculator.calculate_score(answers)
        
        # Aggiungi timestamp
        results['timestamp'] = datetime.now().isoformat()
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/results')
def results():
    """
    Pagina risultati (riceve dati via query params o POST).
    """
    return render_template('results.html')

@app.route('/api/generate-pdf', methods=['POST'])
def generate_pdf():
    """
    Genera report PDF dettagliato.
    TODO: implementare generazione PDF con reportlab
    """
    try:
        data = request.json
        # Implementeremo questo dopo
        return jsonify({'status': 'coming_soon'}), 501
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/about')
def about():
    """Pagina informativa sul framework GIST."""
    return render_template('about.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Development mode
    app.run(debug=True, host='0.0.0.0', port=5000)
