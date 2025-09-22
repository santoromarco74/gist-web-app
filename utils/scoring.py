# utils/scoring.py
class QuestionnaireProcessor:
    
    # Mapping domande → componenti
    QUESTION_MAPPING = {
        'physical': list(range(1, 9)),      # Domande 1-8
        'architectural': list(range(9, 19)), # Domande 9-18
        'security': list(range(19, 28)),     # Domande 19-27
        'compliance': list(range(28, 34))    # Domande 28-33
    }
    
    def process_answers(self, answers):
        """
        Converte risposte form (0-100 per domanda) 
        in punteggi componenti per GIST Calculator
        """
        component_scores = {}
        
        for component, questions in self.QUESTION_MAPPING.items():
            total_points = sum(answers.get(f'q{i}', 0) for i in questions)
            max_possible = len(questions) * 100
            score = (total_points / max_possible) * 100
            component_scores[component] = round(score, 1)
            
        return component_scores