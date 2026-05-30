# Crie um programa que utilize um laço for para exibir as seguintes mensagens:
# •	Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
# •	Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
# •	Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".


# Repita o código usando os valores da sequência. A variável "segundos" vai receber de 10 até 1. range(início, fim, passo) -> (10,0,-1) -> Começa no 10, vai até antes do 0, diminuindo de 1 em 1.
for segundos in range(10, 0, -1):   

# Aqui ele verifica se o número é PAR. 
    if segundos % 2 == 0:
# Quando for par ele vai mostrar esse print. 
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
# Quando for ímpar vai aparecer esse print.
    else: 
        print(f"A contagem continua: {segundos} segundos restantes.")
# Depois que o for termina essa mensagem aparece uma única vez. 
print("Aproveite a promoção agora!")

