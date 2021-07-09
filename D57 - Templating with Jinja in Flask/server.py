from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year

    return render_template("index.html",
                           num=random_number,
                           year=current_year)


@app.route("/guess/<name>")
def guess(name):
    name = name.title()
    agify_url = f"https://api.agify.io?name={name}"
    genderize_url = f"https://api.genderize.io?name={name}"

    agify_response = requests.get(agify_url)
    genderize_response = requests.get(genderize_url)

    age_data = agify_response.json()
    gender_data = genderize_response.json()

    age = age_data["age"]
    gender = gender_data["gender"]

    # print(age_data, gender_data)

    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/d7bf2ebce4e9b239ad2f"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
