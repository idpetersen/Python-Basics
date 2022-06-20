# ------------------------------------------------ #
'''first_letter'''

# Write a function called first_letter that takes in a string and returns the first character of that string.


### YOUR CODE STARTS HERE ###
def first_letter(string):
  return string[0]



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''last_three'''

# Write a function called last_three that takes in a string and returns the last three characters of the string. You can assume the string argument will always be at least three characters long.


### YOUR CODE STARTS HERE ###
def last_three(string):
  return string[-3:]



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''char_count'''

# Write a function called char_count that takes in a string of a single character as well as a larger string. char_count will return the amount of times the character is found within the larger string (upper or lowercase).

#is it working now?

### YOUR CODE STARTS HERE ###
def char_count(single_letter, string):
  single = single_letter.lower()
  word = string.lower()
  count = 0 

  
  for value in word:
    if value == single:
      count += 1


  return count



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''remove_vowels'''

# Write a function called remove_vowels that takes in a string and returns a string with all the vowels removed.



### YOUR CODE STARTS HERE ###
def remove_vowels(string):

  newstring = ''
  
  for i in string:
    if not i.lower() in 'aeiou':
      newstring += i

  return newstring
      



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''hello_goodbye'''

# Write a function called hello_goodbye that takes in a string representing a name and an integer. If the integer is 1, return the string "Hello, <NAME>". If the integer is 2, return the string "Goodbye, <NAME>"



### YOUR CODE STARTS HERE ###
def hello_goodbye(name, int):

  if int == 1:
    return "Hello, " + name

  elif int == 2:
    return "Goodbye, " + name



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''spooky'''

# Write a function called spooky which takes in a string and returns a string, composed of the same characters, in alternating case (beginning with lowercase).



### YOUR CODE STARTS HERE ###
def spooky(string):
  result = ""
  for i in range(len(string)):
    if not i % 2 == 0:
       result = result + string[i].upper()
    else:
       result = result + string[i].lower()

  return result


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''initials'''

# Write a function called initials which takes in a string of a full-name, where each name is separated by a space. Return back a string representing the initials of a string passed to this function.



### YOUR CODE STARTS HERE ###
def initials(string):


  name_list = string.split()

  initials = ''

  for name in name_list:
      initials += name[0]

  return initials
  



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''mixup'''

# Write a function called mixup which takes in two strings. Return a string that is the concatenation of the two inputted strings (space-separated) except the first characters have been swapped.



### YOUR CODE STARTS HERE ###
def mixup(str1, str2):
  
  mixup1 = str1.replace(str1[0], str2[0], 1)
  
  mixup2 = str2.replace(str2[0], str1[0], 1)

  result = mixup1 + ' ' + mixup2


  return result



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''mixup_extended'''

# When you are done with the mixup function above, go ahead and copy the functionality and name it mixup_extended. This new function will instead take in two strings AND a number. This number represents how many characters you should swap from the beginning of each string. You can assume that the number will always be valid, that is it will be less than the number of characters in the shorter string.



### YOUR CODE STARTS HERE ###

def mixup_extended(str1, str2, int):
  
  mixup1 = str1.replace(str1[0:int], str2[0:int], 1)
  
  mixup2 = str2.replace(str2[0:int], str1[0:int], 1)

  result = mixup1 + ' ' + mixup2


  return result



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''not_bad'''

# Write a function called not_bad that takes in a string. Assume this string always has the substrings 'not' and 'bad'. Replace all of the words from the word 'not' until the word 'bad' with 'good'.


### YOUR CODE STARTS HERE ###
def not_bad(string):

  where_not = string.find("not")

  where_bad = string.find("bad")

  goodified = string.replace(string[where_not:where_bad + 3], "good")

  return goodified



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''h4ck3r_sp33k'''

# Write a function called h4ck3r_sp33k that takes in a string and returns the string in "h4cker sp33k" by replacing characters the following way:

  # 'A','a' => '4'
  # 'E','e' => '3'
  # 'L','l' => '1'
  # 'T','t' => '+'  

### YOUR CODE STARTS HERE ###
def h4ck3r_sp33k(string):

  for i in range(len(string)):

    if string[i] == 'a':
      
      string = string.replace(string[i], '4', 1)

    elif string[i] == 'e':

      string = string.replace(string[i], '3', 1)

    elif string[i] == 'l':

      string = string.replace(string[i], '1', 1)

    elif string[i] == 't':

      string = string.replace(string[i], '+', 1)

  return string
      


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''same_x_and_o'''

# Write a function called same_x_and_o that takes in a string and returns true if it has the same number of "x" and "o" characters in it.


### YOUR CODE STARTS HERE ###
def same_x_and_o(string):

  x_counter = 0

  o_counter = 0

  result = False

  for i in string:
    if i == 'x':
      x_counter += 1
    elif i == 'o':
      o_counter += 1

  if x_counter == o_counter:
    result = True

  return result



### YOUR CODE ENDS HERE ###