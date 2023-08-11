# mySet={5,4,3,3,2,3,1,2,3,4,5,6,2}
# print(mySet)


# False -> 0
# True-> 1
thisset={'Apple','banana','cherry','apple',1,3,True,0,False}
# print(thisset)

# set1={'Apple','banana','cherry'}
# print(set1)
set2={True,False,False}
# print(set2)



# print(set1[1])
# for x in set1:
    # print(x)
# set1={'Apple','banana','cherry'}

# print('apple'  in set1)
# print('apple' not in set1)

# Adding Element in set
# .add()
# .update()
set3={'Apple','banana','cherry'}

# set3.add(4)
# set3.update([3,4,5,6])
# set3.remove(3)
# set3.discard('Apple')
# set3.pop()
set3.clear()
# for x in range(len(set3)):  # This Gives A EROR
#  print(set3[])

#  print(set3[1])

# union() : Comibining All Element
# intersection  :  comibine elemnt and ite remove duplicate element


setone={1,2,3}
settwo={3,4,5}
# combineSet=setone.union(settwo)
combine= setone | settwo
print(combine)
# print(combineSet)
