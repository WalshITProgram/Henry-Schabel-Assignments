
#creates a list of courses already taken
courses_taken = ["it410", "it202", "com405", "mgt201"]

#courses planned to be taken
courses_taken.append("it402")
courses_taken.append("it408")
courses_taken.append("it412")
courses_taken.append("it461")

#sorts the list
courses_taken.sort()

#prints the taken courses
print("Courses I have taken at Walsh College:")
print("I have taken " + courses_taken[0].upper() + " at Walsh College.")
print("I have taken " + courses_taken[1].upper() + " at Walsh College.")
print("I have taken " + courses_taken[2].upper() + " at Walsh College.")
print("I have taken " + courses_taken[3].upper() + " at Walsh College.")
print("I have taken " + courses_taken[4].upper() + " at Walsh College.")
print("I have taken " + courses_taken[5].upper() + " at Walsh College.")
print("I have taken " + courses_taken[6].upper() + " at Walsh College.")
print("I have taken " + courses_taken[7].upper() + " at Walsh College.")

#prints upcoming courses
print("\nThis is my course of study with upcoming courses added:")
print(courses_taken[0])
print(courses_taken[1])
print(courses_taken[2])
print(courses_taken[3])
print(courses_taken[4])
print(courses_taken[5])
print(courses_taken[6])
print(courses_taken[7])

#removes taken courses
removed_course_one = courses_taken.pop(0)
removed_course_two = courses_taken.pop(0)
removed_course_three = courses_taken.pop(2)
removed_course_four = courses_taken.pop(4)

#prints courses that do not need to be retaken
print("\nI do not have to take these courses:")
print(removed_course_one)
print(removed_course_two)
print(removed_course_three)
print(removed_course_four)

#prints planned courses
print("\nI plan to take the following courses next term:")
print(courses_taken[0])
print(courses_taken[1])
print(courses_taken[2])
print(courses_taken[3])

#creates a list of numbers divisible by 6 from 1 to 1000
numbers = list(range(6, 1001, 6))

#prints the first 20 numbers
print("\nHere are twenty numbers divisible by 6.")
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
print(numbers[6])
print(numbers[7])
print(numbers[8])
print(numbers[9])
print(numbers[10])
print(numbers[11])
print(numbers[12])
print(numbers[13])
print(numbers[14])
print(numbers[15])
print(numbers[16])
print(numbers[17])
print(numbers[18])
print(numbers[19])

#calculates the maximum number in the list
maximum_number = max(numbers)

#prints the maximum number
print("\nThe maximum value in the list is: " + str(maximum_number))

#calculates the sum of values from the 10th through the 50th position
sum_of_values = sum(numbers[9:50])

#prints the sum
print("Here is the sum of several values in the list: " + str(sum_of_values))

#overwrites the original courses_taken variable with the numbers list
courses_taken = numbers
