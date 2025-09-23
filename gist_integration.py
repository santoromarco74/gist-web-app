# app/gist_integration.py
import sys
import os

# Assumendo che il tuo codice sia in una sottocartella
sys.path.append('gist_framework')

class GISTWebCalculator:
    def __init__(self):
        """Wrapper del tuo GISTCalculator per web app"""
        pass
    
    def calculate_from_questionnaire(self, answers):
        """
        Converte risposte questionario in GIST Score
        answers: dict con risposte del form
        """
        # Mappa risposte alle 4 componenti
        scores = self._map_answers_to_scores(answers)
        
        # Usa il tuo algoritmo originale
        gist_score = self._calculate_gist_score(scores)
        
        return {
            'total_score': gist_score,
            'component_scores': scores,
            'maturity_level': self._get_maturity_level(gist_score),
            'recommendations': self._get_recommendations(scores)
        }
    
    def _map_answers_to_scores(self, answers):
        """Converte 20-25 risposte nelle 4 componenti"""
        physical = self._calc_physical_score(answers)
        architectural = self._calc_architectural_score(answers) 
        security = self._calc_security_score(answers)
        compliance = self._calc_compliance_score(answers)
        
        return {
            'physical': physical,
            'architectural': architectural, 
            'security': security,
            'compliance': compliance
        }