from flask import render_template, url_for, request, redirect
from model import *
import datetime


@app.route('/')
def index():
	projects = Projects.query.all()
	return render_template('index.html', projects=projects)


@app.route('/about')
def about():
	projects = Projects.query.all()	
	return render_template('about.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
	projects = Projects.query.all()
	if request.method == "POST":
		new_project = Projects(title=request.form['title'], url=request.form['github'], skills_used=request.form['skills'],description=request.form['desc'], date=create_form_date(request.form['date']))
		db.session.add(new_project)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('projectform.html', projects=projects)


@app.route('/projects/<id>')
def projects(id): 
	projects = Projects.query.all()
	project = Projects.query.get_or_404(id)
	return render_template('detail.html', projects=projects, project=project)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    projects = Projects.query.all()
    project = Projects.query.get_or_404(id)
    if request.form:
        project.title = request.form['title']
        project.date = create_form_date(request.form['date'])
        project.description = request.form['desc']
        project.skills_used = request.form['skills']
        project.url = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', project=project, projects=projects)


@app.route('/projects/<id>/delete', methods=['GET', 'POST'])
def delete(id):
	project = Projects.query.get_or_404(id)
	db.session.delete(project)
	db.session.commit()
	return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html', msg='error'), 404


def create_form_date(request_form_date):
	"""creates a datetime object based on a request.form date to make a database ready object"""
	try:
		clean_date = datetime.datetime.strptime(request_form_date, '%Y-%m')
	except ValueError:
		clean_date = datetime.datetime.strptime(request_form_date, '%Y-%m-%d')
	return clean_date


def undo_form_date(string):
	"""will create a string to display in html"""
	project_date_string = datetime.datetime.strftime(string, '%-m/%-d/%Y')
	return project_date_string


if __name__ == "__main__":
	with app.app_context():
		db.create_all()
	app.run(debug=True, port=8000	, host='127.0.0.1')