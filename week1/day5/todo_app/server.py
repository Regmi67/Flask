from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = "password1234"

list_of_todos = [{
    "todo" : "Learning Flask",
    "status" : "in_progress",
    "id" : 123
},
{
    "todo" : "Learning Routes",
    "status" : "cancelled",
    "id" : 456
},
{
    "todo" : "Learning Templates",
    "status" : "complete",
    "id" : 789
},
{
    "todo" : "Learning Sessions",
    "status" : "pending",
    "id" : 987
}]

@app.route( '/todos', methods=['GET'] )
def get_todos():
    session[ 'full_name' ] = "Alex Miller"
    return render_template( "home.html", list_of_todos=list_of_todos )

@app.route( '/todo/form', methods=['GET'] )
def display_todo_form():
    if 'full_name' in session:
        current_user = session[ 'full_name' ]
        print( current_user )
        # session[ 'full_name' ] = "Alexander Miller"
        return render_template( "todo_form.html" )
    else:
        return redirect( "/todos" )

@app.route( '/todo/new', methods=['POST'] )
def create_todo():
    print( request.form )
    new_todo = {
        "todo" : request.form[ 'todo_name' ],
        "status" : request.form[ 'todo_status' ],
        "id" : request.form[ 'todo_id' ]
    }
    list_of_todos.append( new_todo )
    return redirect( '/todos' )

# At the very end don't forget to place the "run" command
if __name__ == "__main__":
    app.run( debug = True, port=5001 )


"""
Method: GET
Getting all of a particular list
Function: get_all_todos()
          get_todos()
Url: '/todos'
Method: GET
Getting one item of a particular list
Function: get_todo_by_id( id )
          get_todo( id )
Url: '/todo/<int:todo_id>'
     '/todo/<int:id>'
Method: GET
Displaying a form that will eventually refer to a list
Function: display_todo_form()
Url: '/todo/form'
Method: POST
Create a new item of a particular list
Function: create_todo()
          add_todo()
Url: '/todo/new'
     '/todo/add'
Method: POST/PUT
Update an existing item of a particular list
Function: update_todo( id )
          edit_todo( id )
Url: '/todo/update'
     '/todo/edit'
Method: POST/DELETE
Remove an existing item from a particular list
Function: delete_todo( id )
          remove_todo( id )
Url: '/todo/delete'
     '/todo/remove'
"""