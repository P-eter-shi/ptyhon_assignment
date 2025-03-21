#empty list
my_list=[]
my_list.extend([10,20,30,40])#appended values
#print(my_list)
my_list.insert(1,15)
#print(my_list)
thisList=[50,60,70]
#extend my_list
my_list.extend(thisList)
#print(my_list)
my_list.remove(70)
#print(my_list)
my_list.sort()
#print(my_list)
print(my_list.index(30))#index of 30.