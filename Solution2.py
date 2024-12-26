print('Printing current and previous number sum in a range(10)')

for i in range(0,10):
    current_number = i
    previous_number = i - 1
    if previous_number < 0 :
        previous_number = 0
    sum = current_number + previous_number
    print(f'Current Number {current_number} Previous Number {previous_number} Sum : {sum}')

#This will output what was stated in the description of the exercise
#if we wanted to start by the number one we simply change the start of the range to be 1 insted of 0 (the lower bound of the range is always included)

#I wanted to highlight that when you're iterating (whether using a for loop or a while loop) the name you assign to the iteration variable in it self doesn't really matter what actually makes a difference is what you're iterating through or the iterable.
#in the case of a list, string or a dictionnay the iteration variable represents the each element in the iterable. for instance :
#input 

list = [1,2,3,4,5,6,7,8,9]
for i in list:
   print(i)

#output
#1
#2
#3
#4
#5
#6
#7
#8
#9

#the same goes for a string :

string = 'This is a string'
for i in string :
   print(i)

#output
#T
#h
#i
#s
#i
#s
#a
#s
#t
#r
#i
#n
#g

#However, when we iterate through a range things change and the iteration variable we name referes to the index of each element. for instance :

list = [1,2,3,4,5,6,7,8,9]
for i in range(0,len(list)) :
   print(i)

#output
#0
#1
#2
#3
#4
#5
#6
#7
#8
#I asked for help from Claude Ai to try to enrich what I wrote but i didn't really give me what I wanted since my goal is to explain the things i learn in a simple way for those (like me) who do not have an IT background or just want to learn code.

