from flask import Flask,request

app = Flask(__name__)

zoologico= {"animais":[
    {"nome":"Cavalo","cuidador":"pedro"},
    {"nome":"Macaco","cuidador":"José"}
    ],
    "funcionarios":[
        {"nome":"pedro","funcao":"cuidador"},
        {"nome":"José","funcao":"cuidador"}
    ]}

lista = ['andre', 'filipe']

@app.get('/')
def index():
    return zoologico


@app.get('/animais')
def f1():
    for animal in zoologico['animais']:
        return animal

@app.post('/cadastrar-animal')
def cadastrar():
    data = request.get_json()
    zoologico['animais'].append(data)
    return {"mensagem":"Dados Cadastrados!"}

@app.post('/cadastrar-funcionario')
def cadastrar_func():
    data = request.get_json()
    zoologico['funcionarios'].append(data)
    return {"mensagem":"Dados Cadastrados!"}





if __name__ == '__main__':
    app.run(debug=True)
