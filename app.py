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
            return jsonify({'cpf': row['cpf'], 'nome': row['nome'], 'data_nascimento': row['data_nascimento'], 'sexo': row['sexo'], 'escolaridade': row['escolaridade'], 'mae': row['mae'], 'pai': row['pai'], 'parentes': row['parentes'], 'telefones': row['telefones'], 'situacao_cadastral': row['situacao_cadastral'], 'cns': row['cns'], 'obito': row['obito'], 'data_obito': row['data_obito'], 'titulo_eleitor': row['titulo_eleitor'], 'numero_rg': row['numero_rg'], 'orgao_emissor': row['orgao_emissor'], 'uf': row['uf'], 'pis': row['pis'], 'renda': row['renda'], 'poder_aquisitivo': row['poder_aquisitivo'], 'faixa_aquisitiva': row['faixa_aquisitiva'], 'scorecsba': row['scorecsba'], 'scorecsb': row['scorecsb'], 'telefones': row['telefones'], 'emails': row['emails'], 'cep': row['cep'], 'estado': row['estado'], 'municipio': row['municipio'], 'bairro': row['bairro'], 'logradouro': row['logradouro'], 'tipo': row['tipo'], 'numero': row['numero']})

    return jsonify({'error': 'CPF não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
