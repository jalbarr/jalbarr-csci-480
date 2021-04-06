from uuid import *
import json
from Categories import *


# A Sample class with init method
class Answer:
    
    # init method or constructor   
    def __init__(self, answer:str):
        self.answerId = str(uuid4())[:7]
        self.answer = answer
        print("Answer: " + self.answerId + "Created")
        
        
    # Methods
    
    def addAnswer(self, answer:str):
        self.answer = answer

    def getAnswer(self):
    	return self
