from flask import Flask,render_template,request
app = Flask(__name__)
facts = []
@app.route('/')
def main():
    with open('database.txt', 'r', encoding='utf-8') as f:
        facts = [line.strip() for line in f if line.strip()]
    return render_template('index.html',facts = facts)
@app.route('/post',methods = ['GET','POST'])
def posts():
    if request.method == 'POST':
        fact = request.form['fact']
        if fact:
            with open('database.txt', 'a', encoding='utf-8') as f:
                f.write(fact + '\n')
    return render_template('post.html')
app.run(debug=True)
