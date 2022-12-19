# Импортируем Flask
from flask import Flask

# Импортируем функции
import functions

# Создаем экземпляр Flask
app = Flask(__name__)


# Роут выводит следующие данные всех кандидатов по очереди: имя, позицию и навыки
@app.route("/")
def page_index():
    results = functions.load_candidates()
    line = ""
    for result in results:
        line += f"""
            {result['name']}
            {result['position']}
            {result['skills']}"""
        line = "<pre>" + "\n" + line + "\n" + "</pre>"
    return line


# Роут выводит данные кандидата, имеющего введенный номер pk: имя, позицию и навыки вместе с картинкой
@app.route("/candidates/<x>")
def page_candidates(x):
    result = functions.get_by_pk(int(x))
    return f"""<img src="({result['picture']})">
        <pre>
        {result['name']}
        {result['position']}
        {result['skills']}
    </pre>"""


# Роут выводит следующие данные кандидата, имеющего введенный навык: имя, позицию и навыки
@app.route("/skills/<x>")
def page_skills(x):
    results = functions.get_by_skill(x)
    line = ""
    for result in results:
        line += f"""
                {result['name']}
                {result['position']}
                {result['skills']}"""
        line = "<pre>" + "\n" + line + "\n" + "</pre>"
    return line


app.run()
