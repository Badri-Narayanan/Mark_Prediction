from flask import Flask, render_template, url_for, redirect, session, request, abort, flash
import pickle

app = Flask(__name__)

model = pickle.load(file = open("model.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html",admin_page = True, admin_name="Badri Narayanan")

@app.route("/", methods=["POST"])
def predict_marks():
    study_hrs = request.form["study_hrs"]
    print(f"Predicted Mark : {study_hrs}")
    predicted_mark = model.predict([[study_hrs]])
    return render_template("index.html", admin_page = False, predicted_mark = round(predicted_mark[0][0], 6))


if(__name__ == "__main__"):
    app.run(port = 8080, debug = True)



