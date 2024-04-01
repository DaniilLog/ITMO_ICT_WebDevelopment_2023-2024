# Добавление новом читателе

Позволяет добавить нового читателя

***URL*** : `/readers/new`

***Method*** : `POST`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `201 Created`

**Content** :

```json
{
    "id": 2,
    "name": "Arina",
    "second_name": "Vladimirovna",
    "surname": "Sokolovskaya",
    "passport": "AA2222222",
    "birth_date": "2003-09-13",
    "address": "Mem avenue, 3",
    "phone_number": "79811111111",
    "education": "1",
    "if_phd": false,
    "library_card_number": "2",
    "hall": 2
}
```