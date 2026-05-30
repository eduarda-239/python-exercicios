# Programa para interromper a busca assim que um livro específico é encontrado.

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]   # Aqui fazemos a lista com os valores.

for livro in livros:     # O código percorre cada valor automaticamente. 
    if livro == "O Hobbit":     # Se o valor da lista for igual "O Hobbit".
        print(f"Livro encontrado: {livro}")    # Mostre esse texto + a variável.
        break    # Quebre o código quando for achado.
