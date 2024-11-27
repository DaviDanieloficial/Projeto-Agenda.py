# Definindo a classe Contato
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = False

    def __str__(self):
        favorito = "Sim" if self.favorito else "Não"
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Favorito: {favorito}"

# Função para mostrar o menu principal
def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

# Função para adicionar um contato
def adicionar_contato(contatos):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    novo_contato = Contato(nome, telefone, email)
    contatos.append(novo_contato)
    print("Contato adicionado com sucesso!")

# Função para visualizar todos os contatos
def visualizar_contatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        for i, contato in enumerate(contatos):
            print(f"{i + 1}. {contato}")

# Função para editar um contato
def editar_contato(contatos):
    visualizar_contatos(contatos)
    indice = int(input("Digite o número do contato que deseja editar: ")) - 1
    if 0 <= indice < len(contatos):
        contatos[indice].nome = input(f"Novo nome ({contatos[indice].nome}): ") or contatos[indice].nome
        contatos[indice].telefone = input(f"Novo telefone ({contatos[indice].telefone}): ") or contatos[indice].telefone
        contatos[indice].email = input(f"Novo email ({contatos[indice].email}): ") or contatos[indice].email
        print("Contato editado com sucesso!")
    else:
        print("Contato não encontrado.")

# Função para marcar/desmarcar favorito
def marcar_favorito(contatos):
    visualizar_contatos(contatos)
    indice = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
    if 0 <= indice < len(contatos):
        contato = contatos[indice]
        contato.favorito = not contato.favorito
        print(f"Contato {contato.nome} {'marcado' if contato.favorito else 'desmarcado'} como favorito.")
    else:
        print("Contato não encontrado.")

# Função para visualizar apenas os contatos favoritos
def visualizar_favoritos(contatos):
    favoritos = [contato for contato in contatos if contato.favorito]
    if not favoritos:
        print("Nenhum contato favorito.")
    else:
        for i, contato in enumerate(favoritos):
            print(f"{i + 1}. {contato}")

# Função para apagar um contato
def apagar_contato(contatos):
    visualizar_contatos(contatos)
    indice = int(input("Digite o número do contato que deseja apagar: ")) - 1
    if 0 <= indice < len(contatos):
        contatos.pop(indice)
        print("Contato apagado com sucesso!")
    else:
        print("Contato não encontrado.")

# Função principal
def main():
    contatos = []
    while True:
        escolha = mostrar_menu()
        if escolha == '1':
            adicionar_contato(contatos)
        elif escolha == '2':
            visualizar_contatos(contatos)
        elif escolha == '3':
            editar_contato(contatos)
        elif escolha == '4':
            marcar_favorito(contatos)
        elif escolha == '5':
            visualizar_favoritos(contatos)
        elif escolha == '6':
            apagar_contato(contatos)
        elif escolha == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
