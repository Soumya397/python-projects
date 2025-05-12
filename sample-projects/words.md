# Word Value Calculator

This program calculates the numerical value of a word based on the position of each letter in the alphabet.

## Letter Values
- a = 1
- b = 2
- c = 3
...
- z = 26

## How it Works
1. The program prompts the user to enter a word
2. Each letter in the word is converted to its numerical value
3. The values are summed to produce the final result

## Algorithm
The program uses the following algorithm to calculate the word value:

1. For each character in the input word:
   - Convert the character to lowercase using `char.lower()`
   - Calculate its position value using ASCII math: `ord(char) - 96`
     - `ord()` returns the ASCII value of a character
     - We subtract 96 because 'a' has ASCII value 97, and we want 'a' = 1
   - Skip any non-alphabetic characters using `isalpha()`
   
2. Sum all the calculated values using Python's `sum()` function with a generator expression

## Understanding ASCII Values
ASCII (American Standard Code for Information Interchange) is a character encoding standard that assigns numerical values to characters:

### ASCII Character Ranges
- 0-31: Control characters (non-printable)
  - 0: Null
  - 7: Bell
  - 9: Tab
  - 10: Line Feed
  - 13: Carriage Return
  - etc.
- 32-47: Special characters and punctuation
  - 32: Space
  - 33: !
  - 34: "
  - 35: #
  - etc.
- 48-57: Numbers (0-9)
- 58-64: More special characters
  - 58: :
  - 59: ;
  - 60: <
  - 61: =
  - 62: >
  - 63: ?
  - 64: @
- 65-90: Uppercase letters (A-Z)
- 91-96: More special characters ([], ^, _, `)
- 97-122: Lowercase letters (a-z)
- 123-127: Special characters ({|}~)

This is why we subtract 96 in our algorithm:
```python
# If we want 'a' to have value 1:
# 'a' has ASCII value 97
# 97 - 96 = 1
# 'b' has ASCII value 98
# 98 - 96 = 2
# And so on...
```

### Technical Implementation
```python
def calculate_word_value(word):
    return sum(ord(char.lower()) - 96 for char in word if char.isalpha())
```

## Example
Input: "cat"
Calculation: 3 (c) + 1 (a) + 20 (t) = 24

## Usage
Run the program and enter a single word when prompted. The program will display both the final sum and the step-by-step calculation.
