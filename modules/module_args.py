""" class for input task arguments"""
import argparse
class Arguments:
    """Argeparse  arguments class """

    def show_arguments_in_script(self):
        """This the argumentparser configurations!"""
        parser = argparse.ArgumentParser(description='Gasops Config Generator by Andrew Soltes')
        parser.add_argument("-t","--template",metavar="",
                            help="input the task type eg: es_migration") #optional argument
        parser.add_argument("-d","--date",metavar="",
                            help="input date format <year-month-day>")
        parser.add_argument("-p","--post",metavar="",
                            help="post change email")
        args = parser.parse_args()

        return [
            args.template,
            args.date,
            args.post]

    def get_template(self):
        """get the template from the user input"""
        template = Arguments()
        return template.show_arguments_in_script()[0]

    def get_date(self):
        """get the date from the user input"""
        date = Arguments()
        return date.show_arguments_in_script()[1]

    def get_post(self):
        """ get the post email template -- underconstruction"""
        post = Arguments()
        return post.show_arguments_in_script()[2]
