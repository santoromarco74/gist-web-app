# app/gist_calculator.py - Integrato dalla tua tesi
class GISTCalculator:
    def __init__(self, org_name="Web Assessment"):
        self.org_name = org_name
        # Pesi calibrati dalla tua ricerca (Tabella B.5)
        self.weights = {
            'physical': 0.18,      # 18%
            'architectural': 0.32, # 32% 
            'security': 0.28,      # 28%
            'compliance': 0.22     # 22%
        }
        self.gamma = 0.95  # Esponente rendimenti decrescenti
    
    def calculate_score(self, questionnaire_answers):
        """
        Converte risposte questionario in GIST Score
        Formula dalla tua tesi: GIST = Σ(w_k * S_k^γ)
        """
        # Converto risposte in punteggi componenti 0-100
        component_scores = self._answers_to_components(questionnaire_answers)
        
        # Calcolo GIST Score con la formula originale
        gist_score = 0
        for component, score in component_scores.items():
            weighted_score = self.weights[component] * (score ** self.gamma)
            gist_score += weighted_score
        
        return {
            'gist_score': round(gist_score, 1),
            'component_scores': component_scores,
            'maturity_level': self._get_maturity_level(gist_score),
            'recommendations': self._get_recommendations(component_scores),
            'benchmarks': self._get_sector_benchmarks(component_scores)
        }
    
    def _get_sector_benchmarks(self, scores):
        """Benchmark vs medie settore dalla tua Tabella 5.4"""
        sector_averages = {
            'physical': 51.2,      # Media settore GDO italiano
            'architectural': 45.8,
            'security': 48.3,
            'compliance': 52.7
        }
        
        benchmarks = {}
        for component, score in scores.items():
            avg = sector_averages[component]
            benchmarks[component] = {
                'score': score,
                'sector_avg': avg,
                'vs_sector': score - avg,
                'percentile': self._calculate_percentile(component, score)
            }
        
        return benchmarks