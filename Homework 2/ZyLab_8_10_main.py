# Saqib Siddiqui
# PSID: 1495537

palindrome = input()

nospace = palindrome.split(' ')

palindrome2 = ''.join(nospace)

lengthpali = len(palindrome2)
reversed_string = palindrome2[::-1]

#print(palindrome2)
#print(reversed_string)

#conditional = True
if reversed_string == palindrome2:
    print(palindrome, 'is a palindrome')
else:
    print(palindrome, 'is not a palindrome')

#if conditional == True:
 #   print(palindrome, 'is a palindrome')
#else:
 #   print(palindrome, 'is not a palindrome')


