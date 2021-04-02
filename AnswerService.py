from uuid import *
from Answer import *
import json

# A Sample class with init method  
class AnswerService:

    
    answers = []
   
    # Methods

    def convertToJson(self, data):
        return json.dumps(data.__dict__)
    
    def convertToPython(self, data):
        return json.loads(data)
    
    def addAnswer(self, answer: Answer):
        self.answers.append(answer)

    def createAnswer(self, answer:str):
        newAnswer = Answer(answer)
        jsonObj = self.convertToJson(newAnswer)
        pythonObj = self.convertToPython(jsonObj)
        return pythonObj

    def getAnswer(self, answerId:str):
        return self.findAnswer(answerId)

    def getAnswers(self):
        return self.answers

    def findAnswer(self, answerId: str):
        for answer in self.answers:
            newAnswer = self.convertToPython(answer)

            if (newAnswer.get("answerId") == answerId):
                return answer
            else:
                return "Error: Answer does not exist."

answerService = AnswerService()

answer1 = answerService.createAnswer("is it red?")
answerService.addAnswer(answer1)

answer2 = answerService.createAnswer("is it round?")
answerService.addAnswer(answer2)

print("Answer1 ID: ", answer1.get("answerId"))
print("Answer2 ID: ", answer2.get("answerId"))
print("All Answers: ", answerService.getAnswers())
