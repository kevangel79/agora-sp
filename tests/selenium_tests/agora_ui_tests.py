#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: agora_unit_tests.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.contacts.contact_form_validations import ContactFormValidations
from agora.contacts.contacts_create import ContactCreate
from agora.providers.provider_create import CreateProvider
from agora.providers.provider_form_validations import ProviderFormValidations
from agora.resources.resource_create import ResourceCreate
from agora.resources.resource_form_validations import ResourceFormValidations


if __name__ == '__main__':
    contact = ContactCreate("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")
    contact.create_new_contact()
    ContactFormValidations("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")

    provider = CreateProvider("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")
    provider.create_new_provider(required_only=False)
    ProviderFormValidations("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")

    resource = ResourceCreate("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")
    resource.create_new_resource(required_only=False)
    ResourceFormValidations("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")
