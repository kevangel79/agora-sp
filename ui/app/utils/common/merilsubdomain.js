import { field } from 'ember-gen';


const SORT_FIELDS = [
  'name',
];

const TABLE_FIELDS = [
  field('domain.name', {label: 'merilsubdomain.table.domain'}),
  field('name', {label: 'merilsubdomain.table.name'}),
];


const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'subdomain.cards.basic',
  fields: [
    'domain.name',
    'name',
    'description'
  ],
  layout: {
    flex: [100,100,100],
  },
};


const BASIC_INFO_FIELDSET = {
  label: 'subdomain.cards.basic',
  fields: [
    'domain',
    'name',
    'description'
  ],
  layout: {
    flex: [100,100,100],
  },
};

const DETAILS_FIELDSETS = [
  DETAILS_BASIC_INFO_FIELDSET,
];

const CREATE_FIELDSETS = [
  BASIC_INFO_FIELDSET,
];

const EDIT_FIELDSETS = [
  BASIC_INFO_FIELDSET,
];

export {
  TABLE_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  SORT_FIELDS,
}
