# kibe_check

Este é um projeto de bot para o twitter.

Escopo:
  O bot tem a função de checar se o tweet foi copiado de uma fonte dentro do próprio site.

  Funcionalidades a serem implementadas no princípio:
  
    -O bot pode ser ativado ao ser mencionado em resposta a um tweet, a partir daí o tweet relacionado será checado.
    
    -O usuário também pode mencionar o bot + um outro tweet, o bot fará a comparação entre os dois tweets e indicará se houve cópia ou não.
    
    -O usuário também pode mencionar o bot + um outro usuário, o bot fará uma pesquisa nos tweets do usuário mencionado e indicará se houve cópia ou não.

Funcionalidades a serem implementadas futuramente:

  -Comparação de imagens.

# Prova de conceito

## Requisitos

* Python 3.6+ com [Pipenv](https://pipenv.readthedocs.io/).
* Chaves de acesso à [API do Twitter](https://developer.twitter.com/apps)

## Configurações

Copie o arquivo `.env.sample` como `.env` e inclua ali as chaves de acesso à API do Twitter.

## Uso

```python
>>> from kibe import Tweet
>>> tweet = Tweet(1194269206419775488)
>>> tweet.is_kibe
True
>>> print(tweet)
01. https://twitter.com/cuducos/status/1212728475389485056
02. https://twitter.com/cuducos/status/1212015005807370240
03. https://twitter.com/cuducos/status/1211646253790121985
04. https://twitter.com/cuducos/status/1210562865708642306
>>>
```
