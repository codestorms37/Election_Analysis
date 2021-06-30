print("Hello World")

print(type(3))

#Be carful with this, the result is a tuple
ballots = 1,341
print(type(ballots))

print(type(73.81))

print(type("Hello World"))

print(type(True))

num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True

mytemplate = f"""
    The number of candidates is {num_candidates}
    and the winning % is {winning_percentage}
    My candidate is {candidate}
    """

print(mytemplate)

myArray = [0,0,0,0,0,0]

myArray[0] = 5 + 2 * 3
myArray[1] = 8 // 5 - 3
myArray[2] = 8 + 22 * 2 - 4
myArray[3] = 16 - 3 / 2 + 7 - 1
myArray[4] = 3 ** 3 % 5
myArray[5] = 5 + 9 * 3 / 2 - 4

print(myArray)


myArray2 = [0,0,0,0,0,0,0]

myArray2[0] = (5 + 2) * 3
myArray2[1] =(8 // 5) - 3
myArray2[2] =8 + (22 * (2 - 4))
myArray2[3] =16 - 3 / (2 + 7) - 1
myArray2[4] =3 ** (3 % 5)
myArray2[5] = 5 + (9 * 3 / 2 - 4)
myArray2[6] = 5 + (9 * 3 / (2 - 4))

print(myArray2)