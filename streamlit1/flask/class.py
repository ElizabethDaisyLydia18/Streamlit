from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (simple list of dictionaries)
students = []
next_id = 1

# READ - Display all students
@app.route('/')
def index():
    return render_template('index.html', students=students)

# CREATE - Add new student
@app.route('/add', methods=['POST'])
def add_student():
    global next_id
    name = request.form.get('name')
    age = request.form.get('age')
    
    if name and age:
        student = {
            'id': next_id,
            'name': name,
            'age': age
        }
        students.append(student)
        next_id += 1
    
    return redirect(url_for('index'))

# UPDATE - Edit student
@app.route('/update/<int:student_id>', methods=['POST'])
def update_student(student_id):
    name = request.form.get('name')
    age = request.form.get('age')
    
    for student in students:
        if student['id'] == student_id:
            student['name'] = name
            student['age'] = age
            break
    
    return redirect(url_for('index'))

# DELETE - Remove student
@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    global students
    students = [s for s in students if s['id'] != student_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)