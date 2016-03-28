

# Error codes
OWNER_NOT_FOUND = 1
SERVICE_NOT_FOUND = 2
INVALID_UUID = 3
SERVICE_COMPONENTS_IMPLEMENTATION_NONMATCHING_UUID = 4
SERVICE_COMPONENT_INVALID_UUID = 5
SERVICE_DETAILS_NOT_FOUND = 6
SERVICE_COMPONENT_NO_IMPLEMENTATIONS = 7
SERVICE_COMPONENT_NOT_FOUND = 8
SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID = 9
SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND = 10
SLA_INVALID_UUID = 11
SLA_NOT_FOUND = 12
SLA_SERVICE_DETAILS_MISMATCH = 13
SLA_PARAMETER_INVALID_UUID = 14
SERVICE_DETAILS_OPTIONS_NOT_FOUND = 15
PAGE_NOT_FOUND = 16
SLA_PARAMETER_NOT_FOUND = 17
INVALID_QUERY_PARAMETER = 18
SERVICE_COMPONENT_NAME_NOT_PROVIDED = 19
SERVICE_COMPONENT_NAME_EMPTY = 20
SERVICE_COMPONENT_DESCRIPTION_NOT_PROVIDED = 21
SERVICE_COMPONENT_UUID_EXISTS = 22
SERVICE_COMPONENT_IMPLEMENTATION_NAME_NOT_PROVIDED = 23
SERVICE_COMPONENT_IMPLEMENTATION_NAME_EMPTY = 24
SERVICE_COMPONENT_IMPLEMENTATION_DESCRIPTION_NOT_PROVIDED = 25
SERVICE_COMPONENT_IMPLEMENTATION_UUID_EXISTS = 26
SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_NOT_PROVIDED = 27
SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_CONFIGURATION_PARAMETERS_NOT_PROVIDED = 28
SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_EMPTY = 29
SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID = 30
SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_EXISTS = 31
SERVICE_COMPONENT_IMPLEMENTATION_NOT_FOUND = 32

# Info codes
SERVICE_OWNER_INSTITUTION = 1
SERVICE_OWNER_INFORMATION = 2
SERVICE_COMPONENTS_INFORMATION = 3
SERVICE_COMPONENT_IMPLEMENTATIONS_INFORMATION = 4
SERVICE_COMPONENT_IMPLEMENTATION_DETAILS = 5
SLA_INFORMATION = 6
SLA_PARAMETER_INFORMATION = 7
SERVICE_OPTIONS = 8
SERVICE_LIST = 9
SERVICE_INFORMATION = 10
SERVICE_DETAIL_INFORMATION = 11
SERVICE_DEPENDENCIES_INFORMATION = 12
SERVICE_EXTERNAL_DEPENDENCIES_INFORMATION = 13
SERVICE_COMPONENT_INSERTED = 14
SERVICE_COMPONENT_IMPLEMENTATION_INSERTED = 15
SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_INSERTED = 16

# Status codes
OK_200 = 0
NOT_FOUND_404 = 1
NO_CONTENT_204 = 2
CREATED_201 = 3
FORBIDDEN_403 = 4
REJECTED_405 = 5
CONFLICT_409 = 6