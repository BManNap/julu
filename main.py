def skip():
    while ta == 1:
        print("what scene would you like to skip to? 0:Scene 1, 1:Scene 2, 2:Scene 3, 3:Scene 4")
        ta = ITa(4)
        if ta == 0: pass;
        if ta == 1: boolS1=False;
        if ta == 2: boolS1=False; boolS2=False;
        exit

def scene1():
    while boolS1:
        exit
        pass




def main():
    scene1()
    #scene2()
    pass

def ITa(limit):
    ta = 66
    while ta > limit+1 or ta < -1:
        print("please input a number listed")
        try:
            ta = int(input(": "))
        except:
            print("please input a whole number!")
    return ta

if __name__=='__main__':
    print("would you like to skip to a scene? 1:yes 0:no\n")
    ta = ITa(1)
    skip()
    boolS1 = True
    boolS2 = True
    boolS3 = True
    main()