from operator import itemgetter
# ------------------------------------------------ #
'''largest_num'''

# Write a function called largest_num which will take in a list of numbers and return the largest number from that list. Do not use any built-in methods to solve this problem.


### YOUR CODE STARTS HERE ###
def largest_num(list):

  list.sort()

  return list[-1]





### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''includes'''

# Write a function called includes that takes a list of numbers and a number as input. This function returns a boolean indicating whether or not the list contains the number. Do not use the list.index() method.


### YOUR CODE STARTS HERE ###
def includes(list, int):
  is_there = False
  for i in list:
    if int == i:
      is_there = True

  return is_there
      



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''average'''

# Write a function called average that takes in a list of numbers and returns a float representing the average value of the those numbers.


### YOUR CODE STARTS HERE ###
def average(list):

  total = 0
  for i in list:
    total += i

  average = total / len(list)

  return average
    
    



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''median'''

# Write another function called median that takes in a list of numbers and returns a float representing the median from that list.


### YOUR CODE STARTS HERE ###
def median(list):
  sorted_list = sorted(list)
  list_length = len(list)
  median = 0
  index = (list_length - 1) // 2

  if (list_length % 2):
    median = sorted_list[index]

  else:
    median = (sorted_list[index] + sorted_list[index + 1])/2.0

  return median



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''only_a'''

# Write a function called only_a that takes in a list of strings and returns a list of strings that contain the letter 'a'.


### YOUR CODE STARTS HERE ###
def only_a(list):
  new_list = []

  for word in list:
    for a in word:
      if a == "a":
        new_list.append(word)

  return new_list

  # new_list = []
  # for word in list:
  #   if 'a' in str:
  #     new_list.append(str)
  #   else:
  #     pass

  # return new_list
        



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''odd_couple'''

# Write a function called odd_couple that takes a list and returns a list.

# odd_couple should:

  # return a list with the first two odd numbers of the input.
  
  # return a list with only one odd number if the input is only one odd number.
  
  # returns an empty list if the input has no odd numbers


### YOUR CODE STARTS HERE ###

def odd_couple(list):

  new_list = []

  for int in list:
    if int % 2 != 0:
      new_list.append(int)
  if len(new_list) == 1:
    return new_list
  elif len(new_list) > 1:
    return new_list[0:2]
  elif len(new_list) == 0:
    return new_list

    
      


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''overachiever'''

# Write a function called overachiever which takes in a list of lists. The sublists contain both a name (string) of a student followed by a float representing his/her/their average for the class. Return the name of the student with the highest exam score.


### YOUR CODE STARTS HERE ###
def overachiever(list):
  name = ''

  sorted_list = sorted(list, key=itemgetter(1))

  name = sorted_list[-1][0]
  
  return name




### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''absolute_total'''

# Write a function called absolute_total which takes in a list of integers. return the sum of the absolute value of each element.


### YOUR CODE STARTS HERE ###

def absolute_total(list):

  abs_list = [abs(int) for int in list]
  total = 0

  for i in abs_list:
    total += i

  return total


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''sum_of_cubes'''

# Write a function called sum_of_cubes which takes in a list of integers. return the sum of the cubes of each element.


### YOUR CODE STARTS HERE ###

def sum_of_cubes(list):
  temp_power = 0
  sum = 0
  for i in list:
    temp_power = pow(i, 3)
    sum += temp_power

  return sum
  


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''multiply_by_index'''

# Write a function called multiply_by_index which takes in a list of integers. return the sum of the elements multiplied with their list indices.


### YOUR CODE STARTS HERE ###
def multiply_by_index(list):
  temp_sum = 0
  sum = 0
  for index in range(len(list)):
    temp_sum = list[index] * index
    sum += temp_sum

  return sum



### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''move_knight'''

'''Write a function move_knight which takes in a list coords_and_dirs, whose first element is a list, indicating the coordinates of the Knight's starting position, and whose second element is a four-character string, indicating where the Knight should move in one turn.

A Knight must move exactly three spaces, either two spaces in a vertical direction and one in a horizontal direction, or one space in a vertical direction and two spaces in a horizontal direction.

Assume the string at the first index of coords_and_dirs will always be formatted such that:

  The first character is either 'U' or 'D' (where 'U' is up and 'D' is down) and represents the file (vertical direction)

  The second character is either '1' or '2' and represents how many spaces in the vertical direction the Knight will travel

  The third character is either 'L' or 'R' (where 'L' is left and 'R' is right) and represents the rank (horizontal direction)
  
  The fourth character is either '1' or '2' and represents how many spaces in the horizontal direction the Knight will travel

For example: "U1L2" would read as "up one space, left two spaces".



The chess board is a grid, with each space identified as [file, rank]:

  [0, 7] --> .    .    .    .    .    .    .    . <-- [7, 7]

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    .

             .    .    .    .    .    .    .    . 

  [0, 0] --> .    .    .    .    .    .    .    . <-- [7, 0]

For example: The starting coordinates [7, 7] would represent the knight starting in the upper right corner of the chess board.



If the given directions would be an illegal move, or if the move would cause the Knight to fall off the board, return the string "Illegal Move - Horsey Down!"

Else, the function should return a string with updated file and rank, formatted as such: "The knight has moved to [file, rank]."
'''

### YOUR CODE STARTS HERE ###

def move_knight(coord_and_dirs):
  
  move = coord_and_dirs[1]
  loc = coord_and_dirs[0]
  if int(move[1]) + int(move[3]) != 3:
    return "Illegal Move - Horsey Down!"

    
  if move[0] == "U":
    if int(move[1]) + loc[1] > 7:
      return "Illegal Move - Horsey Down!"
    else:
     loc[1] = int(move[1]) + loc[1]
  elif move[0] == "D":
    if loc[1] - int(move[1]) < 0:
      return "Illegal Move - Horsey Down!"
    else: 
      loc[1] = loc[1] - int(move[1])

  if move[2] == "L":
    if loc[0] - int(move[3]) < 0:
      return "Illegal Move - Horsey Down!"
    else:
      loc[0] = loc[0] - int(move[3])
  elif move[2] == "R":
    if loc[0] + int(move[3]) > 7:
      return "Illegal Move - Horsey Down!"
    else:
      loc[0] = loc[0] + int(move[3])

  return "The knight has moved to [" + str(loc[0]) + ", " + str(loc[1]) + "]."


### YOUR CODE ENDS HERE ###