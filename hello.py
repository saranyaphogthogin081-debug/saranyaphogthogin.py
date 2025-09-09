fruits = ("apple","banana","cherry","orange","grape","kiwi")

#for f in fruits:
#  Print(f)
for i in range(5,-1,-1):   #len(fruits) = 0
    print(fruits[3])
    
    

seta = {"a","b","c","d"}
setd = {"c","d","e","f"}

print("bange" in seta)
seta.add("bange")
print("bange" in setd)

#print(seta.union(setd))
#seta.intersection(setd)
#seta.intersection_update(setd) #A^B 
print(seta.symmetric_difference(setd))  #A^B
seta.difference_update(setd)

fruitsSet = {"apple","banana","cherry"}
fruitsSet.discard("banana")
print(fruitsSet)

fruitsSet.discard("banana")
