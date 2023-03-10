from flask import Flask, render_template  
app = Flask(__name__)  
print(__name__)                   
    
@app.route('/')                           
def Welcome():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return "add '/play/ *a number of your choice* / *a colour of your choice*' to the URL"

@app.route("/play")
def block_render():
    return render_template('index1.html')


@app.route("/play/<number>/<color>")
def play(number, color):
    return render_template("index.html", num=int(number), change=color)
# @app.route('/dojo')
# def hello_dojo():
#     print(" Dojo")
#     return " Dojo"

# @app.route('/flask')
# def say_flask():
#     return "Hi Flask!"

# @app.route('/say/<name>')
# def say_name(name):
#     return f"Hi {name.capitalize()}!"

# @app.route( '/john')
# def say_john():
#     return "Hi John!"

# @app.route('/repeat/<int:num>/<string:word>')
# def repeat_word(num, word):
#     output = ''

#     for i in range(0,num):
#         output += f"<p>{word}</p>"

#     return output

if __name__=="__main__":    
    app.run(debug=True,port=5000)    
