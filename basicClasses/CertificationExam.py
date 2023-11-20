"""
    Topic: Certification Exam Class
    Date: 13 Nov 2023
    Author: Kathleen
"""
class CertificationExam:
    def __init__(self, id="", title="", successMark=0, nbOfDaysToWait=0):
        self._id = id
        self._title = title
        self._successMark = successMark
        self._nbOfDaysToWait = nbOfDaysToWait

    def getID(self):
        return self._id

    def getTitle(self):
        return self._title

    def getSuccessMark(self):
        return self._successMark

    def setSuccessMark(self, successMark):
        if successMark == None:
            print(f"Error, the success mark can not be null")
        else:
            self._successMark = successMark

    def getNbOfDaysToWait(self):
        return self._nbOfDaysToWait

    def setNbOfDaysToWait(self, nbOfDaysToWait):
        if nbOfDaysToWait == None:
            print(f"Error, the number of days to wait can not be null")
        else:
            self._nbOfDaysToWait = nbOfDaysToWait

    def __str__(self):
        return f"ID: {self._id} Title: {self._title} Success Mark: {self._successMark} Number of Days to Wait: {self._nbOfDaysToWait}"

