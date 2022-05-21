"""
Time and date module class
"""
from datetime import datetime, timedelta
import pytz
from modules.module_args import GetArguments

class DateTime:
    """class for time """

    @staticmethod
    def show_current_time():
        """show philippines local and current time"""
        ph_current_time = datetime.now(pytz.timezone('Asia/Manila'))
        pht = ph_current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        return pht

    @staticmethod
    def show_current_time_cdt():
        """US/CHICAGO local and current time"""
        chicago_current_time_real = datetime.now(pytz.timezone('US/Central'))
        cdt = chicago_current_time_real.strftime("%Y-%m-%d %H:%M:%S %Z")
        return cdt

    @staticmethod
    def show_add_10_minutes_to_cdt():
        """US/CHICAGO local and current time + 10 minutes"""
        ten_mins = 10
        chicago_current_time_add_10 = datetime.now(pytz.timezone('US/Central')
        ) + timedelta(minutes=ten_mins)
        cdt_added_10_minutes = chicago_current_time_add_10.strftime("%Y-%m-%d %H:%M:%S %Z")
        return cdt_added_10_minutes

    @staticmethod
    def convert_to_underscore_format():
        """create an underscore date format example: 1992-11-30 ---> 1992_11_30"""
        # input_date = GetArguments()
        show_input_date = GetArguments.get_date()
        formatted_date = show_input_date.replace("-","_")
        return formatted_date
