"""Generate template for ES Migration Project"""

from jinja2 import Template
from modules.module_args import Arguments
from modules.module_date_time import DateTime

class GenerateTemplate:
    """Super/Parent Class to Generate the template"""
    def __init__(self):
        """Instance variable function """
        self.raw_date = Arguments()
        self.date_to = DateTime()

    def generate_es_migration_template(self):
        """parse gathered data to jinja2 and generate template"""
        template = "./templates/es_migration/template.j2"
        with open (template, encoding="utf_8") as file:
            config = Template(file.read(), keep_trailing_newline=True)
            rendered_config = config.render(
                default_date_input=self.raw_date.get_date(),
                formatted_date=self.date_to.convert_to_underscore_format())

        return rendered_config


    def generate_ssl_template(self):
        """reserve for ssl template"""
        return self.raw_date
