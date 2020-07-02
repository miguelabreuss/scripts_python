saque = notas50 = notas20 = notas10 = notas1 = 0
print('-'*30)
print("{:^30}".format('CAIXA ELETRÔNICO'))
print('-'*30)
saque = int(input('Qual o valor deseja sacar? '))
while True:
    if saque >= 50:
        notas50 = saque // 50
        saque = saque - (notas50 * 50)
    if saque >= 20:
        notas20 = saque // 20
        saque = saque - (notas20 * 20)
    if saque >=10:
        notas10 = saque // 10
        saque = saque - (notas10 * 10)
    if saque < 10:
        break
print(f'''{notas50} x R$50.00
{notas20} x R$20.00
{notas10} x R$10.00
{saque} x R$1.00''')