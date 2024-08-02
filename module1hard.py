grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
my_class = {}
for i in range(len(students)):
    my_class[students_sorted[i]] = sum(grades[i]) / len(grades[i])
print('Словарь класса:', my_class)









