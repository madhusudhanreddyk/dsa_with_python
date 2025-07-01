def check_paranthesis(line):
    stack = []
    for char in line:
        if char=='(' or char=='{' or char=='[':
            stack.append(char)
        elif char==')' or char=='}' or char==']':
            if not stack:
                return False
            stack.pop()
    return not stack
print(check_paranthesis('(({{aojsjd}][]}))'))