from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    sayi = 10
    article = dict()
    article["a"] ="deneme"
    article["b"] ="deneme2"

    return render_template("layout.html", number = sayi, article = article)
@app.route("/about")
def about():
    return "hakkımda"
@app.route("/about/ysi")
def ysi():
    return "ysi"


if __name__ == "__main__":
    app.run(debug = True)
