# gist_calculator.py
class GISTCalculator:
    def __init__(self):
        self.weights = {
            'physical': 0.18,
            'architectural': 0.32,
            'security': 0.28,
            'compliance': 0.22
        }
    
    def calculate_score(self, components):
        """
        components = {
            'physical': 72,
            'architectural': 68,
            'security': 65,
            'compliance': 78
        }
        """
        gamma = 0.95
        score = sum(
            self.weights[k] * (v ** gamma) 
            for k, v in components.items()
        )
        return score