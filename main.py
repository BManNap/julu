def skip(ta):
    while ta == 1:
        global boolS1, boolS2, boolS3
        print("what scene would you like to skip to? 0:Scene 1, 1:Scene 2 part A, 2:Scene 2 part B, 3:Scene 3")
        ta = ITa(4)
        if ta == 0: pass;
        if ta == 1: boolS1=False;
        if ta == 2: boolS1=False; boolS2=False;
        exit

def answers(ta, correctNum, sceneNum, questinNum):
    global cool
    if ta == correctNum:
        cool[f"Scene {sceneNum} question {questinNum}"] = "Correct"
    else:
        cool[f"Scene {sceneNum} question {questinNum}"] = "Wrong"

def ITa(limit):
    ta = 66
    while ta > limit+1 or ta < 0:
        print("please input a number listed")
        try:
            ta = int(input(": "))
        except:
            print("please input a whole number!")
    print("\n\n\n\n")        
    return ta

def readF(loc):
    with open(loc, "r") as r:
        page = r.readlines()
    return page

def rTl(file, start, end):
    for x in range(start, end):
        print(file[x])
        pass
    print(file[end])
    pass

def singleQ(file, line):
    print(file[line])

def debug():
    print(cool)
    input("enter debug 050")

def end():
    global boolS1
    print(cool)
    print("Would you like to retry?0:No 1:Yes")
    if ITa(1)==1:boolS1 = False;

def main():
    scene1()
    scene2A()
    scene2B()
    pass

def scene1():
    while boolS1:
        global cool
        cool = {}
        loc = readF("S1.txt")
        rTl(loc, 0, 8)
        answers(ITa(3), 0, 1, 1)
        
        rTl(loc, 9, 17)
        answers(ITa(3), 2, 1, 2)

        rTl(loc, 18, 49)
        answers(ITa(2), 1, 1, 3)

        rTl(loc, 50, 76)
        answers(ITa(3), 3, 1, 4)

        rTl(loc, 77, 102)
        answers(ITa(3), 1, 1, 5)
        end()

def scene2A():
    while boolS2A:
        global cool
        cool = {}
        loc = readF("S2.txt")
        rTl(loc, 0, 39)
        answers(ITa(3), 2, 2, 1)

        rTl(loc, 40, 181)
        answers(ITa(4), 3, 2, 2)

        singleQ(loc, 182)
        answers(ITa(3), 2, 2, 3)

        rTl(loc, 183, 218)
        answers(ITa(4), 3, 2, 4)

        singleQ(loc, 219)
        answers(ITa(2), 0, 2, 5)
        end()

def scene2B():
    while boolS2B:
        global cool
        cool = {}
        loc = readF("S2.txt")
        rTl(loc, 220, 267) #6
        answers(ITa(3), 1, 2, 6)

        singleQ(loc, 268) #7
        answers(ITa(3), 1, 2, 7)

        rTl(loc, 269, 269) #8
        answers(ITa(3), 2, 2, 8)

        rTl(loc, 270, 353) #9
        answers(ITa(3), 0, 2, 9)
        
        rTl(loc, 354, 376) #10
        answers(ITa(3), 2, 2, 10)

        rTl(loc, 378, 386) #11
        answers(ITa(3), 1, 2, 11)

        rTl(loc, 387, 398) #12
        answers(ITa(3), 0, 2, 12)

        rTl(loc, 399, 413) #13
        answers(ITa(2), 0, 2, 13)

        rTl(loc, 414, 450) #14
        answers(ITa(4), 1, 2, 14)

def scene3():
    while boolS3:
        global cool
        cool = {}
        loc = readF("S3.txt")
        rTl(loc, 0, 19)
        answers(ITa(3), 2, 3, 1)

        rTl(loc, 20, 48)
        answers()

        rTl(loc, 49, 83)
        answers()

        rTl(loc, 84, 177)
        answers()

        rTl(loc, 178, 223)
        answers()

        singleQ(loc, 224)
        answers
        singleQ(loc, 225)
        answers()

if __name__=='__main__':
    boolS1 = True
    boolS2A = True
    boolS2B = True
    boolS3 = True
    print("would you like to skip to a scene? 1:yes 0:no\n")
    ta = ITa(1)
    skip(ta)
    main()