from strings import *

ERROR_MESSAGES = {
    OWNER_NOT_FOUND: "The requested service owner was not found",
    SERVICE_NOT_FOUND: "The requested service was not found",
    INVALID_UUID: "An invalid UUID was supplied",
    SERVICE_COMPONENTS_IMPLEMENTATION_NONMATCHING_UUID: "A service component matching the specified service version does not exists",
    SERVICE_COMPONENT_INVALID_UUID: "An invalid service component UUID was supplied",
    SERVICE_DETAILS_NOT_FOUND: "The requested service details were not found",
    SERVICE_COMPONENT_NO_IMPLEMENTATIONS: "There are no implementations for the specified service component",
    SERVICE_COMPONENT_NOT_FOUND: "The requested service component was not found",
    SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID: "An invalid service component implementation UUID was supplied",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND: "The requested service component implementation details do not exist",
    SLA_INVALID_UUID: "An invalid service sla UUID was supplied",
    SLA_NOT_FOUND: "The requested SLA object was not found",
    SLA_SERVICE_DETAILS_MISMATCH: "This SLA object does not belong to the specified service and service details",
    SLA_PARAMETER_INVALID_UUID: "An invalid service sla parameter UUID was supplied",
    SLA_PARAMETER_NOT_FOUND: "The requested SLA parameter does not belong to the specified service",
    SERVICE_DETAILS_OPTIONS_NOT_FOUND: "This service has no service options for the current version",
    PAGE_NOT_FOUND: "The requested page was not found",
    INVALID_QUERY_PARAMETER: "The query parameter is invalid",
    SERVICE_COMPONENT_NAME_NOT_PROVIDED: "Service component name not provided",
    SERVICE_COMPONENT_NAME_EMPTY: "The provided service component name is empty",
    SERVICE_COMPONENT_DESCRIPTION_NOT_PROVIDED: "Service component description not provided",
    SERVICE_COMPONENT_IMPLEMENTATION_NAME_NOT_PROVIDED: "Service component implementation name not provided",
    SERVICE_COMPONENT_IMPLEMENTATION_NAME_EMPTY: "The provided service component implementation name is empty",
    SERVICE_COMPONENT_IMPLEMENTATION_DESCRIPTION_NOT_PROVIDED: "Service component implementation description not provided",
    SERVICE_COMPONENT_UUID_EXISTS: "A service component object with the provided UUID already exists",
    SERVICE_COMPONENT_IMPLEMENTATION_UUID_EXISTS: "A service component implementation object with the provided UUID already exists",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_NOT_PROVIDED: "Service component implementation details version not provided",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_CONFIGURATION_PARAMETERS_NOT_PROVIDED: "Service component implementation details configuration parameters not provided",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_EMPTY: "The provided service component implementation detail version is empty",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID: "An invalid service component implementation details UUID was supplied",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_EXISTS: "A service component implementation details object with the provided UUID already exists",
    SERVICE_COMPONENT_IMPLEMENTATION_NOT_FOUND: "The requested service component implementation was not found",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED: "Service component implementation details UUID not provided",
    SERVICE_DETAILS_COMPONENT_EXISTS: "The provided service component implementation details already is associated with the provided service details",
    EXTERNAL_SERVICE_NAME_NOT_PROVIDED: "External service name not provided",
    EXTERNAL_SERVICE_NAME_EMPTY: "The provided external service name is empty",
    EXTERNAL_SERVICE_INVALID_UUID: "An invalid external service UUID was supplied",
    EXTERNAL_SERVICE_UUID_EXISTS: "An external service object with the provided UUID already exists",
    SERVICE_DEPENDENCY_UUID_NOT_PROVIDED: "Service dependency UUID not provided",
    SERVICE_DEPENDENCY_INVALID_UUID: "An invalid service dependency UUID was supplied",
    SERVICE_DEPENDENCY_NOT_FOUND: "No service found with the provided UUID for service dependency",
    SERVICE_DEPENDENCY_EXISTS: "The service already has the provided service dependency",
    EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED: "External service dependency UUID not provided",
    EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID: "An invalid external service dependency UUID was supplied",
    EXTERNAL_SERVICE_DEPENDENCY_NOT_FOUND: "The requested external service was not found",
    EXTERNAL_SERVICE_DEPENDENCY_EXISTS: "The service already has the provided service dependency",
    USER_CUSTOMER_NAME_NOT_PROVIDED: "User customer name not provided",
    USER_CUSTOMER_ROLE_EMPTY: "The provided user customer role is empty",
    USER_CUSTOMER_ROLE_NOT_PROVIDED: "User customer role not provided",
    USER_CUSTOMER_NAME_INVALID: "The provided user customer name is invalid",
    USER_CUSTOMER_INVALID_UUID: "An invalid user customer UUID was supplied",
    USER_CUSTOMER_EXISTS: "A user customer object with the provided UUID already exists",
    SERVICE_NAME_NOT_PROVIDED: "Service name not provided",
    SERVICE_OWNER_UUID_NOT_PROVIDED: "Service owner UUID not provided",
    SERVICE_CONTACT_INFORMATION_UUID_NOT_PROVIDED: "Service contact information UUID not provided",
    SERVICE_NAME_EMPTY: "The provided service name is empty",
    SERVICE_OWNER_INVALID_UUID: "An invalid service owner UUID was supplied",
    SERVICE_CONTACT_INFORMATION_INVALID_UUID: "An invalid contact information UUID was supplied",
    SERVICE_INVALID_UUID: "An invalid service UUID was supplied",
    SERVICE_UUID_EXISTS: "A service object with the provided UUID already exists",
    SERVICE_OWNER_NOT_FOUND: "No service owner object exists with the provided UUID",
    CONTACT_INFORMATION_NOT_FOUND: "No contact information object exists with the provided UUID",
    INSTITUTION_UUID_EXISTS: "An institution object with the provided UUID already exists",
    OWNER_FIRST_NAME_EMPTY:  "The provided first name is empty",
    OWNER_LAST_NAME_EMPTY:  "The provided last name is empty",
    OWNER_EMAIL_EMPTY:  "The provided email is empty",
    OWNER_PHONE_EMPTY:  "The provided phone number is empty",
    OWNER_URL_EMPTY:  "The provided url is empty",
    CONTACT_INFORMATION_UUID_EXISTS: "A contact information object with the provided UUID already exists",
    SERVICE_OWNER_UUID_EXISTS: "A service owner with the provided UUID already exists",
    INSTITUTION_UUID_NOT_PROVIDED: "Institution UUID not provided",
    INSTITUTION_NOT_FOUND: "The requested institution was not found",
    SERVICE_OPTION_NAME_NOT_PROVIDED: "Service option name not provided",
    SERVICE_OPTION_NAME_EMPTY: "The provided service option name is empty",
    SERVICE_OPTION_UUID_EXISTS: "A service option object with the provided UUID already exists",
    SLA_NAME_NOT_PROVIDED: "SLA name not provided",
    SLA_NAME_EMPTY: "The provided SLA name is empty",
    SERVICE_OPTION_NOT_FOUND: "The requested service option was not found",
    SLA_UUID_EXISTS: "A SLA object with thr provided UUID already exists",
    SERVICE_OPTION_UUID_EMPTY: "The provided service option uuid is empty",
    PARAMETER_NAME_NOT_PROVIDED: "Parameter name not provided",
    PARAMETER_NAME_EMPTY: "The provided parameter name is empty",
    PARAMETER_UUID_EXISTS: "A Parameter object with the provided UUID already exists",
    PARAMETER_TYPE_EMPTY: "The provided parameter type is empty",
    PARAMETER_TYPE_NOT_PROVIDED: "Parameter type not provided",
    PARAMETER_UUID_NOT_PROVIDED: "Parameter UUID not provided",
    SLA_UUID_NOT_PROVIDED: "SLA UUID not provided",
    SERVICE_OPTION_UUID_NOT_PROVIDED: "Service Option UUiD not provided",
    PARAMETER_UUID_EMPTY: "The provided parameter UUID is empty",
    SLA_UUID_EMPTY: "The provided SLA UUID is empty",
    PARAMETER_NOT_FOUND: "The requested parameter was not found",
    SLA_PARAMETER_UUID_EXISTS: "A SLA Parameter object with the provided UUID already exists",
    SERVICE_UUID_EMPTY: "The provided service UUID is empty",
    SERVICE_DETAILS_UUID_EMPTY: "The provided service details UUID is empty",
    SERVICE_DETAILS_OPTION_EXISTS: "A Service Details Option object with the provided UUID already exits",
    SERVICE_UUID_NOT_PROVIDED: "Service UUID not provided",
    SERVICE_DETAILS_UUID_NOT_PROVIDED: "Service Details UUID not provided",
    SERVICE_DETAILS_EXISTS: "A Service Details object with the provided UUID already exists",
    SERVICE_DETAILS_VERSION_NOT_PROVIDED: "Service Details version not provided",
    SERVICE_COMPONENT_UUID_NOT_PROVIDED: "Service component UUID not provided",
    SERVICE_COMPONENT_IMPLEMENTATION_UUID_NOT_PROVIDED: "Service component implementation UUID not provided",
    SLA_PARAMETER_EXISTS: "A SLA Parameter object with the provided information already exists",
    SERVICE_OPTION_EXISTS: "A Service Option with the provided information already exists",
    VARIABLE_MUST_BE_BOOLEAN: "The provided variable must be boolean: ",
    SLA_PARAMETER_UUID_NOT_PROVIDED: "SLA parameter UUID not provided",
    EXTERNAL_SERVICE_NOT_FOUND: "The requested external service was not found",
    EXTERNAL_SERVICE_UUID_NOT_PROVIDED: "External service UUID not provided",
    USER_CUSTOMER_NOT_FOUND: "The requested user customer was not found",
    USER_CUSTOMER_UUID_NOT_PROVIDED: "User customer UUID not provided",
    INSTITUTION_NAME_NOT_PROVIDED: "Institution name not provided",
    INSTITUTION_NAME_EMPTY: "The provided institution name is empty",
    SERVICE_DETAILS_VERSION_EMPTY: "The provided service details version is empty",
    NEW_SERVICE_UUID_NOT_PROVIDED: "New service UUID not provided",
    NEW_SERVICE_DETAILS_UUID_NOT_PROVIDED: "New service details UUID not provided",
    NEW_SERVICE_OPTION_UUID_NOT_PROVIDED: "New service option UUID not provided",
    NEW_SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED: "New service component implementation details UUID not provided",
    NEW_SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID: "The provided new service component implementation details UUID is invalid",
    NEW_SERVICE_DETAILS_VERSION_NOT_PROVIDED: "New service details version not provided",
    NEW_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED: "New service dependency UUID not provided",
    NEW_SERVICE_DEPENDENCY_INVALID_UUID: "The provided new service dependency UUID is invalid",
    NEW_EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED: "New external service dependency UUID not provided",
    NEW_EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID: "The provided new external service dependency UUID is invalid",
    SERVICE_DETAILS_COMPONENT_NOT_FOUND: "The provided service details are not associated to the provided service component implementation details",
    SERVICE_DETAILS_OPTIONS_EXISTS: "The provided service details are already associated with the provided service options",
    OPERATION_NOT_PERMITTED: "You do not have permissions to perform this task",
    OWNER_URL_OR_EMAIL_NOT_PROVIDED: "Email or url parameter not provided",
    SERVICE_OWNER_EMAIL_NOT_PROVIDED: "Service Owner email not provided"
}


INFO_MESSAGES = {
    SERVICE_OWNER_INSTITUTION: "service owner institution information",
    SERVICE_OWNER_INFORMATION: "service owner information",
    SERVICE_COMPONENTS_INFORMATION: "service components information",
    SERVICE_COMPONENT_IMPLEMENTATIONS_INFORMATION: "service component implementation information",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS: "service component implementation detail",
    SLA_INFORMATION: "service SLA information",
    SLA_PARAMETER_INFORMATION: "service SLA parameter information",
    SERVICE_OPTIONS: "options for service detail information",
    SERVICE_LIST: "list of services",
    SERVICE_INFORMATION: "service information",
    SERVICE_DETAIL_INFORMATION: "service details information",
    SERVICE_DEPENDENCIES_INFORMATION: "service dependencies information",
    SERVICE_EXTERNAL_DEPENDENCIES_INFORMATION: "service external dependencies information",
    SERVICE_COMPONENT_INSERTED: "service component inserted",
    SERVICE_COMPONENT_IMPLEMENTATION_INSERTED: "service component implementation inserted",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_INSERTED: "service component implementation details inserted",
    SERVICE_DETAILS_COMPONENT_INSERTED: "relationship between the provided service component implementation details and service details inserted",
    EXTERNAL_SERVICE_INSERTED: "external service inserted",
    SERVICE_DEPENDENCY_INSERTED: "service dependency inserted",
    EXTERNAL_SERVICE_DEPENDENCY_INSERTED: "external service dependency inserted",
    USER_CUSTOMER_INSERTED: "user customer inserted",
    SERVICE_INSERTED: "service inserted",
    INSTITUTION_INSERTED: "institution inserted",
    CONTACT_INFORMATION_INSERTED: "contact information inserted",
    SERVICE_OWNER_INSERTED: "service owner inserted",
    SERVICE_OPTION_INSERTED: "service option inserted",
    SLA_INSERTED: "SLA inserted",
    PARAMETER_INSERTED: "parameter inserted",
    SLA_PARAMETER_INSERTED: "sla parameter inserted",
    SERVICE_DETAILS_OPTION_INSERTED: "service details option inserted",
    SERVICE_DETAILS_INSERTED: "service details inserted",
    SERVICE_OWNER_UPDATED: "service owner updated",
    INSTITUTION_UPDATED: "institution updated",
    CONTACT_INFORMATION_UPDATED: "contact information updated",
    SERVICE_OPTION_UPDATED: "service option updated",
    SLA_UPDATED: "SLA updated",
    PARAMETER_UPDATED: "parameter updated",
    SLA_PARAMETER_UPDATED: "SLA parameter updated",
    SERVICE_DETAILS_OPTION_UPDATED: "service details options updated",
    SERVICE_COMPONENT_UPDATED: "service component updated",
    SERVICE_COMPONENT_IMPLEMENTATION_UPDATED: "service component implementation updated",
    SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UPDATED: "service component implementation details updated",
    SERVICE_UPDATED: "Service updated",
    EXTERNAL_SERVICE_UPDATED: "External service updated",
    SERVICE_DETAILS_UPDATED: "Service details updated",
    USER_CUSTOMER_UPDATED: "User customer updated",
    SERVICE_DETAILS_COMPONENT_UPDATED: "Service details component updated",
    SERVICE_DEPENDENCY_UPDATED: "Service dependency updated"
}

STATUS_CODES = {
    OK_200: "200 OK",
    NOT_FOUND_404: "404 Not Found",
    NO_CONTENT_204: "204 No Content",
    CREATED_201: "201 Created",
    FORBIDDEN_403: "403 Forbidden",
    REJECTED_406: "406 Not Acceptable",
    CONFLICT_409: "409 Conflict",
    UPDATED_202: "202 Updated"
}
