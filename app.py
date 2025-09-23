# app.py
from flask import Flask, render_template, request, jsonify
from app.gist_calculator import GISTCalculator
from app.questionnaire import QUESTIONNAIRE
import json

app = Flask(__name__)
app.secret_key = 'gist-framework-2024'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assessment')
def assessment():
    return render_template('assessment.html', questions=QUESTIONNAIRE)

@app.route('/calculate', methods=['POST'])
def calculate_gist():
    answers = request.json
    
    calculator = GISTCalculator(answers.get('company_name', 'Anonymous'))
    results = calculator.calculate_score(answers)
    
    return jsonify(results)

@app.route('/report/<gist_score>')
def detailed_report(gist_score):
    # Genera report PDF dettagliato
    return render_template('report.html', score=gist_score)

if __name__ == '__main__':
    app.run(debug=True)