# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")

import string
def fun_applycaesarcipher(msg, shift):
	# letter=string.ascii_letters
	lower= string.ascii_lowercase+string.ascii_lowercase
	upper=string.ascii_uppercase+string.ascii_uppercase


	b=(list(map(str,msg.split(" "))))
	l=""
	for i in b:
		c=i
		d=""
		for i in c:
			if i in upper:
				f=upper.index(i)
				d=d+upper[f+(shift)]
			elif i in lower:
				f=lower.index(i)
				d=d+lower[f+(shift)]
		ashish=" "
		l=l+d
		return(l) 
# fun_applycaesarcipher("zodiac",-2)
# fun_applycaesarcipher("ABCDXYZ",-3)		
# fun_applycaesarcipher("ABCDXYZ",3)
# fun_applycaesarcipher("abcdxyz",-3)

# fun_applycaesarcipher("abcdxyz",3)		



			









