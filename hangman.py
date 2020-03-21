import os 
import sys
import random
from words import word_list


def word():
    word=random.choice(word_list)
    word.upper()
    return word


def game_play(word,letter):
    if letter in word:
        return True
    else:
        return False
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

word=word()
aword=[]
for i in word:
    aword.append(i)
user=[]
index=[]
b=0
s=0

for i in range(len(word)):
    user.append("_")

os.system('clear')
while True:
    
    if b==0:
        print("         _______      ")
        print("        |       |     ")
        print("        |       |     ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("    ____|_______      ")
        print()

    elif b==1:
        print("         _______      ")
        print("        |       |     ")
        print("        |       |     ")
        print("        |       O     ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("    ____|_______      ")
        print()
        
    elif b==2:
        print("         _______      ")
        print("        |       |     ")
        print("        |       |     ")
        print("        |       O     ")
        print("        |       |     ")
        print("        |       |     ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("    ____|_______      ")
        print()
        
    elif b==3:
        print("         _______      ")
        print("        |       |     ")
        print("        |       |     ")
        print("        |       O     ")
        print("        |      /|     ")
        print("        |       |     ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("    ____|_______      ")
        print()
        
    elif b==4:
        print("         _______      ")
        print("        |       |     ")
        print("        |       |     ")
        print("        |       O     ")
        print("        |      /|\    ")
        print("        |       |     ")
        print("        |             ")
        print("        |             ")
        print("        |             ")
        print("    ____|_______      ")
        print()
        
    elif b==5:
        print("         _______      ")
        print("        |       |     ")
        print("        |       |     ")
        print("        |       O     ")
        print("        |      /|\    ")
        print("        |       |     ")
        print("        |      /      ")
        print("        |             ")
        print("        |             ")
        print("    ____|_______      ")
        print()
            
    print()
    print()
    for i in user:
        print(i,end=' ')
    print()
    print()
    if s==1:
        print("good!!! the letter exists in the word")
        print()
    elif s==2:
        print("ohh!!! the letter is not present in the word")    
        print()
    letter=input("guess a word or letter >>>")
    
    if game_play(word,letter):
        s=1
    else:
        s=2

    if game_play(word,letter)==False:
        b+=1
    
    if b==6:
        os.system('clear')
        print("         _______      ")
        print("        |       |     ")
        print("        |       |     ")
        print("        |       O     ")
        print("        |      /|\    ")
        print("        |       |     ")
        print("        |      / \    ")
        print("        |             ")
        print("        |             ")
        print("    ____|_______      ")
        print() 

    if game_play(word,letter):
        for i in find(word, letter):
            user[i]=letter

    if user==aword:
        print()
        print('*'*40)
        print("hurray!!! you saved the man")
        print('*'*40)
        print()
        c=input("do you want to play again (y or n)>>>")
        if c=='y':
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif c=='n':
            break    
        else:
            print("invalid input")
            break

          
    if "_" not in user or b==6:
        print()
        print("OOPS!! the man is HANGED")
        print()
        print("the word is >>>",word)
        print()
        c=input("do you want to play again (y or n)>>>")
        if c=='y':
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif c=='n':
            break    
        else:
            print("invalid input")
            break
        
    os.system('clear')


