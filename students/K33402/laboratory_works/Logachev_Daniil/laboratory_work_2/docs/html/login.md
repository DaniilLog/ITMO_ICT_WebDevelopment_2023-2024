```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
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
        }
        .btn-secondary {
            background-color: #6c757d;
            color: #fff;
        }
        .btn-secondary:hover {
            background-color: #5a6268;
        }
        h1 {
            color: #007BFF;
            text-align: center;
        }
        form {
            max-width: 400px;
            margin: 0 auto;
        }
        .messages {
            list-style-type: none;
            padding: 0;
        }
        .messages li {
            margin-bottom: 10px;
        }
        /* Add custom style for form controls */
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .btn-block {
            width: 100%;
        }
    </style>
    <title></title>
</head>
<body>
<div class="container mt-5">
    <a href="{% url 'base' %}" class="btn btn-secondary">Назад</a>
    <form method="post" class="mb-3">
        {% csrf_token %}

        {% if messages %}
        <ul class="messages">
            {% for message in messages %}
            <li
            {% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}

        <div class="form-group">
            <label for="{{ form.username.id_for_label }}">Имя пользователя:</label>
            {{ form.username }}
        </div>
        <div class="form-group">
            <label for="{{ form.password.id_for_label }}">Пароль:</label>
            {{ form.password }}
        </div>

        <button type="submit" class="btn btn-primary btn-block">Войти</button>
    </form>
</div>
</body>
</html>
```