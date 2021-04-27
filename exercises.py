# Please answer the practice questions at the end of chapters 1-6 here under the cooresponding comment:

# Chapter 1
1. Which of the following are operators, and which are values?
* = OPERATOR
'hello' = STRING
-88.8 = VALUE
- = OPERATOR
/ = OPERATOR
+ = OPERATOR
5 = OPERATOR

2. Which of the following is a variable, and which is a string?
spam 
'spam' = STRING

3. Name three data types. = INTEGER, FLOAT, STRING

4. What is an expression made up of? What do all expressions do? = EXPRESSION IS MADE UP OF OPERATORS AND VALUES. EXPRESSIONS DO SIMPLE MATH AND EVALUATE TO A SINGLE  VALUE.

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement? AN ASSIGNMENT STATEMENT STORES THE INTEGER VALUE.

6. What does the variable bacon contain after the following code runs?
bacon = 20
bacon + 1  = 21

7. What should the following two expressions evaluate to?
'spam' + 'spamspam'
'spam' * 3 = SPAMSPAMSPAM 

8. Why is eggs a valid variable name while 100 is invalid? = 100 SHOULD BE DEFINED BY str(100) A VARIABLE CANT START WITH A NUMBER.

9. What three functions can be used to get the integer, floating-point number, or string version of a value? = INT(), FLOAT(), STR()

10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.' = 99 IS AN INTEGER. 99 SHOULD BE DEFINED AS str(99).

# Chapter 2
1. What are the two values of the Boolean data type? How do you write them? = TRUE AND FALSE; Written, True/False

2. What are the three Boolean operators? AND, OR, NOT

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
   TRUE and TRUE = True
   TRUE and FALSE = False
   FALSE and TRUE = False
   FALSE and FALSE = False
   TRUE or TRUE = True
   TRUE or FALSE = True
   FALSE or TRUE = True
   FALSE or FALSE = False
   not TRUE = False
   not FALSE = True

4. What do the following expressions evaluate to?
(5 > 4) and (3 == 5)
not (5 > 4) 
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
False
False
True
False
False
True

5. What are the six comparison operators? ==, !=, <, >, <=, >=

6. What is the difference between the equal to operator and the assignment operator?
The == operator asks is two values are the same as each other
The = The = operator puts the value on the right into the variable on the left.

7. Explain what a condition is and where you would use one.
A condition is used in a flow control statement and gives a True or False value.

8. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
PRINT('EGGS')
IF SPAM > 5:
PRINT(BACON)
ELSE:
PRINT('HAM')
PRINT('SPAM')

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else: 
    print('Greetings')    

10. What keys can you press if your program is stuck in an infinite loop?
Ctrl-C

11. What is the difference between break and continue?
A BREAK breaks out of a while loop early/A CONTINUE continues the while loop

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
RANGE(10) - SETS RANGE 0 UP TO 10
RANGE(0, 10) - SETS RANGE SPECIFICALLY FROM 0-10
RANGE(0, 10, 1) - INCREASES VARIABLE BY 1 ON EACH LOOP

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1 11):
print(i)

i = 1
while i <= 10
print(i)

i = i + 1

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
SPAM.BACON()

# Chapter 3
1. Why are functions advantageous to have in your programs?
FUNCTIONS LIMIT THE USE OF REPETITIVE CODE 

2. When does the code in a function execute: when the function is defined or when the function is called?
WHEN THE CODE IS CALLED 

3. What statement creates a function?
DEF 

4. What is the difference between a function and a function call?
A FUNCTION CONTAINS THE def AND A FUNCTION CALL IS WHAT EXECUTES THE FUNCTION

5. How many global scopes are there in a Python program? How many local scopes?
ONE global SCOPE AND A local SCOPE IS MADE WHEN THE FUNCTION IS CALLED.

6. What happens to variables in a local scope when the function call returns?
THE LOCAL SCOPE IS DESTROYED.

7. What is a return value? Can a return value be part of an expression?
A RETURN VALUE IS THE OUTCOME OF A FUNCTION CALL. YES, IT CAN BE PART OF AN EXPRESSION.

8. If a function does not have a return statement, what is the return value of a call to that function?
NONE

9. How can you force a variable in a function to refer to the global variable?
BY USING A GLOBAL STATEMENT

10. What is the data type of None?
NONETYPE

11. What does the import areallyourpetsnamederic statement do?
IT IMPORTS A MODULE NAMED areallyyourpetsnamederic.

12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
spam.bacon()

13. How can you prevent a program from crashing when it gets an error?
USE A TRY CLAUSE FOR THE CODE EXPECTED TO FAIL

14. What goes in the try clause? What goes in the except clause?
TRY CLAUSE: CODE THAT COULD CAUSE AN ERROR  

# Chapter 4

1. What is []? LIST

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
spam[2] = 'hello'

3. What does spam[int(int('3' * 2) // 11)] evaluate to?
'd'
4. What does spam[-1] evaluate to?
'd'

5. What does spam[:2] evaluate to?
['a','b']
For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?
'1'

7. What does bacon.append(99) make the list value in bacon look like?
[3.14, 'cat', 11, 'cat', True, 99]

8. What does bacon.remove('cat') make the list value in bacon look like?
[3.14, 11, 'cat', True]

9. What are the operators for list concatenation and list replication?
CONCATENATION = +
REPLICATION = *

10. What is the difference between the append() and insert() list methods?
APPEND() ADDS A VALUE TO THE END OF A LIST.
INSERT() ADDS WHERE YOU WANT THE VALUE IN THE LIST.

11. What are two ways to remove values from a list?
REMOVE() AND DEL

12. Name a few ways that list values are similar to string values.
THEY BOTH CAN BE USED IN FOR LOOPS.
BOTH CAN BE CONCATENATED AND REPLICATED.
BOTH CAN HAVE INDEXES.

13. What is the difference between lists and tuples?
LISTS ARE WRITTEN USING [] AND CAN BE MODIFIED.
TUPLES ARE WRITTEN USING () AND CAN NOT BE CHANGED.

14. How do you type the tuple value that has just the integer value 42 in it?
(42,)

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
THEY CONTAIN REFERENCES TO THE VALUES WITHIN THE LIST.

17. What is the difference between copy.copy() and copy.deepcopy()?
COPY.COPY() COPIES LISTS AND DICTIONARIES WHERE COPY.DEEPCOPY() COPIES LISTS AND LISTS WITHIN LISTS.

# Chapter 5

1. What does the code for an empty dictionary look like?
{}

2. What does a dictionary value with a key 'foo' and a value 42 look like?
{'foo': 42}

3. What is the main difference between a dictionary and a list?
ITEMS IN A DICTIONARY ARE UNORDERED.

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
KEYERROR IS DISPLAYED

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
NOTHING

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
YOU CHECK TO SEE IF CAT IS STORED IN THE DICTIONARY BY TYPING 'cat'.
IN spam.values(), 'cat' CHECKS THE VALUE OF CAT.

7. What is a shortcut for the following code?
if 'color' not in spam:
    spam['color'] = 'black'
spam.setdefault('color', 'black')

8. What module and function can be used to “pretty print” dictionary values?
pprint.pprint()

# Chapter 6

1. What are escape characters?
ESCAPE CHARACTERS ARE USED FOR CHARACTERS THAT WOULD BE DIFFICULT TYPE IN CODE.

2. What do the \n and \t escape characters represent?
\n NEW LINE
\t TAB

3. How can you put a \ backslash character in a string?
BY TYPING \\

4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
DOUBLE QUOTES WERE USED TO SHOW THE START AND END OF THE STRING.

5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
MAKE A MULTILINE STRING

6. What do the following expressions evaluate to?
'Hello, world!'[1] 'E'
'Hello, world!'[0:5] 'HELLO'
'Hello, world!'[:5] 'HELLO'
'Hello, world!'[3:] 'LO WORLD'

7. What do the following expressions evaluate to?
'Hello'.upper() 'HELLO'
'Hello'.upper().isupper() True
'Hello'.upper().lower() 'hello'

8. What do the following expressions evaluate to?
'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
'There-can-only-be-one'

9. What string methods can you use to right-justify, left-justify, and center a string?
rjust(), ljust(), center()

10. How can you trim whitespace characters from the beginning or end of a string?
lstrip() and rstrip()

