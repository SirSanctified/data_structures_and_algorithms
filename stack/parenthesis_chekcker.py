"""Check whether the parenthesis in a given string are balanced or not.
Possible parenthesis are '()' or '[]' or '{}'. 

For example, '{[(())]}' is a balanced parathesis string, but '{[(])}' is not.
"""

from stack_using_collections_deque import Stack

def parenthesis_checker(string:str) -> bool:
    stack = Stack()
    index = 0
    is_balanced = True # Initially assume that the parenthesis are balanced

    while is_balanced and index < len(string):  # as long as the paranthesis are balanced and the string is not exhausted

        if string[index] in '([{':  # if you encounter an opening parenthesis
            stack.push(string[index])   # push it to the top of the stack
        
        if string[index] == ')':    # if you encounter a closing parenthesis
            if stack.pop() != '(':  # pop the top of the stack and compare it to the current closing parenthesis
            # and if they do not close each other, the parenthesis are not balanced
                is_balanced = False
        
        elif string[index] == ']':    # if you encounter a closing parenthesis
            if stack.pop() != '[':  # pop the top of the stack and compare it to the current closing parenthesis
            # and if they do not close each other, the parenthesis are not balanced
                is_balanced = False
        
        elif string[index] == '}':    # if you encounter a closing parenthesis
            if stack.pop() != '{':  # pop the top of the stack and compare it to the current closing parenthesis
            # and if they do not close each other, the parenthesis are not balanced
                is_balanced = False
        
        index += 1
    
    return True if is_balanced and stack.is_empty() else False
