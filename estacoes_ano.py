#A partir do mês e do ano informar a estação do ano... Objetivo:
#- Praticar o uso de estruturas de decisão complexas;
#- Implementar um sistema de informação focado em Entradas, Processamento e Saída de dados;
#- Usar as ferramentas de versionamento e colaboração.
#Proposta:
#- Criar um sistema de informação que receba o dia e o mês deste ano de 2023 e seja capaz de informar a estação do ano.
#- Considere os dados do Instituto Nacional de Meteorologia anexos.
#Outono = 20 Março de 2023 a 20 Junho de 2023.
#Inverno = 21 Junho de 2023 a 22 de Setembro de 2023.
#Primavera = 23 de Setembro de 2023 a 21 de Dezembro de 2023.
#Verão = 22 de Dezembro de 2023 a 19 de Março de 2023.

print('\n\t\t\t --- Estação do ano --- \n\t\t\t')

#Entradas
dat = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

#Processamento

if mes == 1 or mes == 2 or mes == 3:
    print('Você nasceu no Verão')
elif mes == 4 or mes == 5 or mes == 6:
    print('Você nasceu no Outorno')
elif mes == 7 or mes == 8 or mes == 9:
    print('Você nasceu no inverno')
elif mes == 10 or mes == 11 or mes == 12:
    print('Você nasceu na primavera')
else:
    print('invalido')
