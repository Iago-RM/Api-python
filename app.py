from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []
id = 1

@app.route('/users', methods=['GET'])
def getusers():
    if request.method == "GET":
        return jsonify(usuarios), 200

@app.route('/users/<user_id>', methods=['GET'])
def getuser(user_id):
    for i in range(len(usuarios)):
        if int(usuarios[i]["id"]) == int(user_id):
            user = usuarios[i]
            break
    return jsonify(user), 200



@app.route('/users', methods=["POST"])
def postUsers():
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



@app.route('/users/<user_id>', methods=["DELETE"])
def deleteUsers(user_id):
    
    for i in range(len(usuarios)):
        if int(usuarios[i]["id"]) == int(user_id):
            usuarios.pop(i)
            break
    return jsonify({"sucesso": "deletou o usuario"}), 201

@app.route('/users/<user_id>', methods=["PUT"])
def updateUsers(user_id):
    user = usuarios[0]
    for i in range(len(usuarios)):
        if int(usuarios[i]["id"]) == int(user_id):
            user = usuarios[i]
            break
    dados = request.json
    nome = dados.get('nome')
    email = dados.get('email')
    if not nome or not email:
        return jsonify({"Erro": "tem que informar tanto nome quanto email para atualizar"})
    user["nome"] = nome
    user["email"] = email
    return jsonify(user), 201
    

if __name__ == "__main__":
    app.run(debug=True, port=5001)