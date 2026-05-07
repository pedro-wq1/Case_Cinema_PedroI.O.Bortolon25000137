from app.views.console_view import FilmeView

def main():
    """Inicia a aplicação."""
    sistema = FilmeView()
    
    while True:
        sistema.exibir_menu_cadastro()
        opcao = input("\nDeseja cadastrar outro filme? (s/n): ").lower()
        if opcao != 's':
            print("Encerrando sistema...")
            break

if __name__ == "__main__":
    main()