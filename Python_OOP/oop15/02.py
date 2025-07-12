import enum
from enum import Enum

@enum.unique
class Status(Enum):
    SUCCESS = 1

    FAIL =2


def main():
    for s in Status:
        print(s.name)
    print(Status.__members__)



if __name__ =="__main__":
    main()