from model.project import Project
import random


def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    if len(app.project.get_project_list) == 0:
        app.project.create(Project(name="test"))
    # old_projects = app.project.get_project_list()
    old_projects = app.soap.get_project_list(username=app.config["webadmin"]["username"],
                                             password=app.config["webadmin"]["password"])
    project = random.choice(old_projects)
    print(project.name)
    app.project.delete_project_by_name(project.name)
    # new_projects = app.project.get_project_list()
    old_projects.remove(project)
    new_projects = app.soap.get_project_list(username=app.config["webadmin"]["username"],
                                            password=app.config["webadmin"]["password"])
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)