"""Crie um programa que leia as duas notas do aluno e calcula sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0 :'REPROVADO' 
- Média entre 5.0 e 6.9 : 'RECUPERAÇÃO'
- Média 7.0 ou superior : 'APROVADO' """ 
    


print ("Média abaixo de 5.0 :'REPROVADO'" ) 
print ("Média entre 5.0 e 6.9 : 'RECUPERAÇÃO'" )
print ("Média 7.0 ou superior : 'APROVADO'" )

nota_1 = input('Digite a nota: ')
nota_2 = input('Digite a nota: ')

nota_1 = float(nota_1)
nota_2 = float(nota_2)

media = (nota_1 + nota_2) / 2

print(f'Tirando nota {nota_1:.1f} e nota {nota_2:.1f} a média do aluno será {media:.1f}')

if media >= 5 and media < 7:
    print(f'O aluno está de RECUPERAÇÃO.')
elif media < 5:
    print(f'O aluno está REPROVADO.')
else:
    print(f'O aluno está APROVADO.')    

        

