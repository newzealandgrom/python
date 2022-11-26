"""
Скрипт для оценки оценок блять
"""
    
from grades.predict import predict_score
from grades.results import get_grade

score_history = [455, 10, 100, 200]
predicted_score = predict_score(score_history)

predicted_grade = get_grade(predicted_score)
print(f'Возможная оценка: {predicted_grade}')



