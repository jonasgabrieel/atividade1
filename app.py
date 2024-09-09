from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Lista de usuários para armazenar dados temporariamente
usuarios = [
    {'id': 1, 'cpf': 12345678900, 'nome': 'João da Silva', 'data_nascimento': '1990-01-01'},
    {'id': 2, 'cpf': 1233452567, 'nome': 'Maria da Silva', 'data_nascimento': '1960-03-15'},
    {'id': 3, 'cpf': 123676756300, 'nome': 'Felipe da Silva', 'data_nascimento': '1980-05-10'},
    {'id': 4, 'cpf': 98765432100, 'nome': 'Ana Souza', 'data_nascimento': '1992-07-21'},
    {'id': 5, 'cpf': 11223344556, 'nome': 'Carlos Pereira', 'data_nascimento': '1985-11-05'},
    {'id': 6, 'cpf': 55667788999, 'nome': 'Fernanda Lima', 'data_nascimento': '1978-09-13'},
    {'id': 7, 'cpf': 33445566778, 'nome': 'Lucas Oliveira', 'data_nascimento': '2001-02-28'},
    {'id': 8, 'cpf': 77889900112, 'nome': 'Mariana Costa', 'data_nascimento': '1995-12-30'},
    {'id': 9, 'cpf': 22334455667, 'nome': 'Ricardo Santos', 'data_nascimento': '1982-06-15'},
    {'id': 10, 'cpf': 1233452567, 'nome': 'Maria da Feitosa', 'data_nascimento': '1960-03-15'},
]

@app.route('/usuarios',methods=['GET'])
def obter_usuarios():
   return jsonify(usuarios)

@app.route('/usuarios/<int:id>',methods=['GET'])
def obter_usuario_id(id):
   for usuario in usuarios:
      if usuario.get('id') == id:
         return jsonify(usuario)
      
@app.route('/usuarios/<int:id>',methods=['PUT'])
def editar_usuario_por_id(id):
   usuario_alterado = request.get_json()
   for indice,usuario in enumerate(usuarios):
      if usuario.get('id') == id:
        usuarios[indice].update(usuario_alterado)
        return jsonify(usuarios[indice])
      
@app.route('/usuarios',methods=['POST'])
def criar_usuario():
   novo_usuario = request.get_json()
   usuarios.append(novo_usuario)

   return jsonify(usuarios)

@app.route('/usuarios/<int:id>',methods=['DELETE'])
def excluir_usuario(id):
   for indice,usuario in enumerate(usuarios):
      if usuario.get('id') == id:
         del usuarios[indice]

   return jsonify(usuarios)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
