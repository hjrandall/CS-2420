import random
def main():
    print()
    powers=["1","2","4","8","16","32","64","128","256","512","1k","2k","4k","8k","16k","32k","64k","128k","256k","512k","1m","2m","4m","8m","16m","32m","64m","128m","256m","512m","1b","2b","4b","8b","16b","32b","64b","128b","256b","512b","1t","2t","4t","8t","16t","32t","64t","128t","256t","512t"]
    p_answers=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49"]
    asked_q=[]
    print("welcome to 2's power practice course! click enter when you are ready to begin->")
    input("")
    
    while len(asked_q)!=49:
        num= random.randrange(0,50)
        while powers[num] in asked_q:
            num= random.randrange(0,50)
        asked_q.append(powers[num])
        print ("which 2's power equals",powers[num],"? ->" , end=" ")
        answer=input ("")
        answer.strip()
        while answer != p_answers[num]:
            print("wrong! try again! ->", end=" ")
            answer=input("")
main()
        
        
