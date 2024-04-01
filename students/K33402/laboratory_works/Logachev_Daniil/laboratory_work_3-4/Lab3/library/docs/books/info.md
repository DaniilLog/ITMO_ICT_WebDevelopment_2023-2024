# Показать информацию о книге

Выводит полную информацию о книге по id

***URL*** : `/books/<int:pk>`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 1,
    "name": "A Clockwork Orange",
    "author": "Anthony Burgess",
    "publisher": "AST Publishers",
    "publishing_year": "2020-01-01",
    "cipher": "1"
}
```