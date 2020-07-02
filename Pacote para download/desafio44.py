preco = float(input('Qual o valor do item? [R$] '))
forma = int(input('''Qual a forma de pagamento? Digite: 
1 - À vista em dinheiro: 10% de desconto;
2 - À vista no cartão: 5% de desconto;
3 - Em até 2x no cartão: Preço cheio;
4 - 3x ou mais no cartão: 20% juros. '''))

if forma == 1:
    preco = preco * 0.9
elif forma == 2:
    preco = preco * 0.95
elif forma == 4:
    preco = preco * 1.2
elif forma == 3:
    preco = preco
else:
    print('Opção de pagamento inválida. Tente novamente.')
print('O valor final a ser pago é \33[4:33mR${:.2f}\33[m.'.format(preco))