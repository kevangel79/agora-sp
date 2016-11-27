var formName = 'Service Form';

var opType;
var serviceOwnerId;
var internalContactInformationId;
var externalContactInformationId;

var globalOwnerData;
var globalInternalContactData;
var globalExternalContactData;

var optionsOwnerData = [
  {id: 1, value: -1, text: "Select service owner"}
];

var optionsInternalContactData = [
  {id: 1, value: -1, text: "Select internal contact information"}
];

var optionsExternalContactData = [
  {id: 1, value: -1, text: "Select external contact information"}
];

var optionsArea = [
  {id: 1, value: -1, text: "Select service area"}
];

var optionsType = [
  {id: 1, value: -1, text: "Select service type"}
];

var resourceObject = [
	{ tag: 'input', type: 'text', name: 'name', placeholder: 'Enter name', label: 'Name', required: true },
	{ tag: 'textarea', type: 'textarea', name: 'description_external', placeholder: "Enter external description", label: 'External Description', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'description_internal', placeholder: "Enter internal description", label: 'Internal Description', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'select', type: 'text', name: 'service_area', placeholder: 'Enter service area', label: 'Service Area', required: true, optionsData: optionsArea },
	{ tag: 'select', type: 'text', name: 'service_type', placeholder: 'Enter service type', label: 'Service Type', required: true, optionsData: optionsType },
	{ tag: 'textarea', type: 'textarea', name: 'request_procedures', placeholder: "Enter request procedures", label: 'Request Procedures', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'funders_for_service', placeholder: "Enter funders for service", label: 'Funders for Service', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'value_to_customer', placeholder: "Enter value to customer", label: 'Value to customer', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'risks', placeholder: "Enter risks", label: 'Risks', required: true, onChange: 'textareaHTMLValidation' },
	{ tag: 'textarea', type: 'textarea', name: 'competitors', placeholder: "Enter competitors", label: 'Competitors', required: true, onChange: 'textareaHTMLValidation' },
	// todo: how to fill the data for the options (should be done before rendering)
	{ tag: 'select', type: 'text', name: 'service_owner', label: 'Service Owner', placeholder: "Enter service owner name", optionsData: optionsOwnerData },
	{ tag: 'select', type: 'text', name: 'contact_information_external', label: 'Contact Information External', placeholder: "Enter external contact info", optionsData: optionsExternalContactData },
	{ tag: 'select', type: 'text', name: 'contact_information_internal', label: 'Contact Information Internal', placeholder: "Enter internal contact info", optionsData: optionsInternalContactData }
];

var OptionsComponent = React.createClass({
	render: function(){
		var htmlOptions = this.props.options.map(function(option) {
      return(
      	<option value={option.value} key={option.id}>{option.text}</option>
      );
		});		
		return (
			<select name={this.props.selectName} id={this.props.selectName} className="form-control">
				{htmlOptions}
		  </select>
		);
	}
});

var FormWrapper = React.createClass({

	generateFormElements: function(resourceObject){
		var formElements = resourceObject.map(function(field, i){
			if(field.tag == 'input'){
				if(field.type == 'text'){					
					return (
						<div className="form-group" key={i}>
			      	        <label htmlFor={field.name}>{field.label}</label>			      	        
			      	        <input className="form-control" id={field.name} type={field.type} name={field.name} placeholder={field.placeholder} aria-describedby={field.name + '-error'} />
			      	        <span id={field.name + '-error'} className="validation-message sr-only"></span>
			      	    </div>
					);
				}
			}
			else if(field.tag == 'textarea'){
				return(
					<div className="form-group" key={i}>
					    <label htmlFor={field.name}>{field.label}</label>
					    <textarea className="form-control" id={field.name} placeholder={field.placeholder} name={field.name} rows="6" onChange={this[field.onChange]}></textarea>
					    <span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);				
			}
			else if(field.tag == 'select'){
				return(
					<div className="form-group" key={i}>
					    <label htmlFor={field.name}>{field.label}</label>
					    <OptionsComponent options={field.optionsData} selectName={field.name}></OptionsComponent>
					    <span id={field.name + '-error'} className="validation-message sr-only"></span>
					</div>
				);				
			}
		}, this);
		return formElements;
	},

	markInvalid: function(elRef, message){
		$('#' + elRef).next().removeClass('sr-only');
		$('#' + elRef).next().html(message);
		$('#' + elRef).parent().addClass('has-error');
		$('html, body').animate({
        scrollTop: $('#' + elRef).offset().top
    	}, 800);
	},

	clearValidations: function(){
		$('body').find('.has-error').removeClass('has-error');
		$('body').find('.validation-message').addClass('sr-only');
	},

	textareaHTMLValidation: function(e){
		var div = document.createElement('div');
		div.innerHTML = $(e.target).val();
		if($(div).find('script').length > 0 || $(div).find('link').length){
			div = null;
			this.markInvalid($(e.target).attr('name'), 'This HTML content must not have script or css tags');
		}
		else{	
			$(e.target).parent().removeClass('has-error');
			$(e.target).parent().find('.validation-message').addClass('sr-only');
		}
		div = null
	},

	validateForm: function(e){
		this.clearValidations();
		var validationObjects = [];
		var validationMessage = '';

		// --- validation code goes here ---

		if($('#name').val() == ''){
			validationMessage = "The name is required"
			validationObjects.push( { field: 'name', message: validationMessage } );
		}

		if($('#name').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'name', message: validationMessage } );			
		}

		if($('#service_area').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'service_area', message: validationMessage } );			
		}

		if($('#service_type').val().length > 255){
			validationMessage = "Content exceeds max length of 255 characters."
			validationObjects.push( { field: 'service_type', message: validationMessage } );
		}

		if(validationObjects.length > 0){
			var i = 0;
			for (i = 0; i < validationObjects.length; i++) {
			    this.markInvalid(validationObjects[i].field, validationObjects[i].message);
			}
			return false;
		}

		return true;
	},

	handleSubmit: function(e) {
		// some validation
		// ajax url call + redirect
		e.preventDefault();

		if(this.validateForm()){
			this.clearValidations();
			//var formValues = JSON.stringify($("#service-form").serializeJSON());
			//console.log("The form values are ->", formValues);


			var service_owner_id =  $("#service_owner").val();

			if(service_owner_id != "")
			{
				serviceOwnerId = null;
				for(var i = 0; i < globalOwnerData.length; i++){
					if(service_owner_id == globalOwnerData[i].first_name + " " + globalOwnerData[i].last_name){
						serviceOwnerId = globalOwnerData[i].uuid;
						break;
					}
				}
			}


			var external_contact_information =  $("#contact_information_external").val();

			if(external_contact_information != "")
			{
				externalContactInformationId = null;
				for(var i = 0; i < globalExternalContactData.length; i++){
					if(external_contact_information == globalExternalContactData[i].internal_contact_information.internal_contact_information.first_name +
						" " + globalExternalContactData[i].internal_contact_information.internal_contact_information.last_name){
						externalContactInformationId = globalExternalContactData[i].internal_contact_information.internal_contact_information.uuid;
						break;
					}
				}
			}


			var internal_contact_information =  $("#contact_information_internal").val();

			if(internal_contact_information != "")
			{
				internalContactInformationId = null;
				for(var i = 0; i < globalInternalContactData.length; i++){
					if(internal_contact_information == globalInternalContactData[i].internal_contact_information.internal_contact_information.first_name + " "
						+ globalInternalContactData[i].internal_contact_information.internal_contact_information.last_name){
						internalContactInformationId = globalInternalContactData[i].internal_contact_information.internal_contact_information.uuid;
						break;
					}
				}
			}


			var params = {};
			params["name"] = $("#name").val();
			params["description_external"] = $("#description_external").val();
			params["description_internal"] = $("#description_internal").val();
			params["service_area"] = $("#service_area").val();
			params["service_type"] = $("#service_type").val();
			params["request_procedures"] = $("#request_procedures").val();
			params["funders_for_service"] = $("#funders_for_service").val();
			params["value_to_customer"] = $("#value_to_customer").val();
			params["risks"] = $("#risks").val();
			params["competitors"] = $("#competitors").val();
			params["service_owner_uuid"] = serviceOwnerId;
			params["service_contact_information_uuid"] = externalContactInformationId;
			params["service_internal_contact_information_uuid"] = internalContactInformationId;


			var parts = window.location.href.split("/");
			var host = "http://" + parts[2];
			var url = "";

			if(this.props.source != null && this.props.source != ""){
				params["uuid"] = parts[parts.length - 1];
				url = host + "/api/v1/services/edit";
				opType = "edit";
			}
			else {
				url = host + "/api/v1/services/add";
				opType = "add";
			}

			this.serverRequest = $.ajax({
				url: url,
				headers: {"X-CSRFToken": $("input[name=csrfmiddlewaretoken]")[0].value },
				dataType: "json",
				crossDomain: true,
				type: "POST",
				contentType:"application/json",
				cache: false,
				data: JSON.stringify(params),
				success: function (data) {
					if(opType == "add")
						$("#modal-success-body").text("You have successfully inserted a new service");
					else
						$("#modal-success-body").text("You have successfully updated the service");
					$("#modal-success").modal('show');
				}.bind(this),
				error: function (xhr, status, err) {
					var response = JSON.parse(xhr.responseText);
					$("#modal-body").text(response.errors.detail);
					$("#modal-danger").modal('show');
				}.bind(this)
			});
		}
		else{
		}	
	},

	getInitialState: function () {
		return {
			service: {
				name: "",
				description_internal: ""
			}
		}
	},

    componentDidMount: function () {

		jQuery.support.cors = true;
		var url = window.location.href;
        var contents = url.split("/");
        var host = contents[0] + "//" + contents[2];

		$.getJSON(
            host + "/api/v1/owner/all",
            function (data) {
				var service_owner = $("#service_owner");
				var current = service_owner.val();

				if(current != -1){
					$("#service_owner option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].first_name + " " + data.data[i].last_name )
						.text(data.data[i].first_name + " " + data.data[i].last_name);
					service_owner.append(option);

				}
				if(current != -1)
					service_owner.val(current).change();

				globalOwnerData = data.data;

            });


		$.getJSON(
            host + "/api/v1/owner/contact_information/all",
            function (data) {
				var contact_information_external = $("#contact_information_external");
				var current = contact_information_external.val();

				if(current != -1){
					$("#contact_information_external option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var v = data.data[i].internal_contact_information.internal_contact_information.first_name + " "
						+ data.data[i].internal_contact_information.internal_contact_information.last_name;
					var option = $('<option></option>').attr("value",  v).text(v);
					contact_information_external.append(option);

				}
				if(current != -1)
					contact_information_external.val(current).change();

				globalExternalContactData = data.data;


				var contact_information_internal = $("#contact_information_internal");
				current = contact_information_internal.val();

				if(current != -1){
					$("#contact_information_internal option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var v = data.data[i].internal_contact_information.internal_contact_information.first_name + " "
						+ data.data[i].internal_contact_information.internal_contact_information.last_name;
					var option = $('<option></option>').attr("value", v ).text(v);
					contact_information_internal.append(option);

				}
				if(current != -1)
					contact_information_internal.val(current).change();

				globalInternalContactData = data.data;

            });


		$.getJSON(
            host + "/api/v1/services/area/all",
            function (data) {
				var service_area = $("#service_area");
				var current = service_area.val();

				if(current != -1){
					$("#service_area option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].area).text(data.data[i].area);
					service_area.append(option);

				}
				if(current != -1)
					service_area.val(current).change();
            });

		$.getJSON(
            host + "/api/v1/services/type/all",
            function (data) {
				var type = $("#service_type");
				var current = type.val();

				if(current != -1){
					$("#service_type option[value='" + current + "']").remove();
				}
				for(var i = 0; i < data.data.length; i++) {
					var option = $('<option></option>').attr("value", data.data[i].type).text(data.data[i].type);
					type.append(option);

				}
				if(current != -1)
					type.val(current).change();

            });


        if(this.props.source == null || this.props.source == "")
            return;

        this.serverRequest = $.ajax({
            url: this.props.source,
            dataType: "json",
            crossDomain: true,
            type: "GET",
            cache: false,
            success: function (data) {
                this.setState({service: data.data});
                $("#name").val(this.state.service.name);
                $("#description_internal").val(this.state.service.description_internal);
                $("#description_external").val(this.state.service.description_external);
                $("#request_procedures").val(this.state.service.request_procedures);
                $("#funders_for_service").val(this.state.service.funders_for_service);
                $("#value_to_customer").val(this.state.service.value_to_customer);
                $("#risks").val(this.state.service.risks);
                $("#competitors").val(this.state.service.competitors);



				var service_area = $("#service_area");
				var optionsCount = $("#service_area>option").length;
				var sa = this.state.service.service_area;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", sa).text(sa);
						service_area.append(option);
				}
				service_area.val(sa).change();

				var service_type = $("#service_type");
				optionsCount = $("#service_type>option").length;
				var st = this.state.service.service_type;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", st).text(st);
						service_type.append(option);
				}
				service_type.val(st).change();

				var service_owner = $("#service_owner");
				optionsCount = $("#service_owner>option").length;
				var so = this.state.service.service_owner.first_name + " " + this.state.service.service_owner.last_name;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", so).text(so);
						service_owner.append(option);
				}
				service_owner.val(so).change();

				var contact_information_internal = $("#contact_information_internal");
				optionsCount = $("#contact_information_internal>option").length;
				var cii = this.state.service.contact_information.internal_contact_information
					.internal_contact_information.internal_contact_information.first_name + " " + this.state.service.contact_information.internal_contact_information
					.internal_contact_information.internal_contact_information.last_name;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", cii).text(cii);
						contact_information_internal.append(option);
				}
				contact_information_internal.val(cii).change();


				var contact_information_external = $("#contact_information_external");
				optionsCount = $("#contact_information_external>option").length;
				var cie = this.state.service.contact_information.external_contact_information
					.external_contact_information.external_contact_information.first_name + " " + this.state.service.contact_information.external_contact_information
					.external_contact_information.external_contact_information.last_name;
				if(optionsCount <= 1){
					var option = $('<option></option>').attr("value", cie).text(cie);
						contact_information_external.append(option);
				}
				contact_information_external.val(cie).change();

				serviceOwnerId = this.state.service.service_owner.uuid;
				internalContactInformationId = this.state.service.contact_information.internal_contact_information.
					internal_contact_information.internal_contact_information.uuid;
				externalContactInformationId = this.state.service.contact_information.external_contact_information.
					internal_contact_information.internal_contact_information.uuid;

            }.bind(this),
            error: function (xhr, status, err) {
                console.log(this.props.source, status, err.toString());
            }.bind(this)
        });
    },

    componentWillUnmount: function () {
        this.serverRequest.abort();
    },

	render: function(){		
		var formElements = this.generateFormElements(this.props.resourceObject);
		return(
			<div className="widget">
					<div className="widget-header bordered-bottom bordered-blue">
			     	<span className="widget-caption">{this.props.formName}</span>
			    </div>
			    <div className="widget-body">
			    	<form role="form" onSubmit={this.handleSubmit} id="service-form">
			    		{formElements}
			    		<button type="submit" className="btn btn-blue">Submit</button>
			    	</form>
			   	</div>
			</div>
		);
	}
});

ReactDOM.render(  
  <FormWrapper resourceObject={resourceObject} formName={formName} source={$("#source")[0].value}/>,
  document.getElementById('write-content')
);
