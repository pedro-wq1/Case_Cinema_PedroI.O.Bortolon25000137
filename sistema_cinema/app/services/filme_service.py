class FilmeService:
    """Onde as Regras de Negócio (RN) são validadas."""
    def __init__(self, repository):
        self.repository = repository

    def validar_e_cadastrar(self, titulo, duracao, genero):
        if duracao < 30:
            raise ValueError("Regra RN04: A duração mínima permitida é de 30 minutos.")
        
        if not titulo.strip():
            raise ValueError("O título do filme não pode estar vazio.")

        return self.repository.salvar(titulo, duracao, genero)