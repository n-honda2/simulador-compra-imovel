<center><h1>Planning</h1></center>
<center>Documentação dos requisitos, ferramentas e decisões do projeto</center>

## Problema Fonecido

___Nota: todas as infos desse tópico foram retiradas do documento do teste técnico.___

- Implemente uma API REST.
- Endpoint `POST /simulacao` recebendo:
- valor_imovel (número),
- `percentual_entrada` (entre 5 e 20),
- `anos_contrato` (entre 1 e 5).
- Calcule e retorne no JSON:
- `valor_entrada`,
- `valor_financiado`,
- `total_a_guardar`,
- `parcela_mensal`.
- Valide os parâmetros de entrada e retorne erro se inválido.

**Entrega**

1. Todo código no mesmo repositório público no GitHub.
2. README com instrução para rodar, exemplos de uso e comandos.
3. Docker e testes são diferenciais, não obrigatórios.

## Requisitos e Decisões de Projeto

Essa seção documentas as implementações, ferramentas e justificativas para serem colocadas no projeto final para atender o problema fornecido da maneira mais completa possível ~~na deadline fornecida~~

### Obrigatórias

Implementações e decisões que eu considerei obrigatórias para entregar uma api _*_funcional_*_ e documentada 

1. **Tecnologia de backend** que atenda os requisitos do problema (contruir API REST, lidar com JSON e verificar parâmetros de entrada)
    - **Python/FastAPI:** Tenho mais familiaridade com python e, avaliando as ferramentas indicadas, essa ferramenta é muito útil já que tem validação automática via Pydantic e geração de documentação interativa (Swagger UI/ReDoc) de forma nativa

2. **Arquitetura** que seja modular e encapsule cada parte da API para facilitar implementações, depurações e testes.
    - **Framework de APIs:** Foi escolhido um framework padronizado na construção de APIs que atenda esse requisito de modularização (``app/schemas``, ``app/services``, ``app/routers``)

3. **Ambiente** configurar o ambiente local para desenvolvimento para poder compilar e validar as implementações
    - **venv:** usar o recurso de ambiente vitual do python para poder ter um feedback e alterações das depedndências cotinuo e rápido em paralelo do desenvolvimento.

4. **Documentação** criar um Readme com instruções, exemplos e comandos da api e dos testes. Deixar explicito diretirizes de contribuição (implementação de acordo com a arquitetura e adição de novos testes)

### Features "Extras"

Implementações e decisões que eu considerei não essenciais mas que têm sua relevância para um projeto robusto

1. **Testes** unitários e de integração que verifiquem diferentes situações para validar a robustez das lógicas encapsuladas e integragindo entre si, além de evitar bugs em novas implementações
    - **Ferramentas:** utilizar o ``pytest`` para testes unitários e ``httpx`` para testes de integração
    - **Arquitetura:** criar uma nova arquitetura que modularize os testes (``test/unit``, ``test/integration``)

2. **Verificar 1ualidade do código** ao utilizar ferramentas de analise estática e formatação como linter e sast
    - **Linter:** ferramenta a decidir que verifique qualidade e formatação, será configurada e adicionada ao precommit
    - **SAST** ferramenta a decidir que será executada poucas vezes para verificar falhas de segurança e melhorar a detecção e avisos de erros de input

3. **Docker** para ter escalabilidade e consistência de deploy da API

4. **CI/CD** setup de pipeline para desenvolvimento contínuo com verificação dos testes e features como atualização automática da API para MarkDown
    - **GitHub Actions** para utilizar a imgaem criada e o ambiente de git que já estou acostumado