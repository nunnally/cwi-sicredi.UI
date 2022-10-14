# CWI- Sicredi

Este repositório contém o desafio do Sicredi proposto pela CWI. 

## Executando

Para executar o primeiro nível, basta executar (abrir em um navegador) o arquivo index.html. Também é possível acessar através do seguinte link:   [Sicredi.UI](https://nunnally.github.io/cwi-sicredi.UI/). 
### Django level

Para acessar o conteúdo do próximo nível, basta mudar a para branch e seguir o seguinte roteiro:

```bash
# Clone o repositório e acesse a pasta no terminal

#instale as dependências 
$ npm install 

# Instale o virtual env
$ pip install virtualenv

# Crie uma virtual env 
virtualenv sicredi_cwi

#ative a virtualenv
$ source sicredi_cwi/bin/activate # (Linux ou macOS)

#Instale o django na nova virtual env 
$pip install django 

#Execute as migrações
$ python manage.py migrate

#Execute o servidor
$ python manage.py runserver
# O servidor inciará na porta:8000 - acesse http://localhost:8000 
```

