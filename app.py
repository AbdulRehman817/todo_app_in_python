from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []
counter = 1

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    global counter
    title = request.form['title']
    if title.strip():
        tasks.append({ 'id': counter, 'title': title, 'done': False })
        counter += 1
    return redirect('/')

@app.route('/done/<int:id>')
def done(id):
    for task in tasks:
        if task['id'] == id:
            task['done'] = not task['done']
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    global tasks
    tasks = [t for t in tasks if t['id'] != id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)