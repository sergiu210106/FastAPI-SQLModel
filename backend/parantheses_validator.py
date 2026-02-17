'''
Get a string of paranthesis and check if it is valid
'''

def validate_paranthesis(input : str):
    paranthesis_dict  = {'(' : 1, ')' : -1, '[' : 2, ']' : -2, '{' : 3, '}' : -3}

    stack = []
    for character in input:
        if character not in paranthesis_dict:
            return {"valid" : False, "message" : f"Invalid character: {character}"}
        if paranthesis_dict[character] < 0:
            if stack and paranthesis_dict[stack[-1]] + paranthesis_dict[character] == 0:
                stack.pop()
            else:
                return {"valid": False, "message": f"Invalid parenthesis at character: {character}"}

        else:
            stack.append(character)
    if stack:
        return {"valid": False, "message": "Unclosed parentheses remaining"}
    else:
        return {"valid": True, "message": "The parentheses in the file are valid!"}