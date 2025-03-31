# Responsavel pela execução do servidor
from src.app import create_app # Importando módulo de app.py
from src.controller.colaborador_controller import bp_colaborador

# Registrando módulos
app = create_app()
app.register_blueprint(bp_colaborador) 

if __name__ == '__main__':
    app.run(debug=True)