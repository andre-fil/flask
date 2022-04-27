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

@app.delete('/deletar-animal/<string:nome_do_animal>')
def delete_animal(nome_do_animal):
    #nome_do_animal = request.args.get('nome_do_animal')
    #{"nome":"Cavalo","cuidador":"pedro"}
    for animal in zoologico["animais"]:
        if animal.get('nome') == nome_do_animal:
            zoologico['animais'].remove(animal)
            return {"message":"Animal Removido!"}
    return {"message":"Animal não encontrado!"}


@app.delete('/deletar-funcionario/<string:nome_do_func>')
def delete_funcionario(nome_do_func):
    for funcionario in zoologico['funcionarios']:
        if funcionario.get('nome') == nome_do_func:
            zoologico['funcionarios'].remove(funcionario)
            return {"message":"Funcionário Removido!"}
        return {"message":"Funcionário não encontrado!"}







if __name__ == '__main__':
    app.run(debug=True)
