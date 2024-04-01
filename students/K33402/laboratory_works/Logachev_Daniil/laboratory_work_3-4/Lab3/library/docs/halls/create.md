# Добавление нового зала

Позволяет добавить новый читальный зал

***URL*** : `/halls/new`

***Method*** : `POST`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `201 Created`

**Content** :

```json
{
    "id": 2,
    "sequence_number": 2,
    "name": "German Authors",
    "capacity": 30
}
```