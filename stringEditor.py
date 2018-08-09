# Python little project on String Manipulation
# 2018/08/07 Started
# 2018/08/09 Finished
# Yan, Ming-Lun

import string

print("Welcome to stringEditor.py")
print("1. Enter a new string")
print("2. Print the current string")

# print("3. Change words in the current string")

print("3. Information about the current string")
print("4. Clear the current string")
print("5. Exit")
newString = ""
    i = 0
    while i < 1:
        w=int(input("Please enter the number of intended work: "))
        if w == 1:
            newString = str(input("Please enter the new string: "))
        if w == 2:
            print("The current string is: " + newString)
        if w == 3:
            string_list = newString.split(" ")
            print("1. Location -> Word")
            print("2. Total occurrence(s) of a word")
            print("3. Total number of words")
            print("4. Back")
                j = 0
                while j < 1:
                    w2 = int(input("What do you want to know about the string: "))
                    if w2 == 1:
                        n = int(input("Enter a number n for the nth word in the string: n= "))
                        if n <= len(string_list):
                            print("The nth word in the string is: "+ string_list[n-1].strip(string.punctuation))
                    if w2 == 2:
                        x = str(input("Please enter a word for its occrrence: "))
                        print("There are " + str(newString.count(x)) + " occurrence(s) of the word \""+ x + "\".")
                    if w2 == 3:
                        print("There are " + str(len(string_list))+ " word(s) in the string.")
                    if w2 == 4:
                        j=0
        if w == 4:
            newString = ""
            print("The current string is empty now.")
        if w == 5:
            i = 1

