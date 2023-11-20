"""
    Topic: Do Certification Exam Class
    Date: 14 Nov 2023
    Author: Kathleen
"""

from basicClasses.Candidate import Candidate
from basicClasses.CertificationExam import CertificationExam

class DoCertificationExam:
    def __init__(self, candidate = None):
        self.__candidate = candidate
        self._java = CertificationExam('1z0-151', 'Java', self.__candidate._grade, self.__candidate._nbOfDaysToWait)
        self._python = CertificationExam('1z0-147', 'Python', self.__candidate._grade, self.__candidate._nbOfDaysToWait)
        self.validateCertification()

    def getCandidate(self):
        return self.__candidate
    
    def setCandidate(self, candidate):
        if candidate == None:
            print("Error, the candidate can not be null")
        else:
            self.__candidate = candidate
    
    def getJavaExam(self):
        return self._java
    
    def setJavaExam(self, javaExam):
        if javaExam == None:
            print("Error, the java exam can not be null")
        else:
            self._java = javaExam

    def getPythonExam(self):
        return self._python
    
    def setPythonExam(self, pythonExam):
        if pythonExam == None:
            print("Error, the python exam can not be null")
        else:
            self._python = pythonExam

    def getGrade(self, examMark):
        
        if examMark >= 95:
            return "A+"
        elif examMark >=90 and examMark<95:
            return "A"
        elif examMark >85 and examMark <= 90:
            return "B+"
        elif examMark >80 and examMark<=85:
            return "B"
        elif examMark >75 and examMark<=80:
            return "C+"
        elif examMark >70 and examMark<=75:
            return "C"
        elif examMark >65 and examMark<=70:
            return "D+"
        elif examMark >60 and examMark<=65:
            return "D"
        else:
            return "E"

    def getMark(self, examId, lastName):
        with open("Mark.txt", 'r') as rf:
            lines = rf.readlines()
            for line in lines:
                elements = line.strip().split(',')
                if elements[0] == examId and elements[1] == lastName:
                    self.__candidate.setExamMark(int(elements[2]))
                    return int(elements[2])

    
    def validateCertification(self):
        if self.__candidate._certificationExam._id == self._java._id:
            javaMark = self.getMark(self._java._id, self.__candidate._lastName)
            grade = self.getGrade(javaMark)
            if javaMark >= 65:
                self.__candidate.serviceSuccess(grade)
            else:
                self.__candidate.serviceFailure(7, grade)

        elif self.__candidate._certificationExam._id == self._python._id:
            pythonMark = self.getMark(self._python._id, self.__candidate._lastName)
            grade = self.getGrade(pythonMark)
            if pythonMark >= 60:
                self.__candidate.serviceSuccess(grade)
            else:
                self.__candidate.serviceFailure(7, grade)


    def __str__(self):
        if self.__candidate._grade:
                return f"Pass Certification exam: {self.__candidate._certificationExam._id} Certification Exam Title: {self.__candidate._certificationExam._title} Exam Mark: {self.__candidate._examMark} Grade: {self.__candidate._grade}"
        else: 
            return f"Fails Certification exam: {self.__candidate._certificationExam._id} Certification Exam Title: {self.__candidate._certificationExam._title} Exam Mark: {self.__candidate._examMark} Number Of Days to Wait: {self.__candidate._nbOfDaysToWait} Grade: {self.__candidate._grade}"
