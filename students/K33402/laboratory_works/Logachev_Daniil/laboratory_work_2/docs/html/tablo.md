```html
{% load custom_filters %}
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f0f0f0;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        .btn-secondary {
            background-color: #6c757d;
            color: #fff;
        }
        .btn-secondary:hover {
            background-color: #5a6268;
        }
        .table {
            margin-top: 20px;
        }
        .table thead th {
            background-color: #f8f9fa;
            color: #333;
        }
    </style>
    <title>Таблица игр</title>
</head>
<body>
<div class="container mt-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            {% load static %}
            <a href="{% url 'profile' %}" class="btn btn-secondary">Управление профилем</a>
            {% if user.is_authenticated %}
            <a href="{% url 'logout' %}" class="btn" style="background: none; border: none;">
                <img src="{% static 'exit.png' %}" alt="Выход" width="30" height="30">
            </a>
            {% endif %}
        </div>
    </div>

    <table class="table table-striped table-bordered">
        <thead class="thead-light text-center">
        <tr>
            <th scope="col">Номер игры</th>
            <th scope="col">Название</th>
            <th scope="col">Дата</th>
            <th scope="col">Победитель</th>
            <th scope="col"></th>
        </tr>
        </thead>
        <tbody>
        {% for result in game_results %}
        <tr>
            <td>{{ result.game.id }}</td>
            <!-- Добавленная ссылка для перехода на страницу подробностей о гонке -->
            <td><a href="{% url 'game_detail' result.game.id %}">{{ result.game.name }}</a></td>
            <!-- Конец добавленной ссылки -->
            <td>{{ result.game.date }}</td>
            <td>
                {% if result.game.winner %}
                {% if result.min_time %}
                {{ result.game.winner.name }} - {{ result.min_time|format_duration }}
                {% else %}
                No result available
                {% endif %}
                {% else %}
                No winner yet
                {% endif %}
            </td>
            <td>
                <a href="{% url 'comments' result.game.id %}" class="btn btn-primary">Комментировать</a>
            </td>
        </tr>
        {% endfor %}
        </tbody>
    </table>
    <a href="{% url 'all_game_results' %}" class="btn btn-info">Все результаты игр</a>
</div>
</body>
</html>
```