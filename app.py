# app.py
from flask import Flask, render_template, request, jsonify, send_file
from utils.scoring import QuestionnaireProcessor
from utils.pdf_generator import GISTReportGenerator
from gist_framework.gist_calculator import GISTCalculator
import stripe
import os

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assessment')
def assessment():
    return render_template('assessment.html')

@app.route('/calculate', methods=['POST'])
def calculate_gist():
    # Ricevi risposte form
    answers = request.get_json()
    
    # Converti in punteggi componenti
    processor = QuestionnaireProcessor()
    component_scores = processor.process_answers(answers)
    
    # Calcola GIST Score usando il tuo framework
    calc = GISTCalculator("Web Assessment")
    result = calc.calculate_score(component_scores)
    
    return jsonify(result)

@app.route('/generate-report', methods=['POST'])
def generate_report():
    # Genera PDF report
    data = request.get_json()
    
    generator = GISTReportGenerator()
    pdf_path = generator.create_report(data)
    
    return send_file(pdf_path, as_attachment=True)