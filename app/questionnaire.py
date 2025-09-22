"""
Questionario semplificato GIST Assessment
20 domande totali (5 per componente)
"""

QUESTIONNAIRE = {
    'physical': [
        {
            'id': 'power_supply',
            'question': 'Quale sistema di alimentazione utilizzate per i sistemi critici?',
            'options': [
                ('0', 'Nessun UPS (0 pt)'),
                ('25', 'UPS singolo 15-30 min (25 pt)'), 
                ('50', 'UPS 1-2 ore (50 pt)'),
                ('75', 'Configurazione ridondante N+1 (75 pt)'),
                ('100', 'Configurazione 2N completa (100 pt)')
            ]
        },
        {
            'id': 'connectivity',
            'question': 'Connettività internet dei punti vendita:',
            'options': [
                ('20', 'ADSL base (20 pt)'),
                ('40', 'Fibra ottica (40 pt)'),
                ('60', 'Dual ISP diversi (60 pt)'), 
                ('80', 'SD-WAN gestito (80 pt)'),
                ('100', 'Fibra + 5G backup (100 pt)')
            ]
        },
        {
            'id': 'cooling',
            'question': 'Sistema raffreddamento datacenter:',
            'options': [
                ('20', 'Aria condizionata standard (20 pt)'),
                ('40', 'HVAC dedicato (40 pt)'),
                ('60', 'Contenimento corridoi caldi/freddi (60 pt)'),
                ('80', 'Raffreddamento liquido (80 pt)'),
                ('100', 'AI-driven cooling PUE<1.3 (100 pt)')
            ]
        },
        {
            'id': 'redundancy',
            'question': 'Ridondanza hardware sistemi critici:',
            'options': [
                ('0', 'Single point of failure (0 pt)'),
                ('25', 'Spare parts disponibili (25 pt)'),
                ('50', 'Clustering attivo-passivo (50 pt)'),
                ('75', 'Clustering attivo-attivo (75 pt)'),
                ('100', 'Multi-datacenter geo-replicato (100 pt)')
            ]
        },
        {
            'id': 'monitoring',
            'question': 'Monitoraggio infrastruttura:',
            'options': [
                ('10', 'Check manuali (10 pt)'),
                ('30', 'Alert email automatici (30 pt)'),
                ('50', 'Dashboard 24/7 (50 pt)'),
                ('75', 'Monitoring predittivo ML (75 pt)'),
                ('100', 'Self-healing infrastructure (100 pt)')
            ]
        }
    ],
    
    'architectural': [
        {
            'id': 'cloud_adoption',
            'question': 'Percentuale servizi su cloud:',
            'options': [
                ('10', 'Solo email/backup (10 pt)'),
                ('30', '25-40% servizi non critici (30 pt)'),
                ('50', '40-60% workload misto (50 pt)'),
                ('75', '60-80% cloud first (75 pt)'),
                ('100', 'Full cloud-native >90% (100 pt)')
            ]
        },
        {
            'id': 'architecture_style',
            'question': 'Architettura applicazioni principali:',
            'options': [
                ('20', 'Monolitica centralizzata (20 pt)'),
                ('40', 'Modulare multi-tier (40 pt)'),
                ('60', 'Service-oriented (SOA) (60 pt)'),
                ('80', 'Microservizi containerizzati (80 pt)'),
                ('100', 'Cloud-native serverless (100 pt)')
            ]
        },
        {
            'id': 'deployment',
            'question': 'Processo deployment applicazioni:',
            'options': [
                ('20', 'Manuale (20 pt)'),
                ('40', 'Script automatizzati (40 pt)'),
                ('60', 'CI/CD pipeline (60 pt)'),
                ('80', 'GitOps + container orchestration (80 pt)'),
                ('100', 'Full DevOps con canary deployment (100 pt)')
            ]
        },
        {
            'id': 'scalability',
            'question': 'Gestione picchi di carico (es. Black Friday):',
            'options': [
                ('20', 'Dimensionamento fisso (20 pt)'),
                ('40', 'Scale up manuale (40 pt)'),
                ('60', 'Auto-scaling configurato (60 pt)'),
                ('80', 'Elastic scaling multi-cloud (80 pt)'),
                ('100', 'Predictive scaling con AI (100 pt)')
            ]
        },
        {
            'id': 'disaster_recovery',
            'question': 'Strategia disaster recovery:',
            'options': [
                ('20', 'Backup giornalieri (20 pt)'),
                ('40', 'DR site passivo (40 pt)'),
                ('60', 'DR attivo con RTO <4h (60 pt)'),
                ('80', 'Active-active multi-region (80 pt)'),
                ('100', 'Chaos engineering + auto-recovery (100 pt)')
            ]
        }
    ],
    
    'security': [
        {
            'id': 'identity_access',
            'question': 'Gestione identità e accessi:',
            'options': [
                ('20', 'Username/password (20 pt)'),
                ('40', 'MFA per amministratori (40 pt)'),
                ('60', 'MFA esteso + RBAC (60 pt)'),
                ('80', 'Zero Trust con risk-based auth (80 pt)'),
                ('100', 'Passwordless + behavioral analytics (100 pt)')
            ]
        },
        {
            'id': 'network_security',
            'question': 'Sicurezza di rete:',
            'options': [
                ('20', 'Firewall perimetrale (20 pt)'),
                ('40', 'VLAN segmentation (40 pt)'),
                ('60', 'Micro-segmentazione (60 pt)'),
                ('80', 'Zero Trust network (80 pt)'),
                ('100', 'SASE + AI-driven security (100 pt)')
            ]
        },
        {
            'id': 'data_protection',
            'question': 'Protezione dati sensibili:',
            'options': [
                ('30', 'Crittografia at-rest base (30 pt)'),
                ('50', 'Crittografia at-rest + in-transit (50 pt)'),
                ('70', 'Key management + tokenizzazione (70 pt)'),
                ('85', 'Data loss prevention (DLP) (85 pt)'),
                ('100', 'Homomorphic encryption + PET (100 pt)')
            ]
        },
        {
            'id': 'threat_detection',
            'question': 'Rilevamento minacce:',
            'options': [
                ('20', 'Antivirus + log review manuale (20 pt)'),
                ('40', 'SIEM con regole base (40 pt)'),
                ('60', 'SOC interno + threat intel (60 pt)'),
                ('80', 'AI-powered detection + response (80 pt)'),
                ('100', 'Predictive threat hunting (100 pt)')
            ]
        },
        {
            'id': 'incident_response',
            'question': 'Processo gestione incidenti:',
            'options': [
                ('20', 'Ad-hoc su escalation (20 pt)'),
                ('40', 'Playbook documentati (40 pt)'),
                ('60', 'Team dedicato + esercitazioni (60 pt)'),
                ('80', 'Automated response + forensics (80 pt)'),
                ('100', 'AI-orchestrated + threat attribution (100 pt)')
            ]
        }
    ],
    
    'compliance': [
        {
            'id': 'policy_framework',
            'question': 'Framework gestione policy:',
            'options': [
                ('20', 'Documenti statici (20 pt)'),
                ('40', 'Policy centralizzate (40 pt)'),
                ('60', 'Version control + review (60 pt)'),
                ('80', 'Policy as code + automation (80 pt)'),
                ('100', 'AI-generated compliance policies (100 pt)')
            ]
        },
        {
            'id': 'audit_monitoring',
            'question': 'Frequenza e tipo di audit:',
            'options': [
                ('20', 'Annuale manuale (20 pt)'),
                ('40', 'Trimestrale con tool (40 pt)'),
                ('60', 'Mensile automatizzato (60 pt)'),
                ('80', 'Continuous compliance monitoring (80 pt)'),
                ('100', 'Real-time compliance + auto-remediation (100 pt)')
            ]
        },
        {
            'id': 'data_governance',
            'question': 'Classificazione e gestione dati:',
            'options': [
                ('20', 'Classificazione manuale limitata (20 pt)'),
                ('40', 'Tassonomia dati documentata (40 pt)'),
                ('60', 'Auto-discovery + tagging (60 pt)'),
                ('80', 'Data lineage + quality monitoring (80 pt)'),
                ('100', 'AI-powered data governance (100 pt)')
            ]
        },
        {
            'id': 'risk_management',
            'question': 'Approccio al risk management:',
            'options': [
                ('20', 'Risk assessment qualitativo (20 pt)'),
                ('40', 'Risk register + rating (40 pt)'),
                ('60', 'Quantitative risk analysis (60 pt)'),
                ('80', 'Monte Carlo + scenario planning (80 pt)'),
                ('100', 'AI predictive risk modeling (100 pt)')
            ]
        },
        {
            'id': 'training',
            'question': 'Formazione sicurezza/compliance:',
            'options': [
                ('20', 'Training annuale generico (20 pt)'),
                ('40', 'Role-based training (40 pt)'),
                ('60', 'Continuous learning + testing (60 pt)'),
                ('80', 'Adaptive training + simulation (80 pt)'),
                ('100', 'AI-personalized + VR training (100 pt)')
            ]
        }
    ]
}

def calculate_component_score(answers, component):
    """Calcola score per una componente dalle risposte"""
    questions = QUESTIONNAIRE[component]
    total_points = 0
    
    for question in questions:
        question_id = question['id']
        if question_id in answers:
            total_points += int(answers[question_id])
    
    # Media dei punti ottenuti
    return total_points / len(questions)