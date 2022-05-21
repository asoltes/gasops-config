"""Generate template for ES Migration Project"""

from jinja2 import Template
from modules.module_args import GetArguments
from modules.module_date_time import DateTime

class GenerateTemplate:
    """Super/Parent Class to Generate the template"""
    def __init__(self):
        """Instance variable function """

    @staticmethod
    def es_migration():
        """parse gathered data to jinja2 and generate template"""
        template = "./templates/es_migration/template.j2"
        with open (template, encoding="utf_8") as file:
            config = Template(file.read(), keep_trailing_newline=True)
            rendered_config = config.render(
                default_date_input=GetArguments.get_date(),
                formatted_date=DateTime.convert_to_underscore_format())

        return rendered_config
