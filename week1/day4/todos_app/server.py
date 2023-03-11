from flask import Flask, render_template

app = Flask( __name__ )

list_of_todos = [{
    "todo" : "Learning Flask",
    "status" : "in_progress"
},
{
    "todo" : "Learning Routes",
    "status" : "cancelled"
},
{
    "todo" : "Learning Templates",
    "status" : "complete"
},
{
    "todo" : "Learning Sessions",
    "status" : "pending"
}]

@app.route( "/" )
def hello_class():
    print( "Thank you for the request, the server is listening!" )
    return "Hey there class of March 2023"

@app.route( "/hello" )
def hello_there():
    return "Hey there class of March 2023, this is the second route of the server!"

@app.route( "/hello/<string:firstName>/<string:lastName>")
def greeting( firstName, lastName ):
    print( f"Hey there from the server {firstName} {lastName}" )
    return ( f"Welcome to our server {firstName} {lastName}" )

@app.route( "/home" )
def home():
    fName = "Alex"
    lName = "Miller"
    return render_template( "index.html", fullName=f"{fName} {lName}", list_of_todos=list_of_todos )

# At the very end don't forget to place the "run" command
if __name__ == "__main__":
    app.run( debug = True, port=5001 )