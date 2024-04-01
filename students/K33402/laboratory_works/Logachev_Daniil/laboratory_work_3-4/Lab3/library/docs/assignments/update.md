# Изменение информации о закреплении книги

Позволяет обновить информацию о закреплении книги за читателем

***URL*** : `assignments/update/<int:pk>`

***Method*** : `PUT`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 1,
    "date_assigned": "2023-12-04",
    "date_returned": "2023-12-05",
    "copy": 1,
    "reader": 1
}
```