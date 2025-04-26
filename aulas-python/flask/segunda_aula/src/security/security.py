# pip install flask-bcrypt -> Lib de criptografia
from flask_bcrypt import bcrypt

def hash_senha(senha):
    salt = bcrypt.gensalt() # Adiciona caracteres a mais para mesclar na senha
    return bcrypt.hashpw(senha.encode('utf-8'), salt) # Encode transforma em String PRECISA ser desta forma

def checar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')) # Encode transforma em String PRECISA ser desta forma



