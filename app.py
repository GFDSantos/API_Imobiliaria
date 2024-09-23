from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, Apartamento
from schemas import *
from flask_cors import CORS


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
apartamento_tag = Tag(name="Apartamento", description="Adição, visualização e remoção de apartamento à base")



@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/apartamento', tags=[apartamento_tag],
          responses={"200": ApartamentoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_apartamento(form: ApartamentoSchema):
    """Adiciona um novo Apartamento à base de dados

    Retorna uma representação dos apartamentos e comentários associados.
    """
    apartamento = Apartamento(
        condominio=form.condominio,
        endereco=form.endereco,
        disposicao=form.disposicao,
        valor=form.valor
        )
    
    try:
        # criando conexão com a base
        session = Session()
        # adicionando apartamento
        session.add(apartamento)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        return apresenta_apartamento(apartamento), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Apartamento de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409
    
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo apartamennto :/"
        return {"mesage": error_msg}, 400



@app.get('/apartamentos', tags=[apartamento_tag],
        responses={"200": ListagemApartamentosSchema, "404": ErrorSchema}) 
def get_apartamentos():
    """Faz a busca por todos os Apartamentos cadastrados

    Retorna uma representação da listagem de apartamentos.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    apartamentos = session.query(Apartamento).all()
    if not apartamentos:
        # se não há apartamentos cadastrados
        ok_msg = "Nenhum apartamento cadastrado na base"
        return {"message": ok_msg}, 200
    else:
        # retorna a representação do apartamento
        print(apartamentos)
        return apresenta_apartamentos(apartamentos), 200


@app.delete('/apartamento', tags=[apartamento_tag],
            responses={"200": ApartamentoDelSchema, "404": ErrorSchema})
def del_apartamento(query: ApartamentoBuscaSchema):
    """Deleta um Apartamento a partir do nome do condomínio informado

    Retorna uma mensagem de confirmação da remoção.
    """
    apartamento_condominio = query.condominio
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    apartamento = session.query(Apartamento).filter(Apartamento.condominio == apartamento_condominio).delete()
    session.commit()

    if not apartamento:
        # se o jogo não foi encontrado
        error_msg = "apto não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:
        return {"mesage": "apto removido", "id": apartamento_condominio}

def find_in_list(lst, target):
    if target in lst:
        print(True)
    else:
        print(False)



