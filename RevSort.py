students=("patrick","monik","moon","kroom")

sorted_student = sorted(students)

for i in sorted_student:
    print(i,end=" ")

#reverse sort..
print()

sorted_student = sorted(students,reverse=True)

for i in sorted_student:
    print(i,end=" ")
print()

#condition sort in lists...

    # index 0    1   2 
students=[("awak","A",10),("Swaq","B",80),("pop","F",30),("out","D",50)]

age = lambda x: x[1] #accessing by index 1
students.sort(key=age)

for i in students:
    print(i)
print()
#reverse the condition sort..

age = lambda y:y[2]
students.sort(key=age,reverse=True)


for i in students:
    print(i)