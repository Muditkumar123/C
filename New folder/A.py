def equal(strOne,strTwo):
    lenOne = len(strOne)
    lenTwo = len(strTwo)

    if lenOne==lenTwo:      
        i = 0
        chk = 0
        while i<lenOne:
            #a
            if strOne[i] != strTwo[i]:
                chk = 1
                break
            i = i+1
        if chk==0:
            print("\nStrings are Equal")
        else:
            print("\nStrings are Not Equal")
    else:
        print("\nStrings are Not Equal")














l=[]
for i in range(int(input())):
    n=int(input())
    a=input()
    a1=list(a.strip())
        

