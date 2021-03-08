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

    return sum(incoming_list)


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    LongestKey = ''
    for Key in thisdict:
        if len(Key) > len(LongestKey):
            LongestKey = Key

    return LongestKey
