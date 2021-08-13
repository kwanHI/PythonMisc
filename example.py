import pandas as pd

#--------------------#
#First, prepare example of dictionary with tuples and value 
#--------------------#


d = {(1,'Truck'):2,(1,'Bus'):13,
     (2, 'Bus'):33, (2,'Truck'):32, (2,'Van'): 14, (2,'Zfly'):32,
     (3,'Washer'):66,
     (4,'Bus'):33, (4,'Truck'):4,(4,'ZFly'):40,
     (5,'Van'):22, (5,'Washer'):11, (5,'Zfly'):9}
print('DATA CONTAINS \n', type(d),d)

#----------------#
# Second, make wk to setwk and objecttype to setobj
#----------------#

# initialize set
setwk = set()
setobj = set()

for k in d.keys():
    setwk.add(k[0])
    setobj.add(k[1])

print('DISTINCT WEEK ARE :', setwk)
print('DISTINCT OBJ ARE :', setobj)

#---------------#
# Third, we will print out and also store result in a dictionary
#---------------#
storage ={}

# first print header or columns 
print([o for o in setobj])

# next walk through data dict to print rows
for r in setwk:
    print([d.get((r,obj)) for obj in setobj])    
