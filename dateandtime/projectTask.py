import datetime


class Project:
    def __init__(self, name, startDate, endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.tasks = []

    def addTask(self, task):
        if self.startDate + datetime.timedelta(days=task.days) <= self.endDate:
            self.tasks.append(task)

    def displayProject(self):
        print('Project:\n ', self.name)
        for eachTask in self.tasks:
            print('Task: ', eachTask.name)
            for eachResource in eachTask.resources:
                print('Resource: ', eachResource.name)
        print('\n\n')


class Task:
    def __init__(self, name, startDate, days):
        self.name = name
        self.startDate = startDate
        self.days = days
        self.resources = []

    def addResource(self, resource):
        if resource.learningDays <= self.days:
            self.resources.append(resource)


class Resources:
    def __init__(self, name, learningDays):
        self.name = name
        self.learningDays = learningDays


project = Project('Simple projects', datetime.date.fromisoformat('2020-01-01'), datetime.date.fromisoformat('2021-01-01'))
task1 = Task('Creating chatbot', datetime.date.fromisoformat('2020-03-01'), 150)
task2 = Task('Creating games', datetime.date.fromisoformat('2020-02-01'), 210)
resource1 = Resources('Java', 90)
resource2 = Resources('Python', 120)
resource3 = Resources('Javascript', 90)
resource4 = Resources('Ruby', 280)

task1.addResource(resource1)
task1.addResource(resource2)
task1.addResource(resource3)
task1.addResource(resource4)

task2.addResource(resource1)
task2.addResource(resource2)
task2.addResource(resource3)
task2.addResource(resource4)

project.addTask(task1)
project.addTask(task2)

project.displayProject()




