from model.project import Project
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(name=random_string("name", 10), description=random_string("description", 20))
]

@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    app.session.login("administrator", "root")
    # old_projects = app.project.get_project_list()
    old_projects = app.soap.get_project_list(username=app.config["webadmin"]["username"], password=app.config["webadmin"]["password"])
    app.project.create(project)
    # new_projects = app.project.get_project_list()
    # assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    new_projects = app.soap.get_project_list(username=app.config["webadmin"]["username"], password=app.config["webadmin"]["password"])
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)






