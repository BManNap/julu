def skip(ta):
    while ta == 1:
        print("what scene would you like to skip to? 0:Scene 1, 1:Scene 2, 2:Scene 3, 3:Scene 4")
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

def rTl(loc, start, end):
    with open(loc, "r") as r:
        page = r.readlines()
    for x in range(start, end):
        print(page[x])
        pass
    print(page[end])

def debug():
    print(cool)
    input("enter debug 050")

def main():
    scene1()
    #scene2()
    pass

def scene1():
    while boolS1:
        loc = "S1.txt"
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

def scene2():
    while boolS2:
        pass


if __name__=='__main__':
    global cool
    cool = {}
    print("would you like to skip to a scene? 1:yes 0:no\n")
    ta = ITa(1)
    skip(ta)
    boolS1 = True
    boolS2 = True
    boolS3 = True
    main()