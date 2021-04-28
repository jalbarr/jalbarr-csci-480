from uuid import *
import json
from Categories import *


# A Sample class with init method
class Answer:  
      
    answer = ''
    answerId = None
    
    # init method or constructor   
    def __init__(self, answer:str):
        self.answer = answer
        self.answerId = str(uuid4())[:7]
    # Methods
    def convertToJson(self):
        return json.dumps(self.__dict__)
    
    def addAnswer(self, answer:str):
        self.answer = answer

    def getAnswer(self):
    	return self.convertToJson()

answer = Answer("Test Answer")
