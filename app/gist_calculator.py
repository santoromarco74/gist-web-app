"""
GIST Calculator Web Wrapper
Integra il framework GIST per web application
"""
import math

class GISTCalculator:
    def __init__(self):
        # Pesi calibrati dalla tua tesi (pagina 125)
        self.weights = {
            'physical': 0.18,      # 18%
            'architectural': 0.32, # 32% 
            'security': 0.28,      # 28%
            'compliance': 0.22     # 22%
        }
        self.gamma = 0.95  # Esponente per rendimenti decrescenti
    
    def calculate_gist_score(self, component_scores):
        """
        Calcola GIST Score dalle 4 componenti
        Formula dalla tesi: GIST = Σ(w_k * S_k^γ)
        """
        total_score = 0
        
        for component, score in component_scores.items():
            if component in self.weights:
                weighted_score = self.weights[component] * (score ** self.gamma)
                total_score += weighted_score
        
        return round(total_score, 1)
    
    def get_maturity_level(self, gist_score):
        """Determina livello maturità da GIST Score"""
        if gist_score < 25:
            return "Iniziale"
        elif gist_score < 50:
            return "In Sviluppo" 
        elif gist_score < 75:
            return "Avanzato"
        else:
            return "Ottimizzato"
    
    def get_recommendations(self, component_scores):
        """Genera raccomandazioni basate sui gap"""
        recommendations = []
        
        # Target per settore GDO (dalla tua analisi)
        targets = {
            'physical': 65,
            'architectural': 70,
            'security': 68,
            'compliance': 75
        }
        
        for component, score in component_scores.items():
            gap = targets[component] - score
            if gap > 10:  # Gap significativo
                priority = "Alta" if gap > 20 else "Media"
                recommendations.append({
                    'component': component.title(),
                    'current': score,
                    'target': targets[component], 
                    'gap': gap,
                    'priority': priority,
                    'action': self._get_component_action(component, gap)
                })
        
        return sorted(recommendations, key=lambda x: x['gap'], reverse=True)
    
    def _get_component_action(self, component, gap):
        """Azioni specifiche per componente"""
        actions = {
            'physical': "Upgrade alimentazione ridondante e connettività backup",
            'architectural': "Migrazione cloud ibrido e implementazione microservizi", 
            'security': "Implementazione Zero Trust e SOC 24/7",
            'compliance': "Automazione controlli e continuous compliance monitoring"
        }
        return actions.get(component, "Miglioramento generale richiesto")