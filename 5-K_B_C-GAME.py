# KBC Game In Python............///////////////////

questions = [
    ["Q1: What is the value of \"Pie\"?", "5.12", "6.54", "3.14", '7.89\n', 1],
    ["Q2: Which of the following is a programming language?", "HTML", "JPEG", "PDF", "CSS\n", 1],
    ["Q3: What does the acronym \"IDE\" stand for in programming?", "Integrated Development Engine",
    "Integrated Design Environment\n\t", "Integrated Development Environment", "Intelligent Development Engine\n", 1],
    ["Q4: Which data structure follows the \"Last In, First Out\" (LIFO) principle?", "Queue", "Stack",
    " Array ", "Linked List\n", 1],
    ["Q5: What does the acronym \"API\" stand for in programming?", "Advanced Programming Interface ",
    "Application Programming Interface \n\t", "Application Processing Interface", " None\n", 1],
    ["Q6: What does the acronym \"API\" stand for in programming?", "Advanced Programming Interface ",
    "Application Programming Interface \n\t", "Application Processing Interface", " None\n", 1],
    ["Q7: What does the acronym \"API\" stand for in programming?", "Advanced Programming Interface ",
    "Application Programming Interface \n\t", "Application Processing Interface", " None\n", 1],
]

levels = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 0]
print("\n\t\t\t\t\t\t\t~~~~***** WELCOME TO KAUN BANEGA CROREPATI *****~~~~~\n")
for i in range(0, len(questions)):
    question = questions[i]
    if i - 1 == len(question):
        break
    print(f"Question For Rs. {levels[i]}")
    print(f"{question[i == -1]}")
    print(f"1){question[1]}          2){question[2]}")
    print(f"3){question[3]}          4){question[4]}")
    reply = int(input("Enter Your Answer(1-4):\t"))
    if reply == question[-1]:
        print(f'\n\t\t\t!!!CORRECT ANSWER!!!\n\t*** CONGRATULATIONS! YOU WON RS. {levels[i]} ***\n')
    else:
        print(f"\n\t\t!!!WRONG ANSWER!!!\n***** YOU WON TOTAL AMOUNT RS.{levels[i - 1]} *****")
        break
    print("\t\t\t\t\t\t\t^^^^^!!!!!!!!!!~~~~~~%%%%%%%%%**********%%%%%%%%%~~~~~!!!!!!!!!!^^^^^\n")
