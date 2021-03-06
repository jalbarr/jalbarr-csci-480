from uuid import *

# A Sample class with init method  
class Question:

    
    clue = ""
    answer = ""
    questionId = str(uuid4())[:7]

    def __init__(self, clue:str):

        self.clue = clue
  
    # Methods
    def addAnswer(self, answer:str):
        self.answer = answer
        
    def addClue(self, clue:str):
        self.clue = clue

    def getAnswer(self):
        return self.answer
    
    def getClue(self):
        return self.clue

question = Question("Test Clue")