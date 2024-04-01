# Изменение информации о зале

Позволяет обновить информацию о зале

***URL*** : `halls/update/<int:pk>`

***Method*** : `PUT`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 1,
    "sequence_number": 1,
    "name": "British Literature",
    "capacity": 40
}
```