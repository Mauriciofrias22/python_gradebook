# list that saves the names of the subjects and the grades of those subjects
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# lists that saves other subjects and grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# this adds computer science to subjects and 100 to grades
subjects.append("computer science")
grades.append(100)

# the zip() function combines subjects and grades and it saves this zip object
# as a list into a variable called gradebook.
gradebook = list(zip(grades, subjects))

# this append adds ("visual arts", 93) to the variable gradebook.
gradebook.append(("visual arts", 93))

# the items from both gradebook and last_semester_gradebook are stored into the
#variable full_gradebook
full_gradebook = last_semester_gradebook + gradebook

print(list(gradebook))
