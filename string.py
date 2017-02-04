
'''
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." 
So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:

    Ask the user to input a word in English.
    Make sure the user entered a valid word.
    Convert the word from English to Pig Latin.
    Display the translation result.

'''

def pig_latin():
    word = input("word: ")
    if( len(word) > 3 ) :
        latin = word[1:len(word)] + "pay" 
        print (latin)
    else :
       print ("Não e valido:" + word )
       pig_latin()

	   
	   
print ('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word:")

if( len(original) > 0 and original.isalpha()):
    print (original)
else:
   print ("empty")
   
pig_latin()

