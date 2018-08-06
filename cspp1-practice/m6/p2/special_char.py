"""Program for special characters"""
STR = input()
LE = len(STR)
I = 0
X = ""
while I < LE:
    if (STR[I] == '!' or STR[I] == '@' or STR[I] == '#' or STR[I] == '$' or STR[I] == '%' or STR[I] == '^' or STR[I] == '&' or STR[I] == '*'):
        X = X + " "
    else:
        X = X + STR[I]
    I = I +1
print(X)
