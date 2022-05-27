import re
# from modules.module_date_time import DateTime
# from modules.module_args import Arguments, GetArguments
class StringFormatting:

    @staticmethod
    def get_number(user_input):
        """Only get the number/interget of the user input""" #output 36
        cg_number = re.findall(r'\d+', f"{user_input}")
        result = ''.join(cg_number) # convert string to number
        return result

    @staticmethod
    def get_uppercase(user_input):
        """Only get the uppercase letter of the user input""" #output GE
        get_input_uppercase = ''.join([c for c in user_input if c.isupper()])
        result = f"{get_input_uppercase[0: -1]}"  # remove the last uppercase letter
        print(get_input_uppercase)
        return result

    @staticmethod
    def remove_underscore(user_input):
        result =  user_input.replace('_', '')
        return result
