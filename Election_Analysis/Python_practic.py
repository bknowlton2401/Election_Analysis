counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

# memberships operator

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")


if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties. ")
else:
    print("Arapahoe and El Paso ar enot in the list of counties.")

# for loops

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])
    

# Iterate through a Dictionary

counties_dict = {"Arapahoe": 422829, "Denver":4363353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print (voters)


for county in counties_dict:
    print(counties_dict[county])

for county, voers in counties_dict.items():
    print(county, voters)

# to print through a list of dicitionaries and form sentence

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson":390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# to print using f-strings

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson":390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
    

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
