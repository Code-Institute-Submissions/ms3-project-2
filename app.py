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

# Look into why test can't be 0? 
comparison_number = None

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


# This is the OG screen with one search box as default.
@app.route('/search_report')
def search_report():
    parameter = "Not chosen"
    global comparison_number
    comparison_number = 1
    search_parameter1=mongo.db.search_parameters.find()
    return render_template("searchResults.html", search_parameter1=search_parameter1, parameter=parameter, comparison_number=comparison_number)

# Will search the basic parameters.
@app.route('/search_report_parameter',  methods=["POST"])
def search_report_parameter():
    if request.method == "POST":
        global comparison_number
        x = 1
        parameterChoices=[]
        chosen_parameter_options=[]
        checkedParameters = request.form.getlist("searchParameter")
        print(request.form.getlist("searchParameter"))
        for choice in checkedParameters:
            parameterChoices.append(choice)
            print(parameterChoices)
        for option in parameterChoices:
            options = mongo.db.report.distinct(option)
            chosen_parameter_options.append(options)
            print(chosen_parameter_options)
        number_of_fields = len(chosen_parameter_options)
        return render_template("pickValuesBasic.html", comparison_number=comparison_number, number_of_fields=number_of_fields, chosen_parameter_options=chosen_parameter_options, parameterChoices=parameterChoices, x=x)

# This submits the final report and returns the reports
@app.route('/retrieving_report', methods=["POST"])
def retrieving_report():
    global extra_parameters
    choices = []
    values = []
    fields = request.form["number_of_fields"]
    number_of_fields = int(fields)
    print(str(number_of_fields))
    for x in range(int(number_of_fields)):
        print(x)
        key = request.form["search_choice{}".format(x)]
        print(key)
        choices.append(key)
        value = request.form["search_value{}".format(x)]
        print(value)
        values.append(value)

        # Return values
    if number_of_fields == 2:
        print("if 2")
        the_report = mongo.db.report.find( { "$or": [ { choices[0]:values[0] }, { choices[1] : values[1]} ] } )
    elif number_of_fields  == 3:
        the_report = mongo.db.report.find( { "$or": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]} ] } )
    elif number_of_fields  == 4:
        the_report = mongo.db.report.find( { "$or": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]} ] } )
    elif number_of_fields  == 5:
        the_report = mongo.db.report.find( { "$or": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]}, { choices[4] : values[4]} ] } )
    else:
        the_report = mongo.db.report.find( {choices[0]: values[0]})
    return render_template("resultsDisplayBasic.html", report=the_report)



# For a comparison search

# Tells the computer how many extra boxes we need.
@app.route('/comparison_number')
def comparison_number():
    global comparison_number
    comparison_number = comparison_number + 1
    return redirect(url_for('adding_comparisons'))

# You need to make a 'remove parameter'

@app.route('/adding_comparisons')
def adding_comparisons():
    parameter = "Not chosen"
    search_parameter1=mongo.db.search_parameters.find()
    return render_template("searchResults.html", search_parameter1=search_parameter1, parameter=parameter, comparison_number=comparison_number)

# Here we need a route that can store the 

@app.route('/collecting_comparison_parameters', methods=["POST"])
def collecting_comparison_parameters():
    return "Here will be your comparison results!"




# This submits the final report and returns the reports
@app.route('/retrieving_report_with_filters', methods=["POST"])
def retrieving_report_with_filters():
    global comparison_number
    the_report_array = []
    choices = []
    values = []
    fields = request.form["number_of_fields"]
    number_of_fields = int(fields)
    print("number of fields" + str(number_of_fields))

    for r in range(comparison_number):
        for x in range(int(number_of_fields)):
            print(x)
            key = request.form["search_choice{}".format(x)]
            print(key)
            choices.append(key)
            value = request.form["search_value{}".format(x)]
            print(value)
            values.append(value)

            # Return values
        if number_of_fields == 2:
            the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]} ] } )
        elif number_of_fields == 3:
            the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]} ] } )
        elif number_of_fields  == 4:
            the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]} ] } )
        elif number_of_fields  == 5:
            the_report = mongo.db.report.find( { "$and": [ { choices[0]:values[0] }, { choices[1] : values[1]}, { choices[2] : values[2]}, { choices[3] : values[3]}, { choices[4] : values[4]} ] } )
        else:
            the_report = mongo.db.report.find( {choices[0]: values[0]})
        the_report_array.append(the_report)
        print(the_report[0])

    return render_template("results_display.html", report=the_report_array[0], report2=the_report_array[1], report3=the_report_array[2])























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





