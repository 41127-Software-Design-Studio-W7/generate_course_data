from hashlib import new
from random import random
import random


class Course:
    def __init__(self, id, name, credit_points):
        self.id = id
        self.name = name
        self.creditPoints = credit_points

class Subject:
    def __init__(self, id, name, course, topic, prereqs, assignment_percent, test_percent, presentation_percent, credit_points):
        self.id = id
        self.name = name 
        self.course = course
        self.topic = topic
        self.prerequisites = prereqs
        self.assignments = assignment_percent
        self.tests = test_percent
        self.presentations = presentation_percent
        self.creditPoints = credit_points

class Topic: 
    def __init__(self, id, name):
        self.id = id
        self.name = name

allCourses = []
courses = 0
allSubjects = []
subjects = 0
allTopics = []
topics = 0
CP_STANDARD = 6
SUBJECTSPERSEM_STANDARD = 4

'''
for i in range(0, 4):
    topics = topics + 1
    newTopic = Topic(topics, "Topic_" + str(topics))
    allTopics.append(newTopic)
'''

courses = courses + 1
newCourse = Course(1, "Course_" + str(courses), CP_STANDARD * SUBJECTSPERSEM_STANDARD * 5)
allCourses.append(newCourse)

'''
for i in range(0, newCourse.creditPoints//CP_STANDARD/SUBJECTSPERSEM_STANDARD):
    subjects = subjects + 1
    newSubject = Subject(subjects, "Subject_" + str(subjects), courses[0].id, topics[random.randint(0, len(topics)-1)], [], 0.4, 0.3, 0.3, CP_STANDARD)
'''

i = 0
while subjects < newCourse.creditPoints//CP_STANDARD - 1:
    topics = topics + 1
    newTopic = Topic(topics, "Topic_" + str(topics))
    allTopics.append(newTopic)

    subjectsThisTopic = 0
    totalSubjectsThisTopic = random.randint(1, newCourse.creditPoints//CP_STANDARD//SUBJECTSPERSEM_STANDARD-2)
    while subjectsThisTopic < totalSubjectsThisTopic: #### newCourse.creditPoints//CP_STANDARD//SUBJECTSPERSEM_STANDARD
        subjects = subjects + 1
        #prerequisites
        thisSubPrereqs = []
        if subjectsThisTopic > 0:
            thisSubPrereqs.append(allSubjects[-1])
        #coursework
        assignments = random.randint(0, 20)
        tests = random.randint(0, 20-assignments)
        presentations = 20 - assignments - tests


        newSubject = Subject(subjects, "Subject_" + str(subjects), allCourses[0].id, allTopics[-1].name, thisSubPrereqs, float(assignments)/20, float(tests)/20, float(presentations)/20, CP_STANDARD)
        allSubjects.append(newSubject)
        subjectsThisTopic = subjectsThisTopic + 1
        print(newSubject.name + " " + str(newSubject.topic) + " " + str(newSubject.assignments))



print(newCourse.creditPoints)