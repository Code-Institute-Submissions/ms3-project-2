# import pymongo
import os
from flask import Flask, render_template, url_for, request, redirect, session
from os import path
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'thefluffiestofdogs'

if path.exists("env.py"):
    import env

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = "projectDB"


mongo = PyMongo(app)
# Initial home page
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("home.html", report=mongo.db.report.find().limit(5))

# Reading reports

@app.route('/get_report')
def get_report():
    return render_template("report.html", report=mongo.db.report.find())    

@app.route('/search_report')
def search_report():
    parameter = "Not chosen"
    return render_template("searchResults.html", parameter=parameter)

@app.route('/search_report_parameter',  methods=["POST"])
def search_report_parameter():
    parameter = request.form["search_parameter"]
    username=mongo.db.report.distinct("username")
    incident_description=mongo.db.report.distinct("incident_description")
    category=mongo.db.report.distinct("category_name")
    sub_category=mongo.db.report.distinct("sub_category")
    building=mongo.db.report.distinct("building")
    street=mongo.db.report.distinct("street")
    city=mongo.db.report.distinct("ci")
    county=mongo.db.report.distinct("county")
    postcode=mongo.db.report.distinct("postcode")
    reported=mongo.db.report.distinct("reported_to_authorities")
    return render_template("searchResults.html", postcode=postcode, county=county, city=city, street=street, sub_category=sub_category, building=building, incident_description=incident_description, category=category, emails=emails, username=username, parameter=parameter)

@app.route('/retrieving_report', methods=["POST"])
def retrieving_report():
    key = request.form["search_choice"]
    value = request.form["search_value"]
    the_report = mongo.db.report.find({key: value})
    return render_template("results_display.html", report=the_report)

























# Adding reports

@app.route('/add_report')
def add_report():
    return render_template("add_report.html", categories=mongo.db.categories.find(),
                           sub_category=mongo.db.sub_category.find(),
                           )

@app.route('/insert_report', methods=['POST'])
def insert_report():
    report = mongo.db.report
    report.insert_one(request.form.to_dict())
    return redirect(url_for('homepage'))



# Updating reports
@app.route('/user_modify/<report_id>')
def user_modify(report_id):
    the_report = mongo.db.report.find_one({"_id": ObjectId(report_id)})
    available_categories = mongo.db.categories.find()
    available_sub_categories = mongo.db.sub_category.find()
    return render_template('user_modify.html', report=the_report, categories=available_categories, sub_category=available_sub_categories)

@app.route('/edit_report/<report_id>', methods=["POST"])
def edit_report(report_id):
    report = mongo.db.report
    report.update({'_id': ObjectId(report_id)},
                  {
                  'email': request.form.get('email'),
                  'username': request.form.get('username'),
                  'category_name': request.form.get('category_name'),
                  'new_category_name': request.form.get('new_category_name'),
                  'sub_category': request.form.get('sub_category'),
                  'new_sub_category': request.form.get('new_sub_category'),
                  'incident_description': request.form.get('incident_description'),
                  'building': request.form.get('building'),
                  'street': request.form.get('street'),
                  'city': request.form.get('city'),
                  'county': request.form.get('county'),
                  'postcode': request.form.get('postcode'),
                  'report_to_authorities': request.form.get('report_to_authorities')
                  })
    return redirect(url_for('get_report'))


# Deleting reports

@app.route('/confirm_delete_report/<report_id>')
def confirm_delete_report(report_id):
    the_report = mongo.db.report.find_one({"_id": ObjectId(report_id)})
    available_categories = mongo.db.categories.find()
    available_sub_categories = mongo.db.sub_category.find()

    return render_template('confirm_delete.html', report=the_report, categories=available_categories, sub_category=available_sub_categories)


@app.route('/delete_report/<report_id>', methods=["POST"])
def delete_report(report_id):
    # Trigger a modal of some kind where the user has to input the correct email.
    report = mongo.db.report
    report.update({'_id': ObjectId(report_id)}, {"$set": {"archive_report": request.form.get('archive')}})
    return redirect(url_for('get_report'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

