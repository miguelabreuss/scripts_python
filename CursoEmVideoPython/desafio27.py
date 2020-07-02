nome = str(input('Digite seu nome completo: '))
print('O seu primeiro nome é', nome.split(" ")[0])
print('O seu último nome é', nome.rsplit(" ", 2)[2] if nome.count(" ") >= 2 else nome.split(" ")[1])
#      print('O seu último nome é', nome.rsplit(" ", 2)[2])
#  else:
#      print('O seu último nome é', nome.split(" ")[1])
