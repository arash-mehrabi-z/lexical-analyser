'''
A simple lexical analyser for python scripts.
Input: Address of a python script
Output: Prints each token with its name, type, row & column.

Attention: The number of states of finite machine of lexical analyser can
be reduced.
'''
import keyword

lst = []

class Token:
    def __init__(self, name, kind, row, col):
        self.name = name
        self.kind = kind
        self.row = row
        self.col = col

        
def print_token(name, kind):
    global state
    global token
    global row
    global col
    global lst
    
    print(f'value : "{name}", type : "{kind}", row : {row}, col : {col-(len(name))}')
    print()
    obj = Token(name, kind, row, col-(len(name)))
    lst.append(obj)
    token = ''
    state = 0
    
def move_on(s, char, j):
    global state
    global token
    global i
    global col
    
    if j > 0 :
        col += j
        
    state = s
    token += char
    i += j

    
operator = ['+', '-', '*', '/', '<', '>', '<=', '>=', '=', '!' ]
delimeter = ['(', ')', '[', ']', '{','}', ',', ':', '.', ';']
white_space = ' '
tab = '\t'
new_line = '\n'

adrs = input("Please enter the adrress of the file:\n")
with open(adrs) as f:
    string = f.read()

state = 0
i = 0
row = 1
col = 1
token = ''

while i < len(string):
    
    char = string[i]
    
    if state == 0: #STATE = 0
        if char == white_space or char == tab or char == new_line:
            if char == white_space:
                col += 1
            elif char == tab:
                col += 4
            else:
                col = 1
                row += 1
            i += 1
            continue
        elif char.isalpha(): #Letter
            move_on(1, '', 0)
            continue
        elif char.isnumeric(): #Digit
            move_on(3, '', 0)
            continue
        elif char in operator:
            move_on(8, '', 0)
            continue
        elif char in delimeter:
            move_on(25, '', 0)
            continue
        else:
            print("STATE 1 Problem")
            
    elif state==1: #STATE = 1
        if char.isalpha() or char.isnumeric() or char == '_':
            move_on(1, char, 1)
            continue
        else: #Whitespace
            move_on(2, '', 0)
            continue
    
    elif state==2: #STATE = 2
        if keyword.iskeyword(token):
            print_token(token, 'keyword')
            continue
        else:
            print_token(token, 'ID')
            continue
            
    elif state==3: #STATE = 3
        if char.isnumeric():
            move_on(3, char, 1)
            continue
        elif char == '.':
            move_on(4, char, 1)
            continue
        else:
            move_on(7, '', 0)
            continue
            
    elif state==4: #STATE = 4
        if char.isnumeric():
            move_on(5, char, 1)
            continue
    
    elif state==5: #STATE = 5
        if char.isnumeric():
            move_on(5, char, 1)
            continue
        else:
            move_on(6, '', 0)
            continue
            
    elif state==6: #STATE = 6
        print_token(token, 'Real No')
        continue
        
    elif state==7: #STATE = 7
        print_token(token, 'Integer No')
        continue
        
    elif state==8: #State = 8 ; Operators
        if char == '+':
            move_on(9, char, 1)
            continue
            
        elif char == '-':
            move_on(10, char, 1)
            continue
            
        elif char == '*':
            move_on(11, char, 1)
            continue
            
        elif char == '/':
            move_on(12, char, 1)
            continue
            
        elif char == '>':
            move_on(13, char, 1)
            continue
        
        elif char == '<':
            move_on(16, char, 1)
            continue
            
        elif char == '=':
            move_on(20, char, 1)
            continue
            
        elif char == '!':
            move_on(23, char, 1)
            continue
    
    elif state == 9: # Operator: +
        print_token(token, 'Operator')
        continue
        
    elif state == 10: #Operator: -
        print_token(token, 'Operator')
        continue
        
    elif state == 11: #Operator: *
        print_token(token, 'Operator')
        continue
    
    elif state == 12: #Operator: /
        print_token(token, 'Operator')
        continue
        
    elif state == 13: # >= or >
        if char == '=' :
            move_on(14, char, 1)
            continue
            
        else:
            move_on(15, '', 0)
            continue
    
    elif state == 14: #>=
        print_token(token, 'Operator')
        continue

    elif state == 15: #>
        print_token(token, 'Operator')
        continue
        
    elif state == 16: # <= or <
        if char == '=':
            move_on(17, char, 1)
            continue
        else:
            move_on(19, '', 0)
            continue

    elif state == 17:
        print_token(token, 'Operator')
        continue

    elif state == 19:
        print_token(token, 'Operator')
        continue
        
    elif state == 20: # = or ==
        if char == '=':
            move_on(21, char, 1)
            continue
        else:
            move_on(22, '', 0)
            continue
  
    elif state == 21: #Operator: ==
        print_token(token, 'Operator')
        continue
        
    elif state == 22: #Operator: =
        print_token(token, 'Delimeter')
        continue
        
    elif state == 23: #Operator: !=
        if char == '=':
            move_on(24, char, 1)
            continue
    
    elif state == 24: #Operator: !=
        print_token(token, 'Operator')
        continue
        
    elif state == 25: #State = 8 ; Delimeters
        if char == '(':
            move_on(26, char, 1)
            continue
            
        elif char == ')':
            move_on(27, char, 1)
            continue
            
        elif char == '[':
            move_on(28, char, 1)
            continue
            
        elif char == ']':
            move_on(29, char, 1)
            continue
            
        elif char == '{':
            move_on(30, char, 1)
            continue
        
        elif char == '}':
            move_on(31, char, 1)
            continue
            
        elif char == ',':
            move_on(32, char, 1)
            continue
            
        elif char == ':':
            move_on(33, char, 1)
            continue

        elif char == '.':
            move_on(34, char, 1)
            continue

        elif char == ';':
            move_on(35, char, 1)
            continue
            
    elif state == 26: #Delimeter
        print_token(token, 'Delimeter')
        continue
        
    elif state == 27: #Delimeter
        print_token(token, 'Delimeter')
        continue
        
    elif state == 28: #Delimeter
        print_token(token, 'Delimeter')
        continue
        
    elif state == 29: #Delimeter
        print_token(token, 'Delimeter')
        continue
        
    elif state == 30: #Delimeter
        print_token(token, 'Delimeter')
        continue
        
    elif state == 31: #Delimeter
        print_token(token, 'Delimeter')
        continue

    elif state == 32: #Delimeter
        print_token(token, 'Delimeter')
        continue
        
    elif state == 33: #Delimeter
        print_token(token, 'Delimeter')
        continue

    elif state == 34: #Delimeter
        print_token(token, 'Delimeter')
        continue
        
    elif state == 35: #Delimeter
        print_token(token, 'Delimeter')
        continue
    
print(lst[2])