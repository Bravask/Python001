#listas compostas

pc = ['Procesador', 'Mouse', 'Teclado',['memoria RAM', 'HD', 'SSD'],'webcam' ]; #lista dentro da outra aqui
print("Item 1: ", pc[0]);
print("Item 4", pc[3]);
print("Item 4.1 primeiro da sublista: ", pc[3][0]); # - mostra o item dentro da sub lista
print("Ultimo item da sublista: 4.1: ", pc[3][-1]);

print(pc);
print ("-"*100);
pc[0] = "Fonte" #substitui o valor aqui
pc[3][0] = "Memoria Flash"
print(pc);


