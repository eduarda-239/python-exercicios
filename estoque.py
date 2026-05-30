# Programa de estoque que verifique a quantidade de exemplares de um livro em estoque e continuar vendendo até que o estoque se esgote. 
# Sempre que ocorrer uma venda, o sistema informa o usuário a quantidade atual disponível. Exemplo com estoque inicial de 5 exemplares.

estoque = 5   # Faz uma contagem do 5,4,3,2,1. Define a quantidade inicial do estoque. 
while estoque > 0:    # Repetir enquanto o estoque for maior que 0.
	estoque -= 1        # Diminui uma unidade do estoque a cada repetição. "estoque = estoque - 1".
    print(f"Venda realizada! Estoque restante: {estoque}")   # A cada contagem diminuída ele mostra o texto junto com estoque atual.
print("Estoque esgotado")  # Caso chegue na contagem -0 ele mostra Estoque esgotado.
