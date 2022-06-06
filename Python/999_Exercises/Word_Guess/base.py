import random
list_words=[]
with open('wordle.txt') as f:
    for line in f:
        l = line.strip()
        print(l)
answer = list_words[random.randrange(2310)]

for i in range(0,6):
    guess= input("Guess a 5 letter word: ")
    if answer == guess:
        print("You won!")
        break
    for j in range(2310):
        if(guess == list_words(j)):
            a=a+1
    if(a>0):
        print("wrong answer")
    else:
        print("Invalid word")
        i=i-1
print(answer)
f.close()
