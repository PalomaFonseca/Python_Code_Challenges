#Desafio

#Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao lorde do mal, Sauron. Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de Angmar, um dos Nazgûl (antigos reis humanos que foram corrompidos pelos poderes dos anéis de Sauron). Saruman comanda a torre de Orthanc, onde cria seus servos Uruk-hai, orcs mais terríveis que os convencionais. Para comunicação, eles utilizam as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres.
#A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a acometem diariamente. Um dos problemas que tem atrapalhado sua população é a Interferência de Comunicação Mágica (ICM). Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que para calcular o ICM para Palantír’s, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos. Gandalf, o Cinza, chegou a questionar essa conclusão, alegando que ela não fazia muito sentido, mas ele mesmo concluiu que dar sentido às coisas não faz sentido.
#Saruman e Sauron precisam de uma comunicação estável, pois têm medo que Frodo e seus amigos consigam atrapalhar seus planos, portanto, querem saber quanto de ICM há na comunicação de seus Palantír’s, para que saibam quanto de magia devem empregar na comunicação.

#Entrada
#A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.

#Saída
#Um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais.

#Exemplos de Entrada: 100 2 2	Exemplos de Saída: 25.00
#Exemplos de Entrada: 200 3 8	Exemplos de Saída: 18.18

#Resolução Desafio

values = input().split()

distance = int(values[0])
diameter1 = int(values[1])
diameter2 = int(values[2])
icm = distance/(diameter1+diameter2)

print(f"{icm:.2f}")

#Outras formas de se chegar ao mesmo resultado

distance = 200
diameter1 = 3
diameter2 = 8
icm = distance/(diameter1+diameter2)

print(f"{icm:.2f}")

#ou

distance = int(input("Qual a distância entre os Palantír? "))
diameter1 = int(input("Qual o diâmetro do Palantír de Sauron? "))
diameter2 = int(input("Qual o diâmetro do Palantír de Saruman? "))
icm = distance/(diameter1+diameter2)

print(f"{icm:.2f}")