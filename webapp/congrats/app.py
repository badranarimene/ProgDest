from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Happy Birthday App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 40px;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px #ccc;
            }
            form {
                max-width: 300px;
                margin: auto;
            }
            input[type="text"], input[type="date"], input[type="submit"] {
                width: 100%;
                padding: 8px;
                margin: 10px 0;
                display: inline-block;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
            }
            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <form action="/congratulate" method="get">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br>
            <label for="birthday">Birthday (YYYY-MM-DD):</label>
            <input type="date" id="birthday" name="birthday" required><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    '''

@app.route('/congratulate')
def congratulate():
    name = request.args.get('name', 'Friend')
    birthday_str = request.args.get('birthday', '')
    
    if not birthday_str:
        return "Please enter a valid birthday."

    try:
        birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
        today = datetime.now()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        return f'''
        <html>
            <head>
                <title>Congratulations</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f9;
                        margin: 40px;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px #ccc;
                        text-align: center;
                    }}
                    .message {{
                        color: navy;
                        margin: 20px;
                        padding: 20px;
                        border: 2px solid navy;
                        border-radius: 4px;
                        display: inline-block;
                    }}
                </style>
            </head>
            <body>
                <div class="message">Congratulations, {name}! You are {age} years old and still alive!</div>
		<a href="http://192.168.49.2:32500" class="choice-button">Do you want to choose between a 'croissant' and a 'pain au chocolat'?</a>
            </body>
        </html>
        '''
    except ValueError:
        return "Invalid format for birthday. Please use YYYY-MM-DD."

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
