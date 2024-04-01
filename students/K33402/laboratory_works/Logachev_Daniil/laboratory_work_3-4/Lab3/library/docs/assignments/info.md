# Показать информацию о закреплении книгах

Выводит полную информацию о закреплении книг по id

***URL*** : `assignments/<int:pk>`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

**Code** : `200 OK`

**Content** :

```json
{
    "id": 1,
    "copy": {
        "id": 1,
        "book": {
            "id": 1,
            "name": "A Clockwork Orange",
            "author": "Anthony Burgess",
            "publisher": "AST Publishers",
            "publishing_year": "2020-01-01",
            "cipher": "1"
        },
        "hall": {
            "id": 1,
            "sequence_number": 1,
            "name": "British Literature",
            "capacity": 40
        }
    },
    "reader": {
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
        "library_card_number": "3"
    },
    "date_assigned": "2023-12-03",
    "date_returned": null
}
```