class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            "\n"
            "\nAuthors:"
            f"\n- {'\n- '.join(self.authors)}"
            "\n"
            "\nDependencies:"
            f"\n- {self._stringify_dependencies(self.dependencies)}"
            "\n"
            "\nDevelopment dependencies:"
            f"\n- {self._stringify_dependencies(self.dev_dependencies)}"
        )
