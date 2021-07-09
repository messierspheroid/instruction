from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()

MY_EMAIL = "bjornbergchad@gmail.com"
MY_PASSWORD = "5hoKV2kwo6cw"

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="bjornbergchad@yahoo.com",
                msg=f"New 'contact me' message\n\n{data['message']}"
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
