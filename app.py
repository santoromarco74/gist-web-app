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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)