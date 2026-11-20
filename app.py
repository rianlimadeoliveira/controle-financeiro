from flask import Flask
# Traz a ferramenta Flask para dentro do nosso arquivo.
# (Flask é o pacote que instalamos com o pip.)

app = Flask(__name__)
# Cria o aplicativo e guarda na variável "app".
# __name__ é o nome do arquivo atual; o Flask usa isso para saber onde o projeto está (e, mais tarde, encontrar as páginas HTML).

@app.route("/")
# Decorador: liga o endereço "/" (página inicial) à função logo abaixo.
# Ou seja: quando alguém acessar "/", o Flask chama a função "inicio".

def pagina_oficial():
    return "Olá! Meu controle financeiro está funcionando."
    # O que a função devolve é o que aparece na tela do navegador.

if __name__ == "__main__":
    # Só executa o que está abaixo se o arquivo for rodado diretamente (com "python app.py"), e não quando for importado por outro arquivo.
    app.run(debug=True)
    # Liga o servidor e fica esperando pedidos do navegador.
    # debug=True: mostra erros detalhados e reinicia sozinho ao salvar.
    # Usar só durante o desenvolvimento, nunca no site publicado.