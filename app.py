from flask import Flask, render_template, redirect, url_for
from forms import RegistrationForm
from extensions import db
from models import Member

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gym.db'
db.init_app(app)

def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    plans = [
        {
            'name': 'Normal',
            'description': 'Период карты – 3 месяца; 50 посещений; доступ во все зоны с 7:00 до 23:00'
        },
        {
            'name': 'Normal+',
            'description': 'Период карты – 6 месяцев; доступ с 7:00 до 16:00; 4 гостевых визита'
        },
        {
            'name': 'VIP',
            'description': '12 месяцев; VIP-раздевалка, парковка, прачечная, 12 гостевых визитов'
        },
        {
            'name': 'VIP+',
            'description': 'Все привилегии VIP, но с бонусами: 2 фитнес-тестирования, 60 дней заморозки'
        },
        {
            'name': 'Unlim',
            'description': '12 месяцев; 15 персональных тренировок; доступ в любое время'
        }
    ]
    return render_template('services.html', plans=plans)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_member = Member(
            name=form.name.data,
            email=form.email.data,
            membership_type=form.membership_type.data
        )
        db.session.add(new_member)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
