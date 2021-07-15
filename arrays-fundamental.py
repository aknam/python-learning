from array import *
val=array('i',[5,9,6,2,3])
print(val)
val.reverse()
newArr=array(val.typecode,(a*a for a in val) )
for i in newArr:
    print(i)