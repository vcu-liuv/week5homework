"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    return max(incoming_list)


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    return min(incoming_list)


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    sum_list = 0

    if incoming_list is None:
        sum_list = None
    elif len(incoming_list) == 0:
        sum_list = None
    else:
        sum_list = sum(incoming_list)

    return sum_list


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    if incoming_dict is None:
        return None
    elif len(incoming_dict) == 0:
        return None
    else:
        longest_key = ''
        longest_value = ''
        for key, value in incoming_dict.items():
            if len(value) > len(longest_value):
                longest_key = key
                longest_value = value
        
        return longest_key
