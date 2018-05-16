''' This funcion open a file and count its number of words.
Also, it gives a option to the user to search and count the number 
of a specific word.'''
import os
def count_words(file_name):
    try:
# Instruction to open the file read it and storage its content into 
# the variable content
        with open(file_name) as file_object:
            content = file_object.read()
# If the file is not found a error message is shown to the user
    except FileNotFoundError:
        print('\n------------------------------------------------------------')
        print('File not found! Verify if it is in your work folder!')
        print('Your current work folder is: {}'.format(os.getcwd()))
        print('--------------------------------------------------------------')
    else:
# The user can choose a specifc word to search and count in the file
        choice = input('You wanna know how many times a word appears in the file? y/n : ')
        if choice == 'y' or choice == 'Y':
            w = input('What word do you want to search? ')
            times_w = content.lower().count(w)
            print('\n--------------------------------------------------------')
            print('The word {} appears {} times in the file.'.format(w, times_w))
            print('--------------------------------------------------------')
# If he/she doesn't want to count a specific word, the total number of 
# words in the file will be shown
        elif choice == 'n' or choice == 'N':
            print('\n--------------------------------------------------------')
            print('So, I will show you the total word number of the file.')
            words = []
            num_words = 0
# The words in the content variable will be storage at a list called words.
            words = content.split()
# The instruction bellow will count the lenght of the list words, 
# the number of the words in the file
            num_words = len(words)
            print('The file {} has about {} words!'.format(file_name, num_words))
            print('--------------------------------------------------------')
        else:
# If the user type other letter than Y ou N, a error message will me shown
            print('\n--------------------------------------------------------')
            print('You type a invalid command')
            print('Please run the code again and type "y" or "n".')
            print('\n--------------------------------------------------------')
