from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def plrimeiraAPI():
    usuarios = [
        {"nome": "mairia","idade":25,"cidade":"fortaleza"},
        {"nome": "pedro","idade":35,"cidade":"maranguape"},
        {"nome": "ana","idade":23,"cidade":"maracanaú"},
        {"nome": "paulo","idade":50,"cidade":"aquiraz"},
    ]

    return produtos

@app.get('/produtos/{id}')
def carregar_produto(id:int):

        

    produtos = [
        {"id":1,"nome":"celular","preço":1200},
        {"id":2,"nome":"ssd","preço":500},
        {"id":3,"nome":"carregador","preço":120},
        {"id":4,"nome":"monitor","preço":1100},
    ]

    for produto in produtos:
       if id == produto['id']:
           return produto
           
    return {"msg":"erro, produto não encontrado"}



@app.get('/buscarUsuario')
def buscar_Usuario(nome:str, idade:int):

    usuarios = [
        {"nome": "mairia","idade":25,"cidade":"fortaleza"},
        {"nome": "pedro","idade":35,"cidade":"maranguape"},
        {"nome": "ana","idade":23,"cidade":"maracanaú"},
        {"nome": "paulo","idade":50,"cidade":"aquiraz"},
    ]
     
    for usuario in usuarios:
        if usuario['nome'] == nome:
            if usuario['idade'] == idade:
                return usuario
    return {'msg': 'usuario não encontrado'}