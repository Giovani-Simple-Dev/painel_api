from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Função para ler dados do arquivo JSON
def ler_dados_json():
    with open('nomes.json', 'r') as file:
        dados = json.load(file)
    return dados

# Rota para consultar CPF
@app.route('/consulta_nome', methods=['GET'])
def consulta_nome():
    nome = request.args.get('nome')
    if not nome:
        return jsonify({'error': 'Nome é obrigatório'}), 400

    dados = ler_dados_json()
    for row in dados:
        if row['nome'] == nome:
            return jsonify({
                'cpf': row['cpf'],
                'nome': row['nome'],
                'nascimento': row['nascimento'],
                'mae': row['mae'],
            })

    return jsonify({'error': 'Nome não encontrado'}), 404

if __name__ == '__main__':
    app.run(port=5000, host='localhost',debug=True)
