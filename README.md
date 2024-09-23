# Minha API
Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Básico.** 

O objetivo aqui é ilustrar o conteúdo apresentado ao longo das três aulas da disciplina.
---
Desenvolvi o meu MVP para um Cliente meu que possui o domínio www.curyvendas.com.br, ainda a ser utilizado com Landing Pages que desenvolverei e colocarei no ar depois da aprovação do cliente. 

Tal MVP visa apenas os Empreendimentos que a Construtora Cury, Projeta, Incorpora e Constrói. Essa Imobiliária venderá de forma exclusiva os Empreendimentos da Construtora Cury. 

No mercado de imóveis chamamos Imobiliária de Construtora de "House." Isso significa que a Construtora possui um CNPJ para comercialização dos imóveis que constroi e o registro no CRECI - Conselho Regional de Corretores de Imóveis.

A solicitação original do meu cliente foi para que fizesse para os Apartamentos que a Construtora Cury constroi. 

Como funciona o mercado das Construtoras.

Todas as construtoras lançam um empreendimento mediante a apvrovação da Prefeitura do Município onde será construído. Uma vez obtido essa aprovação as contrutoras, na sua maioria, providenciam um estande para receberem as visitas dos clientes potenciais. Os estandes são dos mais diversos tipos, podendo ter Apartamento(s) Tipo(s) Decorado(s), maquete(s), fotos do empreendimento, salão de atendimento de clientes, salas de imersão com vídeos para atrair a atenção dos clientes potenciais e outras coisas mais que a(s) contrutora(s) julgar necessário.

---
## Como executar 
Será necessário ter todas as libs, bibliotecas, python listadas no arquivo `requirements.txt` estejam instaladas instaladas.

Certifique-se de que o conteúdo do arquivo `requirements.txt`seja igual ao descrito abaixo.

Flask
Flask-Cors
flask-openapi3
Flask-SQLAlchemy
nose2
pydantic
SQLAlchemy
SQLAlchemy-Utils
typing_extensions

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Comandos para rodar a API do Backend

Passos para instalar chamar e ativar o ambiente virtual nas máquinas baseadas em sistemas operacionais Windows, eu utilizo o Windows 11.

python -m venv my env 
pip install virtualenv
.\env\scripts\activate

Certifique-se de que o ambiente virtual está instalado e ativo, conforme texto indicativo abaixo.

PS C:\Users\gfern\MVP_GFDSantos\api> .\env\scripts\activate
(env) PS C:\Users\gfern\MVP_GFDSantos\api>

Digitar os comandos abaixo

pip install flask reload
pip install pydantic
pip install -r requirements.txt

Ao digitar o comando abaixo a Api será inicializada.

flask run --host 0.0.0.0 --port 5000

Nota; Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

Mensagens que aparecerão depois do comando `flask run --host 0.0.0.0 --port 5000`

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.103:5000
Para sair da aplicação `Press CTRL+C to quit`

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


Abaixo alguns exemplos de Condomínios a serem cadastrados.

Condominio Heitor dos Prazeres, Rua General Luís Mendes de Morais, S/N, Dois quartos, 420000
Condominio Vargas 1140, Av. Pres. Vargas 1140, Estúdio, 410000 
Condominio Epicentro, Av. Professor Pereira Reis, 42, Dois quartos c/suíte, 520000 
Residencial Quinta do Bispo, Rua do Bispo, 83, Dois quartos c/suíte, 490000
Cury Trendy Cachambi, Rua do Cachambi 703, Dois quartos, 320000

Os preços acima são meramente ilustrativos não tendo nenhuma validade comercial.

