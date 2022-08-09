# Samkelisiwe Mlanzeli <2420037332@bootcamp.wethinkcode.co.za>

def read_file():
    '''
    Reads contents from the text file (questions.txt)
    @return a list of five random questions
    '''
    question_list = []
    with open('questions.txt', 'r') as questions:
        question_list = set(questions.read().split('\n'))
    while('' in question_list):
        question_list.remove('')

    if (not question_list):
        return None
    return list(question_list)


def ask_questions(list_of_questions):
    '''
    Sends quesions one at a time to be displayed
    @param list of five questions
    @return a list of questions the user answer incorrectly
    '''
    incorrect_questions = []
    correct_questions = []

    for x, question in enumerate(list_of_questions):
        solution = question.split(',')[1].split()[0]
        user_answer = display_question(x+1, question)
        if (is_correct_answer(solution, user_answer)):
            correct_questions.append(question)
        else:
            incorrect_questions.append(question)

    return incorrect_questions


def display_question(question_number, question):
    '''
    Displays a single question from the list of questions
    Takes in an answer
    @param a single question
    @return the answer given by the user
    '''
    qna_list = []
    final_question = ""

    _question = question.split(', ')

    for x, q in enumerate(_question):
        if (x == 1):
            continue
        new_q = q.rstrip()
        qna_list.append(new_q)
    for qna in qna_list:
        final_question = final_question + qna.rstrip() + '\n'

    answer = input(f'{question_number}. '+final_question)
    return answer


def is_correct_answer(solution, user_answer):
    '''
    Checks if the answer given by the user is correct
    @param solution - The correct answer
    @param user_answer - The answer entered by the user
    @return boolean indicating if user answered correctly or not
    '''
    answer = str(user_answer)
    result = str(solution)
    if (not result == answer):
        return False
    return True

1
def next_round(current_round):
    '''
    Calculates the next round
    @param current round completed
    @return integer next round
    '''
    current_round = current_round + 1
    return current_round


if __name__ == '__main__':

    score = 0
    current_round = 0
    question_list = read_file()

    while score < 5:
        current_round = next_round(current_round)
        question_list = ask_questions(question_list)
        score = 5 - len(question_list)
    print("You have passed the Test. Hurray!!!")
