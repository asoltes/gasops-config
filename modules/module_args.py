""" class for input task arguments"""
import argparse

class Arguments:
    """Argeparse  arguments class """
    @staticmethod
    def show_arguments_in_script():
        """This the argumentparser configurations!"""
        parser = argparse.ArgumentParser(description='Gasops Config Generator by Andrew Soltes')
        parser.add_argument("-t","--template",metavar="",
                            help="input the task type eg: es_migration") #optional argument
        parser.add_argument("-d","--date",metavar="",
                            help="input date format <year-month-day>")
        parser.add_argument("-p","--post",metavar="",
                            help="post change email")
        parser.add_argument("-jrt","--jira_ticket",metavar="",
                            help="Jira ticket")
        parser.add_argument("-srv","--servers",metavar="",
                            help="Linux/Windows Server")

        args = parser.parse_args()

        return [
            args.template,
            args.date,
            args.post,
            args.jira_ticket,
            args.servers]


class GetArguments:
    """ Get Arguments from the Argument class """
    @staticmethod
    def get_template():
        """get the template from the user input"""
        return Arguments.show_arguments_in_script()[0]

    @staticmethod
    def get_date():
        """get the date from the user input"""
        return Arguments.show_arguments_in_script()[1]

    @staticmethod
    def get_consumer_group():
        """Get the consumer group"""
        return Arguments.show_arguments_in_script()[2]

    @staticmethod
    def get_jira_ticket():
        """Get the Jira Ticket Number"""
        return Arguments.show_arguments_in_script()[3]

    # @staticmethod
    # def get_servers(*kwargs):
    #     """Get the host for decom"""
    #     return [Arguments.show_arguments_in_script()[4]]
