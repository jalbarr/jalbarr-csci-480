from uuid import *
from Answer import *

# A Sample class with init method  
class AnswerService:

    
    answers = []
   
    # Methods

    
    def addAnswer(self, answer: Answer):
        self.answers.append(answer)

    def createAnswer(self, answer:str):
        newAnswer = Answer(answer)
        return newAnswer

    def getAnswer(self, answerId:str):
        return self.findAnswer(answerId)

    def getAnswers(self):
        return self.answers

    def findAnswer(self, answerId: str):
        for answer in self.answers:
            if (answer.answerId == answerId):
                return answer
            else:
                return "Error: Answer does not exist."
        

answerService = AnswerService()
answer1 = answerService.createAnswer("is it red?")
answerService.addAnswer(answer1)
answer2 = answerService.createAnswer("is it round?")
answerService.addAnswer(answer2)
print("Answer1 ID: ", answerService.getAnswer(answer1.answerId))
print("Answer2 ID: ", answerService.getAnswer(answer2.answerId))
print("All Answers: ", answerService.getAnswers())
