# Показать информацию обо всех копиях

Выводит полную информацию обо всех копиях

***URL*** : `api/copys/all`

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
    {
        "id": 2,
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
    {
        "id": 3,
        "book": {
            "id": 2,
            "name": "Brave New World",
            "author": "Aldous Huxley",
            "publisher": "AST Publishers",
            "publishing_year": "2021-01-01",
            "cipher": "2"
        },
        "hall": {
            "id": 1,
            "sequence_number": 1,
            "name": "British Literature",
            "capacity": 40
        }
    },
    {
        "id": 4,
        "book": {
            "id": 2,
            "name": "Brave New World",
            "author": "Aldous Huxley",
            "publisher": "AST Publishers",
            "publishing_year": "2021-01-01",
            "cipher": "2"
        },
        "hall": {
            "id": 1,
            "sequence_number": 1,
            "name": "British Literature",
            "capacity": 40
        }
    },
    {
        "id": 5,
        "book": {
            "id": 2,
            "name": "Brave New World",
            "author": "Aldous Huxley",
            "publisher": "AST Publishers",
            "publishing_year": "2021-01-01",
            "cipher": "2"
        },
        "hall": {
            "id": 1,
            "sequence_number": 1,
            "name": "British Literature",
            "capacity": 40
        }
    }
]
```