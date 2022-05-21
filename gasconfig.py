#
"""
update workflows
1. adding new template need to be added in the modules/module_args.py
2. add to GetArgument if needed to access to outside
3. add new method to GenerateTemplate class for jinja2 parser
4. call the new method to gasconfig.py
"""

from scripts.template_scripts import GenerateTemplate
from modules.module_args import GetArguments

def main():
    """calling the functions created in script directory"""
    if  GetArguments.get_template() == "es_migration":
        print(GenerateTemplate.es_migration())
    else:
        print ("Argument provided not available! Kindly contact andrew.soltes@trustwave.com")

if __name__=="__main__":
    main()
