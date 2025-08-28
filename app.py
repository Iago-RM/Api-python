from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []
id = 1

@app.route('/users', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users():
    if request.method == "GET":
        return jsonify(usuarios), 200
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
    elif request.method == "POST":
        global id
        dados = request.json
        nome = dados.get('nome')
        email = dados.get('email')

        if not nome or not email:
            return jsonify({"erro": "Nome ou email faltando"}), 400
        novo_usuario = {
            'id': id,
            'nome': nome,
            'email': email
        }
        usuarios.append(novo_usuario)
        id += 1
        return jsonify(novo_usuario), 201


if __name__ == "__main__":
    app.run(debug=True, port=5001)