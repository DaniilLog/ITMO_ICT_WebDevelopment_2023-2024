# Показать информацию о зале

Выводит полную информацию о зале по id

***URL*** : `/halls/<int:pk>`

***Method*** : `GET`

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
    "capacity": 30
}
```