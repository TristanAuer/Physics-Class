subjects= ["physics", "calculus", "poetry", "history"]
grades= [98, 97, 85, 88]

gradebook = [["physics", 98], ["calsulus", 97], ["poetry", 85], ["history", 88]]
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][-1] = 97
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)
last_semester_gradebook = [["pe", 99], ["astronomy", 89]]
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)