from enum import Enum

class SubjectType(Enum):
    FRENCH = 1
    ENGLISH = 2
    MATH = 3
    EMC = 4
    SPANISH = 5
    ITALIAN = 5.1
    PHYSICAL = 6
    SES = 7
    SNT = 8
    SVT = 9
    GERMAN = 10

def get_subjectType_by_string(subject: str) -> SubjectType:
    if subject == "FRENCH":
        return SubjectType.FRENCH
    elif subject == "ENGLISH":
        return SubjectType.ENGLISH
    elif subject == "MATH":
        return SubjectType.MATH
    elif subject == "SPANISH":
        return SubjectType.SPANISH
    elif subject == "ITALIAN":
        return SubjectType.ITALIAN
    elif subject == "PHYSICAL":
        return SubjectType.PHYSICAL
    elif subject == "SES":
        return SubjectType.SES
    elif subject == "SNT":
        return SubjectType.SNT
    elif subject == "SVT":
        return SubjectType.SVT
    elif subject == "GERMAN":
        return SubjectType.GERMAN
    return None
