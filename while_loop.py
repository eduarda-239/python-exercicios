# Um loop infinito ocorre quando a condição de parada nunca é alcançada. 
# Necessário garantir o valor do contador seja atualizado dentro do loop, permitindo que a condição seja eventualmente falsa.

contador = 0 

while contador<10:
  print("Processando dados...")
  contador +=1    #Atualiza o contador para evitar o loop infinito 

# Se colocar o contador +=1 pulando linha ele fica loop infinito.
