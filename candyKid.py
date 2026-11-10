good_answers = ['yes', 'yup' , "ok", 'fine', "sure", "yeah"]

while True:
    answer = input("Can I have my candy now?")
    answer = answer.lower()
    if answer in good_answers:
        break
    else:
        print("No realllllllllllllly.......")
print("Yes, you gave the 'right' answer")