'''
Created on 17-Jul-2016

@author: Lokeshwar
'''
# CS61002: Algorithms and Programming 1 
# Name: Lokeshwar Reddy Kasarla
# Date: 07/17/2016
# Lab05.py



##### Template for assignments. Duplicate for appropriate number of exercises. ######

print "********** Exercise 1**********"




import stdio
import sys

#reading string for DNA species
species1 = raw_input("Enter species one DNA string :")
species2 = raw_input("Enter species two DNA string :")
#writing DNA Species strings 
stdio.writeln("Species 1: "+species1)
stdio.writeln("Species 2: "+species2)
#strating infinte loop
while True:
    #asking for user choices
    choice = raw_input("What do you want to do:\n\t\t\t\t a ( add indel )\n\t\t\t\t d (delete indel) \n\t\t\t\t s (score) \n\t\t\t\t q (quit) : ")
    #if user selects add indel
    if (choice == 'a'):
        #ask for which string and which position to add
        strChoice=input("Which string do you want to add an indel(1 or 2) : ")
        strPos =input("Which position do you want to insert indel : ")
        if(strChoice == 1):
            #add a indel to to selected string
            if(strPos>0 and len(species1)>=strPos+1):
                species1=species1[:strPos]+'-'+species1[strPos:]
                stdio.writeln("Successfully pushed indel")
            else:
                stdio.writeln("Error While trying to push an indel in "+species1+" at position :"+str(strPos))
        elif(strChoice == 2):
            if(strPos>0 and len(species2)>=(strPos)+1):
                species2=species2[:strPos]+'-'+species2[strPos:]
                stdio.writeln("Successfully pushed indel")
            else:
                stdio.writeln("Error While trying to push an indel in "+species2+" at position :"+str(strPos))
        else:
            stdio.writeln("Please select the string as 1 or 2 only, Please try again")
    #if user select delete
    elif(choice == 'd'):
        #ask for which string to delete and what position to delete
        strChoice=input("Which string do you want to delete an indel(1 or 2) : ")
        strPos =input("Which position do you want to remove indel : ")
        if(strChoice == 1):
            #checking if indel exisits before deleting said position
            if(strPos>0 and len(species1)>(strPos)):
                if(species1[strPos]=='-'):
                    species1=species1[:strPos]+species1[strPos+1:]
                    stdio.writeln("Successfully pop indel")
                else:
                    stdio.writeln("No indel found to pop")
            else:
                stdio.writeln("Error While trying to pop an indel in "+species1+" at position :"+str(strPos))
        elif(strChoice == 2):
            if(strPos>0 and len(species2)>(strPos)):
                if(species2[strPos]=='-'):
                    species2=species2[:strPos]+species2[strPos+1:]
                    stdio.writeln("Successfully poped indel")
                else:
                    stdio.writeln("No indel found to pop")
            else:
                stdio.writeln("Error While trying to pop an indel in "+species2+" at position :"+str(strPos))
        else:
            stdio.writeln("Please select the string as 1 or 2 only, Please try again")
    #user selected score option
    elif(choice =='s'):
        #creating temporary duplicate species to calculate string
        tspecies1 = species1
        tspecies2 = species2
        if(len(tspecies1)<len(tspecies2)):
            for indel in range(len(tspecies2)-len(tspecies1)):
                tspecies1=tspecies1+'-'
        elif(len(tspecies1)>len(tspecies2)):
            for indel in range(len(tspecies1)-len(tspecies2)):
                tspecies2=tspecies2+'-'
        #setting matches to zero
        matches = 0
        tspecies1 = tspecies1.upper()
        tspecies2 = tspecies2.upper()
        for index in range(0,len(tspecies1)):
            if(tspecies1[index]==tspecies2[index]):
                #incrementing matches if match found
                matches=matches+1
                tspecies1 = tspecies1[:index]+tspecies1[index].lower()+tspecies1[index+1:]
                tspecies2 = tspecies2[:index]+tspecies2[index].lower()+tspecies2[index+1:]
            else:
                tspecies1 = tspecies1[:index]+tspecies1[index].upper()+tspecies1[index+1:]
                tspecies2 = tspecies2[:index]+tspecies2[index].upper()+tspecies2[index+1:]
        #displaying found matches and indented string
        stdio.writeln("Number of Matches : "+str(matches)+". Number of mismatches : "+str(len(tspecies1)-matches))
        stdio.writeln(" Species 1 : "+tspecies1+"\n Species 2 : "+tspecies2)
    #breaking from infinte loop on user specific choice
    elif(choice =='q'):
        stdio.writeln("Terminating the program")
        break
    #if your entered wrongchoice
    else:
        stdio.writeln("Please enter your choice as a,d,s or q only. Please try again")
#terminating the program
sys.exit(0)