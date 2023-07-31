from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    if 'html' in page_name:
        return render_template(page_name)
    return page_name


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank_you.html')
    else:
        return 'oops, something went wrong!'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        file = database.write(f'\n{email},{name},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, name, message])


if __name__ == "__main__":
    app.run(debug=True)
