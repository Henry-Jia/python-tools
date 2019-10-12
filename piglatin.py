#Translates text to "pig latin"
#Pig latin is made by moving to the first consonant or group of consonants to the end of the word and then adding "ay"
#Pig latin -> igpay atinlay

def translate(word):
	for i in range(len(word)):
		if word[i] in "aeiouyAEIOUY":
			return word[i:] + word[:i] + "ay"
	return word + "ay"

starttext = input("Please enter the text you want translated to pig latin: ")
wordlist = starttext.split(" ")
for word in wordlist:
	if word:
		word = translate(word)
		print(word, end=" ")