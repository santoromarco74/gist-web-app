# gist_calculator.py - GIST Score Calculator
# Implementazione basata sulla tesi "Framework GIST per la GDO"
# Formula: GIST = Σ(w_k * S_k^γ) dove γ=0.95

import math
from questionnaire import COMPONENT_WEIGHTS, SECTOR_BENCHMARKS, COMPONENT_LABELS

class GISTCalculator:
    """
    Calcolatore GIST Score secondo formula dalla ricerca originale.
    
    Formula: GIST = Σ(w_k * S_k^γ)
    dove:
    - w_k: peso componente k (physical, architectural, security, compliance)
    - S_k: score normalizzato 0-100 della componente k
    - γ: esponente per rendimenti decrescenti (0.95)
    """
    
    def __init__(self, organization_name="Assessment"):
        self.organization_name = organization_name
        self.weights = COMPONENT_WEIGHTS
        self.gamma = 0.95  # Esponente per rendimenti decrescenti
        self.benchmarks = SECTOR_BENCHMARKS
        
    def calculate_score(self, questionnaire_answers):
        """
        Calcola GIST Score da risposte questionario.
        
        Args:
            questionnaire_answers: dict con risposte per ogni componente
                formato: {component_id: {question_id: value}}
        
        Returns:
            dict con score, component_scores, maturity_level, recommendations
        """
        # 1. Converti risposte in punteggi componenti 0-100
        component_scores = self._calculate_component_scores(questionnaire_answers)
        
        # 2. Calcola GIST Score con formula originale
        gist_score = self._calculate_gist_formula(component_scores)
        
        # 3. Determina livello maturità
        maturity_level = self._get_maturity_level(gist_score)
        
        # 4. Genera raccomandazioni prioritizzate
        recommendations = self._generate_recommendations(component_scores)
        
        # 5. Calcola benchmark vs settore
        benchmarks = self._calculate_benchmarks(component_scores)
        
        return {
            'gist_score': round(gist_score, 1),
            'component_scores': component_scores,
            'maturity_level': maturity_level,
            'recommendations': recommendations,
            'benchmarks': benchmarks,
            'organization': self.organization_name
        }
    
    def _calculate_component_scores(self, answers):
        """Calcola score medio 0-100 per ogni componente."""
        component_scores = {}
        
        for component, questions in answers.items():
            if questions:
                # Media dei valori delle risposte
                values = list(questions.values())
                avg_score = sum(values) / len(values)
                component_scores[component] = round(avg_score, 1)
            else:
                component_scores[component] = 0
                
        return component_scores
    
    def _calculate_gist_formula(self, component_scores):
        """
        Applica formula GIST originale: Σ(w_k * S_k^γ)
        """
        gist_score = 0
        
        for component, score in component_scores.items():
            if component in self.weights:
                # Formula con esponente per rendimenti decrescenti
                weighted_score = self.weights[component] * (score ** self.gamma)
                gist_score += weighted_score
        
        return gist_score
    
    def _get_maturity_level(self, gist_score):
        """
        Determina livello maturità organizzativa.
        Livelli dalla tesi (sezione 5.4.6):
        - 0-25: Iniziale
        - 26-50: In Sviluppo
        - 51-75: Avanzato
        - 76-100: Ottimizzato
        """
        if gist_score < 25:
            return {
                'level': 'Iniziale',
                'description': 'Architettura legacy, sicurezza reattiva, gap normativi significativi',
                'color': '#EF4444'  # rosso
            }
        elif gist_score < 50:
            return {
                'level': 'In Sviluppo',
                'description': 'Modernizzazione parziale in corso, sicurezza proattiva, conformità base',
                'color': '#F59E0B'  # arancione
            }
        elif gist_score < 75:
            return {
                'level': 'Avanzato',
                'description': 'Architettura moderna, sicurezza integrata, conformità automatizzata',
                'color': '#3B82F6'  # blu
            }
        else:
            return {
                'level': 'Ottimizzato',
                'description': 'Trasformazione completa, sicurezza adattiva, compliance-as-code',
                'color': '#10B981'  # verde
            }
    
    def _generate_recommendations(self, component_scores):
        """
        Genera raccomandazioni prioritizzate basate su gap vs target.
        Target dalla Tabella 5.4 della tesi.
        """
        recommendations = []
        
        for component, score in component_scores.items():
            target = self.benchmarks[component]['target']
            gap = target - score
            
            if gap > 5:  # Solo se c'è un gap significativo
                priority = self._calculate_priority(gap, component)
                action = self._get_action_plan(component, score, target)
                
                recommendations.append({
                    'component': COMPONENT_LABELS[component],
                    'component_id': component,
                    'current_score': round(score, 1),
                    'target_score': target,
                    'gap': round(gap, 1),
                    'priority': priority,
                    'action_plan': action,
                    'estimated_effort': self._estimate_effort(gap),
                    'estimated_roi': self._estimate_roi(component, gap)
                })
        
        # Ordina per priorità (gap * peso componente)
        recommendations.sort(
            key=lambda x: x['gap'] * self.weights[x['component_id']], 
            reverse=True
        )
        
        return recommendations
    
    def _calculate_priority(self, gap, component):
        """Calcola priorità basata su gap e peso componente."""
        weighted_gap = gap * self.weights[component]
        
        if weighted_gap > 15:
            return 'CRITICA'
        elif weighted_gap > 8:
            return 'Alta'
        elif weighted_gap > 4:
            return 'Media'
        else:
            return 'Bassa'
    
    def _get_action_plan(self, component, current, target):
        """Genera piano d'azione specifico per componente."""
        actions = {
            'physical': {
                'short': 'Implementare ridondanza N+1 per alimentazione e connettività critica',
                'medium': 'Deploy SD-WAN multi-path e monitoring predittivo infrastruttura',
                'long': 'Migrazione verso architettura multi-datacenter georeplicata'
            },
            'architectural': {
                'short': 'Avviare migrazione cloud ibrido per servizi non-critici',
                'medium': 'Implementare microservizi e CI/CD pipeline per nuovi sviluppi',
                'long': 'Adozione completa cloud-native con multi-cloud orchestration'
            },
            'security': {
                'short': 'Deploy MFA universale e EDR su tutti gli endpoint',
                'medium': 'Implementare Zero Trust Network Access (ZTNA) e SOC 24/7',
                'long': 'Adozione framework SASE con AI-powered threat detection'
            },
            'compliance': {
                'short': 'Automazione controlli PCI-DSS e GDPR con monitoring continuo',
                'medium': 'Implementare compliance-as-code e automated remediation',
                'long': 'Adozione piattaforma GRC integrata con AI predictive compliance'
            }
        }
        
        gap = target - current
        if gap > 30:
            return actions[component]['long']
        elif gap > 15:
            return actions[component]['medium']
        else:
            return actions[component]['short']
    
    def _estimate_effort(self, gap):
        """Stima effort in mesi."""
        if gap > 30:
            return '18-24 mesi'
        elif gap > 20:
            return '12-18 mesi'
        elif gap > 10:
            return '6-12 mesi'
        else:
            return '3-6 mesi'
    
    def _estimate_roi(self, component, gap):
        """
        Stima ROI percentuale a 3 anni.
        Basato su dati dalla sezione 5.4.9 della tesi.
        """
        base_roi = {
            'physical': 280,
            'architectural': 340,
            'security': 420,
            'compliance': 310
        }
        
        # ROI scala con il gap da colmare
        roi = base_roi[component] * (gap / 30)
        return f"{int(roi)}% a 3 anni"
    
    def _calculate_benchmarks(self, component_scores):
        """Calcola posizione vs media settore GDO."""
        benchmarks = {}
        
        for component, score in component_scores.items():
            sector_avg = self.benchmarks[component]['avg']
            target = self.benchmarks[component]['target']
            
            # Calcola percentile approssimato (distribuzione normale)
            vs_sector = score - sector_avg
            percentile = self._score_to_percentile(vs_sector)
            
            benchmarks[component] = {
                'label': COMPONENT_LABELS[component],
                'score': round(score, 1),
                'sector_avg': sector_avg,
                'target': target,
                'vs_sector': round(vs_sector, 1),
                'percentile': percentile,
                'status': 'above' if vs_sector > 0 else 'below'
            }
        
        return benchmarks
    
    def _score_to_percentile(self, vs_sector):
        """Converte differenza vs settore in percentile."""
        # Approssimazione: assume std dev ~ 12 punti
        if vs_sector > 20:
            return 95
        elif vs_sector > 12:
            return 85
        elif vs_sector > 6:
            return 70
        elif vs_sector > 0:
            return 55
        elif vs_sector > -6:
            return 45
        elif vs_sector > -12:
            return 30
        elif vs_sector > -20:
            return 15
        else:
            return 5
