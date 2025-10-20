# questionnaire.py - GIST Framework Assessment Questions
# 36 domande totali calibrate sulla ricerca GIST

QUESTIONNAIRE = {
    'physical': [
        {
            'id': 'power_supply',
            'question': 'Sistema di alimentazione per sistemi critici (POS, server, networking):',
            'options': [
                {'value': 15, 'text': 'UPS basic <30min, singolo'},
                {'value': 35, 'text': 'UPS esteso 1-2h, singolo'}, 
                {'value': 60, 'text': 'Configurazione N+1 ridondante'},
                {'value': 85, 'text': 'Configurazione 2N completa'},
                {'value': 100, 'text': 'Multi-site con generatori backup'}
            ]
        },
        {
            'id': 'connectivity_primary',
            'question': 'Connettività primaria punti vendita:',
            'options': [
                {'value': 15, 'text': 'ADSL/fibra singola <20Mbps'},
                {'value': 35, 'text': 'Fibra singola >50Mbps'},
                {'value': 55, 'text': 'Dual ISP provider diversi'},
                {'value': 75, 'text': 'SD-WAN multi-path intelligente'},
                {'value': 100, 'text': 'Fibra + 5G backup + load balancing'}
            ]
        },
        {
            'id': 'cooling_systems',
            'question': 'Raffreddamento e controllo ambientale data center/server room:',
            'options': [
                {'value': 20, 'text': 'Aria condizionata standard uffici'},
                {'value': 40, 'text': 'HVAC dedicato con ridondanza'},
                {'value': 60, 'text': 'Contenimento corridoi caldi/freddi'},
                {'value': 80, 'text': 'Raffreddamento liquido + monitoraggio'},
                {'value': 100, 'text': 'AI-driven cooling optimization PUE <1.3'}
            ]
        },
        {
            'id': 'hardware_redundancy',
            'question': 'Ridondanza hardware per sistemi critici:',
            'options': [
                {'value': 10, 'text': 'Single point of failure - no backup'},
                {'value': 30, 'text': 'Spare parts on-site + contratti SLA'},
                {'value': 50, 'text': 'Clustering attivo-passivo'},
                {'value': 75, 'text': 'Clustering attivo-attivo bilanciato'},
                {'value': 100, 'text': 'Multi-datacenter georeplicato'}
            ]
        },
        {
            'id': 'infrastructure_monitoring',
            'question': 'Monitoraggio proattivo infrastruttura fisica:',
            'options': [
                {'value': 15, 'text': 'Check manuali periodici'},
                {'value': 35, 'text': 'Alert email automatici base'},
                {'value': 55, 'text': 'Dashboard 24/7 con SLA definiti'},
                {'value': 75, 'text': 'Monitoring predittivo con ML'},
                {'value': 100, 'text': 'Self-healing infrastructure automation'}
            ]
        },
        {
            'id': 'network_segmentation',
            'question': 'Segmentazione fisica della rete:',
            'options': [
                {'value': 20, 'text': 'Rete unica flat per tutti i servizi'},
                {'value': 40, 'text': 'VLAN separate per aree principali'},
                {'value': 60, 'text': 'Micro-segmentazione per funzioni'},
                {'value': 80, 'text': 'Software-defined networking (SDN)'},
                {'value': 100, 'text': 'Zero-trust network micro-perimetri'}
            ]
        },
        {
            'id': 'backup_power_testing',
            'question': 'Test e manutenzione sistemi di backup energetico:',
            'options': [
                {'value': 10, 'text': 'Test occasionali o assenti'},
                {'value': 30, 'text': 'Test annuali programmati'},
                {'value': 50, 'text': 'Test trimestrali documentati'},
                {'value': 70, 'text': 'Test mensili + load testing'},
                {'value': 100, 'text': 'Test automatizzati + simulazioni failure'}
            ]
        },
        {
            'id': 'environmental_monitoring',
            'question': 'Controllo ambientale (temperatura, umidità, sicurezza fisica):',
            'options': [
                {'value': 15, 'text': 'Controllo manuale sporadico'},
                {'value': 35, 'text': 'Sensori base con alert email'},
                {'value': 55, 'text': 'Sistema SCADA con dashboard'},
                {'value': 75, 'text': 'IoT sensors + predictive analytics'},
                {'value': 100, 'text': 'Digital twin + automated response'}
            ]
        }
    ],
    
    'architectural': [
        {
            'id': 'cloud_adoption_level',
            'question': 'Livello di adozione cloud computing:',
            'options': [
                {'value': 10, 'text': 'Solo on-premise, architettura monolitica'},
                {'value': 30, 'text': 'Backup cloud, core applications on-premise'},
                {'value': 50, 'text': 'Hybrid: 30-50% servizi migrati su cloud'},
                {'value': 75, 'text': 'Cloud-first strategy, <20% on-premise'},
                {'value': 100, 'text': 'Cloud-native, multi-cloud orchestrato'}
            ]
        },
        {
            'id': 'microservices_architecture',
            'question': 'Architettura applicativa predominante:',
            'options': [
                {'value': 15, 'text': 'Applicazioni monolitiche legacy'},
                {'value': 35, 'text': 'Modularizzazione iniziale, alcuni API'},
                {'value': 55, 'text': 'Microservizi per nuovi sviluppi'},
                {'value': 75, 'text': 'Microservizi + container orchestration'},
                {'value': 100, 'text': 'Serverless + event-driven architecture'}
            ]
        },
        {
            'id': 'automation_devops',
            'question': 'Automazione deployment e DevOps practices:',
            'options': [
                {'value': 10, 'text': 'Deploy manuali, no version control'},
                {'value': 30, 'text': 'Scripts automatizzati base'},
                {'value': 50, 'text': 'CI/CD pipeline per sviluppi principali'},
                {'value': 75, 'text': 'GitOps + Infrastructure as Code'},
                {'value': 100, 'text': 'Full DevSecOps + auto-rollback'}
            ]
        },
        {
            'id': 'api_management',
            'question': 'Gestione API e integrazione sistemi:',
            'options': [
                {'value': 15, 'text': 'Integrazioni point-to-point custom'},
                {'value': 35, 'text': 'API REST basic senza governance'},
                {'value': 55, 'text': 'API Gateway + basic security'},
                {'value': 75, 'text': 'API management platform completo'},
                {'value': 100, 'text': 'Mesh architecture + API versioning'}
            ]
        },
        {
            'id': 'data_architecture',
            'question': 'Architettura dati e analytics:',
            'options': [
                {'value': 10, 'text': 'Database relazionali isolati'},
                {'value': 30, 'text': 'Data warehouse centrale'},
                {'value': 50, 'text': 'Data lake + basic analytics'},
                {'value': 75, 'text': 'Real-time streaming + ML pipelines'},
                {'value': 100, 'text': 'Data mesh + AI-driven insights'}
            ]
        },
        {
            'id': 'disaster_recovery',
            'question': 'Business continuity e disaster recovery:',
            'options': [
                {'value': 15, 'text': 'Backup tradizionali, no DR testing'},
                {'value': 35, 'text': 'DR site passivo, RTO >24h'},
                {'value': 55, 'text': 'Active-passive DR, RTO 4-8h'},
                {'value': 75, 'text': 'Active-active multi-site, RTO <2h'},
                {'value': 100, 'text': 'Chaos engineering + auto-failover'}
            ]
        },
        {
            'id': 'scalability_elasticity',
            'question': 'Capacità di scalabilità per picchi stagionali:',
            'options': [
                {'value': 10, 'text': 'Hardware fixed, performance degradation'},
                {'value': 30, 'text': 'Scale-up manuale programmato'},
                {'value': 50, 'text': 'Auto-scaling basic per alcuni servizi'},
                {'value': 75, 'text': 'Elastic scaling + load balancing'},
                {'value': 100, 'text': 'Predictive scaling + chaos testing'}
            ]
        },
        {
            'id': 'edge_computing',
            'question': 'Implementazione edge computing nei punti vendita:',
            'options': [
                {'value': 10, 'text': 'Solo thin client, elaborazione centrale'},
                {'value': 30, 'text': 'Server locale per POS, no intelligence'},
                {'value': 50, 'text': 'Edge computing per analytics locali'},
                {'value': 75, 'text': 'AI/ML inference in-store'},
                {'value': 100, 'text': 'Distributed computing + fog architecture'}
            ]
        },
        {
            'id': 'container_orchestration',
            'question': 'Containerization e orchestrazione:',
            'options': [
                {'value': 10, 'text': 'VM tradizionali, no containerization'},
                {'value': 30, 'text': 'Docker containers base'},
                {'value': 50, 'text': 'Kubernetes per alcuni workload'},
                {'value': 75, 'text': 'Full Kubernetes + service mesh'},
                {'value': 100, 'text': 'Multi-cluster + GitOps + policy automation'}
            ]
        },
        {
            'id': 'performance_optimization',
            'question': 'Ottimizzazione performance e monitoring APM:',
            'options': [
                {'value': 15, 'text': 'Monitoring reattivo basic'},
                {'value': 35, 'text': 'APM tools + dashboard operative'},
                {'value': 55, 'text': 'Distributed tracing + SLI/SLO'},
                {'value': 75, 'text': 'AI-powered performance optimization'},
                {'value': 100, 'text': 'Autonomous performance management'}
            ]
        }
    ],
    
    'security': [
        {
            'id': 'identity_access_management',
            'question': 'Gestione identità e controllo accessi:',
            'options': [
                {'value': 20, 'text': 'Password locali, accessi condivisi'},
                {'value': 40, 'text': 'Active Directory centralizzato'},
                {'value': 60, 'text': 'SSO + MFA per amministratori'},
                {'value': 80, 'text': 'MFA universale + conditional access'},
                {'value': 100, 'text': 'Zero Trust identity + behavioral analytics'}
            ]
        },
        {
            'id': 'network_security',
            'question': 'Sicurezza perimetrale e di rete:',
            'options': [
                {'value': 15, 'text': 'Firewall perimetrale basic'},
                {'value': 35, 'text': 'Next-gen firewall + IPS'},
                {'value': 55, 'text': 'Network segmentation + micro-perimetri'},
                {'value': 75, 'text': 'Zero Trust network + CASB'},
                {'value': 100, 'text': 'SASE + AI-powered threat detection'}
            ]
        },
        {
            'id': 'endpoint_protection',
            'question': 'Protezione endpoint (POS, workstation, mobile):',
            'options': [
                {'value': 15, 'text': 'Antivirus tradizionale signature-based'},
                {'value': 35, 'text': 'Endpoint protection + comportamentale'},
                {'value': 55, 'text': 'EDR (Endpoint Detection & Response)'},
                {'value': 75, 'text': 'XDR integrato + threat hunting'},
                {'value': 100, 'text': 'AI-driven autonomous response'}
            ]
        },
        {
            'id': 'data_encryption',
            'question': 'Crittografia e protezione dati sensibili:',
            'options': [
                {'value': 20, 'text': 'Crittografia basica per backup'},
                {'value': 40, 'text': 'Encryption at-rest per database'},
                {'value': 60, 'text': 'End-to-end encryption + key management'},
                {'value': 80, 'text': 'Hardware HSM + crypto agility'},
                {'value': 100, 'text': 'Quantum-safe cryptography ready'}
            ]
        },
        {
            'id': 'threat_detection_response',
            'question': 'Rilevamento minacce e incident response:',
            'options': [
                {'value': 15, 'text': 'Alerting reattivo manuale'},
                {'value': 35, 'text': 'SIEM + correlation rules'},
                {'value': 55, 'text': 'SOC 24/7 + playbook automatizzati'},
                {'value': 75, 'text': 'SOAR + machine learning detection'},
                {'value': 100, 'text': 'Autonomous threat response + AI'}
            ]
        },
        {
            'id': 'vulnerability_management',
            'question': 'Gestione vulnerabilità e patch management:',
            'options': [
                {'value': 10, 'text': 'Patch manuali irregolari'},
                {'value': 30, 'text': 'Vulnerability scanning mensile'},
                {'value': 50, 'text': 'Automated patching + testing'},
                {'value': 70, 'text': 'Continuous scanning + risk scoring'},
                {'value': 100, 'text': 'Predictive patching + zero-day defense'}
            ]
        },
        {
            'id': 'security_awareness',
            'question': 'Security awareness e formazione personale:',
            'options': [
                {'value': 15, 'text': 'Formazione sporadica generica'},
                {'value': 35, 'text': 'Training annuale obbligatorio'},
                {'value': 55, 'text': 'Phishing simulation + targeted training'},
                {'value': 75, 'text': 'Continuous education + gamification'},
                {'value': 100, 'text': 'AI-adaptive learning + behavioral change'}
            ]
        },
        {
            'id': 'application_security',
            'question': 'Sicurezza applicativa e DevSecOps:',
            'options': [
                {'value': 10, 'text': 'Security testing post-deployment'},
                {'value': 30, 'text': 'Vulnerability scanning pre-produzione'},
                {'value': 50, 'text': 'SAST/DAST integrato in CI/CD'},
                {'value': 70, 'text': 'Shift-left security + container scanning'},
                {'value': 100, 'text': 'Runtime protection + AI-powered testing'}
            ]
        },
        {
            'id': 'third_party_security',
            'question': 'Sicurezza fornitori e supply chain:',
            'options': [
                {'value': 10, 'text': 'Valutazione informale occasionale'},
                {'value': 30, 'text': 'Security questionnaire standard'},
                {'value': 50, 'text': 'Audit periodici + contratti SLA'},
                {'value': 70, 'text': 'Continuous monitoring + risk scoring'},
                {'value': 100, 'text': 'Blockchain supply chain + real-time intel'}
            ]
        },
        {
            'id': 'backup_recovery_security',
            'question': 'Sicurezza backup e disaster recovery:',
            'options': [
                {'value': 15, 'text': 'Backup non crittografati accessibili'},
                {'value': 35, 'text': 'Backup crittografati off-site'},
                {'value': 55, 'text': 'Immutable backup + air gap'},
                {'value': 75, 'text': 'Multi-cloud backup + regular testing'},
                {'value': 100, 'text': 'Zero-trust backup + automated validation'}
            ]
        }
    ],
    
    'compliance': [
        {
            'id': 'regulatory_frameworks',
            'question': 'Framework normativi implementati e mantenuti:',
            'options': [
                {'value': 15, 'text': 'Solo adempimenti minimi obbligatori'},
                {'value': 35, 'text': 'PCI-DSS Level 4 + GDPR reattivo'},
                {'value': 55, 'text': 'PCI-DSS + GDPR + policy documentate'},
                {'value': 75, 'text': 'Multi-standard (PCI/GDPR/NIS2) integrati'},
                {'value': 100, 'text': 'Compliance-as-code + continuous monitoring'}
            ]
        },
        {
            'id': 'audit_monitoring',
            'question': 'Audit e monitoraggio della conformità:',
            'options': [
                {'value': 20, 'text': 'Audit esterni annuali reattivi'},
                {'value': 40, 'text': 'Audit interni trimestrali + documentazione'},
                {'value': 60, 'text': 'Monitoring mensile automatizzato + KPI'},
                {'value': 80, 'text': 'Continuous compliance + real-time alerting'},
                {'value': 100, 'text': 'AI-powered predictive compliance + auto-remediation'}
            ]
        },
        {
            'id': 'data_governance',
            'question': 'Governance e classificazione dati personali/sensibili:',
            'options': [
                {'value': 10, 'text': 'Approccio best-effort informale'},
                {'value': 30, 'text': 'Data mapping + policy documentate'},
                {'value': 50, 'text': 'Data classification + privacy by design'},
                {'value': 70, 'text': 'Automated data discovery + minimization'},
                {'value': 100, 'text': 'Privacy-enhancing tech + zero-knowledge'}
            ]
        },
        {
            'id': 'risk_management',
            'question': 'Approccio al risk management:',
            'options': [
                {'value': 20, 'text': 'Valutazione qualitativa sporadica'},
                {'value': 40, 'text': 'Risk register + assessment periodici'},
                {'value': 60, 'text': 'Quantificazione rischi + scenario planning'},
                {'value': 80, 'text': 'Predictive risk modeling + simulation'},
                {'value': 100, 'text': 'AI-driven continuous risk assessment'}
            ]
        },
        {
            'id': 'incident_notification',
            'question': 'Gestione notifiche incidenti e breach:',
            'options': [
                {'value': 15, 'text': 'Processo manuale non documentato'},
                {'value': 35, 'text': 'Procedure definite + template comunicazioni'},
                {'value': 55, 'text': 'Workflow automatizzati + escalation'},
                {'value': 75, 'text': 'Real-time notification + legal automation'},
                {'value': 100, 'text': 'AI-powered severity assessment + auto-filing'}
            ]
        },
        {
            'id': 'privacy_rights_management',
            'question': 'Gestione diritti degli interessati (GDPR):',
            'options': [
                {'value': 10, 'text': 'Gestione manuale case-by-case'},
                {'value': 30, 'text': 'Procedure documentate + template'},
                {'value': 50, 'text': 'Self-service portal + workflow semi-auto'},
                {'value': 70, 'text': 'Automated data subject rights + API'},
                {'value': 100, 'text': 'AI-powered privacy automation + blockchain proof'}
            ]
        },
        {
            'id': 'training_certification',
            'question': 'Formazione e certificazione staff su compliance:',
            'options': [
                {'value': 10, 'text': 'Training generico sporadico'},
                {'value': 30, 'text': 'Formazione annuale obbligatoria'},
                {'value': 50, 'text': 'Training targeted per ruolo + testing'},
                {'value': 70, 'text': 'Continuous learning + certificazioni'},
                {'value': 100, 'text': 'Adaptive AI training + competency management'}
            ]
        },
        {
            'id': 'vendor_compliance',
            'question': 'Compliance management fornitori e partner:',
            'options': [
                {'value': 15, 'text': 'Clausole contrattuali generiche'},
                {'value': 35, 'text': 'Due diligence + questionnaire standard'},
                {'value': 55, 'text': 'Audit periodici + SLA compliance'},
                {'value': 75, 'text': 'Continuous monitoring + risk scoring'},
                {'value': 100, 'text': 'Shared compliance platform + real-time assurance'}
            ]
        }
    ]
}

# Pesi delle componenti calibrati dalla ricerca GIST (Tabella B.5)
COMPONENT_WEIGHTS = {
    'physical': 0.18,      # 18%
    'architectural': 0.32, # 32%
    'security': 0.28,      # 28%
    'compliance': 0.22     # 22%
}

# Benchmark settore GDO italiano (dalla Tabella 5.4 della tesi)
SECTOR_BENCHMARKS = {
    'physical': {'avg': 51.2, 'target': 65},
    'architectural': {'avg': 45.8, 'target': 70},
    'security': {'avg': 48.3, 'target': 68},
    'compliance': {'avg': 52.7, 'target': 75}
}

# Labels italiani per le componenti
COMPONENT_LABELS = {
    'physical': 'Infrastruttura Fisica',
    'architectural': 'Architettura',
    'security': 'Sicurezza',
    'compliance': 'Conformità'
}
