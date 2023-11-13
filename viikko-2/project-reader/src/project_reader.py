from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed = toml.loads(content)
        
        project = parsed["tool"]["poetry"]
        dependencies = project["dependencies"].keys()
        dev_dependencies = project["group"]["dev"]["dependencies"].keys()

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(project["name"], project["description"], dependencies, dev_dependencies, project["authors"], project["license"])
