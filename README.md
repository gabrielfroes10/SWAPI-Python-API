# SWAPI Python API

## Descrição
Este projeto é uma API desenvolvida em **Python** utilizando o framework **Flask** que se integra com a **SWAPI (Star Wars API)**. Ele permite a interação com os dados da franquia Star Wars, incluindo personagens, filmes, naves, veículos, espécies e planetas. Além disso, há suporte para persistência de dados em um banco de dados **SQLite**.

### Funcionalidades:
- Retorna todos ou dados específicos de personagens, filmes, naves, veículos, espécies e planetas da SWAPI.
- Permite salvar e remover essas entidades do banco de dados.
- Rota para salvar e recuperar um conjunto de favoritos.
- Tratamento de erros para requisições inválidas.

## Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal do projeto.
- **Flask**: Framework web para a criação da API.
- **Flask-SQLAlchemy**: ORM (Object Relational Mapper) para a interação com o banco de dados SQLite.
- **SQLite**: Banco de dados relacional usado para armazenar dados localmente.
- **Requests**: Biblioteca para fazer requisições HTTP à API SWAPI.
