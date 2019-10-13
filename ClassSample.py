
import json

class ClassSample : 
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job=job
    
    def getInfo(self):
        return f'Name: {self.name}. Age: {self.age}. Job: {self.job}'

    def getInfoJson(self):
        return {
            "name" : self.name,
            "age" : self.age,
            "job" : self.job
        }

worker = ClassSample('alex', 23, 'programmer')

print(worker.getInfoJson())