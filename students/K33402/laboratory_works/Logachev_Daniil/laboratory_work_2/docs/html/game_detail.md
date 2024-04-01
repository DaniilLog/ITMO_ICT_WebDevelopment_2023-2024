```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ game.name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }

        .container {
            width: 80%;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            margin: 20px auto 0;
        }

        h1 {
            color: #333;
        }

        .results {
            margin-top: 20px;
        }

        .result-item {
            margin-bottom: 10px;
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 5px;
        }

        .registration-form {
            margin-top: 20px;
        }

        .registered-users {
            margin-top: 20px;
        }

        .registered-users li {
            list-style: none;
            margin-bottom: 5px;
        }

        .registered-users h3 {
            margin-bottom: 10px;
        }

        .registration-button {
            padding: 5px 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        .registration-button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>{{ game.name }}</h1>
    
    <h2>Results</h2>
    <div class="results">
        {% for result in results %}
            <div class="result-item">
                <p>{{ result.university }} - {{ result.time_taken }}</p>
            </div>
        {% endfor %}
    </div>

    <h2>Registration</h2>
    <form action="" method="post" class="registration-form">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="registration-button">Register</button>
    </form>

    <div class="registered-users">
        <h3>Registered Users</h3>
        <ul>
            {% for user in registered_users %}
                <li>{{ user }}</li>
            {% endfor %}
        </ul>
    </div>
</div>
</body>
</html>
```