import sqlite3

class FilmeRepository:
    """Responsável por toda a interação direta com o SQLite."""
    def __init__(self, db_name="cinema.db"):
        self.db_name = db_name
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS filmes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    duracao INTEGER NOT NULL,
                    genero TEXT NOT NULL
                )
            """)

    def salvar(self, titulo, duracao, genero):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO filmes (titulo, duracao, genero) VALUES (?, ?, ?)",
                (titulo, duracao, genero)
            )
            return cursor.lastrowid