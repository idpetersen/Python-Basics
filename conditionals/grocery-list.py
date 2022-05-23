# NOTE: The test cases for this section are cumulative.  You need to solve the challenges in order, and as you do, don't comment out the print statements from previous problems, as the test cases build upon themselves. Also note that some questions have multiple parts.

# ---------------------------------------------------------------------- #
'''Q1. Grocery List'''

# Print 5 things you need from the grocery store, each item should be output on its own line


### YOUR CODE STARTS HERE ###
print('apple')
print('orange')
print('banana')
print('strawberry')
print('blueberry')
### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q2. Grocery Receipt'''

# Your groceries ring up as 5.63, 13.40, 3.99, 4.57, and 2.47, respectively. Use the 5 items you printed in Q1 and declare variables named after each item. Assign each item with a price listed above.


### YOUR CODE STARTS HERE ###
apple = 5.63
orange = 13.40
banana = 3.99
strawberry = 4.57
blueberry = 2.47
### YOUR CODE ENDS HERE ###


# Use python as a calculator to add your variables together and print out the total cost of all the items


### YOUR CODE STARTS HERE ###
print(apple + orange + banana + strawberry + blueberry)
### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q3. Buy Lots'''

# Pick your favorite snack from the 5 things you listed in Q1 and save it as a string in a variable called favorite_snack. Use the * operator to print 123 copies of it.


### YOUR CODE STARTS HERE ###
favorite_snack = 'blueberry'
print(favorite_snack * 123)
### YOUR CODE ENDS HERE ###


# Use the corresponding variable you declared in Q2 that contains the price for your favorite snack and the * operator to calculate the final price for those 123 snacks and print the total cost.


### YOUR CODE STARTS HERE ###
final_price = blueberry * 123
print(final_price)
### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q4. Formatting'''

# Replicate the code from the first part of Q3 but modified to separate each entry with a comma and a space. (Don't worry about having a trailing comma and space at the end). You might need to use some additional parens here.


### YOUR CODE STARTS HERE ###
favorite_snack_2 = 'blueberry, '
print(favorite_snack_2 * 123)
### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q5. BONUS''' # there are no test cases for this bonus

# Can you figure out how to get the same output as Q1 above with only 1 print statement? If so, can you do it all on one line?


### YOUR CODE STARTS HERE ###
print('apple \norange \nbanana \nstrawberry \nblueberry')
### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
