from app.controllers.filme_controller import FilmeController

class FilmeView:
    """Responsável apenas pela interação (Inputs/Outputs) com o usuário."""
    def __init__(self):
        self.controller = FilmeController()

    def exibir_menu_cadastro(self):
        print("\n=== CADASTRO DE NOVO FILME ===")
        titulo = input("Digite o título: ")
        try:
            duracao = int(input("Digite a duração (em minutos): "))
            genero = input("Digite o gênero: ")

            resultado = self.controller.cadastrar_filme(titulo, duracao, genero)

            if resultado["sucesso"]:
                print(f"\n[OK] {resultado['mensagem']}")
            else:
                print(f"\n[ERRO] {resultado['mensagem']}")
        except ValueError:
            print("\n[ERRO] A duração deve ser um número inteiro.")