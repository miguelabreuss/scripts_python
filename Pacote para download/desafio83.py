exp = str(input('Digite a equação matemátia a ser analisada: '))
count_o = 0
for char in exp:
    if exp[0] == ')' or exp[-1] == '(' or count_o < 0:
        count_o = 1
        break
    else:
        if char == '(':
            count_o += 1
        elif char == ')':
            count_o -= 1
if count_o == 0:
    print('A expressão é \33[4:32mVÁLIDA\33[m.')
else:
    print('A expressão é \33[4:31mINVÁLIDA\33[m.')