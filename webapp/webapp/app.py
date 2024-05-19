from flask import Flask, render_template, request
from datetime import datetime
import requests  

app = Flask(__name__)

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def check_birthday(birth_date):
    today = datetime.today().date()
    return birth_date.day == today.day and birth_date.month == today.month

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        birth_date_str = request.form['birthdate']
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        age = calculate_age(birth_date)
        is_birthday = check_birthday(birth_date)

        # Make request to Pain au Chocolat microservice
        pain_au_chocolat_url = f'http://pain.default.svc.cluster.local:5000/{name}/{age}'
        response = requests.get(pain_au_chocolat_url)

        if response.status_code == 200:
            pain_au_chocolat_message = response.json().get('message')
            return render_template('result.html', name=name, age=age, is_birthday=is_birthday, pain_au_chocolat_message=pain_au_chocolat_message)
        else:
            return render_template('result.html', name=name, age=age, is_birthday=is_birthday, pain_au_chocolat_message='Error')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
