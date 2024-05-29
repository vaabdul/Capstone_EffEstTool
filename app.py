from flask import Flask, render_template, request, redirect, url_for,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from flask_jwt_extended import jwt_required,create_access_token,JWTManager
import secrets
from bson import ObjectId
import re
import matplotlib.pyplot as plt 
import io
import base64

secret_key=secrets.token_hex(12)

app = Flask(__name__)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = secret_key


client = MongoClient('localhost', 27017)
db = client['mydatabase']  # Replace with your MongoDB database name
users_collection = db['data']

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 
       
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$"
        if not re.match(pattern, password):
            return jsonify(" Max lenth 8, 1 upper and 1 number.!")
        else:
            print("Max lenth 8, 1 upper and 1 number.")
        # Check if the username already exists
            if users_collection.find_one({'username': username}):
                hashpwd=generate_password_hash(password)
                return jsonify('Username already exists. Choose a different one.')
            else:
                hashpwd=generate_password_hash(password)
                #hashpwd=generate_password_hash(password)
                users_collection.insert_one({'username': username, 'password':hashpwd})
                #return jsonify('Registration successful. You can now log in.', 'success')
                return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password match
        user = users_collection.find_one({'username': username})
        if not user:
            return jsonify('user not found')
        if check_password_hash(user['password'],password):
            create_token = create_access_token(identity=username)
            #return jsonify({'Login': 'successful.' ,'token':create_token})
            return redirect(url_for('estimationform'))
            
            # Add any additional logic, such as session management
        else:
            return jsonify('Invalid username or password. Please try again.')

    return render_template('login.html')



@app.route('/estimationform', methods=['GET', 'POST'])
def estimationform():
    if request.method == 'POST':
        tname = request.form.get("tname")
        complexity = request.form.get("complexity")
        size = request.form.get("size")
        Typeoftask= request.form.get("Typeoftask")
        notes = request.form.get("notes")
        users_collection.insert_one({'tname': tname,'complexity': complexity,'size': size,'Typeoftask': Typeoftask,'notes': notes})
        #return render_template('alldata.html')
        #return jsonify('success')
        return redirect('/tasks')
    return render_template('estimationform.html')

@app.route('/tasks')
def get_all_data():
    tasks = list(users_collection.find({}))
    return render_template('alldata.html', tasks=tasks)

@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    task = users_collection.find_one({'_id':ObjectId(id)})
    #print(task)
    if request.method == 'POST':
        tname = request.form.get('tname')
        complexity = request.form.get('complexity')
        size = request.form.get('size')
        Typeoftask = request.form.get('Typeoftask')
        notes = request.form.get('notes')
        
        task_data = {}
        if tname is not None:
            task_data['tname'] = tname        
        if complexity is not None:
            task_data['complexity'] = complexity
        if size is not None:
            task_data['size'] = size
        if Typeoftask is not None:
            task_data['Typeoftask'] = Typeoftask
        if notes is not None:
            task_data['notes'] = notes
        
        query = {"_id": ObjectId(id)}
        content = {"$set": task_data}
        
        result = users_collection.find_one_and_update(query, content, upsert=False)
        if result:
            return redirect('/tasks')
        else:
            return jsonify("Task not found")
    #print(task)
    return render_template('update.html', task = task )
    

@app.route('/delete/<string:id>')
def delete_task(id):
    users_collection.delete_one({'_id':ObjectId(id)})
    return redirect('/tasks')
    #return jsonify("successfully deleted")

@app.route('/logout')
def logout():
    return redirect(url_for('login')) 

@app.route('/estCalculate')
def analize_data():
    data = list(users_collection.find({}))
    sizes = [size['size'] for size in data]
    tasks = [size['complexity'] for size in data]
    print(sizes, tasks)    
    plt.figure(figsize = (10, 5))
    plt.bar(sizes ,tasks, color = 'red', width=0.4)
    plt.xlabel("Tasks")
    plt.ylabel('complexity')
    plt.title('Tasks Priority')    
    #craate plot image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    bar_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return render_template('estcalc.html', bar_url=bar_url)  


if __name__ == '__main__':
    app.run(debug=True)
