from flask import Flask, jsonify, request
app = Flask(__name__)

contacts = {
    "data":[
        {
            "Contact":"9987644456",
            "Name":"Raju",
            "done":False,
            "id":1
        },
        {
            "Contact":"9876543222",
            "Name":"Rahul",
            "done":False,
            "id":2
        }
    ]
}

@app.route("/get-data")

def get_tasks():
    return jsonify({
        "data":contacts
    })

@app.route("/add-data",methods=["POST"])

def add_tasks():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data"
        },400)
    contact = {
        "id":contacts[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    contacts.append(contact)
    return jsonify({
        "status":"Success",
        "message":"Data was sent successfully"
    })

if(__name__=="__main__"):
    app.run(debug=True)




    
