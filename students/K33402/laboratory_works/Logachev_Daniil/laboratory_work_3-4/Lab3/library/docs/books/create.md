# Добавление новой книги

Позволяет добавить новую книгу

***URL*** : `/books/new`

***Method*** : `POST`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `201 Created`

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