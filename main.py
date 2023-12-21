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

        elif room not in available_rooms:
            return render_template("index.html", error="Room does not exist", rooms=available_rooms)
   
        session["room"] = room
        session["name"] = name

        return redirect(url_for("room"))
    
    return render_template("index.html", rooms=available_rooms)

@app.route("/room")
def room():
    room = session.get("room")
    name = session.get("name")
    if not room or not name or room not in rooms:
        return redirect(url_for("home"))
    return render_template("room.html", room=room)

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return
    content = {
        "name": session.get("name"),
        "message": data["data"],
    }

    send(content, to=room)

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = "T-Bots"
    user = session.get("name")

    if not room or not name:
        return
    if room not in rooms:
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
    # socketio.emit("room_users", rooms[room]["room_users"], to=room)

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = "T-Bots"
    user = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        rooms[room]["room_users"].remove(user)
        if rooms[room]["members"] <= 0:
            del rooms[room]

    content = {
        "name": name,
        "message":user + " has entered the room" ,
    }
    send(content, to=room)

if __name__ == "__main__":
    socketio.run(app, debug=True)