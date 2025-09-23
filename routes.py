from flask import Blueprint, render_template, request, jsonify, make_response
from .gist_calculator import GISTCalculator
from .questionnaire import QUESTIONNAIRE, calculate_component_score
import io
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/assessment')
def assessment():
    return render_template('assessment.html', questionnaire=QUESTIONNAIRE)

@main_bp.route('/calculate', methods=['POST'])
def calculate():
    # Estrai risposte dal form
    answers = dict(request.form)
    
    # Calcola score per ogni componente
    component_scores = {}
    for component in ['physical', 'architectural', 'security', 'compliance']:
        component_scores[component] = calculate_component_score(answers, component)
    
    # Calcola GIST Score complessivo
    calculator = GISTCalculator()
    gist_score = calculator.calculate_gist_score(component_scores)
    maturity_level = calculator.get_maturity_level(gist_score)
    recommendations = calculator.get_recommendations(component_scores)
    
    results = {
        'gist_score': gist_score,
        'maturity_level': maturity_level,
        'component_scores': component_scores,
        'recommendations': recommendations
    }
    
    return render_template('results.html', results=results)

@main_bp.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Ricrea i risultati dai dati POST
    data = request.get_json()
    
    # Crea PDF in memoria
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Titolo
    title = Paragraph("GIST Assessment Report", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 20))
    
    # GIST Score
    score_text = f"GIST Score: {data['gist_score']}/100"
    score_para = Paragraph(score_text, styles['Heading2'])
    story.append(score_para)
    
    # Livello maturità
    level_text = f"Livello Maturità: {data['maturity_level']}"
    level_para = Paragraph(level_text, styles['Heading3'])
    story.append(level_para)
    story.append(Spacer(1, 20))
    
    # Componenti
    components_title = Paragraph("Punteggi per Componente", styles['Heading2'])
    story.append(components_title)
    
    for comp, score in data['component_scores'].items():
        comp_text = f"{comp.title()}: {score:.1f}/100"
        comp_para = Paragraph(comp_text, styles['Normal'])
        story.append(comp_para)
    
    doc.build(story)
    
    # Prepara response
    buffer.seek(0)
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=gist_assessment.pdf'
    
    return response