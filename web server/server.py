from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def get_page(page_name=None):
    # app.run(threaded=True)
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def lsubmit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        # print(data)
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went Wrong, try after sometime.'


def write_to_file(data):
    with open('database.txt',  mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv',  mode='a',newline='') as csvdatabase:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(csvdatabase, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])