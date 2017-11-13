# Mike Gorman
# 10.2: Trivia Game

"""
In this programming exercise, you will create a simple trivia game for two players.
The program will work like this:
Starting with player 1, each player gets a turn at answering 5 trivia questions.
(There should be a total of 10 questions.) When a question is displayed, 4 possible
answers are also displayed. Only one of the answers is correct, and if the player
selects the correct answer, he or she earns a point.
After answers have been selected for all the questions, the program displays the number of
points earned by each player and declares the player with the highest number of points
the winner.

To create this program, write a Question class to hold the data for the trivia question.
The question class should have attributes for the following data:
    A trivia question
    Possible answer 1
    Possible answer 2
    Possible answer 3
    Possible answer 4
    The number of the correct answer (1, 2, 3, or 4)

The Question class should also have an appropriate __init__ method, accessors, and mutators.

The program should have a list or a dictionary containing 10 Question Objects,
one for each trivia question.
Make up your own trivia question on the subject or subjects of your choice for the objects.
"""

# IMPORTS
import random


# QUESTION CLASS
class Question:
    # initializer/constructor
    def __init__(self, question, a1, a2, a3, a4, answer):
        self.question = question
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.answer = answer

    # setters/mutators
    def set_question(self, question):
        self.question = question

    def set_a1(self, a1):
        self.a1 = a1

    def set_a2(self, a2):
        self.a2 = a2

    def set_a3(self, a3):
        self.a3 = a3

    def set_a4(self, a4):
        self.a4 = a4

    def set_answer(self, answer):
        self.answer = answer

    # getters/accessors
    def get_question(self):
        return self.question
    def get_a1(self):
        return self.a1

    def get_a2(self):
        return self.a2

    def get_a3(self):
        return self.a3

    def get_a4(self):
        return self.a4

    def get_answer(self):
        return self.answer
#  END QUESTION CLASS


# MAIN()
def main():

    #  QUESTIONS
        # this is where I am writing the questions/creating the question objects
    q1 = Question('In a Robot Chicken spoof, Who asked \'What the hell is an Aluminum Falcon?\'', '1: Han Solo',
                  '2: Mon Mothma', '3: Emperor Palpatine', '4: Darth Vader', 3)
    q2 = Question('As quoted by Han Solo, What is the Millennium Falcon\'s hyper drive speed?', '1: 12 Parsecs',
                  '2: Point 5 past light speed', '3: Twice light speed', '4: Point 2 past light speed', 2)
    q3 = Question('What is the blade color of Anakin Skywalker\'s first lightsaber?', '1: Blue', '2: Green',
                  '3: Yellow', '4: Red', 1)
    q4 = Question('What is the blade color of Anakin Skywalker\'s last lightsaber?', '1: Blue', '2: Green',
                  '3: Yellow', '4: Red', 4)
    q5 = Question('How many lightsabers were owned by Anakin Skywalker/Darth Vader?', '1: 1', '2: 2', '3: 3', '4: 4',
                  3)
    q6 = Question('What is the name of Leia\'s ship at the beginning of A New Hope?', '1: Bantha IV', '2: Slave I',
                  '3: Millennium Falcon', '4: Tantive IV', 4)
    q7 = Question('Who was \'A little short to be a Storm Trooper\'?', '1: Obi Wan', '2: Luke', '3: Han', '4: Lando',
                  2)
    q8 = Question('Outside of which planet was the first Death Star destroyed?', '1: Corusant', '2: Yavin',
                  '3: Tatooine', '4: Dantooine', 2)
    q9 = Question('What is the correct spelling of the Wookie home world?', '1: Kashyyyk', '2: Kachyyk',
                  '3: Kashyk', '4: Kashyyk', 1)
    q10 = Question('Which bounty hunter was NOT in Empire Strikes Back?', '1: Bossk', '2: Zuckuss', '3: IG-88',
                   '4: Cad Bane', 4)
    q11 = Question('Who is the leader of the Gungans?', '1: Jar Jar Binks', '2: Queen Amidala', '3: Boss Nass',
                   '4: Otoh Gunga', 3)
    q12 = Question('What planet is Padme and Palpatine from?', '1: Naboo', '2: Corusant', '3: Mustafar', '4: Kamino', 1)
    q13 = Question('On what planet were the clones created?', '1: Geonosis', '2: Ryloth', '3: Florrum', '4: Kamino', 4)
    q14 = Question('Which Sith lord created the \'Rule of Two\'?', '1: Darth Sidious', '2: Darth Plagueis',
                   '3: Darth Tyranus', '4: Darth Bane', 4)
    q15 = Question('Which Sith lord was Count Dooku?', '1: Darth Sidious', '2: Darth Plagueis',
                   '3: Darth Tyranus', '4: Darth Bane', 3)

    # END OF QUESTIONS

    # PLAYERS SCORE AND QUESTION LIST HOLDERS
    player1_score = 0
    player2_score = 0
    asked = 0

    questions = []
    game_questions = []

    # POPULATE QUESTION LISTS
    for i in range(0, 10):
        x = random.randint(1, 14)
        while x in questions:
            x = random.randint(1, 14)
        questions.append(x)

    for j in questions:
        if j == 0:
            game_questions.append(q1)
        if j == 1:
            game_questions.append(q2)
        if j == 2:
            game_questions.append(q3)
        if j == 3:
            game_questions.append(q4)
        if j == 4:
            game_questions.append(q5)
        if j == 5:
            game_questions.append(q6)
        if j == 6:
            game_questions.append(q7)
        if j == 7:
            game_questions.append(q8)
        if j == 8:
            game_questions.append(q9)
        if j == 9:
            game_questions.append(q10)
        if j == 10:
            game_questions.append(q11)
        if j == 11:
            game_questions.append(q12)
        if j == 12:
            game_questions.append(q13)
        if j == 13:
            game_questions.append(q14)
        if j == 14:
            game_questions.append(q15)


    # test list generation
    #print(questions)
    #print(game_questions)

    # GAME START
    print('      Welcome to your Python Star Wars Trivia Game!!!')
    print('      -----------------------------------------------')
    print('        Two players will answer 5 questions each.')
    print('                 Most correct answers wins.')
    print()
    print('Please enter the number (1-4) for the answer you wish to choose')
    print()
    print()
    for query in game_questions:
        if asked % 2 == 0:
            print('PLAYER 1:')
        else:
            print('PLAYER 2:')
        print()
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = int(input('What is your guess?: '))
        while guess < 1 or guess > 4:
            guess = int(input('Your guess must be between 1 and 4. : '))
        if guess == query.get_answer():
            print('----------------')
            print('You are correct.')
            print('----------------')
            print()
            if asked % 2 == 0:
                player1_score += 1
            else:
                player2_score += 1
        else:
            print('-----------------')
            print('Sorry, incorrect.')
            print('-----------------')
            print()
        asked += 1

    print('Player 1 answered', player1_score, 'questions correctly.')
    print('Player 2 answered', player2_score, 'questions correctly.')
    if player1_score > player2_score:
        print('Player 1 wins.')
    if player1_score < player2_score:
        print('Player 2 wins.')
    if player1_score == player2_score:
        print('Both players tied.')




main()
