"""
Module for exam predictions
"""

def get_avg(score_history):
    """Берет предыдущие оценки и выдает среднее"""
    return sum(score_history) / len(score_history)
 
 
def predict_score(score_history, min_score=0):
    """берет список прошлого процента оценок и возвращает среднее"""
    score_avg = get_avg(score_history)
    if score_avg < min_score:
        return min_score
    
    return score_avg