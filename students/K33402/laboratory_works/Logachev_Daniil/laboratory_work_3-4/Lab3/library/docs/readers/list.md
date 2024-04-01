# Показать информацию обо всех читателях

Выводит полную информацию обо всех читателях

***URL*** : `api/readers/all`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content** :

```json
[
    {
        "id": 1,
        "hall": {
            "id": 1,
            "sequence_number": 1,
            "name": "British Literature",
            "capacity": 40
        },
        "education": "pre-elementary",
        "name": "Maria",
        "second_name": "Vladimirovna",
        "surname": "Pronina",
        "passport": "AA1111111",
        "birth_date": "2003-10-27",
        "address": "Lol Street, 15",
        "phone_number": "79810000000",
        "if_phd": false,
        "library_card_number": "1"
    }
]
```