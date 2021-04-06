from uuid import *
from Question import *
import json

# A Sample class with init method  
class QuestionService:

    
    questions = []
    count = 0
   
    # Methods

    def convertToJson(self, data:Question):
        return json.dumps(data.__dict__)
    
    def convertToPython(self, data):
        return json.loads(data)
    
    def addQuestion(self, question: Question):
        self.questions.append(question)

    def createQuestion(self, clue:str):
        newQuestion = Question(clue)
        jsonObj = self.convertToJson(newQuestion)
        pythonObj = self.convertToPython(jsonObj)
        return pythonObj

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
            newQuestion = self.convertToPython(question)
            if (question.get("questionId") == questionId):
                return question
            else:
                return "Error: Question does not exist."

