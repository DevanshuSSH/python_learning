#methods in list 
#indexing
#lists are mutable we can change them
#strings are imutable
marks = [100, 98, 95, 88, 79]
print(marks)

#marks[2]=99
#print(marks)

#slicling
print(marks[1:5])
print(max(marks))
print(min(marks))
marks.append(101)
print(marks)
marks.sort()
print(marks)
marks.remove(101)
print(marks)