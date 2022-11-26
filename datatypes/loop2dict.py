student_count = {
     'course1': 567,
     'course2': 5667,
     'course3': 56117, 
 }
for course, kol in student_count.items():
     print(f'{course}: {kol}')


# total number
total_students = 0
for k, v in student_count.items():
    total_students += v
print(total_students)

# get all keys from dict
courses = student_count.keys()
print(courses)