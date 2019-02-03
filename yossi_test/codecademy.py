from click._compat import raw_input

print("Hello and welcome to Yossis game :")
original = raw_input("Enter a word : ")
if len(original) > 0:
    print('Your entered a word : ' + original + " and the length of the word is " + str(len(original)))
else:
    print("Empty")
