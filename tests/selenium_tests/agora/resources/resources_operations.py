#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: resources_operators.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.resources.resources import Resources


class ResourcesOperations(Resources):
    """
    Operations on list view of Resources.

    This class is responsible for checking the following:
        * Edit option on ContactsListView is available.
        * Details option on ContactsListView is available.
        * TODO : Delete
    """

    def __init__(self, driver, headless=True, instance="https://testvm.agora.grnet.gr/"):
        """
        Initialization.

        This method ensures that all the prerequisites will be met, so that you can go to Resources list view.
        page.
        @param driver: Which browser will be used.
        @param headless: If you want headless browser - without GUI.
        @param instance: The website instance of the Agora project to be used for the tests.
        """
        super().__init__(driver, headless, instance)
        print("\n# Edit a resources record.")
        super().edit_from_listView()
        # Go again to Resources list view page.
        self.resources_page()
        print("\n# Details of a contact record.")
        super().details_from_listView()
        self.close()

