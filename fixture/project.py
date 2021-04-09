from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init project creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        projects_list = []
        table = wd.find_element_by_css_selector("table.width100:nth-child(6)")
        for row in table.find_elements_by_css_selector("tr.row-1,tr.row-2"):
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            description = cells[4].text
            projects_list.append(Project(name=name, description=description))
        return projects_list

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_name(name)
        #delete
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()

