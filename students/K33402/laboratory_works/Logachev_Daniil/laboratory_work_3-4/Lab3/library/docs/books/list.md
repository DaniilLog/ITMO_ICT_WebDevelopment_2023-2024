# Показать информацию обо всех книгах

Выводит полную информацию обо всех книгах

***URL*** : `api/books/all`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content** :

```json
[
    {
        "id": 1,
        "name": "A Clockwork Orange",
        "author": "Anthony Burgess",
        "publisher": "AST Publishers",
        "publishing_year": "2020-01-01",
        "cipher": "1"
    },
    {
        "id": 2,
        "name": "Brave New World",
        "author": "Aldous Huxley",
        "publisher": "AST Publishers",
        "publishing_year": "2021-01-01",
        "cipher": "2"
    }
]
```