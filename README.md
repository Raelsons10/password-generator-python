# Password Generator

## 📌 Sobre o projeto
Gerador de senhas seguras desenvolvido em Python com foco em estudo de arquitetura, modularização, validações, testes automatizados e boas práticas de desenvolvimento.

O sistema gera senhas aleatórias fortes utilizando geração criptofraficamente segura com o módulo `secrets`.
---

## Funcionalidades

- Geração de senhas aleatórias seguras
- Validação de entrada do usuário
- Garantia de:
    - letras maiúsculas
    - letras minúsculas
    - números
    - símbolos
- Modularização do projeto
- Testes automatizados
---

## Tecnologias utilizadas
- Python
- Pytest
---

## Estrutura do projeto
```
PASSWORD_GENERATOR/
│   .gitignore
│   config.py
│   generator.py
│   main.py
│   README.md
│   requirements.txt
│   utils.py
│   validations.py
│   
├───tests
│   │   test_generator.py
│   │   test_validations.py
│   │   __init__.py
│     
```
---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/password-generator-python.git
```
Instale as dependências:

```bash
pip install -r requirements.txt
```

Acesse a pasta:

```bash
cd password-generator-python
```

Execute o projeto:

```bash
python main.py
```
---

## Executando testes

```bash
pytest tests/ -v
```
---

## Política de segurança da senha

As senhas geradas possuem obrigatoriamente
:
- 1 letra maiúscula
- 1 letra minúsucula
- 1 número
- 1 símbolo

Alíem disso, a geração utiliza o módulo `secrets`, aprimorado para aplicações relacionadas á autenticação e segurança.
---

## Exemplo de uso

```text
Informe o tamanho da senha que deseja gerar: 12

Sua senha gerada:
A@9x!K2p#Lm1
```
---

## Arquitetura

O projeto foi organizado em módulos separados para melhorar:
- manutenção
- legibilidade
- reutilização de código
- separação de responsabilidades
---

## Objetivos do projeto

Este projeto foi desenvolvido com foco em:

- prática de Python
- modularização
- arquitetura básica
- testes automatizados
- boas práticas
- versionamento com Git e GitHub
---

## Melhorias futuras

- Interface gráfica
- API REST com FastAPI
- Configuração personalizada de regras da senha
- Medidor de força da senha
- Exportação de senhas