'''
12.	Faça um Script em Python que solicite ao usuário informar uma quantidade de dias, horas, minutos e segundos. Em seguida, converta tudo para segundos: 
'''
dias = int(input("Digite a quantidade de dias: "));
horas = int(input("Digite a quantidade de horas: "));
minutos = int(input("Digite a quantidade de minutos: "));
segundos = int(input("Digite a quantidade de segundos: "));
dias_seg = dias*86400;
horas_seg = horas*3600;
min_seg= minutos*60;
total_seg = dias_seg + horas_seg + min_seg +segundos;
print(f"O total de segundos do tempo digitado é de: {total_seg}");
