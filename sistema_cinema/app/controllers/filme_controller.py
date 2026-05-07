from app.models.repository import FilmeRepository
from app.services.filme_service import FilmeService

class FilmeController:
    """Coordena o fluxo de dados entre a View e o Service."""
    def __init__(self):
        # Injeta as dependências
        self.repo = FilmeRepository()
        self.service = FilmeService(self.repo)

    def cadastrar_filme(self, titulo, duracao, genero):
        try:
            novo_id = self.service.validar_e_cadastrar(titulo, duracao, genero)
            return {"sucesso": True, "mensagem": f"Filme cadastrado com ID {novo_id}"}
        except Exception as e:
            return {"sucesso": False, "mensagem": str(e)}