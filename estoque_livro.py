# Sistema de filtragem de livros. Deve percorrer uma lista de livros e exibir o nome de cada livro disponível em estoque. No entanto, se o livro estiver esgotado, ele deve ser ignorado durante a iteração.

# Aqui definimos a lista com os valores dos livros. 
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:     # O código vai passando valor por valor da lista automaticamente.
    if livro["estoque"] == 0:    # Verifica se o estoque do livro é igual a 0.
        continue                 # Pule para o próximo livro da lista. 
    print(f"Livro disponível: {livro['nome']}")       # Exibe apenas os livros disponíveis em estoque.
