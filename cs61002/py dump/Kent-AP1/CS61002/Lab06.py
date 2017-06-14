'''
Created on 24-Jul-2016

@author: Lokeshwar
'''
# CS61002: Algorithms and Programming 1 
# Name:Lokeshwar Reddy Kasarla
# Date:07/24/2016
# Lab06.py


print "********** Exercise 6**********"

import stdio
import random
import glob
import sys

#function to take file name as argument

def dictonary_file(file_name):
    dictonary = {}
#opening the file with read access
    for line in open(file_name,'r'):
        #reading each line and processing it
        whole_line = line.replace("\n","")
        word = whole_line[:whole_line.index(":")]
        rest_line =whole_line[whole_line.index(":")+1:]
        number_of_meanings = rest_line.count(',')+1
        if(number_of_meanings==2):
            new_meaning1 = rest_line[:rest_line.index(",")]
            rest_line = rest_line[rest_line.index(",")+1:]
            new_meaning2 = rest_line
            #adding the word and its answer to dictonary
            dictonary[word]=[new_meaning1,new_meaning2]
        else:
            dictonary[word]=rest_line    
    #returning the sictonary
    return dictonary

#setting list of files to empty
list_of_files=""
stdio.writeln("Available file in present directory are: ")
#reading all files in the current directory with .txt extension
for single_file in glob.glob("*.txt"):
    list_of_files+=single_file+"\n"
    stdio.writeln(single_file)
    
list_of_files = list_of_files.split("\n")


#accepting the user choice from list above
found = False
while True:
    choosen_file = raw_input("Please choose one of the files to start : ")
    for selected in list_of_files:
        #checking that the file name in list of files found
        if(choosen_file ==selected):
            found = True
    if found:
        break
    else:
        stdio.writeln("Specified file not found, Please try again !")
#calling the functin with file selected
new_dictonary = dictonary_file(choosen_file)

#checking that there are any meanings on dictonary
if (len(new_dictonary)>0):
    stdio.writeln("There are "+str(len(new_dictonary))+" Items in "+choosen_file)
else:
    stdio.writeln("Unfortunately, The "+choosen_file+" doesnt had entries")
    stdio.writeln("Exiting the program")
    sys.exit(0)

number_of_questions=0
#asking the user to input number of questions he want on quiz and error checking
while True:
    number_of_questions= int(raw_input("How many questions would you like to have on quiz : "))
    if(int(number_of_questions)<=len(new_dictonary) and  int(number_of_questions)>0):
        break
    else:
        stdio.writeln(str(number_of_questions)+" is out of expected range, please enter a number between 1 and "+ str(len(new_dictonary)))

#asking the user number of choices they want
while True:
    number_of_choices= int(raw_input("How many Choices would you like to have on each quiz: "))
    if number_of_choices>0:
        break
    else:
        stdio.writeln(str(number_of_choices)+" is out of expected range, please enter a number greater than 0")


#setting score counter to zero
my_score = 0

#for number of questions nesting the loops
for quizes in range(number_of_questions):
    #selecting a random word key from dictonary
    random_question = random.choice(new_dictonary.keys())
    #retrieving the value for generated question 
    random_answer = str(new_dictonary[random_question])
    multiple_answers = False
    #setting answer to array
    random_answer = random_answer.replace("[","").replace("]","").replace("'","")
    answers = ["",""]
    #checking how many values we for current key
    if random_answer.count(",")>0:
        multiple_answers = True
        answers[0]= random_answer[:random_answer.index(",")]
        answers[1]= random_answer[random_answer.index(",")+1:]
    else:
        answers[0]=random_answer  
    #formating the question
    present_question = str(random_question)
    present_question = present_question.replace("[","").replace("]","").replace("'","")
    stdio.writeln("Question is : "+present_question+", Answer is : "+answers[0]+" Answer 2 is : "+answers[1])
    #showing question to user
    stdio.writeln("Enter the meaning of : " + present_question)
    for choice in range(number_of_choices):
        #accepting the answer from user
        present_answer=raw_input("Choice "+str(choice+1)+" of "+str(number_of_choices)+" Choices : ")
        #checking for number of answers to match
        if answers[0]== present_answer or answers[1]==present_answer:
            #if match found,, incrementing the score and breaking from this question
            my_score+=1
            stdio.writeln("Correct Answer!")
            break
#displaying score
stdio.writeln("Your Score is : "+str(my_score)+ " out of "+str(number_of_questions))
#displaying end message
stdio.writeln("End of Program")