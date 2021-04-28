from uuid import *
from Question import *

# A Sample class with init method  
class QuestionService:

    
    questions = []
    count = 0
   
    # Methods
    def addQuestion(self, question: Question):
        self.questions.append(question)

    def createQuestion(self, clue:str):
        newQuestion = Question(clue)
        return newQuestion

    def getQuestion(self, questionId:str):
        return self.findQuestion(questionId)

    def getQuestions(self):
        return self.questions

    def getCount(self):
        return self.count

    def updateCount(self):
                self.count+= 1

    def findQuestion(self, questionId: str):
        for question in self.questions:
            if (question.questionId == questionId):
                return question
            else:
                return "Error: Question does not exist."
        

questionService = QuestionService()
question1 = questionService.createQuestion("is it red?")
questionService.addQuestion(question1)
print("Question1 ID: ", question1.questionId)
