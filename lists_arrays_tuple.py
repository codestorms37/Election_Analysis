counties = ["Arapahoe","Denver","Jefferson"]

# Creates an empty list
my_list=[]
my_list2=list()

print(counties)

# length of a list
print(len(counties))


counties.insert(2,"El paso")

print(counties)

counties.remove("El paso")

print(counties)

print(counties.pop(2))
print(counties)

counties = ["Arapahoe","Denver","Jefferson"]
print(counties)

counties.insert(1,"El paso")
print(counties)

counties.pop(0)
print(counties)

counties.append(counties.pop(1))
print(counties)

counties.append("Arapahoe")
print(counties)
