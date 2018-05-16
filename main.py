'''The variable file_name receive a string that is the name of the file that you want to analize, the file has to be in your work folder, otherwise a error message will be displayes.
The files used in this code were dowloaded at http://www.gutenberg.org. 
There are a plenty of public domain books that can be downloaded in this website. If you want, you can use another one.'''
import count_words
file_name = 'the_invisible_man.txt'
count_words.count_words(file_name)
