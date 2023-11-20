"""
    Topic: This is the main
    Date: 17 Nov 2023
    Author: Kathleen
"""

from basicClasses.Candidate import Candidate
from basicClasses.CertificationExam import CertificationExam
from basicClasses.DoCertificationExam import DoCertificationExam

if __name__ == "__main__":

    certificationExam = CertificationExam("1z0-151", "Java", 0, 0)
    candidate = Candidate(lastName = "Jordan", certificationExam = certificationExam)
    doCertificationExam = DoCertificationExam(candidate)

    print(f"{doCertificationExam} \n")

    certificationExam2 = CertificationExam("1z0-151", "Java", 0, 0)
    candidate2 = Candidate(lastName = "London", certificationExam = certificationExam2)
    doCertificationExam2 = DoCertificationExam(candidate2)

    print(f"{doCertificationExam2} \n")

    certificationExam3 = CertificationExam("1z0-147", "Python", 0, 0)
    candidate3 = Candidate(lastName = "Smith", certificationExam = certificationExam3)
    doCertificationExam3 = DoCertificationExam(candidate3)

    print(f"{doCertificationExam3} \n")


