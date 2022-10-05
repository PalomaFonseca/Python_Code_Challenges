#Desafio
#Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu carro faz 12 KM/L. Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda. Para efetuar o cálculo, deve-se fornecer o tempo gasto em horas na viagem e a velocidade média durante a mesma em km/h. Assim, você conseguirá passar para Rubens qual a distância percorrida e, em seguida, calcular quantos litros serão necessários para a viagem que ele quer fazer. Mostre o valor com 3 casas decimais após o ponto.

#Entrada
#O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

#Saída
#Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

#Exemplos de Entrada: 10 85     Exemplos de Saída: 70.833
#Exemplos de Entrada: 22 67	    Exemplos de Saída: 122.833

#Resolução Desafio

values = input().split()

time_hour = int(values[0])
average_speed_kmh = int(values[1])
space_km = (time_hour*average_speed_kmh)
liter = (space_km/12)

print(f"{liter:.3f}")