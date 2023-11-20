"""
    Topic: Certification Exam Class
    Date: 14 Nov 2023
    Author: Kathleen
"""

from basicClasses.Person import Person

class Candidate(Person):
    def __init__(self, firstName="", lastName="", phone="", certificationExam=None, examDate=""):
        super().__init__(firstName, lastName, phone)
        self._certificationExam = certificationExam
        self._examDate = examDate
        self._examMark = None
        self._grade = None
        self._nbOfDaysToWait = None

    def getCertificationExam(self):
        return self._certificationExam

    def setCertificationExam(self, certificationExam):
        if certificationExam == None:
            print("Error, the certification exam can not be null")
        else:
            self._certificationExam = certificationExam

    def getExamDate(self):
        return self._examDate

    def setExamDate(self, examDate):
        if examDate == None:
            print("Error, the exam date can not be null")
        else:
            self._examDate = examDate

    def getExamMark(self):
        return self._examMark

    def setExamMark(self, examMark):
        if examMark == None:
            print("Error, the exam mark can not be null")
        else:
            self._examMark = examMark

    def serviceSuccess(self, grade):
        self._grade = grade

    def serviceFailure(self, nbOfDaysToWait, grade=None):
        self._nbOfDaysToWait = nbOfDaysToWait
        self._grade = grade

    def __str__(self):
        if self._nbOfDaysToWait == None:
                return super().__str__() + f"Pass Certification exam: {self._certificationExam._id} Certification Exam Title: {self._certificationExam._title} Exam Mark: {self._examMark}"
        else: 
            return super().__str__() + f"Fails Certification exam: {self._certificationExam._id} Certification Exam Title: {self._certificationExam._title} Exam Mark: {self._examMark} Number Of Days to Wait: {self._nbOfDaysToWait}"
        
       
