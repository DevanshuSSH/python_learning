# tuples in python
# tuples are imutable you cant change them
# tuples written with round brackets

mytuple = ("name: Devanshu",
           "course: mca",
           "field of interest: Ai ml")

print(mytuple)

#empty tuple
emptytuple = ()
singletuple = (6,)
print(type(emptytuple))
print(type(singletuple))
print(mytuple.index("course: mca"))
print(singletuple.count(6))


