#
"""
update workflows
1. add the argsparse arguments in the
scripts.args_task.scripts.argument_task_for_gasops and add to return list
2. create a .py script for new templates for more clean and robust env
3. add a .j2 template under the templates folder
"""

from scripts.template_scripts import GenerateTemplate
from modules.module_args import Arguments

#getting the template argument value
argument = Arguments()
template = argument.get_template()
#generate the template
show_template = GenerateTemplate()

def main():
    """calling the functions created in script directory"""
    if  template == "es_migration":
        print(show_template.generate_es_migration_template())
    else:
        print ("Argument provided not available! Kindly contact andrew.soltes@trustwave.com")

if __name__=="__main__":
    main()
