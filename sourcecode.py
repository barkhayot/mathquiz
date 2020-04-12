import random #importing the randomn function


num_1 = random.randint(0,100) #adding the value to the func
num_2 = random.randint(0,10)  #adding the value to the func

sum = num_1 - num_2    # formula of sum

print("Solve the following problem :")
print(num_1, "-", num_2)

ansWer = int(input("Enter your answer :")) #giving the if function to check answer

if ansWer is sum:
    print("Correct answer!")
else:
    print("Incorrect answer!")
