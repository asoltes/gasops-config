"""Generate template for ES Migration Project"""

from jinja2 import Template
from modules.module_args import GetArguments
from modules.module_date_time import DateTime

class GenerateConfigTemplate:
    """Super/Parent Class to Generate the template"""

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


class GenerateBugzillaTemplate:
    """Generate Bugzilla Template"""
    @staticmethod
    def change_post():
        """parsed the input data to jinja2"""
        template = "templates/bugzilla/post_change/template.j2"
        with open (template, encoding="utf_8") as file:
            config = Template(file.read(), keep_trailing_newline=True)
            rendered_config = config.render()
        return rendered_config

    @staticmethod
    def change_decomm():
        """Parsed and generate decomm template"""
        template = "templates/bugzilla/decommision/template.j2"
        with open (template, encoding="utf_8") as file:
            config = Template(file.read(), keep_trailing_newline=True)
            rendered_config = config.render(
                jira_ticket= GetArguments.get_jira_ticket(),
                cdt=DateTime.show_add_10_minutes_to_cdt(),
                pht=DateTime.show_current_time_pht())
        return rendered_config
