# ------------------------------------------------ #
'''sum_of_two_names'''

# Define a function named sum_of_two_nums, which takes in two numbers and returns the sum of those numbers.


### YOUR CODE STARTS HERE ###
def sum_of_two_nums(num1, num2):
  sum = num1 + num2
  return sum



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''greater_than_ten'''

# Define a function named greater_than_ten, which takes in an integer and returns True if the number is greater than 10 and False if the number is less than 10.


### YOUR CODE STARTS HERE ###
def greater_than_ten(number):
  is_greater = False
  
  if number > 10:
    is_greater = True
    
  return is_greater



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''odd_or_even'''

# Define a function named odd_or_even which takes in an integer and returns 'odd' if the number is odd, and 'even' if the number is even.


### YOUR CODE STARTS HERE ###
def odd_or_even(int):
  odd_or_even = ''
  if int % 2 == 0:
    odd_or_even = 'even'
  elif int % 2 != 0:
    odd_or_even = 'odd'

  return odd_or_even



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''how_many_legs'''

# Define a function named how_many_legs, which takes three parameters, num_cows, num_chickens, and num_spiders and returns the total number of legs.


### YOUR CODE STARTS HERE ###
def how_many_legs(num_cows, num_chicken, num_spiders):
  total_legs = (num_cows * 4) + (num_chicken * 2) + (num_spiders * 8)

  return total_legs



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''multiple_of_3'''

# Define a function named multiple_of_3, which takes one argument, an integer, and returns True if the integer is a multiple of 3 and False otherwise.


### YOUR CODE STARTS HERE ###
def multiple_of_3(int):
  is_multiple = False
  if int % 3 == 0:
    is_multiple = True

  return is_multiple
    



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''area_of_triangle'''

# Define a function named area_of_triangle, which takes two arguments as integers, base, and height and returns the area of a triangle of those dimensions. Note: The formula for area of a triangle is base times height divided by 2


### YOUR CODE STARTS HERE ###
def area_of_triangle(base, height):

  area = ((base * height) / 2 )

  return area



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''concatenator'''

# Define a function named concatenator, which takes in two strings and returns them concatenated together.


### YOUR CODE STARTS HERE ###
def concatenator(str1, str2):
  concated = str1 + str2

  return concated


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''less_than_ten'''

# Define a function named less_than_ten, which takes in a string and returns True if the length of the string is less than 10 and False otherwise.


### YOUR CODE STARTS HERE ###
def less_than_ten(stringy):

  is_ten = False
  string_len = len(stringy)
  
  if string_len < 10:
    
    is_ten = True

  return is_ten

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''even_or_odd'''

# Define a function named even_or_odd which takes in a string and returns 'odd' if the length of the string is odd, and 'even' if the length of the string is even.


### YOUR CODE STARTS HERE ###
def even_or_odd(stringydingy):

  string_check = ''
  string_length = len(stringydingy)

  if string_length % 2 == 0:
    string_check = 'even'

  else:
    string_check = 'odd'

  return string_check



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''space_count'''

# Define a function named space_count, which takes a string as an argument, and returns the number of spaces in the string. Note: If there are no spaces, it should return 0.


### YOUR CODE STARTS HERE ###
def space_count(str):

  counter = 0

  for spaces in range(0, len(str)):

    if str[spaces] == ' ':

      counter += 1

  return counter



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''how_many_vowels'''

# Define a function named how_many_vowels, which takes in a strings and returns the total number of vowels of the string.


### YOUR CODE STARTS HERE ###
def how_many_vowels(str):

  counter = 0

  for vowels in str.lower():

    if vowels in 'aeiou':

      counter += 1

  return counter



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''three_es'''

# Define a function named three_es, which takes in one argument, a string, and returns True if the string contains at least 3 e's and False otherwise. Don't forget to account for capitalization.


### YOUR CODE STARTS HERE ###
def three_es(str):

  counter = 0
  three_e = False

  for e in str.lower():

    if e == 'e':

      counter += 1

      if counter >= 3:

        three_e = True

  return three_e



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''
1. LOG GENERATOR
  Write a Function called log_generator that takes 5 arguments:
    a string date in the form 'mm-dd-yyyy' (exactly 10 characters)
    a string ip_addr in the form 'xxx.xxx.xxx.xxx' (minimum 7 characters, maximum 15 characters)
    a string proto (either 'TCP' or 'UDP')
    an int src_port (in the range of 0-65535)
    an int dst_port (in the range of 0-65535)
  
  Your function should test for proper date length:
    if the length of the given date is not exactly 10 charaters (dashes included), return "Error: Incorrect date format given. Date must be formatted as mm-dd-yyyy"
  
  Your function should test for proper IP address length:
    if the length of the given ip address is less than 7 or greater than 15, your function should return "Error: Impossible IP address length given"
  
  Your function should test for proper protocols:
    if a string other than "TCP"or "UDP" is given (capitalization counts), your function should return "Error: Incorrect protocol given. Must be TCP or UDP"
  
  Your function should test for proper src_port ranges:
    if an int smaller than 0 or larger than 65535 is given for either the src or dst port, your function should return "Error: Incorrect port number given for src_port: <src_port>"

  Your function should test for proper dst_port ranges:
    if an int smaller than 0 or larger than 65535 is given for either the src or dst port, your function should return "Error: Incorrect port number given for dst_port: <dst_port>"

  If everything is formatted correctly, your function should create a log entry and return it in the format:

"<date> | <ip_addr> | <proto> | <src_port> | <dst_port>"'''


### YOUR CODE STARTS HERE ###

def log_generator(date:str, ip_addr:str, proto:str, src_port:int, dst_port:int):

  date_error = date
  ip_error = ip_addr
  proto_error = proto
  src_port_error = src_port
  dst_port_error = dst_port

  
  if len(date) != 10:
    date_error = "Error: Incorrect date format given. Date must be formatted as mm-dd-yyyy"
    
    return date_error
    
  elif len(ip_addr) < 7 or len(ip_addr) > 15:
    
    ip_error = "Error: Impossible IP address length given"
    
    return ip_error
    
  elif proto != "TCP" and proto != "UDP":
    
    proto_error = "Error: Incorrect protocol given. Must be TCP or UDP"
    
    return proto_error
    
  elif src_port < 0 or src_port > 65535:
    
    src_port_error = "Error: Incorrect port number given for src_port: " + str(src_port)
    
    return src_port_error
    
  elif dst_port < 0 or dst_port > 65535:
    
    dst_port_error = "Error: Incorrect port number given for dst_port: " + str(dst_port)
    
    return dst_port_error

  return date_error + " | " + ip_error + " | " + proto_error + " | " + str(src_port_error) + " | " + str(dst_port_error)


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''
2. ASCII BATTLE OF THE B AND P CHARACTER CLANS
  The Bs and the Ps are two warring ASCII Character Clans and they cannot decide who is the better ASCII Character Clan. The B's think they are better because they have an even number of humps, while the Ps think their odd number of humps are more artistically pleasing.

  Write a function Bs_or_Ps that takes a string battle as an argument, that only contains the characters "B" and "P" (capitalization counts) in varying amounts.

  If there are more Bs than Ps, return "The B Character Clan is victorious!"
  If there are more Ps than Bs, return "The P Character Clan is victorious!"
  In the event of a tie:
    If there are an even amount of Bs and Ps, then the Bs ultimately win and return "The B Character Clan is victorious!"
    If there are an odd amount of Bs and Ps, then the Ps ultimately win and return "The P Character Clan is victorious!"
  BONUS: Only use one return statement in the entire function'''


### YOUR CODE STARTS HERE ###

def Bs_or_Ps(battle):
  B_counter = 0
  P_counter = 0
  result = ''
  for char in battle:
    if char.upper() == "B":
      B_counter += 1
    elif char.upper() == "P":
      P_counter += 1

  if B_counter > P_counter:
      result = "The B Character Clan is victorious!"

  elif P_counter > B_counter:
      result = "The P Character Clan is victorious!"

  elif P_counter == B_counter:
      if B_counter % 2 == 0:
        result = "The B Character Clan is victorious!"
      else:
        result = "The P Character Clan is victorious!"

  return result

### YOUR CODE ENDS HERE ###