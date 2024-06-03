from flask import Flask, request, jsonify
import json
import os

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
            return jsonify({
                'cpf': row['cpf'],
                'nome': row['nome'],
                'nascimento': row['nascimento'],
                'sexo': row['sexo'],
                'escolaridade': row['escolaridade'],
                'mae': row['mae'],
                'pai': row['pai'],
                'parentes': row['parentes'],
                'telefones': row['telefones'],
                'situacao_cadastral': row['situacao_cadastral'],
                'cns8': row['csb8'],
                'titulo_eleitor': row['titulo_eleitor'],
                'rg': row['rg'],
                'orgao_emissor': row['orgao_emissor'],
                'uf': row['uf_emissor'],
                'csba': row['csba'],
                'enderecos': row['enderecos'],
                'empresas': row['empresas'],
                'interesses': row['interesses'],
                'nis': row['nis'],
            })

    return jsonify({'error': 'CPF não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
