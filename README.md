<h1 align="center"> 
	🚧  Projeto 🚀 Em construção...  🚧
</h1>

# API REST - MagPy

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/renatomak/teste-instruct-magpy/blob/main/LICENSE)

## Sobre o projeto

Esta é uma API REST construída na fase de Teste Técnico para a vaga de Desenvolvedor(a) Python Júnior da [Instruct](https://instruct.com.br/).

Esta aplicação se destina ao gerenciamento de projetos com foto em tecnologia. Auxiliando o usuário na pesquisa de pacotes válidos com versões válidas. Para casos em que o usuário não tenha uma versão definida, será atribuída a última versão do pacote.
A aplicação utiliza a API pública da PyPi e tem como principal objetivo viabilizar a organização de projetos tecnológicos com pacotes consistentes e válidos.

## Itens obrigatórios:

- [x] Sua API deve validar o projeto cadastrado: todos os pacotes informados devem
      estar cadastrados no [PyPI](https://pypi.org/). Portanto você deve verificar o
      nome e a versão do pacote.
- [x] Quando o pacote vem apenas com o nome, sua API deve assumir que é preciso usar
      a última versão publicada no [PyPI](https://pypi.org/).
- [x] Se um dos pacotes informados não existir, ou uma das versões especificadas for inválida, um erro deve ser retornado.
- [x] Deve ser possível visitar projetos previamente cadastrados, usando o nome na URL.
- [x] Deve ser possível deletar projetos pelo nome.

## Itens opcionais:

- [x] Escrever testes automatizados
- [x] Alterar README.md. Descreva sua aplicação, explique o que ela faz e porque é útil.
- [ ] Documentar sua API com Swagger UI ou ReDoc

## Tecnologias utilizadas

<img src="https://cdn.icon-icons.com/icons2/112/PNG/512/python_18894.png" alt="python" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_django_icon_130645.png" alt="django" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_sqlite_icon_130153.png" alt="sqlite" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_vscode_icon_130084.png" alt="vscode" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;

## Implantação em produção

<img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/heroku_plain_wordmark_logo_icon_146480.png" alt="heroku" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;

## Como executar o projeto

Acesse a aplicação em [MagPy](https://instruct-api-magpy.herokuapp.com/)

## Como testar a aplicação

1 - clone o [repositório](https://github.com/renatomak/teste-instruct-magpy) do projeto;

      - `git clone https://github.com/renatomak/teste-instruct-magpy.git`.
      - Entre na pasta do repositório que você acabou de clonar:
      - `teste-instruct-magpy`

2. Crie o ambiente virtual para o projeto;

   - `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências;

   - `python3 -m pip install -r requirements.txt`

4. Execute os testes;

   - Em um terminal, inicie o servidor
   - `python manage.py runserver`
   - E terminal diferente digite o comando:
   - `python3 -m pytest`
