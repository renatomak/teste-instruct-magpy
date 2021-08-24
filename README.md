<h1 align="center"> 
	🚧  Projeto 🚀 Em construção...  🚧
</h1>

# API - Cadastro de desenvolvedores

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/devsuperior/sds1-wmazoni/blob/master/LICENSE)

# Sobre o projeto

Esta é uma aplicação full stack web construída para treinamento de teste técnico - uma das fases dos processos de contratação das empresas. Organizado pela [Trybe](https://www.betrybe.com/).

A aplicação consiste em criar, atualizar e excluir o cadastro de um/uma Desenvolvedor(a) Web.

## Itens obrigatórios:

- [x] Sua API deve validar o projeto cadastrado: todos os pacotes informados devem
      estar cadastrados no [PyPI](https://pypi.org/). Portanto você deve verificar o
      nome e a versão do pacote.
- [x] Quando o pacote vem apenas com o nome, sua API deve assumir que é preciso usar
      a última versão publicada no [PyPI](https://pypi.org/).

## Layout

<h1 align="center">
  <img alt="layout" title="#layout pagina Web" src="./assets/proj-api-register-dev-Layout.png" />
</h1>

## Modelo conceitual

<h1 align="center">
  <img alt="diagramaEER" title="#DiagramaEER" src="./assets/diagramaEER.png" />
</h1>

# Tecnologias utilizadas

## Back end

<img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/nodejs_plain_logo_icon_146409.png" alt="nodejs" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://img2.gratispng.com/20180604/xox/kisspng-web-development-express-js-javascript-software-fra-frame-work-5b15153ce5bb85.615845371528108348941.jpg" alt="express" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/sequelize_original_logo_icon_146348.png" alt="sequelize" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;

## Front end

<img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/html_original_wordmark_logo_icon_146478.png" alt="html" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_css_icon_130661.png" alt="css" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://cdn.icon-icons.com/icons2/2108/PNG/512/javascript_icon_130900.png" alt="javascript" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/react_original_wordmark_logo_icon_146375.png" alt="react" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;

## Implantação em produção

<img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/mysql_original_wordmark_logo_icon_146417.png" alt="mysql" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/heroku_plain_wordmark_logo_icon_146480.png" alt="heroku" width="40" height="40" style="max-width:100%;" /> &nbsp; &nbsp; &nbsp; &nbsp;

# Como executar o projeto localmente

1º - Clone o [Repositório](https://github.com/renatomak/api-register-dev) do projeto no GitHub

Pré-requisitos: npm / yarn

## Back end

2. Entre na pasta back-end
3. Instale as dependências - npm install
4. Inicie o projeto - npm start

# Teste Técnico Desenvolvedor(a) Python Júnior [REMOTO]

Neste repositório você encontra o enunciado do teste técnico para a vaga de
_Desenvolvedor(a) Python Júnior [REMOTO]_ da
[Instruct](https://instruct.com.br/)! Você provavelmente chegou aqui através da
indicação de alguma pessoa da empresa após passar pelas
[outras etapas](https://instruct.com.br/trabalhe-com-a-gente/processo-de-selecao/)
do processo seletivo. Se este não for o seu caso e mesmo assim você implementar
alguma solução para este exercício ele **não** será avaliado.

> Você _pode_ usar o problema descrito aqui para exercitar suas habilidades de
> desenvolvimento, mas a sua solução será avaliada por alguém da Instruct
> **apenas se** você estiver no processo seletivo da vaga de _Desenvolvedor(a)
> Python Júnior [REMOTO]_.

<details> 
  <summary>Quer se candidatar para uma vaga na Instruct? </summary>

Siga as instruções no site: https://instruct.com.br/trabalhe-com-a-gente/

Nessa página estão listadas as vagas abertas hoje e todos os detalhes de nosso
processo seletivo. Se não encontrou uma vaga que pareça adequada confira a
página novamente em um ou dois meses, pois ela é atualizada com frequência.

</details>

## O problema

A equipe de desenvolvimento _Bleeding Edge Enthusiasts_ (BEE) se orgulha de
usar as tecnologias mais recentes e modernas. Essa regra também se aplica aos
projetos desenvolvidos em Python pela equipe BEE.

Para garantir que todos seus projetos em Python estão usando as últimas versões
disponíves dos pacotes, a equipe pensou em criar uma ferramenta batizada de
MagPy. A ferramenta recebe um nome de projeto, uma lista de pacotes e devolve a
última versão de cada pacote.

Um dos integrantes da BEE apontou que a
[API pública do PyPI](https://warehouse.readthedocs.io/api-reference/json.html)
poderia ser usada para esse fim.

## Solução

Você deve desenvolver a MagPy, uma API REST que gerencia uma coleção de
projetos. Cada projeto tem um nome e uma lista de pacotes. Cada pacote tem um
nome e uma versão.

O cadastro de um projeto recebe o nome e a lista de pacotes. Cada pacote da
lista precisa obrigatoriamente especificar um nome, mas a versão é opcional.

Sua API deve validar o projeto cadastrado: todos os pacotes informados devem
estar cadastrados no [PyPI](https://pypi.org/). Portanto você deve verificar o
nome e a versão do pacote.

Quando o pacote vem apenas com o nome, sua API deve assumir que é preciso usar
a última versão publicada no [PyPI](https://pypi.org/).

Abaixo, alguns exemplos de chamadas que serão feitas nessa API:

```
POST /api/projects
{
    "name": "titan",
    "packages": [
        {"name": "Django"},
        {"name": "graphene", "version": "2.0"}
    ]
}
```

O código HTTP de retorno deve ser 201 e o corpo esperado na resposta é:

```
{
    "name": "titan",
    "packages": [
        {"name": "Django", "version": "3.2.5"},  // Usou a versão mais recente
        {"name": "graphene", "version": "2.0"}   // Manteve a versão especificada
    ]
}
```

Se um dos pacotes informados não existir, ou uma das versões especificadas for
inválida, um erro deve ser retornado.

Para uma chamada semelhante ao exemplo abaixo:

```
POST /api/projects
{
    "name": "titan",
    "packages": [
        {"name": "pypypypypypypypypypypy"},
        {"name": "graphene", "version": "1900"}
    ]
}
```

O código HTTP de retorno deve ser 400 e o corpo esperado na resposta é:

```
{
    "error": "One or more packages doesn't exist"
}
```

Também deve ser possível visitar projetos previamente cadastrados, usando o
nome na URL:

```
GET /api/projects/titan
{
    "name": "titan",
    "packages": [
        {"name": "Django", "version": "3.2.5"},
        {"name": "graphene", "version": "2.0"}
    ]
}
```

E deletar projetos pelo nome:

```
DELETE /api/projects/titan
```

| ⚠️  | Sua solução deve usar a [API pública do PyPI](https://warehouse.readthedocs.io/api-reference/json.html). Não use outro caminho pra buscar as informações necessárias |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## Esqueleto

Este repositório vem com um esqueleto para iniciar o projeto. Ele já tem
algumas partes implementadas e está pronto para o deploy na [Heroku](https://www.heroku.com/).

Conforme detalhado na próxima seção deste README, nós iremos avaliar a sua API
publicada nessa plataforma, então é recomendado que você use este esqueleto
como base para a sua solução.

Usando esta base, você precisará:

1. Fazer uma cópia deste repositório
2. Implementar sua solução
3. Criar uma conta gratuita no Heroku
4. Criar um novo app
5. Seguir as instruções da seção _Deploy using Heroku Git_
6. Adicionar o usuário `jobs@instruct.com.br` como colaborador do app

Fique à vontade para fazer as alterações que julgar necessárias no código
disponibilizado.

## Avaliação

Num primeiro momento não olharemos o seu código. O projeto será testado de
forma automatizada pra checar se implementa a API especificada acima.

Você deve codificar seu projeto em Python e fazer deploy usando os recursos
disponibilizados nos _Frees Tiers_ da [Heroku](https://www.heroku.com/).

Quando finalizar a implementação, adicione o usuário com e-mail
`jobs@instruct.com.br` como colaborador do app publicado até o fim do prazo
estipulado. Isso nos garante acesso ao endereço em que sua API está publicada,
para seguir com os testes automatizados.

| ⚠️  | Você deve adicionar o usuário com e-mail `jobs@instruct.com.br` no app publicado no Heroku! Não é necessário adicionar acesso ao código fonte num repositório do GitHub. |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Nós executaremos dois conjuntos de testes na sua API:

1. Testes básicos (abertos)
2. Testes avançados (fechados)

Se a API não passar nos testes básicos, faremos mais duas tentativas. Se
mesmo assim ela não passar nos testes básicos nós encerramos os testes.

Se a API passar nos testes básicos e não passar nos testes avançados, faremos
mais duas tentativas. Se mesmo assim ela não passar nos testes avançados nós
encerramos os testes.

Se a API passar pelos testes avançados nós conferimos superficialmente o seu
código para identificar problemas; no entanto você provavelmente já garantiu a
sua participação na próxima etapa.

Os testes básicos estão disponíveis neste repositório no arquivo
`tests-open.js`. Use-os durante o desenvolvimento para avaliar se a sua API
está correta. Como explicado acima, você **não passará** para a próxima etapa
se a sua solução não atender todos os testes desse arquivo.
**Use os testes para guiar o desenvolvimento da solução.**

Você pode executar esses testes com o [k6](https://k6.io/). Para instalar o k6
basta [baixar o binário](https://github.com/loadimpact/k6/releases) para o seu
sistema operacional (Windows, Linux ou Mac).

Para rodar os testes abertos, especifique a variável de ambiente "API_BASE"
com o endereço base da API testada.

Exemplo de aplicação rodando no localhost na porta 8080:

```
k6 run -e API_BASE='http://localhost:8080/' tests-open.js
```

## Recomendações finais

- Não deixe para fazer na última hora
- Atente-se para boas práticas da linguagem, siga a PEP 8
- Considere escrever testes automatizados
- Escreva documentação
  - Mude este README. Descreva sua aplicação, explique o que ela faz e porque é útil.
  - Explique como testar a aplicação
  - Considere documentar sua API com Swagger UI ou ReDoc
- [Não teste apenas o _Happy Path_](https://cucumber.io/blog/test-automation/happy-unhappy-paths-why-you-need-to-test-both/)

---

**Boa sorte!**
