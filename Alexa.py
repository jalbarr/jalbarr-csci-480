from AnswerService import *
from QuestionService import *
from AnswerService import *
from Categories import *

# A Sample class with init method  


class Alexa:

    questionService = QuestionService()
    answerService = AnswerService()
    categories = Categories()
    correctAnswer = None


    def __init__(self):
        self.correctAnswer = Categories.getRandomCategory(self.categories)

        
    # Sample Method
    def createQuestion(self, clue:str):
        self.questionService.createQuestion(clue)

    def addQuestion(self, question:Question):
        self.questionService.addQuestion(question)

    def getQuestion(self, questionId:str):
        self.questionService.getQuestion(questionId)

    def getQuestions(self):
        return self.questionService.getQuestions()

    def getQuestionCount(self):
        return self.questionService.getCount()

    def updateQuestionCount(self):
        self.questionService.updateCount()

    def getCorrectAnswer(self):
        return self.correctAnswer

    def addAnswer(self, answer: Answer):
        self.answerService.addAnswer(answer)

    def createAnswer(self, answer:str):
        self.answerService.createAnswer(answer)

    def getAnswer(self, answerId:str):
        return self.answerService.getAnswer(answerId)

    def getAnswers(self):
        return self.answerService.getAnswers()



    '''
    TODO: 
    - Set up function that Initializes the game and key features.
    - database to store game information such as questions, answers, and categories
    '''
    def gameStart(self):
        pass

    '''
    TODO:
    - display a message that the game is ending
    - end the program 
    '''
    def gameStop(self):
        pass

alexa = Alexa()