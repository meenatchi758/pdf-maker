from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/preview', methods=['POST'])
def preview():
    data = request.form
    return render_template('resume.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
