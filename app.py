from Question import Question

question_prompts = [
    "what colour are apples?\n(a)Red\Green\n(b)Purple\n(c)Orange\n\n",
    "what colour are Bananas?\n(a)Red\Green\n(b)Blue\n(c)Yellow\n\n",
    "what colour are Strawberries?\n(a)Green\n(b)Red\n(c)Chocolate\n\n"]


questions =[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
    ]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("you got " + str(score) +"/" + str(len(questions)) + " correct")


run_test(questions)
