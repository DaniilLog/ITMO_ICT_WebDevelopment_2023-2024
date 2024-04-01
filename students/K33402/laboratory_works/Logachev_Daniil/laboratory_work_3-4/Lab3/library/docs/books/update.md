# Изменение информации о книге

Позволяет обновить информацию о книге

***URL*** : `books/update/<int:pk>`

***Method*** : `PUT`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 3,
    "name": "All Quiet on the Western Front",
    "author": "Erich Maria Remarque",
    "publisher": "AST Publishers",
    "publishing_year": "2022-10-17",
    "cipher": "3"
}
```