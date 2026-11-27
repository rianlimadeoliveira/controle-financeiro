import os
# Permite ler variáveis do computador.

from dotenv import load_dotenv
# Função que lê o arquivo .env.

import mysql.connector
# Conector que conversa com o MySQL.

from flask import Flask, jsonify
# Flask é o servidor do site; jsonify transforma dados Python em JSON,
# um formato de texto que o navegador (e o JavaScript) entendem bem.

load_dotenv()
# Lê o .env uma vez, quando o programa começa.

app = Flask(__name__)
# Cria o aplicativo.

app.json.ensure_ascii = False
# Faz o JSON mostrar acentos normalmente (alimentação), sem códigos estranhos.

def conectar():
    # Função que abre uma conexão com o MySQL. Vamos chamá-la sempre que precisarmos do banco.
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        # Endereço do servidor, lido do .env.
        user=os.getenv("DB_USER"),
        # Usuário do banco, lido do .env.
        password=os.getenv("DB_PASSWORD"),
        # Senha, lida do .env (nunca escrita aqui).
        database=os.getenv("DB_NAME"),
        # Nome do banco, lido do .env.
    )
    # Devolve a conexão pronta para quem chamou a função.


@app.route("/")
def inicio():
    # Página inicial (a mesma de antes).
    return "Olá! Meu controle financeiro está funcionando."
    # Texto que aparece no navegador.


@app.route("/transacoes")
def listar_transacoes():
    # Nova rota: quando alguém acessar /transacoes, esta função responde.
    conexao = conectar()
    # Abre a conexão com o banco.
    cursor = conexao.cursor(dictionary=True)
    # dictionary=True faz cada linha vir como um "dicionário" (com nomes de coluna),
    # em vez de uma lista solta de valores.
    cursor.execute("SELECT * FROM transacoes ORDER BY data DESC")
    # Pede todas as transações, da mais recente para a mais antiga.
    linhas = cursor.fetchall()
    # Pega todas as linhas que o MySQL devolveu.
    cursor.close()
    conexao.close()
    # Fecha tudo: sempre fechar quando terminar.
    return jsonify(linhas)
    # Devolve as linhas em formato JSON para o navegador.

if __name__ == "__main__":
    # Só executa se o arquivo for rodado diretamente.
    app.run(debug=True)
    # Liga o servidor (modo de desenvolvimento).