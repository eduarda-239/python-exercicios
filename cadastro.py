# Sistema de cadastro para um site de leitura. As regras são as seguintes:
# * O nome de usuário deve ter pelo menos 5 caracteres.
# *A senha deve ter pelo menos 8 caracteres.
# Queremos que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. 


while True:     # Cria um laço de repetição infinito.
    nome_usuario = input("Digite seu nome de usuário: ")   # Pede para o usuário digitar um nome de usuário.
    senha = input("Digite sua senha: ")     # Pede para o usuário digitar uma senha. 
    if len(nome_usuario) < 5:     # Verifica se o nome de usuário tem menos de 5 caracteres. 
        print("O nome de usuário deve ter pelo menos 5 caracteres.")    # Mostra mensagem de erro caso o nome seja muito curto. 
        continue      # Faz o programa voltar para o começo do while.
    if len(senha) < 8:     # Verifique se a senha tem menos de 8 caracteres.
        print("A senha deve ter pelo menos 8 caracteres.")     # Mostra mensagem de erro caso a senha seja muito curta.
        continue     # Volta para o início do laço para pedir os dados novamente.
    print("Cadastro realizado com sucesso!")    # Se passou em todas as validações, mostra mensagem de sucesso.
    break      # Encerra o laço while.
