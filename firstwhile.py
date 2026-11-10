# number_of_questions = 19
# while number_of_questions >0:
#     print("your question is ....")
#     #number_of_questions = number_of_questions-1

done = False
while not done:
    answer = float(input("Enter gpa, enter number from 0.0 to 4.0:"))
    if 0.0 <=answer  <=4.0:
        done = True
print(f"finally done - you entered {answer}")