# Добавление нового закрепления книги

Позволяет добавить новое закрепление книги за читателем

***URL*** : `/assignments/new`

***Method*** : `POST`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `201 Created`

**Content** :

```json
{
    "id": 2,
    "date_assigned": "2023-12-01",
    "date_returned": "2023-12-05",
    "copy": 4,
    "reader": 1
}
```