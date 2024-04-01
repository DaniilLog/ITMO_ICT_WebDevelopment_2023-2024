# Показать информацию о копии книги

Выводит полную информацию о копии книги по id

***URL*** : `/copys/<int:pk>`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 1,
    "book": {
        "id": 1,
        "name": "A Clockwork Orange",
        "author": "Anthony Burgess",
        "publisher": "AST Publishers",
        "publishing_year": "2020-01-01",
        "cipher": "1"
    },
    "hall": {
        "id": 1,
        "sequence_number": 1,
        "name": "British Literature",
        "capacity": 40
    }
}
```