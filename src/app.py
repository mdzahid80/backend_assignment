import os

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pymongo import MongoClient, errors

from forms import TaxiShareForm, UserForm

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")

# MongoDB Connection
try:
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(mongo_uri)
    db = client["TaxiShare"]
    trip_collection = db["TripDetail"]
    users_collection = db["Users"]
except errors.ConnectionError as e:
    print(f"Error connecting to MongoDB: {e}")
    trip_collection = None
    users_collection = None


# Home route for posting rides
@app.route("/", methods=["GET", "POST"])
def home():
    form = TaxiShareForm()
    if form.validate_on_submit():
        response, status_code = post_ride()  # Data entry
        if status_code == 200:
            return redirect(url_for("success"))
        else:
            errors = response.json().get("errors")
            return render_template("index.html", form=form, errors=errors)

    return render_template("index.html", form=form)


# Success page route
@app.route("/success")
def success():
    return "Your ride has been successfully posted!"


# Route for posting a ride
@app.route("/post-ride", methods=["POST"])
def post_ride():
    form = TaxiShareForm()
    if trip_collection:
        ride = {
            "name": form.name.data,
            "phone_number": form.phone_number.data,
            "email": form.email.data,
            "start_location": form.start_location.data,
            "end_location": form.end_location.data,
            "date_time": form.date_time.data,
            "available_seats": form.available_seats.data,
            "price_per_seat": form.price_per_seat.data,
        }
        trip_collection.insert_one(ride)
        return jsonify({"message": "Ride posted successfully!"}), 200
    return jsonify({"error": "Database connection error"}), 500


# Route to get all rides
@app.route("/get-ride", methods=["GET"])
def get_all_rides():
    if trip_collection:
        rides = trip_collection.find()
        data = []
        for ride in rides:
            data.append(
                {
                    "id": str(ride["_id"]),
                    "name": ride["name"],
                    "phone_number": ride["phone_number"],
                    "email": ride["email"],
                    "start_location": ride["start_location"],
                    "end_location": ride["end_location"],
                    "date_time": ride["date_time"],
                    "available_seats": ride["available_seats"],
                }
            )
        return render_template("rides.html", rides=data)
    return jsonify({"error": "Database connection error"}), 500


# Route to search rides
@app.route("/search", methods=["GET"])
def search_rides():
    start_location = request.args.get("start")
    end_location = request.args.get("end")
    if trip_collection:
        rides = trip_collection.find(
            {"start_location": start_location, "end_location": end_location}
        )
        data = []
        for ride in rides:
            data.append(
                {
                    "id": str(ride["_id"]),
                    "name": ride["name"],
                    "phone_number": ride["phone_number"],
                    "email": ride["email"],
                    "start_location": ride["start_location"],
                    "end_location": ride["end_location"],
                    "date_time": ride["date_time"],
                    "available_seats": ride["available_seats"],
                    "price_per_seat": ride["price_per_seat"],
                }
            )
        return jsonify(data), 200
    return jsonify({"error": "Database connection error"}), 500


# Admin dashboard route
@app.route("/admin-dashboard", methods=["GET", "POST"])
def admin_dashboard():
    form = UserForm()
    message1 = ""
    if form.validate_on_submit():
        if users_collection:
            if users_collection.find_one({"email": form.email.data}):
                users_collection.update_one(
                    {"email": form.email.data},
                    {
                        "$set": {
                            "name": form.name.data,
                            "email": form.email.data,
                            "phone_number": form.phone_number.data,
                        }
                    },
                )
                message1 = f"User {form.name.data} updated successfully"
            else:
                users_collection.insert_one(
                    {
                        "name": form.name.data,
                        "email": form.email.data,
                        "phone_number": form.phone_number.data,
                    }
                )
                message1 = f"User {form.name.data} added successfully"
            return redirect(url_for("admin_dashboard"))
        else:
            message1 = "Database connection error"

    if users_collection:
        users = users_collection.find()
        data = []
        for user in users:
            data.append(
                {
                    "id": str(user["_id"]),
                    "name": user["name"],
                    "phone_number": user["phone_number"],
                    "email": user["email"],
                }
            )
    else:
        data = []

    return render_template("admin.html", form=form, message=message1, users=data)


# Route to get all users
@app.route("/admin/users", methods=["GET"])
def admin_get_users():
    if users_collection:
        users = list(users_collection.find({}, {"_id": False}))
        return jsonify(users), 200
    return jsonify({"error": "Database connection error"}), 500


# Route to get a single user by email
@app.route("/admin/users/<email>", methods=["GET"])
def admin_get_user(email):
    if users_collection:
        user = users_collection.find_one({"email": email}, {"_id": False})
        if user:
            return jsonify(user), 200
        else:
            return jsonify({"error": "User not found"}), 404
    return jsonify({"error": "Database connection error"}), 500


# Route to delete a user by email
@app.route("/admin/users/<email>", methods=["DELETE"])
def admin_delete_user(email):
    if users_collection:
        result = users_collection.delete_one({"email": email})
        if result.deleted_count > 0:
            return jsonify({"message": "User deleted successfully!"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    return jsonify({"error": "Database connection error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
