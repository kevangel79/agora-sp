#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: invalid_fields.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'


def url_input_validation(input_field):
    """
    Function that checks if the received field displays an invalid URL error message.

    @param input_field: The element that contains the input field along with what surrounds it
                        ( labels, input, descriptions and messages ).
    @return: True if it appears below the field, the message that should appear or False if it does not appear.
    """
    input_field.find_element_by_tag_name("input").clear()
    input_field.find_element_by_tag_name("input").send_keys("123")

    if input_field.find_element_by_class_name("paper-input-error"):
        assert "The field must be a valid url" in input_field.find_element_by_class_name("paper-input-error").text
        print("{0:<36} URL Input Validation \t{1}".format('[' + input_field.text.split()[0] + ']', "Success"))
        return True
    else:
        print("[{0}] \t\t URL Input Validation \t\t{1}".format(input_field.text.split()[0], "Failed"))
        return False


def email_input_validation(input_field):
    """
    Function that checks if the received field displays an invalid Email error message.

    @param input_field: The element that contains the input field along with what surrounds it
                        ( labels, input, descriptions and messages ).
    @return: True if it appears below the field, the message that should appear or False if it does not appear.
    """
    input_field.find_element_by_tag_name("input").clear()
    input_field.find_element_by_tag_name("input").send_keys("123")

    if input_field.find_element_by_class_name("paper-input-error"):
        assert "The field must be a valid email address" in input_field.find_element_by_class_name(
            "paper-input-error").text
        print("{0:<36} Email Input Validation \t{1}".format('[' + input_field.text.split()[0] + ']', "Success"))
        return True
    else:
        print("[{0}] Email Input Validation \t{1}".format(input_field.text.split()[0], "Failed"))
        return False


def phone_input_validation(input_field):
    """
    Function that checks if the received field displays an invalid number error message.

    @param input_field: The element that contains the input field along with what surrounds it
                        ( labels, input, descriptions and messages ).
    @return: True if it appears below the field, the message that should appear or False if it does not appear.
    """
    input_field.find_element_by_tag_name("input").clear()
    input_field.find_element_by_tag_name("input").send_keys("GNU/Linux")
    phone = input_field.find_elements_by_class_name("paper-input-error")

    if input_field.find_element_by_class_name("paper-input-error"):
        assert "The field must be a number" in phone[0].text
        assert "The field must be between 10 and 20 characters" in phone[1].text
        print("{0:<36} Phone Input Validation \t{1}".format('[' + input_field.text.split()[0] + ']', "Success"))
        return True
    else:
        print("[{0}] \t\t Phone Input Validation \t{1}".format(input_field.text.split()[0], "Failed"))
        return False
