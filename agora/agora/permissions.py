# COLUMNS = ('collection', 'action', 'role', 'filter', 'check' 'fields', 'comment')
def get_rules():
    rules = [

        ('api/v2/custom-users', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'retrieve', 'serviceadmin', 'me', '*', '*', '*'),
        ('api/v2/custom-users', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/custom-users', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/resource-admins', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-admins', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/resource-admins', 'list', 'serviceadmin', 'manages_or_self_pending', '*', '*', '*'),
        ('api/v2/resource-admins', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-admins', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/resource-admins', 'retrieve', 'serviceadmin', '*', 'is_involved', '*', '*'),
        ('api/v2/resource-admins', 'create', 'superadmin', '*', 'check_create_other', 'resource,admin', '*'),
        ('api/v2/resource-admins', 'create', 'admin', '*', 'check_create_other', 'resource,admin', '*'),
        ('api/v2/resource-admins', 'create', 'serviceadmin', '*', 'check_create_self', 'resource', '*'),
        ('api/v2/resource-admins', 'partial_update', 'superadmin', '*', 'check_update', 'state', '*'),
        ('api/v2/resource-admins', 'partial_update', 'admin', '*', 'check_update', 'state', '*'),
        ('api/v2/resource-admins', 'partial_update', 'serviceadmin', 'manages', 'check_update', 'state', '*'),
        ('api/v2/resource-admins', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-admins', 'delete', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-admins', 'destroy', 'serviceadmin', '*', 'self_pending', '*', '*'),
        ('api/v2/resource-admins', 'delete', 'serviceadmin', '*', 'self_pending', '*', '*'),

        ('api/v2/contact-information', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/contact-information', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/providers', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/providers', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/providers', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/providers', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/providers', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/providers', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/providers', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/providers', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/providers', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/my-providers', 'list', 'serviceadmin', 'filter_belongs', '*', '*', '*'),
        ('api/v2/my-providers', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),

        ('api/v2/resources', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resources', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/resources', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/resources', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/resources', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resources', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/resources', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/resources', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/resources', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resources', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/resources', 'create', 'serviceadmin', '*', 'organisation_owned', '*', '*'),
        ('api/v2/resources', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resources', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/resources', 'update', 'serviceadmin', '*', 'owned', '*', '*'),
        ('api/v2/resources', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resources', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/resources', 'partial_update', 'serviceadmin', '*', 'owned', '*', '*'),
        ('api/v2/resources', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resources', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/target-users', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/target-users', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/target-users', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/target-users', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/affiliations', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/affiliations', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/networks', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/networks', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/networks', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/networks', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/networks', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/networks', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/networks', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/networks', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/networks', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/networks', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/networks', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/networks', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/networks', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/networks', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/networks', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/networks', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/legalstatuses', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/legalstatuses', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/structures', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/structures', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/structures', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/structures', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/structures', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/structures', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/structures', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/structures', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/structures', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/structures', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/structures', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/structures', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/structures', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/structures', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/structures', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/structures', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/esfridomains', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfridomains', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/esfritypes', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/esfritypes', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/activities', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/activities', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/activities', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/activities', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/activities', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/activities', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/activities', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/activities', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/activities', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/activities', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/activities', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/activities', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/activities', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/activities', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/activities', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/activities', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/order-types', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/order-types', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/order-types', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/order-types', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/access-types', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/access-types', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/access-types', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-types', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/access-modes', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/access-modes', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/trls', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/trls', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/trls', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/trls', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/trls', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/trls', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/trls', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/trls', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/trls', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/trls', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/trls', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/trls', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/trls', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/trls', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/trls', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/trls', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/resource-lifecycle-statuses', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/resource-lifecycle-statuses', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/funding-bodies', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-bodies', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/funding-programs', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/funding-programs', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/challenges', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/challenges', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/challenges', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/challenges', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/domains', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/domains', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/domains', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/domains', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/domains', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/domains', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/domains', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/domains', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/domains', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/domains', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/domains', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/domains', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/domains', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/domains', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/domains', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/domains', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/subdomains', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subdomains', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/supercategories', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/supercategories', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/subcategories', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/subcategories', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/categories', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/categories', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/categories', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/categories', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/categories', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/categories', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/categories', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/categories', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/categories', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/categories', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/categories', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/categories', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/categories', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/categories', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/categories', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/categories', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/merildomains', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merildomains', 'delete', 'superadmin', '*', '*', '*', '*'),

        ('api/v2/merilsubdomains', 'list', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'list', 'admin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'list', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'list', 'observer', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'retrieve', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'retrieve', 'admin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'retrieve', 'serviceadmin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'retrieve', 'observer', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'create', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'create', 'admin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'update', 'admin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'partial_update', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'partial_update', 'admin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'destroy', 'superadmin', '*', '*', '*', '*'),
        ('api/v2/merilsubdomains', 'delete', 'superadmin', '*', '*', '*', '*'),


    ]
    return rules
