#
"""
update workflows
1. adding new template need to be added in the modules/module_args.py
2. add to GetArgument if needed to access to outside
3. add new method to GenerateTemplate class for jinja2 parser
4. call the new method to gasconfig.py
"""

from scripts.template_scripts import GenerateConfigTemplate, GenerateBugzillaTemplate
from modules.module_args import GetArguments

def main():
    match GetArguments.get_template():
        case "es_migration":
            print(GenerateConfigTemplate.es_migration())

        case "post":
            print (GenerateBugzillaTemplate.change_post())

        case "decomm":
            print (GenerateBugzillaTemplate.change_decomm())

        case unknown_command:
            print(f"{str(unknown_command).title()} Template not supported!")

if __name__=="__main__":
    main()
