import uuid
from gluon.serializers import json

if not auth.user_id: session.patient=session.patient_id=None

active=Field('active','boolean',default=True,writable=False)
created_by=Field('created_by',db.auth_user,default=auth.user_id,update=auth.user_id,writable=False)
created_on=Field('created_on','datetime',default=request.now,update=request.now,writable=False)
migrate = True

db.define_table('race',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('religious_affiliation',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


    

db.define_table('marital_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)




db.define_table('gender',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)



db.define_table('appointment_reason_code',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('appointment_type_code',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)
    


db.define_table('language_ability',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)



db.define_table('language_proficiency',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)



db.define_table('contact_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)



db.define_table('relationship_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('provider_role1',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)



db.define_table('provider_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('advance_directive_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

  
    
db.define_table('advance_beneficiary_notice',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)



db.define_table('social_history',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('health_insurance_plan',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)
 
    
 
db.define_table('problem_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

db.define_table('adverse_event_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

    
db.define_table('severity',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

    
db.define_table('problem_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

    
db.define_table('diagnosis_priority',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('no_immunization_reason',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

db.define_table('immunization_information_source',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

     
db.define_table('administered_vaccine',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)




db.define_table('drug_manufacturer',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)




db.define_table('vital_sign_result',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


   
db.define_table('diagnosis_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

db.define_table('body_site',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


    

db.define_table('drug_admin_route',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


    
    
db.define_table('medication_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('medication_fill_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

db.define_table('order_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

db.define_table('order_control',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

        
db.define_table('order_setting_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

db.define_table('order_priority',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('specimen_action',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

db.define_table('specimen_risk',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('specimen_collection_method',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

        
db.define_table('patient_class1',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('document_class',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)

db.define_table('admission_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('admission_source',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('specimen_collection_site',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


    
    
db.define_table('procedure_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


    
db.define_table('discharge_disposition',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('result_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


    
db.define_table('result_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)



db.define_table('dispense_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('abnormal_flag',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


    
db.define_table('specimen_rejection_reason',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)


db.define_table('accept_acknowledgment_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(key)s:%(description)s',migrate=migrate)







###########################################################################################################
##Before calling appoitment, patient classification is called to determine whether the patient is         #
##a new patient or an exsiting patient, if a new patient registration of the new patient starts and       #
## then the patient is put in the appointment list after registration is finished. if the patient is an   #
##existing patient counter checking is done and automically inserted in the appointment list              #
##All records are accessed using the appoitment list instead to acces the patient data                    #      
###########################################################################################################
    


db.define_table('patient',
                Field('provider_patient_id',notnull=True,default=uuid.uuid4()),
                Field('first_name',  notnull=True), 
                Field('last_name',  notnull=True),
                Field('email'),
                Field('address'),
                Field('web_page_url',requires=IS_NULL_OR(IS_URL())),
                Field('phone_number_home',default=''),
                Field('phone_number_office',default=''),
                Field('phone_number_cell',default=''),                
                Field('other_contact_info','text'),
                Field('preferred_contact',requires=IS_IN_SET(('email','phone call','sms'),zero=None)),
                Field('gender',db.gender),
                Field('date_of_birth', 'datetime',  notnull=True),
                Field('marital_status',db.marital_status),
                Field('religious_affiliation',db.religious_affiliation),
                Field('race',db.race),
                Field('ethnicity'),
                Field('social_history',db.social_history),
                Field('mother_maiden_name'), 
                Field('multiple_birth_indicator','boolean'),
                Field('birth_order'),
                Field('birth_place'),
                Field('identity_unknown_indicator'),
                Field('comments_on_this_table', 'text'),
                Field('latitude','double',
                      requires=IS_NULL_OR(IS_FLOAT_IN_RANGE(0,100))),
                Field('longitude','double',
                      requires=IS_NULL_OR(IS_FLOAT_IN_RANGE(0,100))),
                active, created_by, created_on, 
                format = '%(first_name)s %(last_name)s [#%(id)s]',
                migrate=migrate)

###################################################
#appointment list can be stored for later referrence#
####################################################

db.define_table('appointment',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('location', notnull=True),
                Field('appointment_type_codes',db.appointment_type_code),
                Field('appointment_reason_codes',db.appointment_reason_code),
                Field('start_time', 'datetime', notnull=True),
                Field('stop_time', 'datetime', notnull=True),
                active, created_by, created_on, 
                format = '%(start_time)s @ %(location)s',
                migrate=migrate)


############################################################################
#if a patient has to fill a form, language is used for the system to switch#
#if the application is internationalized then this function is place##########
##############################################################################

db.define_table('language',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('type_of_language',  notnull=True), 
                Field('language_ability',db.language_ability),
                Field('degree_of_language_ability',db.language_proficiency),
                active, created_by, created_on,
                format = '%(type_of_language)s',
                migrate=migrate)



                
db.define_table('support',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('date_support_provided', 'date', default=request.now),
                Field('contact_type',db.contact_type),
                Field('contact_relationship', db.relationship_type),
                Field('contact_address',  notnull=True),
                Field('contact_phone', notnull=True),
                Field('contact_email', notnull=True),
                Field('contact_URL'),
                Field('contact_language'), # it is a good idea to use the table language here and wherever required
                Field('contact_name', notnull=True),
                active, created_by, created_on, 
                migrate=migrate)
       
db.define_table('provider',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('service_to_patient_date_rage_','datetime'),# date patient start date with the provider to current date or the wordresent
                Field('provider_role1',db.provider_role1),
                Field('provider_type',db.provider_type),
                Field('address'),
                Field('national_provider_id',  notnull=True),
                Field('phone'),
                Field('email'),
                Field('provider_URL'),
                Field('provider_name'),
                Field('organization_name'),
                active, created_by, created_on, 
                migrate=migrate)


db.define_table('payment_provider',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('group_name'),
                Field('health_insurance_type',db.health_insurance_plan),
                Field('health_plan_insurance_information_source_id', label='Insurance Company ID'),#The coded identifier of the payer corresponding to the Health Plan Information Source Name. It is important to note that Health Plan Information Source Name and ID are not synonymous with Health Plan Name or the health plan identifier (when/if health plans are enumerated under HIPAA)
                Field('health_plan_insurance_information_source_address'),
                Field('health_plan_insurance_information_source_phone'),
                Field('health_plan_insurance_information_source_email'),
                Field('health_plan_insurance_information_source_URL'),
                Field('health_plan_insurance_information_source_name'),
                active, created_by, created_on, 
                migrate=migrate)

db.define_table('insurance_information',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('health_plan_coverage_start_dates','date', notnull=True),
                Field('health_plan_coverage_end_date', 'date', notnull=True),
                Field('patient_member_id'), 
                Field('patient_relationship_to_subscriber',db.relationship_type),
#                Field('patient_address',db.patient.id,'%(person_address)s',multiple=False)),
#                Field('patient_phone','string',requires=IS_IN_DB(db, db.patient.id,'%(person_phone)s',multiple=False)),
#                Field('patient_email','string',requires=IS_IN_DB(db, db.patient.id,'%(person_email)s',multiple=False)), 
#                Field('patient_URL','string',requires=IS_IN_DB(db, db.patient.id,'%(person_URL)s',multiple=False)),
#                Field('patient_name','string',requires=IS_IN_DB(db, db.patient.id,'%(person_name)s',multiple=False)), 
#                Field('patient_date_of_birth',requires=IS_IN_DB(db, db.patient.id,'%(date_of_birth)s',multiple=False)), 
                Field('financial_responsibility_party_type'), # The type of party that has responsibility for all or a portion of the patient's healthcare; includes health insurance, the patient directly, a guardian or other guarantor or other third party that is not a health insurance plan
                Field('patient_account_number'), 
                active, created_by, created_on,  migrate=migrate)

db.define_table('subscriber_information', 
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('subscriber_ID'), 
                Field('insurance_subscriber_address'),
                Field('insurance_subscriber_phone'),
                Field('insurance_subscriber_email'),
                Field('insurance_subscriber_URL'),
                Field('insurance_subscriber_name'),
                Field('subscriber_date_of_birth'),
                Field('subscriber_administrative_sex',db.gender),
                active, created_by, created_on, 
                migrate=migrate)

db.define_table('guarantor_or_insurance_provider_data',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('effective_date_of_financial_responsibility', 'date'),#The time span over which the Financial Responsibility Party is responsible for the payment of the patient's healthcar                
                Field('financial_responsibility_party_address'),
                Field('financial_responsibility_party_phone'),
                Field('financial_responsibility_party_email'),
                Field('financial_responsibility_party_URL'),
                Field('financial_responsibility_party_name'),
                Field('advance_beneficiary_notice',
                      db.advance_beneficiary_notice),
                active, created_by, created_on, 
                migrate=migrate)

db.define_table('health_plan', 
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('Health_plan_name1'), #The name of the specific health insurance product as specified by the insurance company offering the healthcare insurance. The HIPAA legislation requires the Secretary of HHS to establish unique health plan identifiers. To date, the Secretary of HHS has not promulgated plans for regulations specifying the enumeration and identification of health plans
                Field('insurance_company_name'),  #The name of the insurance company.  There may be multiple names for the same insurance company,.  The first name listed is assumed to be the legal name.
                active, created_by, created_on, 
                migrate=migrate)

db.define_table('patient_social_history',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('social_history_date',  'datetime'),
                #                Field('social_history_id',db.patient.id,'%(social_history)s',multiple=False)), 
                Field('comments_on_this_table',  'text'), 
                active, created_by, created_on, 
                migrate=migrate)
db.define_table('genetic_result_values',
                Field('code',unique=True,notnull=True),
                Field('common_name'),
                Field('sequence'),
                Field('answer_text'),
                Field('answer_code'),
                active, created_by, created_on, 
                format='%(code)s %(common_name)s',
                migrate=migrate)

db.define_table('disease',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('main_category'),
                Field('subcategory'),
                Field('subcategory_code'),
                Field('disease_category'),
                Field('disease_category_code'),
                Field('disease_subcategory'),
                Field('subdiease_subcategory'),
                Field('disease'),
                Field('description'),
                active, created_by, created_on, 
                format='%(main_category)s %(subcategory)s%(subcategory_code)s%(disease_category)s%(disease_category_code)s%(disease_subcategory)s%(subdiease_subcategory)s %(disease)s%(description)s',
                migrate=migrate)

db.define_table('patient_disease_encounter', 
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('disease_type',db.disease),
#'%(main_category)s %(subcategory)s%(subcategory_code)s%(disease_category)s%(disease_category_code)s%(disease_subcategory)s%(subdiease_subcategory)s %(disease)s%(description)s',multiple=False)),
                active, created_by, created_on, 
                migrate=migrate)


#db.disease.import_from_csv_file(open('C:/Users/User/csv_disease0.csv','r'),migrate=migrate)


db.define_table('allergy_sensitivity',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('diagnosed_by', db.auth_user, default=auth.user_id),
                Field('adverse_event_date', 'datetime'),#This is a date that expresses when this particular allergy or intolerance was known to be active for the patient
                Field('adverse_event_type',db.adverse_event_type),
                Field('product_description'),# cane be non_medication, such as food and medication, 
                Field('product_code'), # the code for medication and non medication
                Field('reaction_description', 'text'), # derived from above aderse event type
                Field('reaction_code'),# the code from aderverse event type above
                Field('severity',db.adverse_event_type),
                Field('severity_description'), #This the description obtained from severity
                Field('severity_code'), # this is the code from severity
                Field('comments_on_this_table'),
                active, created_by, created_on, 
                migrate=migrate)

#Conditions
db.define_table('problem_events',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('problem_date', 'datetime'),
                Field('problem_type',db.problem_type),
#                Field('problem_name'), # derived from above problem type ( description)
#                Field('problem_code'),#derived from above problem type(key)
                Field('treatment_provider'),
                Field('age_at_the_onset','integer'),
                Field('patient_died', 'integer'),
                Field('cause_of_death'), #show if yes for the above question
                Field('age_at_death'),# show if yes for the patient died question
                Field('date_and_time_of_death','datetime'), #show if yes for the patient died question
                Field('diagnosis_priority',db.diagnosis_priority),
                Field('treatment_provider_id',db.provider),
                Field('problem_status',db.problem_status),
                Field('comments_on_this_table'), 
                active, created_by, created_on, 
                migrate=migrate)


db.define_table('prescription_medication',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('prescriber_notes', 'text'), #The instructions, typically from the ordering provider, to the patient on the proper means and timing for the use of the product. This information is free-text but can also be represented as a series of Sig Components
                Field('prescription_information',  'text',  length=100),
                Field('indicate_medication_stopped', 'text', length=100),#prescriber_note: Used to express a “hard stop,” such as the last Sig sequence in a tapering dose, where the last sequence is 'then D/C' or where the therapy/drug is used to treat a condition and that treatment is for a fixed duration with a hard stop, such as antibiotic treatment, etc
                Field('administration_timing',  'text',  length=100),#prescriber_note: defines a specific administration or use time. Can be a text string (Morning, Evening, Before Meals, 1 Hour After Meals, 3 Hours After Meals, Before Bed) or an exact time
                Field('frequency', 'text',  length=100),#prescriber_note: defines how often the medication is to be administered as events per unit of time. Often expressed as the number of times per day (e.g., four times a day), but may also include event-related information (e.g., 1 hour before meals, in the morning, at bedtime). Complimentary to Interval, although equivalent expressions may have different implications (e.g., every 8 hours versus 3 times a day)
                Field('interval',  'text',  length=100),#prescriber_note: defines how the product is to be administered as an interval of time. For example, every 8 hours. Complimentary to Frequency, although equivalent expressions may have different implications (e.g., every 8 hours versus 3 times a day)
                Field('duration',  'text',  length=100),#prescriber_note: for non-instantaneous administrations, indicates the length of time the administration should be continued. For example, (infuse) over 30 minutes
                Field('route', db.drug_admin_route),#prescriber_note: indicates how the medication is received by the patient (e.g., by mouth, intravenously, topically, et cetera)
                Field('dose', 'text',  length=100),#prescriber_note: the amount of the product to be given. This may be a known, measurable unit (e.g., milliliters), an administration unit (e.g., tablet), or an amount of active ingredient (e.g., 250 mg). May define a variable dose, dose range or dose options based upon identified criteria (see Dose Indicator)
                Field('site',db.body_site),#prescriber_note: The anatomic site where the medication is administered. Usually applicable to injected or topical products
                Field('dose_restriction',  'text', length=100),#prescriber_note: defines a maximum or dose limit. This segment can repeat for more than one dose restriction
                Field('product_form',  'text', length=100), # The physical form of the product as presented to the patient. For example: tablet, capsule, liquid or ointment
                Field('delivery_method'), # prescriber_note: A description of how the product is administered/consumed
                Field('code_product_name'), # A code describing the product from a controlled vocabulary;Medication Clinical Drug Names.;When only the class of the drug is known (e.g., Beta Blocker or Sulfa Drug),  SHALL be coded Medication Drug Class.;When only the medication ingredient name is know, the coded product name MAY be coded as the Ingredient Name 
                Field('coded_brand_name'), # A code describing the product as a branded or trademarked entity from a controlled vocabulary
                Field('product_name_description',  'text',  length=100),#The name of the substance or product without reference to a specific vendor (e.g., generic or other non-proprietary name). If a Coded Product Name is present, this is the text associated with the coded concept
                Field('drug_manufacturer',db.drug_manufacturer),
                Field('product_concentration',  'text',  length=100),#The amount of active ingredient, or substance of interest, in a specified product dosage unit, mass or volume. For example 250 mg per 5 ml
                Field('type_of_medication',db.medication_type),
                Field('status_of_medication','string', requires=IS_IN_SET(['active','discharged', 'chronic', 'acute'])), # If the medication is Active, Discharged, Chronic, Acute, etc
                Field('indication',  'text'), # prescriber_note: The medical condition or problem intended to be addressed by the ordered product. For example: for chest pain, for pain, for high blood pressure
                Field('patient_instruction',  'text',  length=100),#Instructions to the patient that are not traditionally part of the Sig. For example, “keep in the refrigerator.” More extensive patient education materials can also be included
                Field('reaction',  'text',  length=100),#Any noted intended or unintended effects of the product. For example: full body rash, nausea, rash resolved
                Field('vehicle'), # prescriber_note: Non-active ingredient(s), or substances not of therapeutic interest, in which the active ingredients are dispersed. Most often applied to liquid products where the major fluid Component is considered the vehicle. For example: Normal Saline is the vehicle in “Ampicillin 150mg in 50ml NS”; Aquaphor is the vehicle in “10% LCD in Aquaphor”
                Field('dose_indicator'), #prescriber_note: A criteria that specifies when an action is, or is not, to be taken. For example, “if blood sugar is above 250 mg/dl”
                Field('comments_on_this_table', 'text'), 
                active, created_by, created_on, 
                migrate=migrate)
                
db.define_table('medication_order_information', 
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('order_number'),#The order identifier from the perspective of the ordering clinician. Also known as the 'placer number' versus the pharmacies prescription number (or 'filler number')
                Field('order_control',db.order_control),#Required for messages that are initiated by the Medication Order Filler. Shall have a value of DR, DU, XO or RF
                Field('Number_of_fills', 'integer'),#The number of times that the ordering provider has authorized the pharmacy to dispense this medication
                Field('quantity_ordered', 'integer'),#The amount of product indicated by the ordering provider to be dispensed. For example, number of dosage units or volume of a liquid substance. Note: this is comprised of both a numeric value and a unit of measure
                Field('order_expiration_date', 'datetime'),
                Field('order_date', 'datetime', default=request.now),
                Field('order_provider'),#The person that wrote this order/prescription (may include both a name and an identifier) At least one repetition shall contain the prescriber's National Provider Identifier (ORC.12.09 = "NPI"), if the provider has an NPI. The NPI OID root is 2.16.840.1.113883.4.6
                Field('fullfillment_instruction', 'text',  length=100),#Instructions to the dispensing pharmacist or nurse that are not traditionally part of the Sig. For example, “instruct patient on the use of occlusive dressing”
                Field('fullfillment_history', 'text', length=100),#History of dispenses for this order. Comprised of Fulfillment History Components
                Field('prescription_number'),#Fulfillment History Component: The prescription identifier assigned by the pharmacy
                Field('dispensing_pharmacy_name_and_identifier'),#Fulfillment History Component: The pharmacy that performed this dispense (may include both a name and an identifier)
                Field('dispensing_pharmacy_location'),#Fulfillment History Component: The date of this dispense
                Field('dispnese_date', 'datetime'),#Fulfillment History Component: The date of this dispense
                Field('quantity_dispensed1'),#Fulfillment History Component: The actual quantity of product supplied in this dispense. Note: this is comprised of both a numeric value and a unit of measure
                Field('fill_number'),#Fulfillment History Component: The fill number for the history entry. Identifies this dispense as a distinct event of the prescription
                Field('fill_status',db.medication_fill_status),#Fulfillment History Component. The fill event status is typically 'complete' indicating the fill event has been, or is expected to be picked up. A status of 'aborted' indicates that the dispense was never picked up (e.g., “returned to stock”)
                active, created_by, created_on, 
                migrate=migrate)


db.define_table('pregnancy',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('patient_pregnant','boolean'),
                active, created_by, created_on, 
                migrate=migrate)             

db.define_table('advance_directives',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('name'),
                Field('advance_directive_type',db.advance_directive_type), 
                Field('advance_directive_code'),# serialized from adavance directive type
                Field('advance_directive_description', 'text'),#serialized from advance directive type
                Field('effective_date', 'date',default=request.now),
                Field('custodian_of_the_document'),#Name, address or other contact information for the person or organization that can provide a copy of the document
                active, created_by, created_on, 
                migrate=migrate)


db.define_table('immunization',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('name'),
                Field('refusal', 'boolean'),#A flag that the immunization event did not occur. The nature of the refusal (e.g., patient or patient caregiver  refused, adverse reaction)
                Field('administered_date' ,  'date'), #The date and time of substance was administered or refused, i.e., when the immunization was administered to the patient, or refused by the patient or patient caregiver.
                Field('medication_series_number'), #Indicate which in a series of administrations a particular administration represents (e.g. “hepatitis B vaccine number 2”)
                Field('reaction'),#Any noted intended or unintended effects of the product. For example: full body rash, nausea, rash resolved
                Field('performer'),#The person that administered the immunization to the patient (may include both a name and an identifier)
                Field('administered_vaccine',db.administered_vaccine),
                Field('coded_product_name'), # serialized from administered_vaccine above - 'key'
                Field('product_name_description'),#serialized from administered_vaccin above -'description'
                Field('drug_manufacturer',db.drug_manufacturer),
                Field('lot_number'),
                Field('immunization_services_funding_eligibility'), 
                Field('refusal_reason',db.no_immunization_reason),
                Field('immunization_information_source',db.immunization_information_source),#The immunization information source is a value which indicates where the information about a specific immunization record came from
                Field('comments_on_this_table', 'text'), 
                active, created_by, created_on, 
                migrate=migrate)


db.define_table('vital_sign',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('result_id'),
                Field('result_date_and_time', 'datetime'),
                Field('result_type',db.vital_sign_result),
                Field('result_status', 'text'), #Status for this vital sign observation, e.g., complete, preliminary
                Field('result_value', 'text'),#The value of the result, including units of measure if applicable
                Field('result_interpretation', 'text'),#An abbreviated interpretation of the vital sign observation, e.g., normal, abnormal, high, etc
                Field('result_reference_range'),
                Field('comments_about_the_table', 'text'), 
                active, created_by, created_on, 
                migrate=migrate)


db.define_table( 'result_event_entry',
                 Field('patient','reference patient',default=session.patient_id,writable=True),
                 Field('result_id'),
                 Field('result_date_time', 'datetime'),
                 Field('result_type',db.result_type),
                 Field('result_status',db.result_status),
                 Field('result_value'),#The value of the result, including units of measure if applicable
                 Field('result_interpretation'),#An abbreviated interpretation of the observation, e.g., normal, abnormal, high, etc
                 Field('abnormal_flag',db.abnormal_flag),
                 Field('result_reference_range'),
                 active, created_by, created_on, 
                 migrate=migrate)

#This module contains data describing the interactions between the patient and clinicians. Interaction includes both in-person and non-in-person encounters such as telephone and email communication.
db.define_table('encounter',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('encounter_id'),
                Field('encounter_type'),#This is a coded value describing the type of the Encounter
                Field('encounter_decription'),
                Field('encounter_date_and_time', 'datetime', default=request.now),
                Field('encounter_provider'),#Name and other information for the person or organization performed or hosted the Encounter
                Field('admission_source',db.admission_source),
                Field('admission_type',db.admission_type),
                Field('immunization_service_funding_eligibility'),#Immunization Services Funding Eligibility is a point in time marker for eligibility category that describes a person. The categories are specified by the federal Vaccines for Children program. It does not refer to who actually paid for a given immunization
                Field('discharge_disposition',db.discharge_disposition),
                Field('patient_class',db.patient_class1),
                Field('in_facility_location'), #The service delivery location
                Field('arrival_date', 'datetime'),
                Field('reason_for_visit'),
                Field('order_to_admit_date', 'datetime'),
                Field('decision_to_admit_date', 'datetime'),
                Field('discharge_date', 'datetime'),
                Field('facility_id'), #The identifier used to identify the facility
                Field('facility_name'),
                Field('facility_address'),
                Field('in_facility_duration'),
                active, created_by, created_on, 
                migrate=migrate)


db.define_table('medical_procedures',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('procedure_id'),
                Field('procedure_type',db.procedure_type),
                Field('medical_procedure_code',  'string'),  # serialized from procedure type'key'
                Field('medical_procedure_description', 'text'),#serialized from procedure type 'description'
                Field('procedure_date', 'datetime', default=request.now),
                Field('procedure_provider','string'), #Name and other information for the person or organization performed or hosted the Procedure
                Field('body_site_procedure_applied',db.body_site),
                active, created_by, created_on, migrate=migrate)


db.define_table('family_member_history',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('pedigree', 'upload'), #A pedigree is a graphic, visual presentation of a family’s health history and genetic relationships for the purpose of health risk assessment. It can provide a mechanism to identify the distribution of a medical condition or a related condition in a group of close relatives. If the condition or related condition clusters among relatives or follows a clear pattern of inheritance, then the risk for the condition can be assessed for the unaffected family members. It is important that the structured data from which the pedigree is derived also be present, because identification of inherited conditions can be complex requiring clinical decision support algorithms
                Field('family_member_information'), #Family member information, including demographic data, health history, genetic test results, and relationships to other family members
                Field('family_member_demographics'),
                Field('family_member_relationship'),
                Field('family_member_relationship_description',
                      db.relationship_type),
                Field('family_member_identifier'),#An identifier used to track the family member in communications between systems
                Field('family_member_name'),
                Field('family_member_date_of_birth'),
                Field('family_member_administrative_gender',db.gender),
                Field('family_member_race',db.race),
                Field('family_member_ethnicity'),
                Field('family_member_medication_history'),
                Field('family_member_condition'), 
                Field('family_member_age'),
                Field('family_member_age_at_onset'),
                Field('family_member_death_indicator','boolean'),
                Field('family_member_cause_of_death'),
                Field('family_member_age_at_death'),
                Field('family_member_biological_sex'),
                Field('family_member_problem_status_id') ,
                Field('family_member_genetic_test_id'),
                Field('family_member_genetic_test_results_id'),                
                Field('family_member_genetic_test_date', 'datetime'),
                Field('family_member_multiple_birth','boolean'),
                Field('family_member_order_of_multiple_birth'),
                active, created_by, created_on, 
                migrate=migrate)


db.define_table('plan_of_care',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('discharge_instructions', 'text'),
                active, created_by, created_on, migrate=migrate)


db.define_table('clinical_research_data',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('sponsor_id'),
                Field('protocol_study_id'),
                Field('study_site'), 
                Field('investigator_id'),
                active, created_by, created_on, 
                migrate=migrate)

db.define_table('clinical_order', 
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('order_control',db.order_control),
                Field('order_group_number'),#An order group is a list of orders associated with an -placer group number.  A group is established when the placer supplies a placer group number with the original order.  	
                Field('order_Status',db.order_status),
                Field('parent_order_number1'),#The Order number of the Parent Order which may have spawned Child orders.  Used to maintain the original connection of the original order.
                Field('date_time_of_transaction'),#The date and time of the order transaction
                Field('order_entered_by'),
                Field('order_verified_by'),
                Field('order_setting',db.order_setting_type),#Indicates the care setting in which the order is executed.
                Field('requested_order_start_date_time'),#will be specified if the Order Placer wants to enforce a starting date/time for the execution of the ordered tests
                Field('order_priority',db.order_priority),
                Field('order_number'),
                Field('fill_number'), #The order identifier from the perspective of the system fulfilling the order.
                Field('order_Code'),
                Field('specimen_action_code',db.specimen_action),
                Field('ordering_provider'),
                Field('Results_distribution_list'),#Identifies the people and/or organization that are to receive copies of the results.  
                Field('specimen_collector_id'),#The person, department, or facility that collected the specimen.  (may include both a name and an identifier)
                Field('comments_on_this_table1', 'text'), 
                active, created_by, created_on, 
                migrate=migrate)
#This module contains data defining the. Specimen related to an Order.

db.define_table('specimen', 
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('specimen_id'), 
                Field('specimen_Parent_id'),
                Field('specimen_type'),
                Field('specimen_collection_method',db.specimen_collection_method),
                Field('specimen_source_site',db.specimen_collection_site),
                Field('specimen_source_site_modifier'),
                Field('specimen_risk',db.specimen_risk),
                Field('specimen_collection_date_time'),
                Field('specimen_received_date_time'),
                Field('specimen_availability'),
                Field('specimen_rejection_reason',
                      db.specimen_rejection_reason),
                Field('number_of_specimen_containers'), 

                active, created_by, created_on, 
                migrate=migrate)

"""
THIS TABLE MAKES NO SENSE - ALL REFERNCES TO BE FIXED!
db.define_table('lab_orders', 
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('MSH3', 
                      label='sending application'),  # contain an OID that represents the sending application when it is available and needed for routing purposes.
                Field('MSH4', 
                      label='Sending Facility'), # contain an OID that represents the sending facility
                Field('MSH5', 
                      label='Receiving Application'), # contain an OID that represents the receiving application when it is available and needed for routing purposes.
                Field('MSH6', 
                      label='Receiving Facility'), # contain an OID that represents the sending facility
                Field('MSH15', 
                      label='Accept Acknowledgment Type'),#  contain the literal value "AL" for order messages. and will be empty for Acknowledgment messages
      
                Field('MSH16', 
                      label='Application Acknowledgment Type'), #  contain the literal value "AL" for order messages.and will be empty for Acknowledgment messages

#MSH|||sending application|sending facility|receiving application|receiving  facility|||||||||accept acknowledgement|application acknowledgment type|...<cr>
# patient personal information

#                Field('PID6', 'string', requires=IS_IN_DB(db, db.patient.id,'%(mother_maiden_name)s',multiple=False), 
#                      label='mother Maiden Name'),
#                Field('PID7','string', requires=IS_IN_DB(db, db.patient.id,'%(date_of_birth)s',multiple=False), 
#                      label='Date of Birth'),
#                Field('PID8','string', requires=IS_IN_DB(db, db.patient.id,'%(gender)s',multiple=False), 
#                      label='Administrative Sex'),
#                Field('PID10','string', requires=IS_IN_DB(db, db.patient.id,'%(race)s',multiple=False), 
#                      label='Race'),
#                Field('PID11','string', requires=IS_IN_DB(db, db.patient.id,'%(person_address)s',multiple=False), 
#                     label='Patient_address'),
#                Field('PID12','string', requires=IS_IN_DB(db, db.insurance_information.id,'%(patient_account_number)s',multiple=False), 
#                      label='Patient Account Number'  ), 
#                Field('PID22','string', requires=IS_IN_DB(db, db.patient.id,'%(ethnicity)s',multiple=False), 
#                      label='Ethnic Group'  ), 
#                Field('PID31','string', requires=IS_IN_DB(db, db.patient.id,'%(identity_unknown_indicator)s',multiple=False), 
#                      label='Identity Unknown Indicator'  ), 
 
#PID| |||||mother Maiden Name|date of birth|aministartive sex||race|patient address|patient account number||||||||||ethnic group|||||||||identity unknown indicator|...<cr>             
# note patient address is represented as |address^city^state^zipcode|
                
#                Field('PV12','string', requires=IS_IN_DB(db.encounter.id,'%(patient_class)s',multiple=False), 
#                      label='Patient Class'  ),  # based on the value of patient class, PV13 and PV1.4 will be shown, if empty will not be shown
#                Field('PV13','string', requires=IS_IN_DB(db, db.encounter.id,'%(in_facility_location)s',multiple=False), 
#                      label='Assigned Patient Location'  ),  # present if the patient calss is inpatient      
#                Field('PV14','string', requires=IS_IN_DB(db, db.encounter.id,'%(admission_type)s',multiple=False), 
#                      label='Admission Type'  ), # for inpatient class
# #PV1||patient class|assigned patient location|admission type|...<cr>                
#                 Field('IN14','string', requires=IS_IN_DB(db, db.payment_provider.id,'%(health_plan_insurance_information_source_name)s',multiple=False), 
#                      label='Insurance Company Name'  ),   # if the lab requires it  
#                Field('IN116','string', requires=IS_IN_DB(db, db.subscriber_information.id,'%(insurance_subscriber_name)s',multiple=False), 
#                      label='Insurance Subscriber Name'  ),  #if the  lab requires insurance information
 
#patient insurance information               
#                 Field('IN117','string', requires=IS_IN_DB(db, db.insurance_information.id,'%(patient_relationship_to_subscriber)s',multiple=False), 
#                      label='Insured Relationship To Subscriber'  ),  # if the lab requires insurance information
#                Field('IN118','string', requires=IS_IN_DB(db, db.subscriber_information.id,'%(subscriber_date_of_birth)s',multiple=False), 
#                      label='Insured Date of Birth'  ), # if insurance information is present
#                 Field('IN149','string', requires=IS_IN_DB(db, db.subscriber_information.id,'%(subscriber_ID)s',multiple=False), 
#                      label='Insured ID Number'  ),      # if insurance information is present
#IN1||||insurance company name||||||||||||insurance subscriber name|insurance relationship to subscriber|insured date of birth|||||||||||||||||||||||||||||||insured ID number|..,<cr>                
# insurance additional information                
#                 Field('IN261','string', requires=IS_IN_DB(db, db.insurance_information.id,'%(patient_member_id)s',multiple=False), 
#                      label='Patient Member ID'  ),      # present only if Insure ID number is not present or relationship is self  and insurance information is present
#IN2|||||||||||||||||||||||||||||||||||||||||||||||||||patient member id|...<cr> 
 #patient common  order information                
#                 Field('ORC1','string', requires=IS_IN_DB(db, db.order.id,'%(order_control)s',multiple=False), 
#                      label='Order_control'  ),      
#                Field('ORC4','string', requires=IS_IN_DB(db, db.order.id,'%(order_group_number)s',multiple=False), 
#                      label='Placer Group Number'), 
#                Field('ORC5', 'string', requires=IS_IN_DB(db, db.order.id,'%(order_status)s',multiple=False), 
#                      label='Order Status'),   # filled by the order filler, not by the order placer              
#                Field('ORC8', 'string', requires=IS_IN_DB(db, db.order.id,'%(parent_order_number1)s',multiple=False), 
#                      label='Parent Order Number'), # has the same value as OBR29
#                Field('ORC9', 'string', requires=IS_IN_DB(db, db.order.id,'%(date_time_of_transaction)s',multiple=False), 
#                      label='Date and Time of Transaction'), 
#                Field('ORC10', 'string', requires=IS_IN_DB(db, db.order.id,'%(order_entered_by)s',multiple=False), 
#                      label='Order Entered By'), 
#                Field('ORC11', 'string', requires=IS_IN_DB(db, db.order.id,'%(order_verified_by)s',multiple=False), 
#                      label='Order Verified By'), 
#                Field('ORC20', 'string', requires=IS_IN_DB(db, db.guarantor_or_insurance_provider_data.id,'%(advance_beneficiary_notice)s',multiple=False),
#                      label='Advance Beneficiary Notice'), 
#                 Field('ORC29', 'string', requires=IS_IN_DB(db, db.order.id,'%(order_setting)s',multiple=False),
#                      label='Order Type'),   
#ORC|order control|||placer order number|order status|||parent order number|date and time of transaction|order entered by|order verified by|||||||||advance beneficiary notice|||||||||order type|...<cr>

#TQ1 – TIMING QUANTITY SEGMENT   
#                 Field('TQ17', 'string', requires=IS_IN_DB(db, db.order.id,'%(requested_order_start_date_time)s',multiple=False),#will be specified if the Order Placer wants to enforce a starting date/time for the execution of the ordered tests
#                      label='start_date_time'), 
#                Field('TQ19', 'string', requires=IS_IN_DB(db, db.order.id,'%(order_priority)s',multiple=False),
#                      label='priority'), #Order Priority
##TQ1||||||start date||priority|... <cr>                      
#OBR – OBSERVATION REQUEST SEGMENT - this part is filled by the order placer entity
#                 Field('OBR2', 'string', requires=IS_IN_DB(db, db.order.id,'%(order_number)s',multiple=False),
#                       label='Order Number'), #The Placer Order Number SHALL be unique across all order for the order placer.
#                 Field('OBR3', 'string', requires=IS_IN_DB(db, db.order.id,'%(fill_number)s',multiple=False),
#                       label='Fill Number'), # this is for order Filler, The Filler Order Number SHALL be unique across all order for the order filler.The Filler Order Number for a particular order SHALL not relate to more than one Placer Order Number.
#                 Field('OBR4', 'string', requires=IS_IN_DB(db, db.order.id,'%(order_code)s',multiple=False),
#                       label='Order Code'), # Laboratory Order Vocabulary when there is a corresponding code in the vocabulary value set
#                 Field('OBR10', 'string', requires=IS_IN_DB(db, db.order.id,'%(specimen_collector_id)s',multiple=False),
#                       label='Specimen Collector ID') , 
#                 Field('OBR11', 'string', requires=IS_IN_DB(db, db.order.id,'%(specimen_action_code)s',multiple=False),
                       label='Specimen Action Code') ,  # optional field, Specimen Action Code  
                Field('OBR16', 'string', requires=IS_IN_DB(db, db.order.id,'%(ordering_provider)s',multiple=False), 
                       label='Ordering Provider') ,   
                 Field('OBR28', 'string', requires=IS_IN_DB(db, db.order.id,'%(results_distribution_list)s',multiple=False),
                       label='Results Distribution List') ,  # when there are persons or care units that need to receive a copy of the results, the Order Placer SHALL provide a value         
                Field('OBR29', 'string', requires=IS_IN_DB(db, db.order.id,'%(parent_order_number)s',multiple=False),
                       label='Parent Order Number') ,#If this field is specified, it SHALL have the same value as ORC8.If the order message refers to a reflex order, this field SHALL be the order number of the original order from which the reflex order was triggered.
#OBR||order number|fill number|order code|||||speciment collection ID|specimen collection code|||||ordering provider||||||||||||results distribution list|parent order number|...<cr>

#OBX – OBSERVATION/RESULT SEGMENT - This part is to filled by a laboratory
                Field('OBX3', requires=IS_IN_DB(db, db.result_event_entry.id,'%(result_id)s',multiple=False), 
                       label='Result ID'), #The Observation Identifier SHOULD be coded as specified in Laboratory Tests Result Vocabulary for results in which there is a corresponding code in the vocabulary
                Field('OBX2_BX6', requires=IS_IN_DB(db, db.result_event_entry.id,'%(result_type)s',multiple=False), 
                       label='Value Type and Unit'),#Value Type SHALL be valued either with "NM", or "SN".The Units of Measure Vocabulary, when applicable
                Field('OBX7', requires=IS_IN_DB(db, db.result_event_entry.id,'%(result_reference_range)s',multiple=False),   
                       label='Result Reference Range'),#    
                Field('OBX8', requires=IS_IN_DB(db, db.result_event_entry.id,'%(abnormal_flag)s',multiple=False),  
                       label='Abnormal Flags') ,#  
                Field('OBX14', requires=IS_IN_DB(db, db.result_event_entry.id,'%(result_date_time)s',multiple=False),  
                       label='Results Date and Time'), 
#OBX||value type and unit|result ID|| |  |result reference range|abnormal flag|||||results date and time|...<cr>             
                Field('SPM2', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_id)s',multiple=False),
                       label=' Specimen ID'),#
                Field('SPM3', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_parent_id)s',multiple=False), 
                       label=' Specimen Parent ID'),#
                Field('SPM4', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_type)s',multiple=False),
                       label=' Specimen Type'),#
                Field('SPM7', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_collection_method)s',multiple=False), 
                      label=' Specimen Collection Method'),#The  Specimen Collection Method
                Field('SPM8', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_source_site)s',multiple=False), 
                      label=' Specimen Source Site'),#
                Field('SPM9', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_source_site_modifier)s',multiple=False),
                      label=' Specimen Source Site Modifier'),# if known inserted
                Field('SPM10', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_source_site)s',multiple=False), 
                     label=' Specimen Collection Site'),#
                 
                Field('SPM16', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_risk)s',multiple=False), 
                     label=' Specimen Risk Code'),#
                Field('SPM17', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_collection_date_time)s',multiple=False), 
                     label=' Specimen Collection Date/Time'),#
                Field('SPM18', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_received_date_time)s',multiple=False),
                     label=' Specimen Received Date/Time'),#
                Field('SPM20', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_availability)s',multiple=False), 
                    label=' Specimen Availability'),#
                Field('SPM21', requires=IS_IN_DB(db, db.specimen.id,'%(specimen_rejection_reason)s',multiple=False),  
                    label=' Specimen Rejection Reason'),#
                Field('SPM26', requires=IS_IN_DB(db, db.specimen.id,'%(number_of_specimen_containers)s',multiple=False), 
                   label=' Number of Specimen Containers'),#
                      
                active, created_by, created_on, 
                migrate=migrate)
#SPM||specimen ID|specimen parent ID|specimen type|||specimen collection method| specimen source site|specimen source site modifier|specimen collection site||||||specimen risk code|specimen collection date and time |specimen receive date and time||specimen availability|specimen rejection reason|||||number of specimen containers|...<cr>                  
db.define_table('drug_prescription_order', 
                Field('patient','reference patient',default=session.patient_id,writable=True),
                
                Field('MSH4', 
                      label='Sending Facility'), # When identifying a pharmacy, NCPDP Provider ID Numbers shall be employed and presented as OIDs These fields have a data type of HD. Support for representing OIDs in HD data types can be found in HL7 V2.5.1 Chap 2A Section 2.A.33. The NCPDP OID root is 2.16.840.1.113883.3.79
                
                Field('MSH6', 
                      label='Receiving Facility'), # When identifying a pharmacy, NCPDP Provider ID Numbers shall be employed and presented as OIDsThese fields have a data type of HD. Support for representing OIDs in HD data types can be found in HL7 V2.5.1 Chap 2A Section 2.A.33. The NCPDP OID root is 2.16.840.1.113883.3.79

#MSH||||sending facility||receiving facility|...<cr>
# the pharmacy agreed upon information may be sent                
                Field('PID6', 'string', requires=IS_IN_DB(db, db.patient.id,'%(mother_maiden_name)s',multiple=False), 
                      label='mother Maiden Name'),
                Field('PID7','string', requires=IS_IN_DB(db, db.patient.id,'%(date_of_birth)s',multiple=False), 
                      label='Date of Birth'),
                Field('PID8','string', requires=IS_IN_DB(db, db.patient.id,'%(gender)s',multiple=False), 
                      label='Administrative Sex'),
                Field('PID10','string', requires=IS_IN_DB(db, db.patient.id,'%(race)s',multiple=False), 
                      label='Race'),
                Field('PID11','string', requires=IS_IN_DB(db, db.patient.id,'%(person_address)s',multiple=False), 
                     label='Patient_address'),
                Field('PID12','string', requires=IS_IN_DB(db, db.insurance_information.id,'%(patient_account_number)s',multiple=False), 
                      label='Patient Account Number'  ), 
                Field('PID22','string', requires=IS_IN_DB(db, db.patient.id,'%(ethnicity)s',multiple=False), 
                      label='Ethnic Group'  ), 
                Field('PID31','string', requires=IS_IN_DB(db, db.patient.id,'%(identity_unknown_indicator)s',multiple=False), 
                      label='Identity Unknown Indicator'  ), 
#PID||||||mother madien name|date of birth|administration sex||race|patient address|patient account number||||||||||ethnic group||||||||||identity unknown indicator|...<cr>
# the following is used in a hospital setting                
                
                Field('PV12','string', requires=IS_IN_DB(db, db.encounter.id,'%(patient_class)s',multiple=False), 
                      label='Patient Class'  ),  # based on the value of patient class, PV13 and PV1.4 will shown, if empty will not be shown
                Field('PV13','string', requires=IS_IN_DB(db, db.encounter.id,'%(in_facility_location)s',multiple=False), 
                      label='Assigned Patient Location'  ),  # present if the patient clals is inpatient      
                Field('PV14','string', requires=IS_IN_DB(db, db.encounter.id,'%(admission_type)s',multiple=False), 
                      label='Admission Type'  ), # for inpatient class
                 Field('IN14','string', requires=IS_IN_DB(db, db.payment_provider.id,'%(health_plan_insurance_information_source_name)s',multiple=False), 
                      label='Insurance Company Name'  ),   # if the lab requires it  
                Field('IN116','string', requires=IS_IN_DB(db, db.subscriber_information.id,'%(insurance_subscriber_name)s',multiple=False), 
                      label='Insurance Subscriber Name'  ),  #if the  lab requires insurance information
 #PV1||patient class|assigned patient location|admission type||insurance subscriber name|...<cr>
 #patient insurance information   may be need or may be not             
                 Field('IN117','string', requires=IS_IN_DB(db, db.insurance_information.id,'%(patient_relationship_to_subscriber)s',multiple=False), 
                      label='Insured Relationship To Subscriber'  ),  # if the lab requires insurance information
                Field('IN118','string', requires=IS_IN_DB(db, db.subscriber_information.id,'%(subscriber_date_of_birth)s',multiple=False), 
                      label='Insured Date of Birth'  ), # if insurance information is present
                 Field('IN143','string', requires=IS_IN_DB(db, db.subscriber_information.id,'%(subscriber_administrative_sex)s',multiple=False), 
                      label='Insured Aministrative Sex'  ), # if insurance information is present
                 Field('IN149','string', requires=IS_IN_DB(db, db.subscriber_information.id,'%(subscriber_ID)s',multiple=False), 
                      label='Insured ID Number'  ),      # if insurance information is present
 #IN1||||||||||||||||||insured relationship to subscriber|insured date of birth|||||||||||||||||||||||||insured administration sex||||||insured ID number|||||||||||patient member ID|...<cr>                
# insurance additional information                
                 Field('IN261','string', requires=IS_IN_DB(db, db.insurance_information.id,'%(patient_member_id)s',multiple=False), 
                      label='Patient Member ID'  ),      # present only if Insure ID number is not present or relationship is self  and insurance information is present
 #patient common  order information                
                 Field('ORC1','string', requires=IS_IN_DB(db, db.medication_order_information.id,'%(order_control)s',multiple=False), 
                      label='Order_control'  ),  # the value from the order filler are :DR, DU, XO, RF, and the values   from order prescriber are:NW, DC, XR, UX, AF, DF, RP, RO 
                Field('ORC12', 'string', requires=IS_IN_DB(db, db.medication_order_information.id,'%(order_provider)s',multiple=False), 
                      label='Order Provider'), 
                
#ORC|order control|||||||||||order provider|...<cr>
#There are duplicate of the same attribute but the code is for different form of the medicine, l
                 Field('RXD40', 'string', requires=IS_IN_DB(db, db.medication_order_information.id,'%(dispensing_pharmacy_name_and_identifier)s',multiple=False),
                       label='Dispensing to Pharmacy ID'), #When identifying a pharmacy, NCPDP Provider ID Numbers shall be employed and presented as OIDsThese fields have a data type of CWE. While it is atypical to represent an identifier as a coded concept, it can be by placing the OID extension in the Code Value and the OID root in the Name of Coding System. The NCPDP OID root is 2.16.840.1.113883.3.79
                 Field('RXE40', 'string', requires=IS_IN_DB(db, db.medication_order_information.id,'%(dispensing_pharmacy_name_and_identifier)s',multiple=False),
                       label='Dispensing Pharmacy'),
#choose one of the above                  
#RXD|||||||||||||||||||||||||||||||||||||||dispensing to pharmacy ID ( dispensing pharmacy)|...<cr>                 
                 Field('RXO5', 'string', requires=IS_IN_DB(db, db.prescription_medication.id,'%(product_form)s',multiple=False),
                       label='Requiested Dosage Form'), #
                 Field('RXE6', 'string', requires=IS_IN_DB(db, db.prescription_medication.id,'%(dose)s',multiple=False),
                       label='Give Dosage Form'), 
                 Field('RXD6', 'string', requires=IS_IN_DB(db, db.prescription_medication.id,'%(dose)s',multiple=False),
 
                      label='Actual Dosage Form') , 
#RXO||||requested dosage form|give dosage form|...<cr>
#choose one of th e above                       
                 Field('RXO14', 'string', requires=IS_IN_DB(db, db.medication_order_information.id,'%(order_provider)s',multiple=False),
                       label='Ordering Provider DEA Number(place)') , 
                Field('RXE13', 'string', requires=IS_IN_DB(db, db.medication_order_information.id,'%(order_provider)s',multiple=False), 
                       label='Ordering Provider DEA Number (filler)') ,   
                 Field('RXO19', 'string', requires=IS_IN_DB(db, db.prescription_medication.id,'%(product_concentration)s',multiple=False),
                       label='Requested Give Strength Units') ,          
                Field('RXO26', 'string', requires=IS_IN_DB(db, db.prescription_medication.id,'%(product_concentration)s',multiple=False),
                       label='Requested Drug Strength Volume Units') ,
                Field('RXC6', requires=IS_IN_DB(db, db.prescription_medication.id,'%(product_concentration)s',multiple=False), 
                       label='Component Strength Unit'), 
                Field('RXC9', requires=IS_IN_DB(db, db.prescription_medication.id,'%(product_concentration)s',multiple=False), 
                       label='Component Drug Strength Volume Units'),

#RXO||||||component strength unit|||||||Ordering Providers DEA Number(placer)|Ordering Providers DEA Number(filler)||||requested give strength units|...<cr>
#choose one from the above based on the prescription product_form of RXO5                       
                Field('RXE26', requires=IS_IN_DB(db, db.medication_order_information.id,'%(quantity_dispensed1)s',multiple=False),   
                       label='Give Strength Units'),#    
                Field('RXE34', requires=IS_IN_DB(db, db.medication_order_information.id,'%(quantity_dispensed1)s',multiple=False),  
                       label='Give Drug Strength Volume Units') ,#  
                Field('RXD29', requires=IS_IN_DB(db, db.medication_order_information.id,'%(quantity_dispensed1)s',multiple=False),  
                       label='Actual Drug Strength Volume Units'), 

#RXE||||||||||||||||||||||||||give strength units||actual drug strength volume uits|||||give drug strength vo;ume units|...<cr>
#choose one from the above based on the prescription product_form of RXO5                          
                active, created_by, created_on, 
                migrate=migrate)               

db.define_table('immunization_query_and_response', 
                Field('patient','reference patient',
                      default=session.patient_id,writable=True),
                
                Field('MSH4', 
                      label='Sending Facility'), 
                
                Field('MSH6', 
                      label='Receiving Facility'), 
                
                Field('PID6', 'string', requires=IS_IN_DB(db, db.patient.id,'%(mother_maiden_name)s',multiple=False), 
                      label='mother Maiden Name'),
                Field('PID7','string', requires=IS_IN_DB(db, db.patient.id,'%(date_of_birth)s',multiple=False), 
                      label='Date of Birth'),
                Field('PID8','string', requires=IS_IN_DB(db, db.patient.id,'%(gender)s',multiple=False), 
                      label='Administrative Sex'),
                Field('PID10','string', requires=IS_IN_DB(db, db.patient.id,'%(race)s',multiple=False), 
                      label='Race'),
                
                Field('PID22','string', requires=IS_IN_DB(db, db.patient.id,'%(ethnicity)s',multiple=False), 
                      label='Ethnic Group'  ), 
                Field('PID25','string', requires=IS_IN_DB(db, db.patient.id,'%(multiple_birth_indicator)s',multiple=False), 
                     label='Multiple Birth Indicator'),
                Field('PID26','string', requires=IS_IN_DB(db, db.patient.id,'%(birth_order)s',multiple=False), 
                      label='Birth Order'  ),    
                Field('PID23','string', requires=IS_IN_DB(db, db.patient.id,'%(birth_place)s',multiple=False), 
                     label='Birth Place'),
 #MSH|||| sending facility value||receiving facility|..<cr>
 #PID||||||mother Maiden Name|date of birth|administration sex||race||||||||||||ethnic group|birth place||multiple birth|birth order| 
 #note : birth place is code as |address^city^state^zipcode|
# PV120 = actual Table name PV1, and 20 is the Field index    
#NK12 = actual Table Name NK1 and 2 is the index of  one of its Field
                
                Field('PV120','string', requires=IS_IN_DB(db, db.immunization.id,'%(immunization_services_funding_eligibility)s',multiple=False), 
                      label='Immunization Services Funding Eligibility'  ),  
                Field('NK12','string', requires=IS_IN_DB(db, db.support.id,'%(contact_name)s',multiple=False), 
                      label='Name'  ),    
                Field('NK13','string', requires=IS_IN_DB(db, db.support.id,'%(contact_relationship)s',multiple=False), 
                      label='Relationship'  ), 
                 Field('NK120','string', requires=IS_IN_DB(db, db.support.id,'%(contact_language)s',multiple=False), 
                      label='Primary Language'  ),   
 
 #PV1||||||||||||||||||||immunization services funding eligibility|...<cr>
 #NK1||name|relationship|||||||||||||||||primary language|..<cr?
 #Below is the part  that is filled by the respnder
 #RXA15 = actual Table RXA and the number 15 is the index of one of its Field                
                 Field('RXA15', 'string', requires=IS_IN_DB(db, db.immunization.id,'%(lot_number)s',multiple=False),
                       label='Substance Lot Number'), #
                 Field('RXA17', 'string', requires=IS_IN_DB(db, db.immunization.id,'%(drug_manufacturer)s',multiple=False),
                       label='Substance Manufacturer'), 
                 Field('RXA5', 'string', requires=IS_IN_DB(db, db.immunization.id,'%(coded_product_name)s',multiple=False),
                       label='Administered Code') ,                     
                 Field('RXA9', 'string', requires=IS_IN_DB(db, db.immunization.id,'%(immunization_information_source)s',multiple=False),
                       label='Administration Notes') , 
                active, created_by, created_on,
                migrate=migrate)     
#RXA|||||administered code||||administration notes||||||substance lot number||sunstance manufacturer|...<cr>

"""
db.define_table('ehr_session',
                Field('locked', 'boolean', default=False),
                Field('client_ip'),                
                Field('unique_key'),
                Field('session_data', 'text'),migrate=migrate)

SECURITY_TABLES = [t for t in db.tables if t.startswith('auth_')]
AUXILIARY_TABLES = [t for t in db.tables if 'key' in db[t].fields]
DATA_TABLES = [t for t in db.tables if not t in SECURITY_TABLES + AUXILIARY_TABLES and not t=='patient']

db.define_table('patient_log',
                Field('patient','reference patient',default=session.patient_id,writable=True),
                Field('tablename','string'),
                Field('record_id','integer'),
                Field('message'),
                created_on)

for tablename in db.tables:
    table=db[tablename]
    for fieldname in table.fields:
        field=table[fieldname]
        if session.patient_id and field.type=='reference patient':
            field.default=session.patient_id
            field.writable=False

if request.vars.reset:
    for table in db:
        import os
        print 'loading',table
        if str(table)[:5]=='auth_': continue
        try:
            table.import_from_csv_file(open(os.path.join(request.folder,'private/table_%s.csv' % table),'r'))
            print table,'loaded'
        except Exception, e:
            raise e

def capitalize(text):
    return ' '.join([x.capitalize() for x in text[text.find('.')+1:].split('_')])

def pluralize(text):    
    if text.lower().endswith('data'):
        return text
    if text.lower().endswith('information'):
        return text
    if text.lower().endswith('y'):
        return text[:-1]+'ies'
    if text.lower().endswith('s'):
        return text+'es'
    return text+'s'

def smarttable(rows):
    headers = dict([(k,capitalize(k[k.find('.')+1:])) for k in rows.colnames])
    return SQLTABLE(rows,headers=headers,columns=headers,truncate=128,_class='smarttable')

if not db(db.race.id>0).count():
    initializer=local_import('initializer')
    initializer.initialize(db)

if not db(db.patient.id>0).count():    
    db.auth_user.insert(first_name='Massimo',
                        last_name='Di Pierro',
                        email='mdipierro@cs.depaul.edu',
                        status='Doctor',
                        password=db.auth_user.password.requires('test')[0])
    from gluon.contrib.populate import populate
    populate(db.patient,100)    
    db.commit()
    for tablename in DATA_TABLES:
        populate(db[tablename],100)
        db.commit()


def enforce_authorization(tablename,mode='read'):
    NURSE_TABLES = ['patient_social_history', 'advance_directives','vital_sign', 'medical_procedures',
                    'orders', 'specimen', 'lab_order','result_event_entry',
                    'prescription_medication','medication_order_information', 'drug_prescription_orders',
                    'genetic_result_values', 'family_member_history']
    ADMIN_TABLES = ['provider',
                    'payment_provider','insurance_information','subscriber_information',
                    'guarantor_or_insurance_provider_data', 'health_plan',
                    'encounters','support','appointment']                    
    if not auth.user:
        return False
    elif mode=='write':
        if auth.user.status=='Doctor': return True
        if auth.user.status=='Nurse' and tablename in NURSE_TABLES: return True
        if auth.user.status=='Administrator' and tablename in ADMIN_TABLES: return True
    elif mode=='read':
        if auth.user.status=='Doctor': return True
        if auth.user.status=='Nurse': return True
        if auth.user.status=='Administrator' and tablename in ADMIN_TABLES: return True
    return False
