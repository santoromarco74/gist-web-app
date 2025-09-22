from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>GIST Assessment Tool</title>
            <style>
                body { 
                    font-family: Arial; 
                    max-width: 800px; 
                    margin: 50px auto;
                    padding: 20px;
                }
                h1 { color: #2563eb; }
                .status { 
                    background: #10b981; 
                    color: white; 
                    padding: 10px; 
                    border-radius: 5px;
                }
            </style>
        </head>
        <body>
            <h1>🚀 GIST Web App</h1>
            <p class="status">✅ Deployment su Render funzionante!</p>
            <p>Framework GIST per la valutazione della maturità digitale GDO</p>
            <hr>
            <p>Next steps: Aggiungere il form di assessment</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "app": "gist-web-app"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)