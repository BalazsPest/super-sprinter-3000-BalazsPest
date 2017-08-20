from flask import Flask, render_template, redirect, request, session
import random
import string
import csv

app = Flask(__name__)


@app.route('/')
def index():
    global id
    id = 1
    try:
        with open("data.csv", "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split(",") for element in lines]
        for data in table:
            id +=1
    except:
        return redirect('/story.html')

    return render_template('list.html', bable =table)

@app.route('/update', methods = ['GET'])
def updel():
     session['update'] =request.args.get('update')
     return redirect('/story_id.html')

@app.route('/save', methods = ['GET'])
def saving():
    story_title = request.args.get('title')
    user_story = request.args.get('story')
    acc_criteria = request.args.get('criteria')
    business_value = request.args.get('value')
    estimation = request.args.get('estim')
    status = request.args.get('statu')
    user_id = id
    story_info = [user_id,story_title, user_story, acc_criteria, business_value, estimation, status]
    
    with open("data.csv", "a") as file:
        for data in story_info:
            if data == story_info[-1]:
                file.write(str(data) + "\n")
            else:
                file.write(str(data) + ",")

    return redirect('/')

@app.route('/story.html')
def story():
    return render_template('story.html',main_title = 'Create story',butt = "Create")


@app.route('/del' , methods = ['GET'])
def delete():
    session['del'] = request.args.get('del')
    with open("data.csv", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]

    for data in table:
        if str(data[0]) == str(session['del']):
            table.remove(data)
    
    return redirect('/')



@app.route('/story_id.html')
def story_id():
    with open("data.csv", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]

    for data in table:
        if str(data[0]) == str(session['update']):
            valid_data = data
    
    return render_template('story.html',main_title = "Update story",butt = "Update",story_title = valid_data[1],user_story = valid_data[2] ,acc_criteria = valid_data[3],\
bus_value = valid_data[4], estimation = valid_data[5], status = valid_data[6])



if __name__ == "__main__":
  app.secret_key = 'subidubi' 
  app.run(
      debug=True,  
      port=5000  
  )


