from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "ilovecs50"
socketio = SocketIO(app)


available_rooms = ["Comedy", "Sport", "Movies"]

rooms = {
        "Comedy": {
            "messages": [], 
            "members": 0,
            "room_users": []
        }, 
        "Sport": {
            "messages": [], 
            "members": 0,
            "room_users": []
        }, 
        "Movies": {
            "messages": [], 
            "members": 0,
            "room_users": []
        }
}

# check if a user with a particular already exist in a room
def check_user_exist(room, username):
    room_users = rooms[room]["room_users"]
    return username.title() in room_users

# ensure users do not exit 10 in a room
def check_users_limit(room):
    return len(rooms[room]["room_users"]) >= 10 


@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        room = request.form.get("room")

        if not name:
            return render_template("index.html", error="Please enter a name.", rooms=available_rooms)
        
        if not room:
            return render_template("index.html", error="Please choose a room to join", rooms=available_rooms)

        if check_user_exist(room, name):
            return render_template("index.html", error=f"{name} is already in the chat! Please use another name.", rooms=available_rooms)
        
        if check_users_limit(room):
            return render_template("index.html", error="Only 6 users can be permitted in each room, kindly join the next available room", rooms=available_rooms)

        elif room not in available_rooms:
            return render_template("index.html", error="Room does not exist", rooms=available_rooms)
   
        session["room"] = room
        session["name"] = name.title()

        return redirect(url_for("room"))
    
    return render_template("index.html", rooms=available_rooms)

@app.route("/room")
def room():
    room = session["room"]
    name = session["name"]
    
    if not room:
        return redirect(url_for("home"))
    if not name:
        return redirect(url_for("home"))
    
    if available_rooms.count(room) <= 0:
        return redirect(url_for("home")) 
    return render_template("room.html", room=room, name=name)

@socketio.on("message")
def message(data):
    room = session["room"]
    if available_rooms.count(room) <= 0:
        return
    content = {
        "name": session["name"],
        "message": data["data"],
    }

    send(content, to=room)

@socketio.on("connect")
def connect():
    room = session["room"]
    name = "T-Bots"
    user = session["name"]

    if not room:
        return 
    if not name:
        return
    if available_rooms.count(room) <= 0:
        leave_room(room)
        return
    
    join_room(room)

    content = {
        "name": name,
        "message":user + " has entered the room" ,
    }

    send(content, to=room)
    rooms[room]["members"] += 1
    rooms[room]["room_users"].append(user)


@socketio.on("disconnect")
def disconnect():
    room = session["room"]
    name = "T-Bots"
    user = session["name"]
    leave_room(room)

    if available_rooms.count(room) >= 1:
        rooms[room]["members"] -= 1
        rooms[room]["room_users"].remove(user)

    content = {
        "name": name,
        "message":user + " has left the room" ,
    }
    send(content, to=room)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8080, debug=True)