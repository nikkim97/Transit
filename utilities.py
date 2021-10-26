import re

def convert_str_to_list(times):
    """ 
    Converts string list to list of strings 

    Input: "[08:00, 09:30, 11:00, 12:30, 14:00, 15:30, 16:00, 18:00]"
    Output: ["08:00", "09:30", "11:00", "12:30", "14:00", "15:30", "16:00", "18:00"] 
    
    """
    return times.strip('][').split(', ')

def validate_time_format(list):
    """
    Validates incoming time list is in HH:MM format and within 24 hour time range
    
    """
    for times in list:
        if not re.match("([01]?[0-9]|2[0-3]):[0-5][0-9]", times):
           return False 
    return True

def valid_timelist_format(list_arg):
    """
    Checks to see if times list is in the correct format: [08:00, 09:30, 16:00, 18:00] 
    """
    if "[" not in list_arg or "]" not in list_arg:
        return False
    return True

