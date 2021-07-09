from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route("/")
def higher_lower():
    return "<h1 'text-align: center'>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/WRddSgfUegCN0b7CWj/giphy.gif'>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess < random_number:
        return "<h1>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3ohhwGIssJMuuEUqxq/giphy.gif'>"
    elif guess > random_number:
        return "<h1>Too high, try again</h1>" \
               "<img src='https://media.giphy.com/media/26mE7vTAAfObnqvOE/giphy.gif'>"
    else:
        return "<h1>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/l4FGq1RrgxMPSqCE8/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)
