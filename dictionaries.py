counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)

print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())

counties_dict.get("Denver")


# List of dictionaries

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print("My voting_data")
print(voting_data)

voting_data.append({"county":"El paso", "registered_voters": 461149})
print(voting_data)

voting_data.pop(0)
print(voting_data)

voting_data.append(voting_data.pop(0))
print(voting_data)

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print("last")
print(voting_data)

