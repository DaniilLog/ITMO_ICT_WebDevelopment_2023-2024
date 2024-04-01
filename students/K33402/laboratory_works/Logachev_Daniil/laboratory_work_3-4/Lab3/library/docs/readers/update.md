# Изменение информации о читателе

Позволяет обновить информацию о читателе

***URL*** : `readers/update/<int:pk>`

***Method*** : `PUT`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 1,
    "name": "Maria",
    "second_name": "Vladimirovna",
    "surname": "Pronina",
    "passport": "AA1111111",
    "birth_date": "2003-10-27",
    "address": "Lol Street, 15",
    "phone_number": "79810000000",
    "education": "0",
    "if_phd": false,
    "library_card_number": "3",
    "hall": 1
}
```