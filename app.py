from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Função para ler dados do arquivo JSON
def ler_dados_json():
    with open('cpfs.json', 'r') as file:
        dados = json.load(file)
    return dados

# Rota para consultar CPF
@app.route('/consulta_cpf', methods=['GET'])
def consulta_cpf():
    cpf = request.args.get('cpf')
    if not cpf:
        return jsonify({'error': 'CPF é obrigatório'}), 400

    dados = ler_dados_json()
    for row in dados:
        if row['cpf'] == cpf:
            return jsonify({'cpf': row['cpf'], 'nome': row['nome'], 'idade': row['idade'], 'data_nascimento': row['data_nascimento'], 'sexo': row['sexo'], 'escolaridade': row['escolaridade'], 'nome_mae': row['nome_mae'], 'nome_pai': row['nome_pai'], 'parentes': row['parentes'], 'telefones': row['telefones']})

    return jsonify({'error': 'CPF não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
