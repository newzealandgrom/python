"""
Функции для расчета результата
"""

A_THRESHHOLD = 70
B_THRESHHOLD = 60
C_THRESHHOLD = 50
D_THRESHHOLD = 40
E_THRESHHOLD = 30

def get_grade(score):
    """Прнимает оценку и выдает в печать"""
    if score >= A_THRESHHOLD:
         return 'A'
    elif score >= B_THRESHHOLD:
         return "B"
    elif score >= C_THRESHHOLD:
         return "C"
    elif score >= D_THRESHHOLD:
         return "D"
    elif score >= E_THRESHHOLD:
         return "E"
    return 'F'