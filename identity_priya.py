print("Task 1")
print("Data types in Python")
print("Numeric  type")
x=10 #int
print("x = ",x)
print("x =",id(x))
x=12
print("x = ",x)
print("x's value changes =",id(x))
y=3.14 #float
print("y = ",y)
print("y=",id(y))
y=4.5
print("y = ",y)
print("y's vlaue changes = ",id(y))
z=2+3j #complex
print("z = ",z)
print("z =",id(z))
z=4+5j 
print("z = ",z)
print("z's value changes =",id(z))

print("Sequence Types")
text = "Lucky" #str
print("text = ",id(text))
text = "lucky's girl"
print("text value changes = ",id(text))
list=[12,20,31]
print("List = ", list)
print("List id = ",id(list))
list.append(1)
print("New list = ",list)
print("New list id = ",id(list))
print("List is mutable")
dictionary={"Name":"Star", "Age" : 20}
print("dic",dictionary)
print("dic id = ",id(dictionary))
dictionary["God"] = "Shiv"
print("New Dictionary = ", dictionary)
print("dictionary vale change = ",id(dictionary))
print("Dictionary is mutable")
set = {1,4,5}
print("Set = ",set )
print("Set id = ", id(set) )
set.add(2)
print(" New Set = ",set )
print(" New Set id = ", id(set) )
print("Set is mutable")
tuple=(34,35)
print("Tuple = ",tuple)
print("Tuple id= ",id(tuple))
tuple +=(22,30)
print("New tuple = ",tuple)
print("New tuple id = " , id(tuple))
print("Boolean Type")
a=20
b=12
c=a>b
print("Comparision = ",c)
print("c = ",id(c))
c=a<b
print("Comparision = ",c)
print("c value changes = ",id(c))

