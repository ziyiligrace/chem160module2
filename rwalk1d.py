from random import choice
trials=1000
steps=1000
gothome=0
for i in range(trials):
    point=1
    for step in range(steps) :
        point+=choice((-1,1))
        if point==0 :
            gothome+=1
            break
print("Fraction that got home=" , gothome/trials)