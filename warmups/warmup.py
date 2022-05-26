# Define a function which takes in a string and returns the number of vowels in that string. For purposes of this exercise 'y' is NOT a vowel.

def vowel_string(input_string):
  vowels = "aeiouAEIOU"
  vowel_count = 0
  for curr_char in input_string:
    if curr_char in vowels:
      vowel_count += 1
  return vowel_count

#print(vowel_string("Spam And eggs"))  


# Given an integer, start_num, write code to print a countdown from start_num to 1. After the countdown is up, print the line "Liftoff!"

def countdown(start_num):
  #while start_num > 1:
    for index in range(start_num,0,-1):
      print(index)
      #start_num -= 1
    print("Liftoff!")

#print(countdown(10))
#countdown(10)

# Define a function which when given a string of words, returns the length of the shortest word.
def short_word(input_string):
  #word_length = 0
  split_string = input_string.split()
  #print(split_string)
  word_length = len(split_string[0])
  short_index = 0
  curr_index = 0
  #print(split_string)
  for word in split_string:
    #print(len(word))
    if len(word) < word_length:
      word_length = len(word)
      short_index = curr_index
    curr_index += 1
  #print(short_index)    
  return word_length
  # empty_list = []
  # for word in split_string:
  #   word_length = len(word)
  #   empty_list.append(word_length)
  # empty_list.sort()
  # return empty_list[0]

#print("Shortest word: " + str(short_word("The quick brown I foxes")))


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6,9. The sum of these is 23. Write a function so that it returns the sum of all the multiples of 3 or 5 BELOW the number passed in

def nat_num(big_num):
  total = 0
  for num in range(big_num-1,2,-1):
    if num % 3 == 0 or num % 5 == 0:
      total += num
  return total

print(nat_num(10))