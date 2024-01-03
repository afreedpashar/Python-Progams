print("******************************")
print("welcome to my quizz")

question_bank=[
    {
        "text":"What is the capital city of karnataka? ", "answer":"A"
    },
     {
        "text":"What is the capital city of Maharashtra? ", "answer":"B"
    },
     {
        "text":"What is the capital city of TamilNadu? ", "answer":"C"
    },
     {
        "text":"What is the capital state city of India? ", "answer":"D"
    },
     {
        "text":"What is the capital city of Punjab ", "answer":"A"
     },
]

options = [
    ["A. Bangalore","B. Chennai","C. Hyderabad","D. Kochi"],
    ["A. Nasik","B. Mumbai","C. Nagpur","D. NaviMumbai"],
    ["A. Madhurai","B. Salem","C. Chennai","D. kadapa"],
    ["A. Maharashtra","B. Karnataka","C. Kerala","D. Delhi"],
    ["A. Amrithsar","B. Lahore","C. kashmir","D. Lonavala"],
]

score = 0

def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_bank)):
    print("**********************************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess=input("Enter your answer(A/B/C/D)").upper()
    is_correct = check_answer(guess,question_bank[question_num]["answer"])

    if is_correct:
        print("Your Answer is Correct!!!")
        score+=1

    else:
        print("Incorrect Answwer ):")
        print(f"The correct answer is {question_bank[question_num]['answer']}")
    print(f"Your score is {score}/{question_num+1}")
print(f"you have given {score} corrrect answers")
print(f"your current score is {(score/len(question_bank))*100}%")            