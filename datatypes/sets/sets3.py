students = {'Mark', 'Vladimir', 'Alisa', 'Peter', 'Kate'}
teachers = {'Abragham', 'McgonaGAL', 'HAGRID', 'Snape', 'Mark', 'Vladimir'}

# same elements
same_elements = students & teachers
print(same_elements)

# объединение
union = students | teachers
print(union)

# узнать тех кто находится только в одном списке
one_set = students ^ teachers
print(one_set)