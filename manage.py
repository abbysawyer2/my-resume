from flask_script import Manager
from myresume import app, db, Professor, Course

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    convery = Professor(name='Amanda Convery', department='Accounting')
    crissinger = Professor(name='Bryan Crissinger', department='Mathematics')
    course1 = Course(coursenum="ACCT315", title="Intermediate Accounting",
                    description="In-depth coverage of financial accounting.", professor=convery)
    course2 = Course(coursenum="ACCT316", title="Intermediate Accounting",
                    description="Continuation of ACCT315.", professor=convery)
    course3 = Course(coursenum="MATH201", title="Introduction to Statistics I",
                description="Exploratory data analysis, basic probability, discrete and continuous distributions, sampling distributions and confidence intervals, and one- and two-sample hypothesis tests on means and proportions. ", professor=crissinger)
    course4 = Course(coursenum="MATH202", title="Introduction to Statistics II",
                description="Two-sample tests on means and proportions, chi-square analysis of contingency tables, completely randomized and randomized block designs, factorial experiments, etc.", professor=crissinger)
    db.session.add(convery)
    db.session.add(crissinger)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
