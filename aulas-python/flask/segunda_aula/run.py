# Responsavel pela execução do servidor
from src.app import create_app # Importando módulo de app.py

# Registrando módulos
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)