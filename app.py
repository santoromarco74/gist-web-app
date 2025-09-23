# app.py - CORRETTO
from flask import Flask, render_template, request, jsonify
from gist_calculator import GISTCalculator  # Import diretto senza app.
from questionnaire import QUESTIONNAIRE     # Import diretto
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
    try:
        answers = request.json
        calculator = GISTCalculator(answers.get('company_name', 'Anonymous'))
        results = calculator.calculate_score(answers)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)