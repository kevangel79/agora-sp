  # djoser_verifier: agora.utils.djoser_verifier
  # userid_extractor: agora.utils.userid_extractor

SERVICE_FIELDS_COMMON = {
    'id': {
        '.field.uuid': {},
        '.flag.nowrite': {}},
    'name': {
        '.field.string': {},
        '.flag.filterable': {},
        '.flag.searchable': {},
        '.flag.orderable': {}},
    'url': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'endpoint': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'description': {
        '.field.string': {},
        '.flag.searchable': {},
        'source': 'short_description',
        '.flag.nullable.default': {}},
    'tagline': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'service_type': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'user_value': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'target_customers': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'target_users': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'screenshots_videos': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'languages': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'standards': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'certifications': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'customer_facing': {
        '.flag.filterable': {},
        '.field.boolean': {}},
    'internal': {
        '.flag.filterable': {},
        '.field.boolean': {}},
    'tags': {
        '.field.string': {},
        '.flag.searchable': {},
        '.flag.nullable.default': {}},
    'scientific_fields': {
        '.field.string': {},
        '.flag.searchable': {},
        '.flag.nullable.default': {}},
    'helpdesk': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'order': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'order_type': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'changelog': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'last_update': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {}},
    'created_at': {
        '.field.datetime': {},
        '.flag.nullable': {},
        '.flag.nowrite': {}},
    'updated_at': {
        '.field.datetime': {},
        '.flag.nullable': {},
        '.flag.nowrite': {}},
    'service_categories_names': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'providers_names': {
        '.field.string': {},
        'source': 'organisations_names',
        '.flag.nowrite': {}},
    'other_required_services': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'other_related_services': {
        '.field.string': {},
        '.flag.nullable.default': {}},
    'related_platform': {
        '.field.string': {},
        '.flag.nullable.default': {}},
}


SERVICE_FIELDS_INT = {
    'logo': {
        '.field.file': {},
        'default': ''},
    'owner_name': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'owner_contact': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'support_name': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'support_contact': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'security_name': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'security_contact': {
        '.field.string': {},
        '.flag.orderable': {},
        '.flag.nullable.default': {},
        '.flag.filterable': {}},
    'service_admins_ids': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'pending_service_admins_ids': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'rejected_service_admins_ids': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'service_categories': {
        '.field.collection.django': {},
        '.flag.nullable.default': {},
        ':filter_compat': True,
        'flat': True,
        'id_field': 'service_category',
        'model': 'service.models.Service.service_categories.through',
        'source': 'service_categories',
        'bound': 'service',
        'fields': {
            'service_category': {'.field.ref': {},
                                 'source': 'servicecategory_id',
                                 'to': 'api/v2/service-categories'},
        },
    },
    'providers': {
        '.field.collection.django': {},
        '.flag.nullable.default': {},
        ':filter_compat': True,
        'flat': True,
        'id_field': 'organisation',
        'model': 'service.models.Service.organisations.through',
        'source': 'organisations',
        'bound': 'service',
        'fields': {
            'organisation': {'.field.ref': {},
                            'source': 'organisation_id',
                            'to': 'api/v2/providers'},
        }
    },
    'adminships': {
        '.field.collection.django': {},
        ':filter_compat': True,
        '.flag.nullable.default': {},
        '.flag.filterable': {},
        'model': 'service.models.ServiceAdminship',
        'source': 'serviceadminships',
        'bound': 'service',
        'fields': {
            'id': {
                '.field.serial': {}},
            'user_id': {
                '.field.integer': {},
                '.flag.nowrite': {},
                '.flag.filterable': {},
                'source': 'admin.pk'},
        }
    },

    'required_services': {
        '.field.collection.django': {},
        '.flag.nullable.default': {},
        ':filter_compat': True,
        'flat': True,
        'id_field': 'service',
        'model': 'service.models.Service.required_services.through',
        'source': 'required_services',
        'bound': 'from_service',
        'fields': {
            'service': {'.field.ref': {},
                        'source': 'to_service_id',
                        'to': 'api/v2/services'},
        },
    },
    'related_services': {
        '.field.collection.django': {},
        '.flag.nullable.default': {},
        ':filter_compat': True,
        'flat': True,
        'id_field': 'service',
        'model': 'service.models.Service.related_services.through',
        'source': 'related_services',
        'bound': 'from_service',
        'fields': {
            'service': {'.field.ref': {},
                        'source': 'to_service_id',
                        'to': 'api/v2/services'},
        },
    },
}

SERVICE_FIELDS_EXT = {
    # extended keys
    'logo': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'logo_absolute_path'},
    'related_services_names': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'required_services_names': {
        '.field.string': {},
        '.flag.nowrite': {}},
}

SERVICE_FIELDS_INTERNAL = dict(SERVICE_FIELDS_COMMON, **SERVICE_FIELDS_INT)
SERVICE_FIELDS_EXTERNAL = dict(SERVICE_FIELDS_COMMON, **SERVICE_FIELDS_EXT)

USERS = {
    '.collection.django': {},
    'model': 'accounts.models.User',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'username': {
            '.flag.orderable': {},
            '.field.string': {}},
        'email': {
            '.flag.orderable': {},
            '.field.string': {}},
        'first_name': {
            '.field.string': {}},
        'last_name': {
            '.field.string': {}},
        'is_staff': {
            '.field.boolean': {}},
        'is_active': {
            '.flag.orderable': {},
            '.field.boolean': {}},
        'date_joined': {
            '.field.string': {}},
        'avatar': {
            '.field.file': {},
            'default': ''},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    }
}

USER_CUSTOMERS = {
    '.collection.django': {},
    'model': 'service.models.UserCustomer',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.ref': {},
            'source': 'name_id',
            'to': 'api/v2/user-roles'},
        'role': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'service_id': {
            '.field.ref': {},
            'source': 'service_id_id',
            '.flag.filterable': {},
            'to': 'api/v2/services'},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    }
}

SERVICE_DEPENDSON_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service_DependsOn_Service',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'id_service_one': {
            '.field.ref': {},
            'source': 'id_service_one_id',
            'to': '/api/v2/service'},
        'id_service_two': {
            '.field.ref': {},
            'source': 'id_service_two_id',
            'to': '/api/v2/service'},
    }
}

SERVICE_EXTERNAL_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service_ExternalService',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'id_service': {
            '.field.ref': {},
            'source': 'id_service_id',
            'to': '/api/v2/service'},
        'id_external_service': {
            '.field.ref': {},
            'source': 'id_external_service_id',
            'to': '/api/v2/external_service'},
    }
}

SERVICE_STATUS = {
    '.collection.django': {},
    'model': 'service.models.ServiceStatus',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'value': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.filterable': {}},
        'description': {
            '.field.string': {},
            '.flag.nullable.default': {},
            '.flag.searchable': {}},
        },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
        },
}

SERVICE_TRLS = {
    '.collection.django': {},
    'model': 'service.models.ServiceTrl',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'value': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'order': {
            '.field.integer': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

EXTERNAL_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.ExternalService',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {}},
        'description': {
            '.field.string': {}},
        'service': {
            '.field.string': {}},
        'details': {
            '.field.string': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

USER_ROLES = {
    '.collection.django': {},
    'model': 'service.models.UserRole',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.flag.orderable': {},
            '.field.string': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

SERVICE_CATEGORIES = {
    '.collection.django': {},
    'model': 'service.models.ServiceCategory',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'icon': {
            '.field.file': {},
            'default': ''},
        'icon_absolute_path': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'description': {
            '.field.string': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

SERVICE_OWNERS = {
    '.collection.django': {},
    'model': 'owner.models.ServiceOwner',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'first_name': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'last_name': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'email': {
            '.field.email': {},
            '.flag.nullable.default': {}},
        'phone': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'id_service_owner': {
            '.field.ref': {},
            'source': 'id_service_owner_id',
            'to': '/api/v2/institutions'},
        'id_account': {
            '.field.ref': {},
            'source': 'id_account_id',
            'to': '/api/v2/custom-users'},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

CUSTOM_USERS = {
    '.collection.django': {},
    'model': 'accounts.models.User',
    ':permissions_namespace': 'agora.checks.User',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'username': {
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.field.string': {}},
        'email': {
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.field.string': {}},
        'first_name': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'last_name': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'is_staff': {
            '.field.boolean': {},
            '.flag.nullable.default': {}},
        'is_active': {
            '.flag.orderable': {},
            '.field.boolean': {}},
        'date_joined': {
            '.flag.nowrite': {},
            '.field.datetime': {}},
        'avatar': {
            '.field.file': {},
            'default': ''},
        'shibboleth_id': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'role': {
            '.flag.orderable': {},
            '.flag.filterable': {},
            '.field.string': {}},
        'organisation': {
            '.field.ref': {},
            'source': 'organisation_id',
            'to': '/api/v2/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'providers': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'organisation',
            'model': 'accounts.models.User.organisations.through',
            'source': 'organisations',
            'bound': 'user',
            'fields': {
                'organisation': {'.field.ref': {},
                                'source': 'organisation_id',
                                'to': 'api/v2/providers'},
            }
        }

    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


INSTITUTIONS = {
    '.collection.django': {},
    'model': 'owner.models.Institution',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'address': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'country': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'department': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

COMPONENTS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponent',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
        'description': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'logo': {
            '.field.file': {},
            'default': ''},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

COMPONENT_IMPLEMENTATIONS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponentImplementation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_id': {
            '.field.ref': {},
            'source': 'component_id_id',
            'to': '/api/v2/components',
            '.flag.filterable': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

COMPONENT_IMPLEMENTATION_DETAILS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponentImplementationDetail',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'component_id_id',
            'to': '/api/v2/components'},
        'component_implementation_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'component_implementation_id_id',
            'to': '/api/v2/component-implementations'},
        'version': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

COMPONENT_IMPLEMENTATION_DETAIL_LINKS = {
    '.collection.django': {},
    'model': 'component.models.ServiceDetailsComponent',
    ':permissions_namespace': 'agora.checks.CIDL',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'service_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'service_id_id',
            'to': '/api/v2/services'},
        'service_details_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'service_details_id_id',
            'to': '/api/v2/service-versions'},
        'service_component_implementation_detail_id': {
            '.flag.filterable': {},
            '.field.ref': {},
            'source': 'service_component_implementation_detail_id_id',
            'to': '/api/v2/component-implementation-details'},
        'service_type': {
            '.flag.searchable': {},
            '.field.string': {},
            '.flag.nullable.default': {}},
        'configuration_parameters': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'service_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


EXT_COMPONENTS = {
    '.collection.django': {},
    'model': 'component.models.ServiceComponentImplementationDetail',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_category': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'component_id.name'},
        'component_category_description': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'component_id.description'},
        'component_description': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'component_implementation_id.description'},
        'component_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'component_implementation_id.name'},
        'component_version': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {},
            'source': 'version'},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}


EXT_COMPONENT_CONNECTIONS = {
    '.collection.django': {},
    'model': 'component.models.ServiceDetailsComponent',
    ':permissions_namespace': 'agora.checks.CIDL',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'component_id': {
            '.field.uuid': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_component_implementation_detail_id.id'},
        'component_version': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_component_implementation_detail_id.version'},
        'component_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_component_implementation_detail_id.component_implementation_id.name'},
        'component_category': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_component_implementation_detail_id.component_implementation_id.component_id.name'},
        'service_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_id.name'},
        'service_id': {
            '.field.uuid': {},
            '.flag.filterable': {},
            'source': 'service_id.id'},
        'service_version': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.filterable': {},
            'source': 'service_details_id.version'},
        'service_type': {
            '.flag.searchable': {},
            '.field.string': {},
            '.flag.nullable.default': {}},
        'configuration_parameters': {
            '.field.string': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_INTERNAL,
    ':permissions_namespace': 'agora.checks.Service',
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},

        'delete': {
            'processors': {
                'post_delete_message': {
                    '.processor': {},
                    'module_path': 'service.models.PostDeleteMessage',
                    'read_keys': {'=': (
                        'backend/instance',
                        'guards/transaction_commit',
                    )},
                    'write_keys': {'=': (
                        'guards/transaction_commit',
                    )},
                },
            },
        },
        'update': {
            'processors': {
                'post_update_message': {
                    '.processor': {},
                    'module_path': 'service.models.PostUpdateMessage',
                    'read_keys': {'=': (
                        'response/content',
                    )},
                    'write_keys': {'=': (
                        'response/content',
                    )},
                },
            },
        },
        'partial_update': {
            'processors': {
                'post_partial_update_message': {
                    '.processor': {},
                    'module_path': 'service.models.PostUpdateMessage',
                    'read_keys': {'=': (
                        'response/content',
                    )},
                    'write_keys': {'=': (
                        'response/content',
                    )},
                },
            },
        },
        'create': {
            'processors': {
                'post_create_message': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateMessage',
                    'read_keys': {'=': (
                        'response/content',
                    )},
                    'write_keys': {'=': (
                        'response/content',
                    )},
                },
                'custom_post_create': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateService',
                    'read_keys': {'=': (
                        'backend/raw_response',
                        'auth/user',
                    )},
                    'write_keys': {'=': (
                        'backend/raw_response',
                    )},
                },
            },
        },
    },
}


EXT_SERVICES = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_EXTERNAL,
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.partial_update': {},
    },
}


SERVICES_MARKETPLACE = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_EXTERNAL,
    ':permissions_namespace': 'agora.checks.Service',
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.partial_update': {},
    },
}

SERVICES_CATALOGUE = {
    '.collection.django': {},
    'model': 'service.models.Service',
    'fields': SERVICE_FIELDS_EXTERNAL,
    ':permissions_namespace': 'agora.checks.Service',
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.partial_update': {},
    },
}

SERVICE_TYPES_FIELDS = {
    'id': {
        '.field.uuid': {},
        '.flag.nowrite': {}},
    'service_name': {
        '.field.string': {},
        '.flag.nowrite': {},
        'source': 'service_id.name'},
    'service_type': {
        '.field.string': {},
        '.flag.nowrite': {}},
    'in_catalogue': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_details_id.is_in_catalogue'},
    'visible_to_marketplace': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_details_id.visible_to_marketplace'},
    'external_service': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.customer_facing'},
    'internal_service': {
        '.field.boolean': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.internal'},
    'service_tagline': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.tagline'},
    'service_description': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.short_description'},
    'service_category': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.service_category.name'},
    'service_version': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_details_id.version'},
    'component_name': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_component_implementation_detail_id.component_id.name'},
    'component_version': {
        '.field.string': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_component_implementation_detail_id.version'},
    'service_id': {
        '.field.uuid': {},
        '.flag.nowrite': {},
        '.flag.filterable': {},
        'source': 'service_id.id'},


}

SERVICE_TYPES = {
    '.collection.django': {},
    'model': 'component.models.ServiceDetailsComponent',
    'fields': SERVICE_TYPES_FIELDS,
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

SERVICE_VERSIONS = {
    '.collection.django': {},
    'model': 'service.models.ServiceDetails',
    ':permissions_namespace': 'agora.checks.ServiceVersion',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'id_service': {
            '.field.ref': {},
            'source': 'id_service_id',
            'to': '/api/v2/services',
            '.flag.filterable': {}},
        'service_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'status': {
            '.field.ref': {},
            'source': 'status_id',
            'to': '/api/v2/service-status',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'version': {
            '.flag.orderable': {},
            '.field.string': {}},
        'terms_of_use_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'privacy_policy_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'user_manual': {
            '.field.string': {},
            'source': 'user_documentation_url',
            #'.flag.blankable': {},
            '.flag.nullable.default': {}},
        'admin_manual': {
            '.field.string': {},
            'source': 'operations_documentation_url',
            '.flag.nullable.default': {}},
        'monitoring_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'is_in_catalogue': {
            '.flag.filterable': {},
            '.flag.orderable': {},
            '.field.boolean': {},
            'default': False},
        'visible_to_marketplace': {
            '.flag.filterable': {},
            '.flag.orderable': {},
            '.field.boolean': {},
            'default': False},
        'sla_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'training_information': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'maintenance_url': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'service_trl': {
            '.field.ref': {},
            'source': 'service_trl_id',
            'to': '/api/v2/service-trls',
            '.flag.orderable': {},
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'created_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        'updated_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        # extended fields
        'id_service_ext': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nowrite': {},
            'source': 'id_service.name'},
        'status_ext': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nowrite': {},
            'source': 'status.value'},
        'access_policies': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'access_policy',
            'model': 'service.models.ServiceDetails.access_policies.through',
            'source': 'access_policies',
            'bound': 'servicedetails',
            'fields': {
                'access_policy': {'.field.ref': {},
                                'source': 'accesspolicy_id',
                                'to': 'api/v2/access-policies'},
            }
        }
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

RESOURCE_ADMINS = {
    '.collection.django': {},
    'model': 'service.models.ResourceAdminship',
    ':permissions_namespace': 'agora.checks.ResourceAdminship',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'state': {
            '.field.string': {},
            'default': 'pending',
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'resource': {
            '.field.ref': {},
            'source': 'resource_id',
            'to': '/api/v2/resources',
            '.flag.nullable.default': {},
            '.flag.filterable': {}},
        'resource_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.orderable': {},
            'source': 'resource.erp_bai_1_name'},
        'admin_email': {
            '.field.string': {},
            '.flag.nowrite': {},
            '.flag.orderable': {},
            'source': 'admin.email'},
        'admin_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'admin.first_name'},
        'admin_last_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'admin.last_name'},
        'admin_id': {
            '.field.uuid': {},
            '.flag.nowrite': {},
            'source': 'admin.id'},
        'created_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        'updated_at': {
            '.field.datetime': {},
            '.flag.nullable': {},
            '.flag.nowrite': {}},
        'admin': {
            '.field.ref': {},
            'source': 'admin_id',
            '.flag.filterable': {},
            '.flag.nullable.default': {},
            'to': '/api/v2/custom-users'},

    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
         'create': {
            'processors': {
                'custom_post_create': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateResourceadminship',
                    'read_keys': {'=': (
                        'backend/raw_response',
                        'auth/user',
                        'request/meta/headers',
                    )},
                    'write_keys': {'=': (
                        'backend/raw_response',  # declared to ensure chaining
                    )},
                },
            },
        },
       'partial_update': {
           'processors': {
               'custom_post_partial_update': {
                   '.processor': {},
                   'module_path': 'service.models.PostPartialUpdateResourceadminship',
                   'read_keys': {'=': (
                       'backend/raw_response',
                       'auth/user',
                       'request/meta/headers',
                   )},
                   'write_keys': {'=': (
                       'backend/raw_response',  # declared to ensure chaining
                   )},
               },
           },
       },


    },
}

MERIL_DOMAINS = {
    '.collection.django': {},
    'model': 'accounts.models.MerilDomain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


DOMAINS = {
    '.collection.django': {},
    'model': 'accounts.models.Domain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

MERIL_SUBDOMAINS = {
    '.collection.django': {},
    'model': 'accounts.models.MerilSubdomain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'domain': {
            '.field.ref': {},
            'source': 'domain_id',
            'to': '/api/v2/merildomains',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

SUBDOMAINS = {
    '.collection.django': {},
    'model': 'accounts.models.Subdomain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'domain': {
            '.field.ref': {},
            'source': 'domain_id',
            'to': '/api/v2/domains',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

SUPERCATEGORIES = {
    '.collection.django': {},
    'model': 'service.models.Supercategory',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

CATEGORIES = {
    '.collection.django': {},
    'model': 'service.models.Category',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'supercategory': {
            '.field.ref': {},
            'source': 'supercategory_id',
            'to': '/api/v2/supercategories',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

SUBCATEGORIES = {
    '.collection.django': {},
    'model': 'service.models.Subcategory',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'category': {
            '.field.ref': {},
            'source': 'category_id',
            'to': '/api/v2/categories',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

LEGAL_STATUSES = {
    '.collection.django': {},
    'model': 'accounts.models.LegalStatus',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


NETWORKS = {
    '.collection.django': {},
    'model': 'accounts.models.Network',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'abbreviation': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

STRUCTURES = {
    '.collection.django': {},
    'model': 'accounts.models.Structure',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

AFFILIATIONS = {
    '.collection.django': {},
    'model': 'accounts.models.Affiliation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ESFRI_DOMAINS= {
    '.collection.django': {},
    'model': 'accounts.models.EsfriDomain',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ESFRI_TYPES= {
    '.collection.django': {},
    'model': 'accounts.models.EsfriType',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ACTIVITIES= {
    '.collection.django': {},
    'model': 'accounts.models.Activity',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

FUNDING_BODIES= {
    '.collection.django': {},
    'model': 'service.models.FundingBody',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

FUNDING_PROGRAMS = {
    '.collection.django': {},
    'model': 'service.models.FundingProgram',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ORDER_TYPES= {
    '.collection.django': {},
    'model': 'service.models.OrderType',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ACCESS_TYPES= {
    '.collection.django': {},
    'model': 'service.models.AccessType',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

ACCESS_MODES= {
    '.collection.django': {},
    'model': 'service.models.AccessMode',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

TRLS= {
    '.collection.django': {},
    'model': 'service.models.TRL',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

RESOURCE_LIFECYCLE_STATUSES= {
    '.collection.django': {},
    'model': 'service.models.LifeCycleStatus',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

CHALLENGES= {
    '.collection.django': {},
    'model': 'accounts.models.Challenge',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


ORGANISATIONS = {
    '.collection.django': {},
    'model': 'accounts.models.Organisation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'epp_bai_0_id': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_bai_1_name': {
          '.field.string': {},
          '.flag.filterable': {},
          '.flag.searchable': {},
        },
        'epp_bai_2_abbreviation': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_bai_3_website': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_bai_4_legal_entity': {
          '.field.boolean': {},
          'default': False},
        'epp_bai_5_legal_status': {
            '.field.ref': {},
            'source': 'epp_bai_5_legal_status_id',
            'to': '/api/v2/legalstatuses',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},

        'epp_cli_1_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'domain',
            'model': 'accounts.models.Organisation.epp_cli_1_scientific_domain.through',
            'source': 'epp_cli_1_scientific_domain',
            'bound': 'organisation',
            'fields': {
                'domain': {'.field.ref': {},
                                'source': 'domain_id',
                                'to': 'api/v2/domains'},
            }},
        'domain_names': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'epp_cli_2_scientific_subdomain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'subdomain',
            'model': 'accounts.models.Organisation.epp_cli_2_scientific_subdomain.through',
            'source': 'epp_cli_2_scientific_subdomain',
            'bound': 'organisation',
            'fields': {
                'subdomain': {'.field.ref': {},
                                'source': 'subdomain_id',
                                'to': 'api/v2/subdomains'},
            }},
        'subdomain_names': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'epp_cli_3_tags': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'affiliation_names': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'epp_loi_1_street_name_and_number': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_2_postal_code': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_3_city': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_4_region': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_loi_5_country_or_territory': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mri_1_description': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mri_2_logo': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mri_3_multimedia': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'main_contact': {
          '.field.ref': {},
          'source': 'main_contact_id',
          'to': '/api/v2/contact-information',
          '.flag.nullable.default': {}},
        'public_contact': {
          '.field.ref': {},
          'source': 'public_contact_id',
          'to': '/api/v2/contact-information',
          '.flag.nullable.default': {}},
        'epp_coi_1_first_name': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'main_contact.first_name',
          '.flag.nullable.default': {}},
        'epp_coi_2_last_name': {
          '.field.string': {},
          'source': 'main_contact.last_name',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_3_email': {
          '.field.string': {},
          'source': 'main_contact.email',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_4_phone': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'main_contact.phone',
          '.flag.nullable.default': {}},
        'epp_coi_5_position': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'main_contact.position',
          '.flag.nullable.default': {}},
        'epp_coi_6_first_name': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.first_name',
          '.flag.nullable.default': {}},
        'epp_coi_7_last_name': {
          '.field.string': {},
          'source': 'public_contact.last_name',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_8_email': {
          '.field.string': {},
          'source': 'public_contact.email',
          '.flag.nowrite': {},
          '.flag.nullable.default': {}},
        'epp_coi_9_phone': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.phone',
          '.flag.nullable.default': {}},
        'epp_coi_10_position': {
          '.field.string': {},
          '.flag.nowrite': {},
          'source': 'public_contact.position',
          '.flag.nullable.default': {}},
        'epp_mti_1_life_cycle_status': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },
        'epp_mti_2_certifications': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'epp_oth_1_hosting_legal_entity': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'epp_oth_2_participating_countries': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },

        'epp_oth_3_affiliations': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'affiliation',
            'model': 'accounts.models.Organisation.epp_oth_3_affiliations.through',
            'source': 'epp_oth_3_affiliations',
            'bound': 'organisation',
            'fields': {
                'affiliation': {'.field.ref': {},
                                'source': 'affiliation_id',
                                'to': 'api/v2/affiliations'},
            }},
        'affiliation_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_4_networks': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'network',
            'model': 'accounts.models.Organisation.epp_oth_4_networks.through',
            'source': 'epp_oth_4_networks',
            'bound': 'organisation',
            'fields': {
                'network': {'.field.ref': {},
                                'source': 'network_id',
                                'to': 'api/v2/networks'},
            }},
        'network_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_5_structure_type': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'structure',
            'model': 'accounts.models.Organisation.epp_oth_5_structure_type.through',
            'source': 'epp_oth_5_structure_type',
            'bound': 'organisation',
            'fields': {
                'structure': {'.field.ref': {},
                                'source': 'structure_id',
                                'to': 'api/v2/structures'},
            }},
        'structure_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_6_esfri_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'esfridomain',
            'model': 'accounts.models.Organisation.epp_oth_6_esfri_domain.through',
            'source': 'epp_oth_6_esfri_domain',
            'bound': 'organisation',
            'fields': {
                'esfridomain': {'.field.ref': {},
                                'source': 'esfridomain_id',
                                'to': 'api/v2/esfridomains'},
            }},
        'esfridomain_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_7_esfri_type': {
            '.field.ref': {},
            'source': 'epp_oth_7_esfri_type_id',
            'to': '/api/v2/esfritypes',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},

        'epp_oth_8_meril_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'merildomain',
            'model': 'accounts.models.Organisation.epp_oth_8_meril_scientific_domain.through',
            'source': 'epp_oth_8_meril_scientific_domain',
            'bound': 'organisation',
            'fields': {
                'merildomain': {'.field.ref': {},
                                'source': 'merildomain_id',
                                'to': 'api/v2/merildomains'},
            }},
        'merildomain_names': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'epp_oth_9_meril_scientific_subdomain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'merilsubdomain',
            'model': 'accounts.models.Organisation.epp_oth_9_meril_scientific_subdomain.through',
            'source': 'epp_oth_9_meril_scientific_subdomain',
            'bound': 'organisation',
            'fields': {
                'merilsubdomain': {'.field.ref': {},
                                'source': 'merilsubdomain_id',
                                'to': 'api/v2/merilsubdomains'},
            }},
        'merilsubdomain_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_10_areas_of_activity': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'activity',
            'model': 'accounts.models.Organisation.epp_oth_10_areas_of_activity.through',
            'source': 'epp_oth_10_areas_of_activity',
            'bound': 'organisation',
            'fields': {
                'activity': {'.field.ref': {},
                                'source': 'activity_id',
                                'to': 'api/v2/activities'},
            }},
        'activity_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_11_societal_grand_challenges': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'challenge',
            'model': 'accounts.models.Organisation.epp_oth_11_societal_grand_challenges.through',
            'source': 'epp_oth_11_societal_grand_challenges',
            'bound': 'organisation',
            'fields': {
                'challenge': {'.field.ref': {},
                                'source': 'challenge_id',
                                'to': 'api/v2/challenges'},
            }},
        'challenge_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'epp_oth_12_national_roadmaps': {
          '.field.string': {},
          '.flag.nullable.default': {},
        },



    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


MY_ORGANISATIONS = {
    '.collection.django': {},
    'model': 'service.models.Organisation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.searchable': {},
            '.flag.orderable': {}},
    },
    ':permissions_namespace': 'agora.checks.Organisation',
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
    },
}

ACCESS_POLICIES = {
    '.collection.django': {},
    'model': 'service.models.AccessPolicy',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'access_mode': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'payment_model': {
            '.field.string': {},
            '.flag.nullable.default': {}},
       'pricing': {
            '.field.string': {},
            '.flag.nullable.default': {}},
       'conditions': {
            '.field.string': {},
            '.flag.nullable.default': {}},
       'geo_availability': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
       'access_policy_url': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


FEDERATION_MEMBERS = {
    '.collection.django': {},
    'model': 'service.models.FederationMember',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'webpage': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'logo': {
            '.field.file': {},
            'default': ''},
        'country': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

TARGET_USERS = {
    '.collection.django': {},
    'model': 'service.models.TargetUser',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'user': {
            '.field.string': {},
            '.flag.filterable': {},
            '.flag.orderable': {}},
        'description': {
            '.field.string': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}


CONTACT_INFORMATION = {
    '.collection.django': {},
    'model': 'owner.models.ContactInformation',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'first_name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'last_name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'email': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'phone': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'position': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'organisation': {
            '.field.ref': {},
            'source': 'organisation_id',
            'to': '/api/v2/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
    },
}

RESOURCES = {
    '.collection.django': {},
    'model': 'service.models.Resource',
    ':permissions_namespace': 'agora.checks.Resource',
    'fields': {
        'id': {
            '.field.uuid': {},
            '.flag.nowrite': {}},
        'erp_bai_0_id': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'erp_bai_1_name': {
            '.field.string': {},
            '.flag.orderable': {},
            '.flag.searchable': {}},
        'erp_bai_2_service_organisation': {
            '.field.ref': {},
            'source': 'erp_bai_2_organisation_id',
            'to': '/api/v2/providers',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_bai_4_webpage': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_bai_3_service_providers': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'organisation',
            'model': 'service.models.Resource.erp_bai_3_providers.through',
            'source': 'erp_bai_3_providers',
            'bound': 'resource',
            'fields': {
                'organisation': {'.field.ref': {},
                                'source': 'organisation_id',
                                'to': 'api/v2/providers'},
            }},
        'providers_names': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_mri_1_description': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_mri_2_tagline': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_mri_3_logo': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mri_4_mulitimedia': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_cli_5_target_users': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'target_user',
            'model': 'service.models.Resource.erp_cli_5_target_users.through',
            'source': 'erp_cli_5_target_users',
            'bound': 'resource',
            'fields': {
                'target_user': {'.field.ref': {},
                                'source': 'targetuser_id',
                                'to': 'api/v2/target-users'},
            }},
        'erp_cli_5_target_users_verbose': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_mri_5_use_cases': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
        'erp_cli_1_scientific_domain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'domain',
            'model': 'service.models.Resource.erp_cli_1_scientific_domain.through',
            'source': 'erp_cli_1_scientific_domain',
            'bound': 'resource',
            'fields': {
                'domain': {'.field.ref': {},
                                'source': 'domain_id',
                                'to': 'api/v2/domains'},
            }},
        'domain_names': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_cli_2_scientific_subdomain': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'subdomain',
            'model': 'service.models.Resource.erp_cli_2_scientific_subdomain.through',
            'source': 'erp_cli_2_scientific_subdomain',
            'bound': 'resource',
            'fields': {
                'subdomain': {'.field.ref': {},
                                'source': 'subdomain_id',
                                'to': 'api/v2/subdomains'},
            }},
        'subdomain_names': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_cli_3_category': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'category',
            'model': 'service.models.Resource.erp_cli_3_category.through',
            'source': 'erp_cli_3_category',
            'bound': 'resource',
            'fields': {
                'category': {'.field.ref': {},
                                'source': 'category_id',
                                'to': 'api/v2/categories'},
            }},
        'category_names': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'erp_cli_4_subcategory': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'subcategory',
            'model': 'service.models.Resource.erp_cli_4_subcategory.through',
            'source': 'erp_cli_4_subcategory',
            'bound': 'resource',
            'fields': {
                'subcategory': {'.field.ref': {},
                                'source': 'subcategory_id',
                                'to': 'api/v2/subcategories'},
            }},
        'subcategory_names': {
            '.field.string': {},
            '.flag.nowrite': {}},

        'erp_cli_6_access_type': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'access_type',
            'model': 'service.models.Resource.erp_cli_6_access_type.through',
            'source': 'erp_cli_6_access_type',
            'bound': 'resource',
            'fields': {
                'access_type': {'.field.ref': {},
                                'source': 'accesstype_id',
                                'to': 'api/v2/access-types'},
            }
        },
        'erp_cli_7_access_mode': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'access_mode',
            'model': 'service.models.Resource.erp_cli_7_access_mode.through',
            'source': 'erp_cli_7_access_mode',
            'bound': 'resource',
            'fields': {
                'access_mode': {'.field.ref': {},
                                'source': 'accessmode_id',
                                'to': 'api/v2/access-modes'},
            }
        },
        'erp_cli_8_tags': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},

        'erp_mgi_1_helpdesk_webpage': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_2_user_manual': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_3_terms_of_use': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_4_privacy_policy': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_5_access_policy': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_6_sla_specification': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_7_training_information': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_8_status_monitoring': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mgi_9_maintenance': {
          '.field.string': {},
          '.flag.nullable.default': {}},

        'erp_gla_1_geographical_availability': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_gla_2_language': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_rli_1_geographic_location': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'main_contact': {
            '.field.ref': {},
            'source': 'main_contact_id',
            'to': '/api/v2/contact-information',
            '.flag.nullable.default': {}},
        'public_contact': {
            '.field.ref': {},
            'source': 'public_contact_id',
            'to': '/api/v2/contact-information',
            '.flag.nullable.default': {}},
        'erp_coi_1_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.first_name',
            '.flag.nullable.default': {}},
        'erp_coi_2_last_name': {
            '.field.string': {},
            'source': 'main_contact.last_name',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_3_email': {
            '.field.string': {},
            'source': 'main_contact.email',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_4_phone': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.phone',
            '.flag.nullable.default': {}},
        'erp_coi_5_position': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.position',
            '.flag.nullable.default': {}},
        'erp_coi_6_organisation': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'main_contact.organisation.epp_bai_1_name',
            '.flag.nullable.default': {}},

        'erp_coi_7_first_name': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.first_name',
            '.flag.nullable.default': {}},
        'erp_coi_8_last_name': {
            '.field.string': {},
            'source': 'public_contact.last_name',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_9_email': {
            '.field.string': {},
            'source': 'public_contact.email',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_coi_10_phone': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.phone',
            '.flag.nullable.default': {}},
        'erp_coi_11_position': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.position',
            '.flag.nullable.default': {}},
        'erp_coi_12_organisation': {
            '.field.string': {},
            '.flag.nowrite': {},
            'source': 'public_contact.organisation.epp_bai_1_name',
            '.flag.nullable.default': {}},
        'erp_coi_13_helpdesk_email': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_coi_14_security_contact_email': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_mti_1_technology_readiness_level': {
            '.field.ref': {},
            'source': 'erp_mti_1_technology_readiness_level_id',
            'to': '/api/v2/trls',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_mti_2_life_cycle_status': {
            '.field.ref': {},
            'source': 'erp_mti_2_life_cycle_status_id',
            'to': '/api/v2/resource-lifecycle-statuses',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_mti_3_certifications': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_4_standards': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_5_open_source_technologies': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_6_version': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_7_last_update': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_mti_8_changelog': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_aoi_1_order_type': {
            '.field.ref': {},
            'source': 'erp_aoi_1_order_type_id',
            'to': '/api/v2/order-types',
            '.flag.filterable': {},
            '.flag.nullable.default': {}},
        'erp_aoi_2_order': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_fni_1_payment_model': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'erp_fni_2_pricing': {
          '.field.string': {},
          '.flag.nullable.default': {}},
        'resource_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'pending_resource_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {}},
        'rejected_resource_admins_ids': {
            '.field.string': {},
            '.flag.nowrite': {}},


        'adminships': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            '.flag.filterable': {},
            'model': 'service.models.ResourceAdminship',
            'source': 'resourceadminships',
            'bound': 'resource',
            'fields': {
                'id': {
                    '.field.serial': {}},
                'user_id': {
                    '.field.integer': {},
                    '.flag.nowrite': {},
                    '.flag.filterable': {},
                    'source': 'admin.pk'},
            }
        },
        'required_resources': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'resource',
            'model': 'service.models.Resource.required_resources.through',
            'source': 'required_resources',
            'bound': 'from_resource',
            'fields': {
                'resource': {'.field.ref': {},
                            'source': 'to_resource_id',
                            'to': 'api/v2/resources'},
            },
        },
        'related_resources': {
            '.field.collection.django': {},
            '.flag.nullable.default': {},
            ':filter_compat': True,
            'flat': True,
            'id_field': 'resource',
            'model': 'service.models.Resource.related_resources.through',
            'source': 'related_resources',
            'bound': 'from_resource',
            'fields': {
                'resource': {'.field.ref': {},
                            'source': 'to_resource_id',
                            'to': 'api/v2/resources'},
            },
        },
        'erp_dei_1_required_resources': {
            '.field.string': {},
            'source': 'required_resources_ids',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_dei_2_related_resources': {
            '.field.string': {},
            'source': 'related_resources_ids',
            '.flag.nowrite': {},
            '.flag.nullable.default': {}},
        'erp_dei_3_related_platforms': {
            '.field.string': {},
            '.flag.nullable.default': {}},
        'erp_ati_1_funding_body': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'funding_body',
            'model': 'service.models.Resource.erp_ati_1_funding_body.through',
            'source': 'erp_ati_1_funding_body',
            'bound': 'resource',
            'fields': {
                'funding_body': {'.field.ref': {},
                                'source': 'fundingbody_id',
                                'to': 'api/v2/funding-bodies'},
            }
        },
        'erp_ati_2_funding_program': {
            '.field.collection.django': {},
            ':filter_compat': True,
            '.flag.nullable.default': {},
            'flat': True,
            'id_field': 'funding_program',
            'model': 'service.models.Resource.erp_ati_2_funding_program.through',
            'source': 'erp_ati_2_funding_program',
            'bound': 'resource',
            'fields': {
                'funding_program': {'.field.ref': {},
                                'source': 'fundingprogram_id',
                                'to': 'api/v2/funding-programs'},
            }
        },
        'erp_ati_3_grant_project_name': {
            '.field.string': {},
            '.flag.searchable': {},
            '.flag.nullable.default': {}},
    },
    'actions': {
        '.action-template.django.list': {},
        '.action-template.django.retrieve': {},
        '.action-template.django.create': {},
        '.action-template.django.delete': {},
        '.action-template.django.update': {},
        '.action-template.django.partial_update': {},
        'create': {
            'processors': {
                'custom_post_create': {
                    '.processor': {},
                    'module_path': 'service.models.PostCreateResource',
                    'read_keys': {'=': (
                        'backend/raw_response',
                        'auth/user',
                    )},
                    'write_keys': {'=': (
                        'backend/raw_response',
                    )},
                },
            },
        },
    },
}

APP_CONFIG = {
    '.apimas_app': {},
    ':permission_rules': 'agora.permissions.get_rules',
    ':authenticator': 'apimas.auth.DjoserAuthentication',
    ':verifier': 'agora.utils.djoser_verifier',
    ':user_resolver': 'agora.utils.userid_extractor',
    ':permissions_namespace': 'agora.checks',
    ':filter_compat': True,
    ':ordering_compat': True,

    'endpoints': {
        'api': {
            'prefix': 'api/v2',
            'collections': {
                'resource-admins': RESOURCE_ADMINS,
                'custom-users': CUSTOM_USERS,
                'providers': ORGANISATIONS,
                'resources': RESOURCES,
                'target-users': TARGET_USERS,
                'contact-information': CONTACT_INFORMATION,
                'legalstatuses': LEGAL_STATUSES,
                'affiliations': AFFILIATIONS,
                'networks': NETWORKS,
                'structures': STRUCTURES,
                'esfridomains': ESFRI_DOMAINS,
                'esfritypes': ESFRI_TYPES,
                'activities': ACTIVITIES,
                'order-types': ORDER_TYPES,
                'challenges': CHALLENGES,
                'domains': DOMAINS,
                'subdomains': SUBDOMAINS,
                'supercategories': SUPERCATEGORIES,
                'categories': CATEGORIES,
                'subcategories': SUBCATEGORIES,
                'funding-programs': FUNDING_PROGRAMS,
                'funding-bodies': FUNDING_BODIES,
                'access-types': ACCESS_TYPES,
                'access-modes': ACCESS_MODES,
                'trls': TRLS,
                'resource-lifecycle-statuses': RESOURCE_LIFECYCLE_STATUSES,
                'merildomains': MERIL_DOMAINS,
                'merilsubdomains': MERIL_SUBDOMAINS,
            },
        },
    },
}
