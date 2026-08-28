# List comprehension


doubles =[]
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

doubles = [ x * 2 for x in range(1,11)]
print(doubles)
triples = [ y * 3 for y in range(1,11)]
print(triples)
squares=[z ** 2 for z in range(1,11)]
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]

fruits = [fruit.upper() for fruit in fruits]
print(fruits)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grade=[]
for grade in grades:
    if grade >= 60:
        passing_grade.append(grade)
print(passing_grade)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
