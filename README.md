# GIST Framework - Digital Maturity Assessment

Web application professionale per la valutazione della maturità digitale nel settore GDO basata sul framework GIST.

## 🎯 Caratteristiche

- ✅ **36 domande strutturate** su 4 dimensioni critiche
- ✅ **Calcolo GIST Score** con formula scientifica validata
- ✅ **Progress bar real-time** e validazione interattiva
- ✅ **Grafici radar e bar chart** per visualizzazione risultati
- ✅ **Raccomandazioni prioritizzate** con ROI stimato
- ✅ **Benchmark settoriale** vs media GDO italiana
- ✅ **Design responsive** con Tailwind CSS
- ✅ **Report dettagliati** con piano d'azione

## 📊 Le 4 Dimensioni GIST

1. **Infrastruttura Fisica (18%)** - Alimentazione, connettività, ridondanza
2. **Architettura (32%)** - Cloud, microservizi, DevOps, API
3. **Sicurezza (28%)** - Identity, network, endpoint, threat detection
4. **Conformità (22%)** - GDPR, PCI-DSS, NIS2, audit

## 🚀 Quick Start - Locale

```bash
# Clona il repository
git clone <your-repo-url>
cd gist-assessment

# Installa dipendenze
pip install -r requirements.txt

# Avvia l'app
python app.py

# Apri browser su http://localhost:5000
```

## ☁️ Deploy su Render

1. **Push del codice su GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo>
   git push -u origin main
   ```

2. **Configura Render**
   - Vai su [render.com](https://render.com)
   - New → Web Service
   - Connetti repository GitHub
   - Configura:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Environment**: Python 3

3. **Deploy automatico**
   - Render farà il deploy automatico ad ogni push su main

## 📁 Struttura Progetto

```
gist-assessment/
├── app.py                      # Flask application principale
├── gist_calculator.py          # GIST Score calculator
├── questionnaire.py            # 36 domande strutturate
├── requirements.txt            # Dipendenze Python
├── templates/
│   ├── base.html              # Template base con navbar
│   ├── index.html             # Homepage
│   ├── assessment.html        # Questionario interattivo
│   ├── results.html           # Pagina risultati con grafici
│   └── about.html             # Informazioni framework
└── static/                     # (Future: CSS, JS, images custom)
```

## 🎨 Tecnologie Utilizzate

- **Backend**: Flask 3.0
- **Frontend**: Tailwind CSS + Chart.js
- **Grafici**: Chart.js per radar e bar charts
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)
- **Deployment**: Gunicorn + Render

## 📈 Roadmap Futuri Sviluppi

### Fase 2 - Business Features
- [ ] Autenticazione utenti (email/password + OAuth)
- [ ] Database PostgreSQL per storico assessment
- [ ] Email delivery con report PDF
- [ ] Payment gateway Stripe (€49/assessment)

### Fase 3 - Premium Features
- [ ] Generazione PDF professionale con reportlab
- [ ] Comparison tracking nel tempo
- [ ] API pubblica per integrazioni
- [ ] Dashboard amministratore

### Fase 4 - AI & Advanced
- [ ] Raccomandazioni AI-powered personalizzate
- [ ] Predictive analytics
- [ ] Multi-lingua (EN/IT/DE)
- [ ] Mobile app nativa

## 🔬 Validazione Scientifica

Il framework GIST è basato su:
- Ricerca accademica validata su 234 organizzazioni
- Dataset reale settore GDO italiano
- Simulazioni Digital Twin con 10.000 iterazioni
- Intervalli di confidenza al 95%

## 📄 Licenza

MIT License - Open Source

## 👤 Autore

Sviluppato come tesi di laurea magistrale in Cybersecurity  
GitHub: [gist-framework](https://github.com/gist-framework)

## 📧 Contatti

Per informazioni commerciali: info@gist-framework.com

---

**Versione**: 1.0.0 (MVP)  
**Data**: Ottobre 2025
