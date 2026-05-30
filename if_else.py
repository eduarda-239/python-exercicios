# Programa que percorra a lista de projetos e exiba os nomes dos projetos válidos. Se encontrar um item NONE, o programa deve exibir a mensagem: "Projeto ausente".

projetos = ["Java", "Python", "C++", None, "Cobol"]   # Aqui fazemos a lista. 
for projeto in projetos:      # Percorre cada item da lista automaticamente. 
  if projeto is None:         # Se o valor for None ele vai dá esse primeiro print. 
        print("Projeto ausente")
    else:
        print(projeto)        # Se não for NONE ele vai mostrar o nome do projeto da lista. 
