from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def choose_pastry():
    if request.method == 'POST':
        choice = request.form['pastry']
        return render_template_string(PASTRY_HTML, result=f"WOW! You chose {choice}!", choice=choice)
    return render_template_string(PASTRY_HTML, result="Choose your pastry!", choice=None)

PASTRY_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pastry Picker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            text-align: center;
            padding-top: 50px;
        }
        form {
            margin: auto;
            width: fit-content;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            background: white;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            color: white;
            background-color: #4CAF50;
            border: none;
            border-radius: 5px;
            margin: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            font-size: 20px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="result">{{ result }}</div>
    <form action="/" method="post">
        <button type="submit" name="pastry" value="Croissant">Croissant</button>
        <button type="submit" name="pastry" value="Pain au Chocolat">Pain au Chocolat</button>
    </form>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
