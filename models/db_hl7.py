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
    format='%(description)s',migrate=migrate)

if not db(db.race.id>0).count():
    db.race.insert(key='1002-5',description='American Indian or Alaska Native')
    db.race.insert(key='2028-9',description='Asian')
    db.race.insert(key='2054-5',description='Black or African American')
    db.race.insert(key='2076-8',description='Native Hawaiian or Other Pacific Islander')
    db.race.insert(key='2106-3',description='White')
    db.race.insert(key='2131-1',description='Other race')

db.define_table('religious_affiliation',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.religious_affiliation.id>0).count():
    db.religious_affiliation.insert(key='ABC',description='Christian: American Baptist Church')
    db.religious_affiliation.insert(key='AGN',description='Agnostic')
    db.religious_affiliation.insert(key='AME',description='Christian: African Methodist Episcopal Zion')
    db.religious_affiliation.insert(key='AMT',description='Christian: African Methodist Episcopal')
    db.religious_affiliation.insert(key='ANG',description='Christian: Anglican')
    db.religious_affiliation.insert(key='AOG',description='Christian: Assembly of God')
    db.religious_affiliation.insert(key='ATH',description='Atheist')
    db.religious_affiliation.insert(key='BAH',description="Baha'i")
    db.religious_affiliation.insert(key='BAP',description='Christian: Baptist')
    db.religious_affiliation.insert(key='BMA',description='Buddhist: Mahayana')
    db.religious_affiliation.insert(key='BOT',description='Buddhist: Other')
    db.religious_affiliation.insert(key='BTA',description='Buddhist: Tantrayana')
    db.religious_affiliation.insert(key='BTH',description='Buddhist: Theravada')
    db.religious_affiliation.insert(key='BUD',description='Buddhist')
    db.religious_affiliation.insert(key='CAT',description='Christian: Roman Catholic')
    db.religious_affiliation.insert(key='CFR',description='Chinese Folk Religionist')
    db.religious_affiliation.insert(key='CHR',description='Christian')
    db.religious_affiliation.insert(key='CHS',description='Christian: Christian Science')
    db.religious_affiliation.insert(key='CMA',description='Christian: Christian Missionary Alliance')
    db.religious_affiliation.insert(key='CNF',description='Confucian')
    db.religious_affiliation.insert(key='NAZ',description='Christian: Church of the Nazarene')
    db.religious_affiliation.insert(key='NOE',description='Nonreligious')
    db.religious_affiliation.insert(key='NRL',description='New Religionist')
    db.religious_affiliation.insert(key='ORT',description='Christian: Orthodox')
    db.religious_affiliation.insert(key='OTH',description='Other')
    db.religious_affiliation.insert(key='PEN',description='Christian: Pentecostal')
    db.religious_affiliation.insert(key='PRC',description='Christian: Other Protestant')
    db.religious_affiliation.insert(key='PRE',description='Christian: Presbyterian')
    db.religious_affiliation.insert(key='PRO',description='Christian: Protestant')
    db.religious_affiliation.insert(key='QUA',description='Christian: Friends')
    db.religious_affiliation.insert(key='REC',description='Christian: Reformed Church')
    db.religious_affiliation.insert(key='REO',description='Christian: Reorganized Church of JesusChrist-LDS')
    db.religious_affiliation.insert(key='SAA',description='Christian: Salvation Army')
    db.religious_affiliation.insert(key='SEV',description='Christian: Seventh Day Adventist')
    db.religious_affiliation.insert(key='SHN',description='Shintoist')
    db.religious_affiliation.insert(key='SIK',description='Sikh')
    db.religious_affiliation.insert(key='SOU',description='Christian: Southern Baptist')
    db.religious_affiliation.insert(key='SPI',description='Spiritist')
    db.religious_affiliation.insert(key='UCC',description='Christian: United Church of Christ')
    db.religious_affiliation.insert(key='UMD',description='Christian: United Methodist')
    db.religious_affiliation.insert(key='UNI',description='Christian: Unitarian')
    db.religious_affiliation.insert(key='UNU',description='Christian: Unitarian Universalist')
    db.religious_affiliation.insert(key='VAR',description='Unknown')
    db.religious_affiliation.insert(key='WES',description='Christian: Wesleyan')
    db.religious_affiliation.insert(key='WMC',description='Christian: Wesleyan Methodist')

db.define_table('marital_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.marital_status.id>0).count():
    db.marital_status.insert(key='A',description='Separated')
    db.marital_status.insert(key='B',description='Unmarried')
    db.marital_status.insert(key='C',description='Common law')
    db.marital_status.insert(key='D',description='Divorced')
    db.marital_status.insert(key='E',description='Legally Separated')
    db.marital_status.insert(key='G',description='Living together')
    db.marital_status.insert(key='I',description='Interlocutory')
    db.marital_status.insert(key='M',description='Married')
    db.marital_status.insert(key='N',description='Annulled')
    db.marital_status.insert(key='O',description='Other')
    db.marital_status.insert(key='P',description='Domestic partner')
    db.marital_status.insert(key='R',description='Registered domestic partner')
    db.marital_status.insert(key='S',description='Single')
    db.marital_status.insert(key='T',description='Unreported')
    db.marital_status.insert(key='U',description='Unknown')
    db.marital_status.insert(key='W',description='Widowed')



db.define_table('gender',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.gender.id>0).count():
    db.gender.insert(key='A',description='Ambiguous')
    db.gender.insert(key='F',description='Female')
    db.gender.insert(key='M',description='Male')
    db.gender.insert(key='N',description='Not applicable')
    db.gender.insert(key='O',description='Other')
    db.gender.insert(key='U',description='Unknown')

db.define_table('appointment_reason_code',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.appointment_reason_code.id>0).count():
    db.appointment_reason_code.insert(key='CHECKUP',description='A routine check-up, such as an annual physical')
    db.appointment_reason_code.insert(key='EMERGENCY',description='Emergency appointment')
    db.appointment_reason_code.insert(key='FOLLOWUP',description='A follow up visit from a previous appointment')
    db.appointment_reason_code.insert(key='ROUTINE',description='Routine appointment - default if not valued')
    db.appointment_reason_code.insert(key='WALKIN',description='A previously unscheduled walk-in visit')

db.define_table('appointment_type_code',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
    
if not db(db.appointment_type_code.id>0).count():
    db.appointment_type_code.insert(key='Complete',description='A request to add a completed appointment, used to maintain records of completed appointments that did not appear in the schedule (e.g., STAT, walk-in, etc.)')
    db.appointment_type_code.insert(key='Normal',description='Routine schedule request type - default if notvalued')
    db.appointment_type_code.insert(key='Tentative',description='A request for a tentative (e.g., "penciled in") appointment')    

db.define_table('language_ability',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.language_ability.id>0).count():
    db.language_ability.insert(key='ESGN',description='Express Signed')
    db.language_ability.insert(key='ESP',description='Expressed Spoken')
    db.language_ability.insert(key='EWR',description='Expressed Written')
    db.language_ability.insert(key='RSGN',description='Received Signed')
    db.language_ability.insert(key='RSP',description='Received Spoken')
    db.language_ability.insert(key='RWR',description='Received Written')

db.define_table('language_proficiency',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.language_proficiency.id>0).count():
    db.language_proficiency.insert(key='1',description='Excellent')
    db.language_proficiency.insert(key='2',description='Good')
    db.language_proficiency.insert(key='3',description='Fair')
    db.language_proficiency.insert(key='4',description='Poor')
    db.language_proficiency.insert(key='5',description='Some (level unknown)')
    db.language_proficiency.insert(key='6',description='None')

db.define_table('contact_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.contact_type.id>0).count():
    db.contact_type.insert(key='C',description='Emergency Contact')
    db.contact_type.insert(key='E',description='Employer')
    db.contact_type.insert(key='F',description='Federal Agency')
    db.contact_type.insert(key='I',description='Insurance Company')
    db.contact_type.insert(key='N',description='Next-of-Kin')
    db.contact_type.insert(key='O',description='Other')
    db.contact_type.insert(key='S',description='State Agency')
    db.contact_type.insert(key='U',description='Unknown')

db.define_table('relationship_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.relationship_type.id>0).count():
    db.relationship_type.insert(key='ASC',description='Associate')
    db.relationship_type.insert(key='BRO',description='Brother')
    db.relationship_type.insert(key='CGV',description='Care giver')
    db.relationship_type.insert(key='CHD',description='Child')
    db.relationship_type.insert(key='DEP',description='Handicapped dependent')
    db.relationship_type.insert(key='DOM',description='Life partner')
    db.relationship_type.insert(key='EMC',description='Emergency contact')
    db.relationship_type.insert(key='EME',description='Employee')
    db.relationship_type.insert(key='EMR',description='Employer')
    db.relationship_type.insert(key='EXF',description='Extended family')
    db.relationship_type.insert(key='FCH',description='Foster child')
    db.relationship_type.insert(key='FND',description='Friend')
    db.relationship_type.insert(key='FTH',description='Father')
    db.relationship_type.insert(key='GCH',description='Grandchild')
    db.relationship_type.insert(key='GRD',description='Guardian')
    db.relationship_type.insert(key='GRP',description='Grandparent')
    db.relationship_type.insert(key='MGR',description='Manager')
    db.relationship_type.insert(key='MTH',description='Mother')
    db.relationship_type.insert(key='NCH',description='Natural child')
    db.relationship_type.insert(key='NON',description='None')
    db.relationship_type.insert(key='OAD',description='Other adult')
    db.relationship_type.insert(key='OTH',description='Other')
    db.relationship_type.insert(key='OWN',description='Owner')
    db.relationship_type.insert(key='PAR',description='Parent')
    db.relationship_type.insert(key='SCH',description='Stepchild')
    db.relationship_type.insert(key='SEL',description='Self')
    db.relationship_type.insert(key='SIB',description='Sibling')
    db.relationship_type.insert(key='SIS',description='Sister')
    db.relationship_type.insert(key='SPO',description='Spouse')
    db.relationship_type.insert(key='TRA',description='Trainer')
    db.relationship_type.insert(key='UNK',description='Unknown')
    db.relationship_type.insert(key='WRD',description='Ward of court')
    db.relationship_type.insert(key='FSTUD',description='Full Time Student')
    db.relationship_type.insert(key='PSTUD',description='Part Time Student')
    db.relationship_type.insert(key='STUD',description='Student')
    db.relationship_type.insert(key='SPON',description='Sponsored Dependent')
    db.relationship_type.insert(key='INJ',description='Inhured Plantiff')
    db.relationship_type.insert(key='HANDIC',description='Handicapped Dependent')

db.define_table('provider_role1',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.provider_role1.id>0).count():
    db.provider_role1.insert(key='AD',description='Admitting')
    db.provider_role1.insert(key='AT',description='Attending')
    db.provider_role1.insert(key='CP',description='Consulting Provider')
    db.provider_role1.insert(key='FHCP',description='Family Health Care Professional')
    db.provider_role1.insert(key='PP',description='Primary Care Provider')
    db.provider_role1.insert(key='RP',description='Referring Provider')
    db.provider_role1.insert(key='RT',description='Referred to Provider')

db.define_table('provider_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.provider_type.id>0).count():
    db.provider_type.insert(key =' Behavioral Health and & Social Service Providers  ',    description=' Broad classification aggregating providers who are trained and educated to perform services related to behavioral health, mental health, and counseling and may be licensed or practice within the scope or licensure or training')                                                                
    db.provider_type.insert(key =' Chiropractic Providers  ',  description=' A provider qualified by a Doctor of Chiropractic (D.C.), licensed by the State and who practices chiropractic medicine -that discipline within the healing arts which deals with the nervous system and its relationship to the spinal column and its interrelationship with other body systems')                                                                
    db.provider_type.insert(key =' Dental Providers  ', description=' Broad category to identify practitioners who render services related the practice of dentistry. Dentistry is defined as the evaluation, diagnosis, prevention and/or treatment (nonsurgical, surgical or related procedures) of diseases, disorders and/or conditions of the oral cavity, maxillofacial area and/or the adjacent and associated structures and their impact on the human body; provided by a dentist, within the scope of his/her education, training and experience, in accordance with the ethics of the profession and applicable law')                                                               
    db.provider_type.insert(key ='Dietary and Nutritional Service Providers ',   description=' Broad category defining practitioners who help prevent and treat illness by promoting healthy eating habits, scientifically evaluating diets and suggesting modifications. They may also assess the nutritional needs of patients, develop and implement nutritional care plans')                                                               
    db.provider_type.insert(key ='Emergency Medical Service Providers',  description='Broad category for individuals who complete additional training and education in the area of pre-hospital emergency services and are licensed and/or practice within the scope of that training')                                                               
    db.provider_type.insert(key ='Eye and Vision Service Providers', description='Broad category grouping individuals who renders services related to the human eye and visual systems, but are not an allopathic or osteopathic physicians')                                                               
    db.provider_type.insert(key ='Nursing Service Providers',    description='Providers who are trained and educated to perform and administer services related to health promotion, disease prevention, acute and chronic care, spiritual guidance and comfort for healing and health, restoration of health and health maintenance across the life span')                                                               
    db.provider_type.insert(key ='Pharmacy Service Providers (Individuals)', description='A broad category grouping providers who render services relating to the preparation and dispensing of drugs ')                                                              
    db.provider_type.insert(key ='Allopathic & Osteopathic Physicians',  description='A broad category grouping state licensed providers in allopathic or osteopathic medicine whose scope of practice is determined by education')                                                               
    db.provider_type.insert(key ='Podiatric Medicine and Surgery Providers', description='Broad category grouping licensed providers who renders services related to the human foot')                                                                  
    db.provider_type.insert(key ='Speech, Language and Hearing Providers',   description='    A provider who renders services to improve communicative skills of people with language, speech and hearing impairments ')                                                                                                           
    db.provider_type.insert(key ='Agencies ',   description=' A non-facility provider that renders outpatient outreach services that are not provided at a specific location. The licensure or registration is assigned to the agency rather than to the individual practitioners as would be the case in a group practice ')                                                                                                                
    db.provider_type.insert(key ='Ambulatory Health Care Facilities',    description='A facility or distinct part of one used for the diagnosis and treatment of outpatients. "Clinic/Center" is irregularly defined, sometimes being limited to organizations serving specialized treatment requirements or distinct patient/client groups (e.g., radiology, poor, and public health) ')                                                                                                                
    db.provider_type.insert(key ='Hospitals',   description='A health care organization that has a governing body, an organized medical staff and professional staff and inpatient facilities and provides medical nursing and related services for ill and injured patients 24 hrs per day, seven days per week. For licensing purposes, each state has its own definition of hospital')                                                                                                       
    db.provider_type.insert(key ='Laboratories',    description='A room or building equipped for scientific experimentation, research, testing, or clinical studies of materials, fluids, or tissues obtained from patients ')                                                                                                              
    db.provider_type.insert(key ='Managed Care Organizations ',     description='Not Available  ')                                                                                                             
    db.provider_type.insert(key ='Nursing and &Custodial Care Facilities ',  description='Broad category identifying licensed facilities with inpatient beds specializing in nursing and custodial careNot Available  ')                                                                                                             
    db.provider_type.insert(key ='Residential Treatment Facilities ',    description='Live in facilities where patients or clients, who because of their physical, mental, or emotional condition, are not able to live independently, and who receive treatment appropriate to their particular needs in a less restrictive environment than an inpatient facility. For example, an RTC may provide educational training and therapy for children with emotional disturbances or continuing care and therapy for people with severe mental handicaps')                                                                                                              
    db.provider_type.insert(key ='Suppliers (including Pharmacies and Durable Medical Equipment) ',     description='    Suppliers, pharmacies, and other health care providers who supply health care related products or medications and associated professional and administrative services')                                                                                                                
    db.provider_type.insert(key ='Physician Assistants and &Advanced Practice Nursing Providers ',   description='    A broad grouping of providers who are: 1) trained, educated, and certified to perform basic medical and minor surgical services (or to assist the physician in performance of more complex services) under general physician supervision; and 2) trained, educated at a post-graduate level, and certified to perform autonomous and specialized roles as nurse practitioners, midwives, nurse anesthetists, or clinical nurse specialists')                                                                                                               
    db.provider_type.insert(key ='Nursing Service Related Providers ',   description='Providers not otherwise classified, who perform or administer services in or related to the delivery or research of health care services, disease, and restoration of health. An individual provider who is not represented in one of the identified categories but whose data may be needed for clinical, operational or administrative processes')                                                                                                               
    db.provider_type.insert(key ='Respite Care Facility',    description=' A facility with dorm rooms where individuals who are unable to care for themselves may stay on a short term basis overnight to allow relief to persons normally providing care to them.Not Available')                                                                                                         



db.define_table('advance_directive_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.advance_directive_type.id>0).count():
    db.advance_directive_type.insert(key='304251008',description='Resuscitation ')
    db.advance_directive_type.insert(key='52765003',description='Intubation ')
    db.advance_directive_type.insert(key='225204009',description='IV Fluid and Support')
    db.advance_directive_type.insert(key='89666000',description='CPR')
    db.advance_directive_type.insert(key='281789004',description='Antibiotics ')
    db.advance_directive_type.insert(key='78823007',description='Life Support ')    
    
db.define_table('advance_beneficiary_notice',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.advance_beneficiary_notice.id>0).count():
    db.advance_beneficiary_notice.insert(key='1',description='Service is subject to medical necessity procedures')
    db.advance_beneficiary_notice.insert(key='2',description='Patient has been informed of responsibility,and agrees to pay for service')
    db.advance_beneficiary_notice.insert(key='3',description='Patient has been informed of responsibility,and asks that the payer be billed')
    db.advance_beneficiary_notice.insert(key='4',description='Advanced Beneficiary Notice has not been signed')

db.define_table('social_history',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.social_history.id>0).count():    
    db.social_history.insert(key='229819007', description='Tobacco use and exposure (observable entity) Not available Smoking')
    db.social_history.insert(key='256235009', description='Exercise (observable entity) Not available Exercise')
    db.social_history.insert(key='364393001', description='Nutritional observable (observable entity) Not available Diet')
    db.social_history.insert(key='364703007', description='Employment detail (observable entity) Not available Employment')
    db.social_history.insert(key='425400000', description='Toxic exposure status (observable entity) Not available Toxic Exposure')
    db.social_history.insert(key='363908000', description='Details of drug misuse behavior (observable entity) Not available Drug Use')
    db.social_history.insert(key='228272008', description='Health-related behavior (observable entity) Not available Other Social History')


db.define_table('health_insurance_plan',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.health_insurance_plan.id>0).count():    
    db.health_insurance_plan.insert(key='12' , description='Medicare Secondary Working Aged Beneficiary or Spouse with Employer Group Health Plan')
    db.health_insurance_plan.insert(key='13', description='Medicare Secondary End-Stage Renal Disease Beneficiary in the 12 month coordination period with an employer’s group health plan')
    db.health_insurance_plan.insert(key='14', description=' Medicare Secondary, No-fault Insurance including Auto is Primary')
    db.health_insurance_plan.insert(key='15', description=' Medicare Secondary Worker’s Compensation')
    db.health_insurance_plan.insert(key='16', description=' Medicare Secondary Public Health Service (PHS)or Other Federal Agency')
    db.health_insurance_plan.insert(key='41', description=' Medicare Secondary Black Lung')
    db.health_insurance_plan.insert(key='42', description=' Medicare Secondary Veteran’s Administration')
    db.health_insurance_plan.insert(key='43', description=' Medicare Secondary Disabled Beneficiary Under Age 65 with Large Group Health Plan (LGHP)')
    db.health_insurance_plan.insert(key='47', description=' Medicare Secondary, Other Liability Insurance is Primary')
    db.health_insurance_plan.insert(key='AP', description=' Auto Insurance Policy')
    db.health_insurance_plan.insert(key='C1', description=' Commercial')
    db.health_insurance_plan.insert(key='CO', description=' Consolidated Omnibus Budget Reconciliation Act (COBRA)')
    db.health_insurance_plan.insert(key='CP', description=' Medicare Conditionally Primary')
    db.health_insurance_plan.insert(key='D', description=' Disability')
    db.health_insurance_plan.insert(key='DB', description=' Disability Benefits')
    db.health_insurance_plan.insert(key='EP', description=' Exclusive Provider Organization')
    db.health_insurance_plan.insert(key='FF', description=' Family or Friends')
    db.health_insurance_plan.insert(key='GP', description=' Group Policy')
    db.health_insurance_plan.insert(key='HM', description=' Health Maintenance Organization (HMO)')
    db.health_insurance_plan.insert(key='HN', description=' Health Maintenance Organization (HMO) - Medicare Risk')
    db.health_insurance_plan.insert(key='HS', description=' Special Low Income Medicare Beneficiary')
    db.health_insurance_plan.insert(key='IN', description=' Indemnity')
    db.health_insurance_plan.insert(key='IP', description=' Individual Policy')
    db.health_insurance_plan.insert(key='LC', description=' Long Term Care')
    db.health_insurance_plan.insert(key='LD', description=' Long Term Policy')
    db.health_insurance_plan.insert(key='LI', description=' Life Insurance')
    db.health_insurance_plan.insert(key='LT', description=' Litigation')
    db.health_insurance_plan.insert(key='MA', description=' Medicare Part A')
    db.health_insurance_plan.insert(key='MB', description=' Medicare Part B')
    db.health_insurance_plan.insert(key='MC', description=' Medicaid')
    db.health_insurance_plan.insert(key='MH', description=' Medigap Part A')
    db.health_insurance_plan.insert(key='MI', description=' Medigap Part B')
    db.health_insurance_plan.insert(key='MP', description=' Medicare Primary')
    db.health_insurance_plan.insert(key='OT', description=' Other')
    db.health_insurance_plan.insert(key='PE', description=' Property Insurance - Personal')
    db.health_insurance_plan.insert(key='PL', description=' Personal')
    db.health_insurance_plan.insert(key='PP', description=' Personal Payment (Cash - No Insurance)')
    db.health_insurance_plan.insert(key='PR', description=' Preferred Provider Organization (PPO)')
    db.health_insurance_plan.insert(key='PS', description=' Point of Service (POS)')
    db.health_insurance_plan.insert(key='QM', description=' Qualified Medicare Beneficiary')
    db.health_insurance_plan.insert(key='RP', description=' Property Insurance - Real')
    db.health_insurance_plan.insert(key='SP', description=' Supplemental Policy')
    db.health_insurance_plan.insert(key='TF', description=' Tax Equity Fiscal Responsibility Act (TEFRA)')
    db.health_insurance_plan.insert(key='WC', description=' Workers Compensation')
    db.health_insurance_plan.insert(key='WU', description=' Wrap Up Policy')
 
 
db.define_table('problem_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.problem_type.id>0).count():     
    db.problem_type.insert(key='404684003', description='Clinical finding (finding)')
    db.problem_type.insert(key='418799008', description='Finding reported by subject or history provider (finding)- Symptom') 
    db.problem_type.insert(key='55607006', description='Problem (finding)') 
    db.problem_type.insert(key='409586006', description='Complaint (finding)') 
    db.problem_type.insert(key='64572001', description='Disease (disorder)-Condition') 
    db.problem_type.insert(key='282291009', description='Diagnosis interpretation (observable entity)') 
    db.problem_type.insert(key='248536006', description='Finding of functional performance and activity (finding)') 
db.define_table('adverse_event_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.adverse_event_type.id>0).count():        
    db.adverse_event_type.insert(key='420134006', description=' Propensity to adverse reactions (disorder)') 
    db.adverse_event_type.insert(key='418038007', description=' Propensity to adverse reactions to substance (disorder)') 
    db.adverse_event_type.insert(key='419511003', description=' Propensity to adverse reactions to drug (disorder)') 
    db.adverse_event_type.insert(key='418471000', description=' Propensity to adverse reactions to food (disorder)') 
    db.adverse_event_type.insert(key='419199007', description=' Allergy to substance (disorder)') 
    db.adverse_event_type.insert(key='416098002', description=' Drug allergy (disorder)') 
    db.adverse_event_type.insert(key='414285001', description=' Food allergy (disorder)') 
    db.adverse_event_type.insert(key='59037007', description='  Drug intolerance (disorder)') 
    db.adverse_event_type.insert(key='235719002', description=' Food intolerance (disorder)') 
    
db.define_table('severity',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.severity.id>0).count():
    db.severity.insert(key='255604002',description='Mild')
    db.severity.insert(key='371923003',description='Mild to Moderate')
    db.severity.insert(key='6736007 ',description='Moderate')
    db.severity.insert(key='371924009',description='Moderate to Severe')
    db.severity.insert(key='24484000',description='Severe')
    db.severity.insert(key='399166001',description='Fatal')
    
db.define_table('problem_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.problem_status.id>0).count():   
    db.problem_status.insert(key='55561003',description='Active') 
    db.problem_status.insert(key='73425007',description='Inactive') 
    db.problem_status.insert(key='413322009',description='Resolved')
    
db.define_table('diagnosis_priority',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.diagnosis_priority.id>0).count():     
    db.diagnosis_priority.insert(key='0 ',description='Not included in diagnosis ranking') 
    db.diagnosis_priority.insert(key='1',description=' The primary diagnosis') 
    db.diagnosis_priority.insert(key='2 or more',description=' For ranked secondary diagnosesRanks the secondarily diagnoses and could be multiple numbers, 2, 3, 4, etc')



db.define_table('no_immunization_reason',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.no_immunization_reason.id>0).count():    
    db.no_immunization_reason.insert(key='IMMUNE',description=' Immunity Testing has shown that the patient already has immunity to the agent targeted by theimmunization')
    db.no_immunization_reason.insert(key='MEDPREC',description=' Medical precaution The patient currently has a medical condition for which the vaccine is contraindicated orfor which precaution is warranted')
    db.no_immunization_reason.insert(key='OSTOCK',description=' Out of stock There was no supply of the product on hand to perform the service')
    db.no_immunization_reason.insert(key='PATOBJ',description=' Patient objection The patient or their guardian objects to receiving the vaccine')
    db.no_immunization_reason.insert(key='PHILISOP',description=' Philosophical objection The patient or their guardian objects to receiving the vaccine because of philosophical beliefs')
    db.no_immunization_reason.insert(key='RELIG',description=' Religious objection The patient or their guardian objects to receiving the vaccine on religious grounds')
    db.no_immunization_reason.insert(key='VACEFF',description=' Vaccine efficacy concerns The intended vaccine has expired or is otherwise believed to no longer be effective Example: Due to temperature exposure')
    db.no_immunization_reason.insert(key='VACSAF',description=' Vaccine safety concerns The patient or their guardian objects to receiving the vaccine because of concerns over its  safety')
db.define_table('immunization_information_source',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.immunization_information_source.id>0).count():   
     db.immunization_information_source.insert(key='00',description='New immunization record')
     db.immunization_information_source.insert(key='01',description=' Historical information - source unspecified')
     db.immunization_information_source.insert(key='02',description=' Historical information - from other provider')
     db.immunization_information_source.insert(key='03',description=' Historical information - from parent’s written record')
     db.immunization_information_source.insert(key='04',description=' Historical information - from parent’s recall')
     db.immunization_information_source.insert(key='05',description=' Historical information - from other registry')
     db.immunization_information_source.insert(key='06',description=' Historical information - from birth certificate')
     db.immunization_information_source.insert(key='07',description=' Historical information - from school record')
     db.immunization_information_source.insert(key='08',description=' Historical information - from public agency')
     
     
db.define_table('administered_vaccine',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.administered_vaccine.id>0).count():
    db.administered_vaccine.insert(key='01',description='DTP')
    db.administered_vaccine.insert(key='02',description='OPV')
    db.administered_vaccine.insert(key='03',description='MMR')
    db.administered_vaccine.insert(key='04',description='M/R')
    db.administered_vaccine.insert(key='05',description='measles')
    db.administered_vaccine.insert(key='06',description='rubella')
    db.administered_vaccine.insert(key='07',description='mumps')
    db.administered_vaccine.insert(key='08',description='Hep B, adolescent or pediatric')
    db.administered_vaccine.insert(key='09',description='Td (adult)')
    db.administered_vaccine.insert(key='10',description='IPV')
    db.administered_vaccine.insert(key='100',description='pneumococcal conjugate')
    db.administered_vaccine.insert(key='101',description='typhoid, ViCPs')
    db.administered_vaccine.insert(key='102',description='DTP-Hib-Hep B')
    db.administered_vaccine.insert(key='103',description='meningococcal C conjugate')
    db.administered_vaccine.insert(key='104',description='Hep A-Hep B')
    db.administered_vaccine.insert(key='105',description='smallpox, diluted')
    db.administered_vaccine.insert(key='106',description='DTaP, 5 pertussis antigens')
    db.administered_vaccine.insert(key='107',description='DTaP, NOS')
    db.administered_vaccine.insert(key='108',description='meningococcal, NOS')
    db.administered_vaccine.insert(key='109',description='pneumococcal, NOS')
    db.administered_vaccine.insert(key='11',description='pertussis')
    db.administered_vaccine.insert(key='12',description='diphtheria antitoxin')
    db.administered_vaccine.insert(key='13',description='TIG')
    db.administered_vaccine.insert(key='14',description='IG, NOS')
    db.administered_vaccine.insert(key='15',description='influenza, split (incl. purified surface antigen)')
    db.administered_vaccine.insert(key='16',description='influenza, whole')
    db.administered_vaccine.insert(key='17',description='Hib, NOS')
    db.administered_vaccine.insert(key='18',description='rabies, intramuscular injection')
    db.administered_vaccine.insert(key='19',description='BCG')
    db.administered_vaccine.insert(key='20',description='DTaP')
    db.administered_vaccine.insert(key='21',description='Varicella')
    db.administered_vaccine.insert(key='22',description='DTP-Hib')
    db.administered_vaccine.insert(key='23',description='plague')
    db.administered_vaccine.insert(key='24',description='anthrax')
    db.administered_vaccine.insert(key='25',description='typhoid, oral')
    db.administered_vaccine.insert(key='26',description='cholera')
    db.administered_vaccine.insert(key='27',description='botulinum antitoxin')
    db.administered_vaccine.insert(key='28',description='DT (pediatric)')
    db.administered_vaccine.insert(key='29',description='CMVIG')
    db.administered_vaccine.insert(key='30',description='HBIG')
    db.administered_vaccine.insert(key='31',description='Hep A, pediatric, NOS')
    db.administered_vaccine.insert(key='32',description='meningococcal')
    db.administered_vaccine.insert(key='33',description='pneumococcal')
    db.administered_vaccine.insert(key='34',description='RIG')
    db.administered_vaccine.insert(key='35',description='tetanus toxoid')
    db.administered_vaccine.insert(key='36',description='VZIG')
    db.administered_vaccine.insert(key='37',description='yellow fever')
    db.administered_vaccine.insert(key='38',description='rubella/mumps')
    db.administered_vaccine.insert(key='39',description='Japanese encephalitis')
    db.administered_vaccine.insert(key='40',description='rabies, intradermal injection')
    db.administered_vaccine.insert(key='41',description='typhoid, parenteral')
    db.administered_vaccine.insert(key='42',description='Hep B, adolescent/high risk infant2')
    db.administered_vaccine.insert(key='43',description='Hep B, adult4')
    db.administered_vaccine.insert(key='44',description='Hep B, dialysis')
    db.administered_vaccine.insert(key='45',description='Hep B, NOS')
    db.administered_vaccine.insert(key='46',description='Hib (PRP-D)')
    db.administered_vaccine.insert(key='47',description='Hib (HbOC)')
    db.administered_vaccine.insert(key='48',description='Hib (PRP-T)')
    db.administered_vaccine.insert(key='49',description='Hib (PRP-OMP)')
    db.administered_vaccine.insert(key='50',description='DTaP-Hib')
    db.administered_vaccine.insert(key='51',description='Hib-Hep B')
    db.administered_vaccine.insert(key='52',description='Hep A, adult')
    db.administered_vaccine.insert(key='53',description='typhoid, parenteral, AKD (U.S. military)')
    db.administered_vaccine.insert(key='54',description='adenovirus, type 4')
    db.administered_vaccine.insert(key='55',description='adenovirus, type 7')
    db.administered_vaccine.insert(key='56',description='dengue fever')
    db.administered_vaccine.insert(key='57',description='hantavirus')
    db.administered_vaccine.insert(key='58',description='Hep C')
    db.administered_vaccine.insert(key='59',description='Hep E')
    db.administered_vaccine.insert(key='60',description='herpes simplex 2')
    db.administered_vaccine.insert(key='61',description='HIV')
    db.administered_vaccine.insert(key='62',description='HPV')
    db.administered_vaccine.insert(key='63',description='Junin virus')
    db.administered_vaccine.insert(key='64',description='leishmaniasis')
    db.administered_vaccine.insert(key='65',description='leprosy')
    db.administered_vaccine.insert(key='66',description='Lyme disease')
    db.administered_vaccine.insert(key='67',description='malaria')
    db.administered_vaccine.insert(key='68',description='melanoma')
    db.administered_vaccine.insert(key='69',description='parainfluenza-3')
    db.administered_vaccine.insert(key='70',description='Q fever')
    db.administered_vaccine.insert(key='71',description='RSV-IGIV')
    db.administered_vaccine.insert(key='72',description='rheumatic fever')
    db.administered_vaccine.insert(key='73',description='Rift Valley fever')
    db.administered_vaccine.insert(key='74',description='rotavirus')
    db.administered_vaccine.insert(key='75',description='smallpox')
    db.administered_vaccine.insert(key='76',description='Staphylococcus bacterio lysate')
    db.administered_vaccine.insert(key='77',description='tick-borne encephalitis')
    db.administered_vaccine.insert(key='78',description='tularemia vaccine')
    db.administered_vaccine.insert(key='79',description='vaccinia immune globulin')
    db.administered_vaccine.insert(key='80',description='VEE, live')
    db.administered_vaccine.insert(key='81',description='VEE, inactivated')
    db.administered_vaccine.insert(key='82',description='adenovirus, NOS1')
    db.administered_vaccine.insert(key='83',description='Hep A, ped/adol, 2 dose')
    db.administered_vaccine.insert(key='84',description='Hep A, ped/adol, 3 dose')
    db.administered_vaccine.insert(key='85',description='Hep A, NOS')
    db.administered_vaccine.insert(key='86',description='IG')
    db.administered_vaccine.insert(key='87',description='IGIV')
    db.administered_vaccine.insert(key='88',description='influenza, NOS')
    db.administered_vaccine.insert(key='89',description='polio, NOS')
    db.administered_vaccine.insert(key='90',description='rabies, NOS')
    db.administered_vaccine.insert(key='91',description='typhoid, NOS')
    db.administered_vaccine.insert(key='92',description='VEE, NOS')
    db.administered_vaccine.insert(key='93',description='RSV-MAb')
    db.administered_vaccine.insert(key='94',description='MMRV')
    db.administered_vaccine.insert(key='95',description='TST-OT tine test')
    db.administered_vaccine.insert(key='96',description='TST-PPD intradermal')
    db.administered_vaccine.insert(key='97',description='TST-PPD tine test')
    db.administered_vaccine.insert(key='98',description='TST, NOS')
    db.administered_vaccine.insert(key='99',description='RESERVED _ do not use')
    db.administered_vaccine.insert(key='998',description='no vaccine administered')
    db.administered_vaccine.insert(key='999',description='Unknown')


db.define_table('drug_manufacturer',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.drug_manufacturer.id>0).count():
    db.drug_manufacturer.insert(key='AB',description='Abbott Laboratories')
    db.drug_manufacturer.insert(key='AD',description='Adams Laboratories, Inc.')
    db.drug_manufacturer.insert(key='ALP',description='Alpha Therapeutic Corporation')
    db.drug_manufacturer.insert(key='AR',description='Armour')
    db.drug_manufacturer.insert(key='AVB',description='Aventis Behring L.L.C.')
    db.drug_manufacturer.insert(key='AVI',description='Aviron')
    db.drug_manufacturer.insert(key='BA',description='Baxter Healthcare Coporation]')
    db.drug_manufacturer.insert(key='BAH',description='Baxter Health Corporation')
    db.drug_manufacturer.insert(key='BAY',description='Bayer Corporation')
    db.drug_manufacturer.insert(key='BP',description='Berna Products')
    db.drug_manufacturer.insert(key='BPC',description='Berna Products Corporation')
    db.drug_manufacturer.insert(key='CEN',description='Centeon L.L.C.')
    db.drug_manufacturer.insert(key='CHI',description='Chiron Corporation')
    db.drug_manufacturer.insert(key='CMP',description='Celltech Medeva Pharmaceuticals')
    db.drug_manufacturer.insert(key='CON',description='Connaught')
    db.drug_manufacturer.insert(key='EVN',description='Evans Medical Limited')
    db.drug_manufacturer.insert(key='GRE',description='Greer Laboratories, Inc.')
    db.drug_manufacturer.insert(key='IAG',description='Immuno International AG')
    db.drug_manufacturer.insert(key='IM',description='Merieux')
    db.drug_manufacturer.insert(key='IUS',description='Immuno-U.S., Inc.')
    db.drug_manufacturer.insert(key='JPN',description='The Research Foundation for Microbial Diseases of Osaka University')
    db.drug_manufacturer.insert(key='KGC',description='Korea Green Cross Corporation')
    db.drug_manufacturer.insert(key='LED',description='Lederle')
    db.drug_manufacturer.insert(key='MA',description='Massachusetts Public Health Biologic Laboratories')
    db.drug_manufacturer.insert(key='MBL',description='Massachusetts Biologic Laboratories')
    db.drug_manufacturer.insert(key='MED',description='MedImmune, Inc.')
    db.drug_manufacturer.insert(key='MIL',description='Miles')
    db.drug_manufacturer.insert(key='MIP',description='Bioport Corporation')
    db.drug_manufacturer.insert(key='MSD',description='Merck & Co., Inc.')
    db.drug_manufacturer.insert(key='NAB',description='NABI')
    db.drug_manufacturer.insert(key='NAV',description='North American Vaccine, Inc.')
    db.drug_manufacturer.insert(key='NOV',description='Novartis Pharmaceutical Corporation')
    db.drug_manufacturer.insert(key='NYB',description='New York Blood Center')
    db.drug_manufacturer.insert(key='ORT',description='Ortho-Clinical Diagnostics.')
    db.drug_manufacturer.insert(key='OTC',description='Organon Teknika Corporation')
    db.drug_manufacturer.insert(key='OTH',description='Other manufacturer')
    db.drug_manufacturer.insert(key='PD',description='Parkedale Pharmaceuticals')
    db.drug_manufacturer.insert(key='PMC',description='Aventis Pasteur Inc.')
    db.drug_manufacturer.insert(key='PRX',description='Praxis Biologics')
    db.drug_manufacturer.insert(key='PWJ',description='PowerJect Pharamaceuticals')
    db.drug_manufacturer.insert(key='SCL',description='Sclavo, Inc.')
    db.drug_manufacturer.insert(key='SI',description='Swiss Serum and Vaccine Inst.')
    db.drug_manufacturer.insert(key='SKB',description='GlaxoSmithKline')
    db.drug_manufacturer.insert(key='UNK',description='Unknown manufacturer')
    db.drug_manufacturer.insert(key='USA',description='United States Army Medical Research andMaterial Command')
    db.drug_manufacturer.insert(key='WA',description='Wyeth-Ayerst')
    db.drug_manufacturer.insert(key='WAL',description='Wyeth-Ayerst')



db.define_table('vital_sign_result',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.vital_sign_result.id>0).count():    
    db.vital_sign_result.insert(key='9279-1',description=' Respiratory Rate')
    db.vital_sign_result.insert(key='8867-4',description=' Heart Rate') 
    db.vital_sign_result.insert(key='2710-2',description=' O2 % BldC Oximetry') 
    db.vital_sign_result.insert(key='8480-6',description=' BP Systolic') 
    db.vital_sign_result.insert(key='8462-4',description=' BP Diastolic')
    db.vital_sign_result.insert(key='8310-5',description=' Body Temperature Body')
    db.vital_sign_result.insert(key='8302-2',description=' Height')
    db.vital_sign_result.insert(key='8306-3',description=' Height (Lying)') 
    db.vital_sign_result.insert(key='8287-5',description=' Head Circumference')
    db.vital_sign_result.insert(key='3141-9',description=' Weight Measured') 
   
db.define_table('diagnosis_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.diagnosis_type.id>0).count():   
    db.diagnosis_type .insert(key='A',description='Admitting')
    db.diagnosis_type .insert(key='F',description=' Final') 
    db.diagnosis_type .insert(key='W',description=' Working') 

db.define_table('body_site',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.body_site.id>0).count():
    db.body_site.insert(key='BE',description='Bilateral Ears')
    db.body_site.insert(key='BN',description='Bilateral Nares')
    db.body_site.insert(key='BU',description='Buttock')
    db.body_site.insert(key='CT',description='Chest Tube')
    db.body_site.insert(key='LA',description='Left Arm')
    db.body_site.insert(key='LAC',description='Left Anterior Chest')
    db.body_site.insert(key='LACF',description='Left Antecubital Fossa')
    db.body_site.insert(key='LD',description='Left Deltoid')
    db.body_site.insert(key='LE',description='Left Ear')
    db.body_site.insert(key='LEJ',description='Left External Jugular')
    db.body_site.insert(key='LF',description='Left Foot')
    db.body_site.insert(key='LG',description='Left Gluteus Medius')
    db.body_site.insert(key='LH',description='Left Hand')
    db.body_site.insert(key='LIJ',description='Left Internal Jugular')
    db.body_site.insert(key='LLAQ',description='Left Lower Abd Quadrant')
    db.body_site.insert(key='LLFA',description='Left Lower Forearm')
    db.body_site.insert(key='LMFA',description='Left Mid Forearm')
    db.body_site.insert(key='LN',description='Left Naris')
    db.body_site.insert(key='LPC',description='Left Posterior Chest')
    db.body_site.insert(key='LSC',description='Left Subclavian')
    db.body_site.insert(key='LT',description='Left Thigh')
    db.body_site.insert(key='LUA',description='Left Upper Arm')
    db.body_site.insert(key='LUAQ',description='Left Upper Abd Quadrant')
    db.body_site.insert(key='LUFA',description='Left Upper Forearm')
    db.body_site.insert(key='LVG',description='Left Ventragluteal')
    db.body_site.insert(key='LVL',description='Left Vastus Lateralis')
    db.body_site.insert(key='NB',description='Nebulized')
    db.body_site.insert(key='OD',description='Right Eye')
    db.body_site.insert(key='OS',description='Left Eye')
    db.body_site.insert(key='OU',description='Bilateral Eyes')
    db.body_site.insert(key='PA',description='Perianal')
    db.body_site.insert(key='PERIN',description='Perineal')
    db.body_site.insert(key='RA',description='Right Arm')
    db.body_site.insert(key='RAC',description='Right Anterior Chest')
    db.body_site.insert(key='RACF',description='Right Antecubital Fossa')
    db.body_site.insert(key='RD',description='Right Deltoid')
    db.body_site.insert(key='RE',description='Right Ear')
    db.body_site.insert(key='REJ',description='Right External Jugular')
    db.body_site.insert(key='RF',description='Right Foot')
    db.body_site.insert(key='RG',description='Right Gluteus Medius')
    db.body_site.insert(key='RH',description='Right Hand')
    db.body_site.insert(key='RIJ',description='Right Internal Jugular')
    db.body_site.insert(key='RLAQ',description='Rt Lower Abd Quadrant')
    db.body_site.insert(key='RLFA',description='Right Lower Forearm')
    db.body_site.insert(key='RMFA',description='Right Mid Forearm')
    db.body_site.insert(key='RN',description='Right Naris')
    db.body_site.insert(key='RPC',description='Right Posterior Chest')
    db.body_site.insert(key='RSC',description='Right Subclavian')
    db.body_site.insert(key='RT',description='Right Thigh')
    db.body_site.insert(key='RUA',description='Right Upper Arm')
    db.body_site.insert(key='RUAQ',description='Right Upper Abd Quadrant')
    db.body_site.insert(key='RUFA',description='Right Upper Forearm')
    db.body_site.insert(key='RVG',description='Right Ventragluteal')
    db.body_site.insert(key='RVL',description='Right Vastus Lateralis')

db.define_table('drug_admin_route',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.drug_admin_route.id>0).count():
    db.drug_admin_route.insert(key='AP',description='Apply Externally')
    db.drug_admin_route.insert(key='B',description='Buccal')
    db.drug_admin_route.insert(key='DT',description='Dental')
    db.drug_admin_route.insert(key='EP',description='Epidural')
    db.drug_admin_route.insert(key='ET',description='Endotrachial Tube*')
    db.drug_admin_route.insert(key='GTT',description='Gastrostomy Tube')
    db.drug_admin_route.insert(key='GU',description='GU Irrigant')
    db.drug_admin_route.insert(key='IA',description='Intra-arterial')
    db.drug_admin_route.insert(key='IB',description='Intrabursal')
    db.drug_admin_route.insert(key='IC',description='Intracardiac')
    db.drug_admin_route.insert(key='ICV',description='Intracervical (uterus)')
    db.drug_admin_route.insert(key='ID',description='Intradermal')
    db.drug_admin_route.insert(key='IH',description='Inhalation')
    db.drug_admin_route.insert(key='IHA',description='Intrahepatic Artery')
    db.drug_admin_route.insert(key='IM',description='Intramuscular')
    db.drug_admin_route.insert(key='IMR',description='Immerse (Soak) Body Part')
    db.drug_admin_route.insert(key='IN',description='Intranasal')
    db.drug_admin_route.insert(key='IO',description='Intraocular')
    db.drug_admin_route.insert(key='IP',description='Intraperitoneal')
    db.drug_admin_route.insert(key='IS',description='Intrasynovial')
    db.drug_admin_route.insert(key='IT',description='Intrathecal')
    db.drug_admin_route.insert(key='IU',description='Intrauterine')
    db.drug_admin_route.insert(key='IV',description='Intravenous')
    db.drug_admin_route.insert(key='MM',description='Mucous Membrane')
    db.drug_admin_route.insert(key='MTH',description='Mouth/Throat')
    db.drug_admin_route.insert(key='NG',description='Nasogastric')
    db.drug_admin_route.insert(key='NP',description='Nasal Prongs*')
    db.drug_admin_route.insert(key='NS',description='Nasal')
    db.drug_admin_route.insert(key='NT',description='Nasotrachial Tube')
    db.drug_admin_route.insert(key='OP',description='Ophthalmic')
    db.drug_admin_route.insert(key='OT',description='Otic')
    db.drug_admin_route.insert(key='OTH',description='Other/Miscellaneous')
    db.drug_admin_route.insert(key='PF',description='Perfusion')
    db.drug_admin_route.insert(key='PO',description='Oral')
    db.drug_admin_route.insert(key='PR',description='Rectal')
    db.drug_admin_route.insert(key='RM',description='Rebreather Mask*')
    db.drug_admin_route.insert(key='SC',description='Subcutaneous')
    db.drug_admin_route.insert(key='SD',description='Soaked Dressing')
    db.drug_admin_route.insert(key='SL',description='Sublingual')
    db.drug_admin_route.insert(key='TD',description='Transdermal')
    db.drug_admin_route.insert(key='TL',description='Translingual')
    db.drug_admin_route.insert(key='TP',description='Topical')
    db.drug_admin_route.insert(key='TRA',description='Tracheostomy*')
    db.drug_admin_route.insert(key='UR',description='Urethral')
    db.drug_admin_route.insert(key='VG',description='Vaginal')
    db.drug_admin_route.insert(key='VM',description='Ventimask')
    db.drug_admin_route.insert(key='WND',description='Wound')
    
db.define_table('medication_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.medication_type.id>0).count():
    db.medication_type.insert(key='329505003',description=' Over the counter products (product)')
    db.medication_type.insert(key='73639000',description=' Prescription drug (product)')

db.define_table('medication_fill_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.medication_fill_status.id>0).count():    
    db.medication_fill_status.insert(key='completed',description='  Completed An Act that has terminated normally after all of its constituents have been performed')
    db.medication_fill_status.insert(key='aborted',description='  Aborted The Act has been terminated prior to the originally intended completion')


db.define_table('order_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.order_status.id>0).count():  
    db.order_status.insert(key='A',description=' Some, but not all, results available')
    db.order_status.insert(key='CA',description=' Order was canceled')
    db.order_status.insert(key='CM',description=' Order is completed')
    db.order_status.insert(key='DC',description=' Order was discontinued')
    db.order_status.insert(key='ER',description=' Error, order not found')
    db.order_status.insert(key='IP',description=' In process, unspecified')
    db.order_status.insert(key='SC',description=' In process, scheduled')

db.define_table('order_control',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.order_control.id>0).count():     
        db.order_control.insert(key='NW',description=' New Order/Service')
        db.order_control.insert(key='OK',description=' Order/Service accepted and OK') 
        db.order_control.insert(key='UA',description=' Unable to accept order/service') 
        db.order_control.insert(key='CA',description=' Cancel Order/Service Request') 
        db.order_control.insert(key='OC',description=' Order/Service Cancelled') 
        db.order_control.insert(key='CR',description=' Cancelled as Requested') 
        db.order_control.insert(key='UC',description=' Unable to Cancel') 
        db.order_control.insert(key='DC',description=' Discontinue Order/Service Request') 
        db.order_control.insert(key='OD',description=' Order/Service Discontinued') 
        db.order_control.insert(key='DR',description=' Discontinued as Requested') 
        db.order_control.insert(key='UD',description=' Unable to Discontinue') 
        db.order_control.insert(key='PA',description=' Parent order/service') 
        db.order_control.insert(key='CH',description=' Child order/service') 
        db.order_control.insert(key='XO',description=' Change Order/Service Request') 
        db.order_control.insert(key='XX',description=' Order/Service Changed') 
        db.order_control.insert(key='XR',description=' Changed as Requested') 
        db.order_control.insert(key='UX',description=' Unable to Change') 
        
db.define_table('order_setting_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.order_setting_type.id>0).count():    
        db.order_setting_type.insert(key='I',description=' Inpatient Order')
        db.order_setting_type.insert(key='O',description=' Outpatient Order')

db.define_table('order_priority',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.order_priority.id>0).count():         
        db.order_priority.insert(key='S',description=' Stat With highest priority')
        db.order_priority.insert(key='A',description=' ASAP Fill after S orders')
        db.order_priority.insert(key='R',description=' Routine Default')
        db.order_priority.insert(key='P',description=' Preop')
        db.order_priority.insert(key='C',description=' Callback')
        db.order_priority.insert(key='T',description=' Timing critical A request implying that it is critical to come as close as possible to the requested time, e.g., for a trough anti-microbial level')

db.define_table('specimen_action',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.specimen_action.id>0).count():      
    db.specimen_action.insert(key='A',description=' Add ordered tests to the existing specimen')
    db.specimen_action.insert(key='G',description=' Generated order; reflex order')
    db.specimen_action.insert(key='L',description=' Lab to obtain specimen from patient')
    db.specimen_action.insert(key='O',description=' Specimen obtained by service other than Lab')
    db.specimen_action.insert(key='P',description=' Pending specimen; Order sent prior to delivery')
    db.specimen_action.insert(key='R',description=' Revised order')
    db.specimen_action.insert(key='S',description=' Schedule the tests specified below')
db.define_table('specimen_risk',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.specimen_risk.id>0).count():         
    db.specimen_risk.insert(key='AGG',description=' Aggressive')
    db.specimen_risk.insert(key='BHZ',description=' Biohazard') 
    db.specimen_risk.insert(key='BIO',description=' Biological') 
    db.specimen_risk.insert(key='COR',description=' Corrosive') 
    db.specimen_risk.insert(key='ESC',description=' Escape Risk') 
    db.specimen_risk.insert(key='EXP',description=' Explosive') 
    db.specimen_risk.insert(key='IFL',description=' MaterialDangerInflammable') 
    db.specimen_risk.insert(key='INF',description=' MaterialDangerInfectious') 
    db.specimen_risk.insert(key='INJ',description=' Injury Hazard') 
    db.specimen_risk.insert(key='POI',description=' Poison') 
    db.specimen_risk.insert(key='RAD',description=' Radioactive') 

db.define_table('specimen_collection_method',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.specimen_collection_method.id>0).count():      
        db.specimen_collection_method.insert(key='FNA',description=' Aspiration, Fine Needle')  
        db.specimen_collection_method.insert(key='PNA',description=' Arterial puncture')  
        db.specimen_collection_method.insert(key='BIO',description=' Biopsy')  
        db.specimen_collection_method.insert(key='BCAE',description=' Blood Culture, Aerobic Bottle')  
        db.specimen_collection_method.insert(key='BCAN',description=' Blood Culture, Anaerobic Bottle')  
        db.specimen_collection_method.insert(key='BCPD',description=' Blood Culture, Pediatric Bottle')  
        db.specimen_collection_method.insert(key='CAP',description=' Capillary Specimen')  
        db.specimen_collection_method.insert(key='CATH',description=' Catheterized')  
        db.specimen_collection_method.insert(key='EPLA',description=' Environmental, Plate')  
        db.specimen_collection_method.insert(key='ESWA',description=' ESWA Environmental, Swab')  
        db.specimen_collection_method.insert(key='LNA',description=' Line, Arterial')  
        db.specimen_collection_method.insert(key='CVP',description=' Line, CVP')  
        db.specimen_collection_method.insert(key='LNV',description=' Line, Venous')  
        db.specimen_collection_method.insert(key='MARTL',description=' Martin-Lewis Agar')  
        db.specimen_collection_method.insert(key='ML11',description=' Mod. Martin-Lewis Agar')  
        db.specimen_collection_method.insert(key='PACE',description=' Pace, Gen-Probe')  
        db.specimen_collection_method.insert(key='PIN',description=' Pinworm Prep')  
        db.specimen_collection_method.insert(key='KOFFP',description=' Plate, Cough')  
        db.specimen_collection_method.insert(key='MLP',description=' Plate, Martin-Lewis')  
        db.specimen_collection_method.insert(key='NYP',description=' Plate, New York City')  
        db.specimen_collection_method.insert(key='TMP',description=' Plate, Thayer-Martin')  
        db.specimen_collection_method.insert(key='ANP',description=' Plates, Anaerobic')  
        db.specimen_collection_method.insert(key='BAP',description=' Plates, Blood Agar')  
        db.specimen_collection_method.insert(key='PRIME',description=' Pump Prime')  
        db.specimen_collection_method.insert(key='PUMP',description=' Pump Specimen')  
        db.specimen_collection_method.insert(key='QC5',description=' Quality Control For Micro')  
        db.specimen_collection_method.insert(key='SCLP',description=' Scalp, Fetal Vein')  
        db.specimen_collection_method.insert(key='SCRAPS',description=' Scrapings')  
        db.specimen_collection_method.insert(key='SHA',description=' Shaving ') 
        db.specimen_collection_method.insert(key='SWA',description=' Swab')  
        db.specimen_collection_method.insert(key='SWD',description=' Swab, Dacron tipped ') 
        db.specimen_collection_method.insert(key='WOOD',description=' Swab, Wooden Shaft')  
        db.specimen_collection_method.insert(key='TMOT',description=' Transport Media')  
        db.specimen_collection_method.insert(key='TMAN',description='Transport Media, Anaerobic')  
        db.specimen_collection_method.insert(key='TMCH',description=' Transport Media, Chalamydia ') 
        db.specimen_collection_method.insert(key='TMM4',description=' Transport Media, M4')  
        db.specimen_collection_method.insert(key='TMMY',description=' Transport Media, Mycoplasma')  
        db.specimen_collection_method.insert(key='TMPV',description=' Transport Media, PVA')  
        db.specimen_collection_method.insert(key='TMSC',description=' Transport Media, Stool Culture')  
        db.specimen_collection_method.insert(key='TMUP',description=' Transport Media, Ureaplasma')  
        db.specimen_collection_method.insert(key='TMVI',description=' Transport Media, Viral')  
        db.specimen_collection_method.insert(key='VENIP',description=' Venipuncture')  
        
db.define_table('patient_class1',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.patient_class1.id>0).count():  
        db.patient_class1.insert(key='EMER',description=' Emergency,  A patient encounter that takes place at a dedicated healthcare service delivery location where the patient receives immediate evaluation and treatment, provided until the patient can be discharged or responsibility for the patients care is transferred elsewhere (for example, the patient could be admitted as an inpatient or transferred to another facility)')
        db.patient_class1.insert(key='IMP',description=' Inpatient, encounter A patient encounter where a patient is admitted by a hospital or equivalent facility, assigned to a location where patients generally stay at least overnight and provided with room, board, and continuous nursing service')
        db.patient_class1.insert(key='AMB',description=' Ambulatory, A comprehensive term for healthcare provided in a healthcare facility (e.g., a practitioners’ office, clinic setting, or hospital) on a nonresident basis. The term ambulatory usually implies that the patient has come to the location and is not assigned to a bed. Sometimes referred to as an outpatient encounter')


db.define_table('document_class',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)
if not db(db.document_class.id>0).count():  
        db.document_class.insert(key='11369-6',description=' History of Immunizations')
        db.document_class.insert(key='11485-0',description=' Anesthesia Records Anesthesia records')
        db.document_class.insert(key='11486-8',description=' Chemotherapy Records Chemotherapy records')
        db.document_class.insert(key='11488-4',description=' Consultation note Provider-unspecified consulting note')
        db.document_class.insert(key='11506-3',description=' Subsequent evaluation note Provider-unspecified progress note')
        db.document_class.insert(key='11543-6',description=' Nursery Records Nursery records')
        db.document_class.insert(key='15508-5',description=' Labor And Delivery Records Labor and delivery records')
        db.document_class.insert(key='18726-0',description=' Radiology Study Reports Radiology study reports (set)')
        db.document_class.insert(key='18761-7',description=' Transfer summarization note Provider-unspecified transfer summary')
        db.document_class.insert(key='18842-5',description=' Discharge summarization note Hospital discharge history (narrative)')
        db.document_class.insert(key='26436-6',description=' Laboratory Studies')
        db.document_class.insert(key='26441-6',description=' Cardiology Studies Cardiology studies (set)')
        db.document_class.insert(key='26442-4',description=' Obstetrical Studies Obstetrical studies (set)')
        db.document_class.insert(key='27895-2',description=' Gastroenterology Endoscopy Studies Gastroenterology endoscopy studies (set)')
        db.document_class.insert(key='27896-0',description=' Pulmonary Studies Pulmonary studies (set)')
        db.document_class.insert(key='27897-8',description=' Neuromuscular Electrophysiology Studies Neuromuscular electrophysiology studies (set)')
        db.document_class.insert(key='27898-6',description=' Pathology Study Reports Pathology study reports (set)')
        db.document_class.insert(key='28570-0',description=' Procedure note Provider-unspecified procedure note')
        db.document_class.insert(key='28619-5',description=' Ophthalmology/Optometry Studies Ophthalmology/optometry studies (set)')
        db.document_class.insert(key='28634-4',description=' Miscellaneous Studies Miscellaneous studies (set)')
        db.document_class.insert(key='29749-9',description=' Dialysis Records Dialysis records')
        db.document_class.insert(key='29750-7',description=' Neonatal Intensive Care Records Neonatal intensive care records')
        db.document_class.insert(key='29751-5',description=' Critical Care Records Critical care records')
        db.document_class.insert(key='29752-3',description=' Perioperative Records Perioperative records')
        db.document_class.insert(key='34109-9',description=' Evaluation and management note')
        db.document_class.insert(key='34117-2',description=' History and physical note')
        db.document_class.insert(key='34121-4',description=' Interventional procedure note')
        db.document_class.insert(key='34122-2',description=' Pathology procedure note')
        db.document_class.insert(key='34133-9',description=' Summarization of episode note')
        db.document_class.insert(key='34140-4',description=' Transfer of care referral note')
        db.document_class.insert(key='34748-4',description=' Telephone encounter note')
        db.document_class.insert(key='34775-7',description=' Pre-operative evaluation and management note')
        db.document_class.insert(key='47039-3',description=' Admission history and physical note')
        db.document_class.insert(key='47042-7',description=' Counseling note')
        db.document_class.insert(key='47045-0',description=' Study report')
        db.document_class.insert(key='47046-8',description=' Summary of death')
        db.document_class.insert(key='47049-2',description=' Communication')
        db.document_class.insert(key='57017-6',description=' Privacy Policy')
        db.document_class.insert(key='57016-8',description=' Privacy Policy Acknowledgment')
db.define_table('admission_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.admission_type.id>0).count():
    db.admission_type.insert(key='A',description='Accident')
    db.admission_type.insert(key='C',description='Elective')
    db.admission_type.insert(key='E',description='Emergency')
    db.admission_type.insert(key='L',description='Labor and Delivery')
    db.admission_type.insert(key='N',description='Newborn (Birth in healthcare facility)')
    db.admission_type.insert(key='R',description='Routine')
    db.admission_type.insert(key='U',description='Urgent')
db.define_table('admission_source',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.admission_source.id>0).count():
    db.admission_source.insert(key='1',description='Physician referral')
    db.admission_source.insert(key='2',description='Clinic referral')
    db.admission_source.insert(key='3',description='HMO referral')
    db.admission_source.insert(key='4',description='Transfer from a hospital')
    db.admission_source.insert(key='5',description='Transfer from a skilled nursing facility')
    db.admission_source.insert(key='6',description='Transfer from another health care facility')
    db.admission_source.insert(key='7',description='Emergency room')
    db.admission_source.insert(key='8',description='Court/law enforcement')
    db.admission_source.insert(key='9',description='Information not available')
db.define_table('specimen_collection_site',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.specimen_collection_site.id>0).count():
    db.specimen_collection_site.insert(key='ABS',description='Abscess')
    db.specimen_collection_site.insert(key='ACNE',description='Tissue, Acne')
    db.specimen_collection_site.insert(key='ACNFLD',description='Fluid, Acne')
    db.specimen_collection_site.insert(key='AIRS',description='Air Sample')
    db.specimen_collection_site.insert(key='ALL',description='Allograft')
    db.specimen_collection_site.insert(key='AMN',description='Amniotic fluid')
    db.specimen_collection_site.insert(key='AMP',description='Amputation')
    db.specimen_collection_site.insert(key='ANGI',description='Catheter Tip, Angio')
    db.specimen_collection_site.insert(key='ARTC',description='Catheter Tip, Arterial')
    db.specimen_collection_site.insert(key='ASERU',description='Serum, Acute')
    db.specimen_collection_site.insert(key='ASP',description='Aspirate')
    db.specimen_collection_site.insert(key='ATTE',description='Environmental, Autoclave Ampule')
    db.specimen_collection_site.insert(key='AUTOC',description='Environment, Attest')
    db.specimen_collection_site.insert(key='AUTP',description='Autopsy')
    db.specimen_collection_site.insert(key='BBL',description='Blood bag')
    db.specimen_collection_site.insert(key='BCYST',description="Cyst, Baker's")
    db.specimen_collection_site.insert(key='BDY',description='Whole body')
    db.specimen_collection_site.insert(key='BIFL',description='Bile fluid')
    db.specimen_collection_site.insert(key='BITE',description='Bite')
    db.specimen_collection_site.insert(key='BLD',description='Whole blood')
    db.specimen_collection_site.insert(key='BLDA',description='Blood arterial')
    db.specimen_collection_site.insert(key='BLDC',description='Blood capillary')
    db.specimen_collection_site.insert(key='BLDCO',description='Cord blood')
    db.specimen_collection_site.insert(key='BLDV',description='Blood venous')
    db.specimen_collection_site.insert(key='BLEB',description='Bleb')
    db.specimen_collection_site.insert(key='BLIST',description='Blister')
    db.specimen_collection_site.insert(key='BOIL',description='Boil')
    db.specimen_collection_site.insert(key='BON',description='Bone')
    db.specimen_collection_site.insert(key='BOWL',description='Bowel contents')
    db.specimen_collection_site.insert(key='BPH',description='Basophils')
    db.specimen_collection_site.insert(key='BPU',description='Blood product unit')
    db.specimen_collection_site.insert(key='BRN',description='Burn')
    db.specimen_collection_site.insert(key='BRO',description='Bronchial')
    db.specimen_collection_site.insert(key='BRSH',description='Brush')
    db.specimen_collection_site.insert(key='BRTH',description='Breath (use EXHLD)')
    db.specimen_collection_site.insert(key='BRUS',description='Brushing')
    db.specimen_collection_site.insert(key='BUB',description='Bubo')
    db.specimen_collection_site.insert(key='BULLA',description='Bulla/Bullae')
    db.specimen_collection_site.insert(key='BX',description='Biopsy')
    db.specimen_collection_site.insert(key='CALC',description='Calculus (=Stone)')
    db.specimen_collection_site.insert(key='CARBU',description='Carbuncle')
    db.specimen_collection_site.insert(key='CAT',description='Catheter')
    db.specimen_collection_site.insert(key='CBITE',description='Bite, Cat')
    db.specimen_collection_site.insert(key='CDM',description='Cardiac muscle')
    db.specimen_collection_site.insert(key='CLIPP',description='Clippings')
    db.specimen_collection_site.insert(key='CNJT',description='Conjunctiva')
    db.specimen_collection_site.insert(key='CNL',description='Cannula')
    db.specimen_collection_site.insert(key='COL',description='Colostrum')
    db.specimen_collection_site.insert(key='CONE',description='Biospy, Cone')
    db.specimen_collection_site.insert(key='CSCR',description='Scratch, Cat')
    db.specimen_collection_site.insert(key='CSERU',description='Serum, Convalescent')
    db.specimen_collection_site.insert(key='CSF',description='Cerebral spinal fluid')
    db.specimen_collection_site.insert(key='CSITE',description='Catheter Insertion Site')
    db.specimen_collection_site.insert(key='CSMY',description='Fluid, Cystostomy Tube')
    db.specimen_collection_site.insert(key='CST',description='Fluid, Cyst')
    db.specimen_collection_site.insert(key='CSVR',description='Blood, Cell Saver')
    db.specimen_collection_site.insert(key='CTP',description='Catheter tip')
    db.specimen_collection_site.insert(key='CUR',description='Curettage')
    db.specimen_collection_site.insert(key='CVM',description='Cervical mucus')
    db.specimen_collection_site.insert(key='CVPS',description='Site, CVP')
    db.specimen_collection_site.insert(key='CVPT',description='Catheter Tip, CVP')
    db.specimen_collection_site.insert(key='CVX',description='Cervix')
    db.specimen_collection_site.insert(key='CYN',description='Nodule, Cystic')
    db.specimen_collection_site.insert(key='CYST',description='Cyst')
    db.specimen_collection_site.insert(key='DBITE',description='Bite, Dog')
    db.specimen_collection_site.insert(key='DCS',description='Sputum, Deep Cough')
    db.specimen_collection_site.insert(key='DEC',description='Ulcer, Decubitus')
    db.specimen_collection_site.insert(key='DEION',description='Environmental, Water (Deionized)')
    db.specimen_collection_site.insert(key='DIA',description='Dialysate')
    db.specimen_collection_site.insert(key='DIAF',description='Dialysis fluid')
    db.specimen_collection_site.insert(key='DISCHG',description='Discharge')
    db.specimen_collection_site.insert(key='DIV',description='Diverticulum')
    db.specimen_collection_site.insert(key='DOSE',description='Dose med or substance')
    db.specimen_collection_site.insert(key='DRN',description='Drain')
    db.specimen_collection_site.insert(key='DRNG',description='Drainage, Tube')
    db.specimen_collection_site.insert(key='DRNGP',description='Drainage, Penrose')
    db.specimen_collection_site.insert(key='DUFL',description='Duodenal fluid')
    db.specimen_collection_site.insert(key='EAR',description='Ear')
    db.specimen_collection_site.insert(key='EARW',description='Ear wax (cerumen)')
    db.specimen_collection_site.insert(key='EBRUSH',description='Brush, Esophageal')
    db.specimen_collection_site.insert(key='EEYE',description='Environmental, Eye Wash')
    db.specimen_collection_site.insert(key='EFF',description='Environmental, Effluent')
    db.specimen_collection_site.insert(key='EFFUS',description='Effusion')
    db.specimen_collection_site.insert(key='EFOD',description='Environmental, Food')
    db.specimen_collection_site.insert(key='EISO',description='Environmental, Isolette')
    db.specimen_collection_site.insert(key='ELT',description='Electrode')
    db.specimen_collection_site.insert(key='ENDC',description='Endocardium')
    db.specimen_collection_site.insert(key='ENDM',description='Endometrium')
    db.specimen_collection_site.insert(key='ENVIR',description='Environmental, Unidentified Substance')
    db.specimen_collection_site.insert(key='EOS',description='Eosinophils')
    db.specimen_collection_site.insert(key='EOTH',description='Environmental, Other Substance')
    db.specimen_collection_site.insert(key='ESOI',description='Environmental, Soil')
    db.specimen_collection_site.insert(key='ESOS',description='Environmental, Solution (Sterile)')
    db.specimen_collection_site.insert(key='ETA',description='Aspirate, Endotrach')
    db.specimen_collection_site.insert(key='ETTP',description='Catheter Tip, Endotracheal')
    db.specimen_collection_site.insert(key='ETTUB',description='Tube, Endotracheal')
    db.specimen_collection_site.insert(key='EWHI',description='Environmental, Whirlpool')
    db.specimen_collection_site.insert(key='EXG',description='Exhaled gas (=breath)')
    db.specimen_collection_site.insert(key='EXS',description='Shunt, External')
    db.specimen_collection_site.insert(key='EXUDTE',description='Exudate')
    db.specimen_collection_site.insert(key='EYE',description='Eye')
    db.specimen_collection_site.insert(key='FAW',description='Environmental, Water (Well)')
    db.specimen_collection_site.insert(key='FBLOOD',description='Blood, Fetal')
    db.specimen_collection_site.insert(key='FGA',description='Fluid, Abdomen')
    db.specimen_collection_site.insert(key='FIB',description='Fibroblasts')
    db.specimen_collection_site.insert(key='FIST',description='Fistula')
    db.specimen_collection_site.insert(key='FLD',description='Fluid, Other')
    db.specimen_collection_site.insert(key='FLT',description='Filter')
    db.specimen_collection_site.insert(key='FLU',description='Body fluid, unsp')
    db.specimen_collection_site.insert(key='FLUID',description='Fluid')
    db.specimen_collection_site.insert(key='FOLEY',description='Catheter Tip, Foley')
    db.specimen_collection_site.insert(key='FRS',description='Fluid, Respiratory')
    db.specimen_collection_site.insert(key='FSCLP',description='Scalp, Fetal')
    db.specimen_collection_site.insert(key='FUR',description='Furuncle')
    db.specimen_collection_site.insert(key='GAS',description='Gas')
    db.specimen_collection_site.insert(key='GASA',description='Aspirate, Gastric')
    db.specimen_collection_site.insert(key='GASAN',description='Antrum, Gastric')
    db.specimen_collection_site.insert(key='GASBR',description='Brushing, Gastric')
    db.specimen_collection_site.insert(key='GASD',description='Drainage, Gastric')
    db.specimen_collection_site.insert(key='GAST',description='Gastric fluid/contents')
    db.specimen_collection_site.insert(key='GEN',description='Genital')
    db.specimen_collection_site.insert(key='GENC',description='Genital cervix')
    db.specimen_collection_site.insert(key='GENL',description='Genital lochia')
    db.specimen_collection_site.insert(key='GENV',description='Genital vaginal')
    db.specimen_collection_site.insert(key='GRAFT',description='Graft')
    db.specimen_collection_site.insert(key='GRANU',description='Granuloma')
    db.specimen_collection_site.insert(key='GROSH',description='Catheter, Groshong')
    db.specimen_collection_site.insert(key='GSOL',description='Solution, Gastrostomy')
    db.specimen_collection_site.insert(key='GSPEC',description='Biopsy, Gastric')
    db.specimen_collection_site.insert(key='GT',description='Tube, Gastric')
    db.specimen_collection_site.insert(key='GTUBE',description='Drainage Tube, Drainage (Gastrostomy)')
    db.specimen_collection_site.insert(key='HAR',description='Hair')
    db.specimen_collection_site.insert(key='HBITE',description='Bite, Human')
    db.specimen_collection_site.insert(key='HBLUD',description='Blood, Autopsy')
    db.specimen_collection_site.insert(key='HEMAQ',description='Catheter Tip, Hemaquit')
    db.specimen_collection_site.insert(key='HEMO',description='Catheter Tip, Hemovac')
    db.specimen_collection_site.insert(key='HERNI',description='Tissue, Herniated')
    db.specimen_collection_site.insert(key='HEV',description='Drain, Hemovac')
    db.specimen_collection_site.insert(key='HIC',description='Catheter, Hickman')
    db.specimen_collection_site.insert(key='HYDC',description='Fluid, Hydrocele')
    db.specimen_collection_site.insert(key='IBITE',description='Bite, Insect')
    db.specimen_collection_site.insert(key='ICYST',description='Cyst, Inclusion')
    db.specimen_collection_site.insert(key='IDC',description='Catheter Tip, Indwelling')
    db.specimen_collection_site.insert(key='IHG',description='Inhaled Gas')
    db.specimen_collection_site.insert(key='ILEO',description='Drainage, Ileostomy')
    db.specimen_collection_site.insert(key='ILLEG',description='Source of Specimen Is Illegible')
    db.specimen_collection_site.insert(key='IMP',description='Implant')
    db.specimen_collection_site.insert(key='INCI',description='Site, Incision/Surgical')
    db.specimen_collection_site.insert(key='INFIL',description='Infiltrate')
    db.specimen_collection_site.insert(key='INS',description='Insect')
    db.specimen_collection_site.insert(key='INTRD',description='Catheter Tip, Introducer')
    db.specimen_collection_site.insert(key='ISLT',description='Isolate')
    db.specimen_collection_site.insert(key='IT',description='Intubation tube')
    db.specimen_collection_site.insert(key='IUD',description='Intrauterine Device')
    db.specimen_collection_site.insert(key='IVCAT',description='Catheter Tip, IV')
    db.specimen_collection_site.insert(key='IVFLD',description='Fluid, IV')
    db.specimen_collection_site.insert(key='IVTIP',description='Tubing Tip, IV')
    db.specimen_collection_site.insert(key='JEJU',description='Drainage, Jejunal')
    db.specimen_collection_site.insert(key='JNTFLD',description='Fluid, Joint')
    db.specimen_collection_site.insert(key='JP',description='Drainage, Jackson Pratt')
    db.specimen_collection_site.insert(key='KELOI',description='Lavage')
    db.specimen_collection_site.insert(key='KIDFLD',description='Fluid, Kidney')
    db.specimen_collection_site.insert(key='LAM',description='Lamella')
    db.specimen_collection_site.insert(key='LAVG',description='Lavage, Bronhial')
    db.specimen_collection_site.insert(key='LAVGG',description='Lavage, Gastric')
    db.specimen_collection_site.insert(key='LAVGP',description='Lavage, Peritoneal')
    db.specimen_collection_site.insert(key='LAVPG',description='Lavage, Pre-Bronch')
    db.specimen_collection_site.insert(key='LENS1',description='Contact Lens')
    db.specimen_collection_site.insert(key='LENS2',description='Contact Lens Case')
    db.specimen_collection_site.insert(key='LESN',description='Lesion')
    db.specimen_collection_site.insert(key='LIQ',description='Liquid NOS')
    db.specimen_collection_site.insert(key='LIQO',description='Liquid, Other')
    db.specimen_collection_site.insert(key='LN',description='Line')
    db.specimen_collection_site.insert(key='LNA',description='Line arterial')
    db.specimen_collection_site.insert(key='LNV',description='Line venous')
    db.specimen_collection_site.insert(key='LSAC',description='Fluid, Lumbar Sac')
    db.specimen_collection_site.insert(key='LYM',description='Lymphocytes')
    db.specimen_collection_site.insert(key='MAC',description='Macrophages')
    db.specimen_collection_site.insert(key='MAHUR',description='Catheter Tip, Makurkour')
    db.specimen_collection_site.insert(key='MAR',description='Marrow')
    db.specimen_collection_site.insert(key='MASS',description='Mass')
    db.specimen_collection_site.insert(key='MBLD',description='Menstrual blood')
    db.specimen_collection_site.insert(key='MEC',description='Meconium')
    db.specimen_collection_site.insert(key='MILK',description='Breast milk')
    db.specimen_collection_site.insert(key='MLK',description='Milk')
    db.specimen_collection_site.insert(key='MUCOS',description='Mucosa')
    db.specimen_collection_site.insert(key='MUCUS',description='Mucus')
    db.specimen_collection_site.insert(key='NAIL',description='Nail')
    db.specimen_collection_site.insert(key='NASDR',description='Drainage, Nasal')
    db.specimen_collection_site.insert(key='NEDL',description='Needle')
    db.specimen_collection_site.insert(key='NEPH',description='Site, Nephrostomy')
    db.specimen_collection_site.insert(key='NGASP',description='Aspirate, Nasogastric')
    db.specimen_collection_site.insert(key='NGAST',description='Drainage, Nasogastric')
    db.specimen_collection_site.insert(key='NGS',description='Site, Naso/Gastric')
    db.specimen_collection_site.insert(key='NODUL',description='Nodule(s)')
    db.specimen_collection_site.insert(key='NOS',description='Nose (nasal passage)')
    db.specimen_collection_site.insert(key='NSECR',description='Secretion, Nasal')
    db.specimen_collection_site.insert(key='ORH',description='Other')
    db.specimen_collection_site.insert(key='ORL',description='Lesion, Oral')
    db.specimen_collection_site.insert(key='OTH',description='Source, Other')
    db.specimen_collection_site.insert(key='PACEM',description='Pacemaker')
    db.specimen_collection_site.insert(key='PAFL',description='Pancreatic fluid')
    db.specimen_collection_site.insert(key='PAT',description='Patient')
    db.specimen_collection_site.insert(key='PCFL',description='Fluid, Pericardial')
    db.specimen_collection_site.insert(key='PDSIT',description='Site, Peritoneal Dialysis')
    db.specimen_collection_site.insert(key='PDTS',description='Site, Peritoneal Dialysis Tunnel')
    db.specimen_collection_site.insert(key='PELVA',description='Abscess, Pelvic')
    db.specimen_collection_site.insert(key='PENIL',description='Lesion, Penile')
    db.specimen_collection_site.insert(key='PERIA',description='Abscess, Perianal')
    db.specimen_collection_site.insert(key='PILOC',description='Cyst, Pilonidal')
    db.specimen_collection_site.insert(key='PINS',description='Site, Pin')
    db.specimen_collection_site.insert(key='PIS',description='Site, Pacemaker Insetion')
    db.specimen_collection_site.insert(key='PLAN',description='Plant Material')
    db.specimen_collection_site.insert(key='PLAS',description='Plasma')
    db.specimen_collection_site.insert(key='PLB',description='Plasma bag')
    db.specimen_collection_site.insert(key='PLC',description='Placenta')
    db.specimen_collection_site.insert(key='PLEVS',description='Serum, Peak Level')
    db.specimen_collection_site.insert(key='PLR',description='Pleural fluid (thoracentesis fld)')
    db.specimen_collection_site.insert(key='PMN',description='Polymorphonuclear neutrophils')
    db.specimen_collection_site.insert(key='PND',description='Drainage, Penile')
    db.specimen_collection_site.insert(key='POL',description='Polyps')
    db.specimen_collection_site.insert(key='POPGS',description='Graft Site, Popliteal')
    db.specimen_collection_site.insert(key='POPLG',description='Graft, Popliteal')
    db.specimen_collection_site.insert(key='POPLV',description='Site, Popliteal Vein')
    db.specimen_collection_site.insert(key='PORTA',description='Catheter, Porta')
    db.specimen_collection_site.insert(key='PPP',description='Platelet poor plasma')
    db.specimen_collection_site.insert(key='PROST',description='Prosthetic Device')
    db.specimen_collection_site.insert(key='PRP',description='Platelet rich plasma')
    db.specimen_collection_site.insert(key='PRT',description='Peritoneal fluid /ascites')
    db.specimen_collection_site.insert(key='PSC',description='Pseudocyst')
    db.specimen_collection_site.insert(key='PUNCT',description='Wound, Puncture')
    db.specimen_collection_site.insert(key='PUS',description='Pus')
    db.specimen_collection_site.insert(key='PUSFR',description='Pustule')
    db.specimen_collection_site.insert(key='PUST',description='Pus')
    db.specimen_collection_site.insert(key='QC3',description='Quality Control')
    db.specimen_collection_site.insert(key='RANDU',description='Urine, Random')
    db.specimen_collection_site.insert(key='RBC',description='Erythrocytes')
    db.specimen_collection_site.insert(key='RBITE',description='Bite, Reptile')
    db.specimen_collection_site.insert(key='RECT',description='Drainage, Rectal')
    db.specimen_collection_site.insert(key='RECTA',description='Abscess, Rectal')
    db.specimen_collection_site.insert(key='RENALC',description='Cyst, Renal')
    db.specimen_collection_site.insert(key='RENC',description='Fluid, Renal Cyst')
    db.specimen_collection_site.insert(key='RES',description='Respiratory')
    db.specimen_collection_site.insert(key='RT',description='Route of medicine')
    db.specimen_collection_site.insert(key='SAL',description='Saliva')
    db.specimen_collection_site.insert(key='SCAR',description='Tissue, Keloid (Scar)')
    db.specimen_collection_site.insert(key='SCLV',description='Catheter Tip, Subclavian')
    db.specimen_collection_site.insert(key='SCROA',description='Abscess, Scrotal')
    db.specimen_collection_site.insert(key='SECRE',description='Secretion(s)')
    db.specimen_collection_site.insert(key='SER',description='Serum')
    db.specimen_collection_site.insert(key='SHU',description='Site, Shunt')
    db.specimen_collection_site.insert(key='SHUNF',description='Fluid, Shunt')
    db.specimen_collection_site.insert(key='SHUNT',description='Shunt')
    db.specimen_collection_site.insert(key='SITE',description='Site')
    db.specimen_collection_site.insert(key='SKBP',description='Biopsy, Skin')
    db.specimen_collection_site.insert(key='SKM',description='Skeletal muscle')
    db.specimen_collection_site.insert(key='SKN',description='Skin')
    db.specimen_collection_site.insert(key='SMM',description='Mass, Sub-Mandibular')
    db.specimen_collection_site.insert(key='SMN',description='Seminal fluid')
    db.specimen_collection_site.insert(key='SNV',description='Synovial fluid (Joint fluid)')
    db.specimen_collection_site.insert(key='SPRM',description='Spermatozoa')
    db.specimen_collection_site.insert(key='SPRP',description='Catheter Tip, Suprapubic')
    db.specimen_collection_site.insert(key='SPRPB',description='Cathether Tip, Suprapubic')
    db.specimen_collection_site.insert(key='SPS',description='Environmental, Spore Strip')
    db.specimen_collection_site.insert(key='SPT',description='Sputum')
    db.specimen_collection_site.insert(key='SPTC',description='Sputum - coughed')
    db.specimen_collection_site.insert(key='SPTT',description='Sputum - tracheal aspirate')
    db.specimen_collection_site.insert(key='SPUT1',description='Sputum, Simulated')
    db.specimen_collection_site.insert(key='SPUTIN',description='Sputum, Inducted')
    db.specimen_collection_site.insert(key='SPUTSP',description='Sputum, Spontaneous')
    db.specimen_collection_site.insert(key='STER',description='Environmental, Sterrad')
    db.specimen_collection_site.insert(key='STL',description='Stool = Fecal')
    db.specimen_collection_site.insert(key='STON',description='Stone (use CALC)')
    db.specimen_collection_site.insert(key='STONE',description='Stone, Kidney')
    db.specimen_collection_site.insert(key='SUBMA',description='Abscess, Submandibular')
    db.specimen_collection_site.insert(key='SUBMX',description='Abscess, Submaxillary')
    db.specimen_collection_site.insert(key='SUMP',description='Drainage, Sump')
    db.specimen_collection_site.insert(key='SUP',description='Suprapubic Tap')
    db.specimen_collection_site.insert(key='SUTUR',description='Suture')
    db.specimen_collection_site.insert(key='SWGZ',description='Catheter Tip, Swan Gantz')
    db.specimen_collection_site.insert(key='SWT',description='Sweat')
    db.specimen_collection_site.insert(key='TASP',description='Aspirate, Tracheal')
    db.specimen_collection_site.insert(key='TEAR',description='Tears')
    db.specimen_collection_site.insert(key='THRB',description='Thrombocyte (platelet)')
    db.specimen_collection_site.insert(key='THRT',description='Throat')
    db.specimen_collection_site.insert(key='TISG',description='Tissue gall bladder')
    db.specimen_collection_site.insert(key='TISPL',description='Tissue placenta')
    db.specimen_collection_site.insert(key='TISS',description='Tissue')
    db.specimen_collection_site.insert(key='TISU',description='Tissue ulcer')
    db.specimen_collection_site.insert(key='TLC',description='Cathether Tip, Triple Lumen')
    db.specimen_collection_site.insert(key='TLGI',description='Tissue large intestine')
    db.specimen_collection_site.insert(key='TLNG',description='Tissue lung')
    db.specimen_collection_site.insert(key='TRAC',description='Site, Tracheostomy')
    db.specimen_collection_site.insert(key='TRANS',description='Transudate')
    db.specimen_collection_site.insert(key='TSERU',description='Serum, Trough')
    db.specimen_collection_site.insert(key='TSMI',description='Tissue small intestine')
    db.specimen_collection_site.insert(key='TSTES',description='Abscess, Testicular')
    db.specimen_collection_site.insert(key='TTRA',description='Aspirate, Transtracheal')
    db.specimen_collection_site.insert(key='TUB',description='Tube NOS')
    db.specimen_collection_site.insert(key='TUBES',description='Tubes')
    db.specimen_collection_site.insert(key='TUMOR',description='Tumor')
    db.specimen_collection_site.insert(key='TZANC',description='Smear, Tzanck')
    db.specimen_collection_site.insert(key='UDENT',description='Source, Unidentified')
    db.specimen_collection_site.insert(key='ULC',description='Ulcer')
    db.specimen_collection_site.insert(key='UMB',description='Umbilical blood')
    db.specimen_collection_site.insert(key='UMED',description='Unknown medicine')
    db.specimen_collection_site.insert(key='UR',description='Urine')
    db.specimen_collection_site.insert(key='URC',description='Urine clean catch')
    db.specimen_collection_site.insert(key='URINB',description='Urine, Bladder Washings')
    db.specimen_collection_site.insert(key='URINC',description='Urine, Catheterized')
    db.specimen_collection_site.insert(key='URINM',description='Urine, Midstream')
    db.specimen_collection_site.insert(key='URINN',description='Urine, Nephrostomy')
    db.specimen_collection_site.insert(key='URINP',description='Urine, Pedibag')
    db.specimen_collection_site.insert(key='URNS',description='Urine sediment')
    db.specimen_collection_site.insert(key='URT',description='Urine catheter')
    db.specimen_collection_site.insert(key='URTH',description='Urethra')
    db.specimen_collection_site.insert(key='USCOP',description='Urine, Cystoscopy')
    db.specimen_collection_site.insert(key='USPEC',description='Source, Unspecified')
    db.specimen_collection_site.insert(key='USUB',description='Unknown substance')
    db.specimen_collection_site.insert(key='VASTIP',description='Catheter Tip, Vas')
    db.specimen_collection_site.insert(key='VENT',description='Catheter Tip, Ventricular')
    db.specimen_collection_site.insert(key='VITF',description='Vitreous Fluid')
    db.specimen_collection_site.insert(key='VOM',description='Vomitus')
    db.specimen_collection_site.insert(key='WASH',description='Wash')
    db.specimen_collection_site.insert(key='WASI',description='Washing, e.g. bronchial washing')
    db.specimen_collection_site.insert(key='WAT',description='Water')
    db.specimen_collection_site.insert(key='WB',description='Blood, Whole')
    db.specimen_collection_site.insert(key='WBC',description='Leukocytes')
    db.specimen_collection_site.insert(key='WEN',description='Wen')
    db.specimen_collection_site.insert(key='WICK',description='Wick')
    db.specimen_collection_site.insert(key='WND',description='Wound')
    db.specimen_collection_site.insert(key='WNDA',description='Wound abscess')
    db.specimen_collection_site.insert(key='WNDD',description='Wound drainage')
    db.specimen_collection_site.insert(key='WNDE',description='Wound exudate')
    db.specimen_collection_site.insert(key='WORM',description='Worm')
    db.specimen_collection_site.insert(key='WRT',description='Wart')
    db.specimen_collection_site.insert(key='WWA',description='Environmental, Water')
    db.specimen_collection_site.insert(key='WWO',description='Environmental, Water (Ocean)')
    db.specimen_collection_site.insert(key='WWT',description='Environmental, Water (Tap)')
    db.specimen_collection_site.insert(key='XXX',description='To be specified in another part of the message')
db.define_table('procedure_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.procedure_type.id>0).count():
    db.procedure_type.insert(key='A',description='Anesthesia')
    db.procedure_type.insert(key='D',description='Diagnostic procedure')
    db.procedure_type.insert(key='I',description='Invasive procedure not classified elsewhere (e.g., IV, catheter, etc.)')
    db.procedure_type.insert(key='P',description='Procedure for treatment (therapeutic, includingoperations)')
    
db.define_table('discharge_disposition',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.discharge_disposition.id>0).count():
    db.discharge_disposition.insert(key='01',description='Discharged to home or self care (routine discharge)')
    db.discharge_disposition.insert(key='02',description='Discharged/transferred to another short term general hospital for inpatient care')
    db.discharge_disposition.insert(key='03',description='Discharged/transferred to skilled nursing facility (SNF)')
    db.discharge_disposition.insert(key='04',description='Discharged/transferred to an intermediate carefacility (ICF)')
    db.discharge_disposition.insert(key='05',description='Discharged/transferred to another type of institution for inpatient care or referred for outpatient services to another institution')
    db.discharge_disposition.insert(key='06',description='Discharged/transferred to home under care of organized home health service organization')
    db.discharge_disposition.insert(key='07',description='Left against medical advice or discontinued care')
    db.discharge_disposition.insert(key='08',description='Discharged/transferred to home under care of Home IV provider')
    db.discharge_disposition.insert(key='09',description='Admitted as an inpatient to this hospital')
    db.discharge_disposition.insert(key='10 _19',description='Discharge to be defined at state level, if necessary')
    db.discharge_disposition.insert(key='20',description='Expired (i.e. dead)')
    db.discharge_disposition.insert(key='21 ... 29',description='Expired to be defined at state level, if necessary')
    db.discharge_disposition.insert(key='30',description='Still patient or expected to return for outpatient services (i.e. still a patient)')
    db.discharge_disposition.insert(key='31 _ 39',description='Still patient to be defined at state level, if necessary (i.e. still a patient)')
    db.discharge_disposition.insert(key='40',description='Expired (i.e. died) at home')
    db.discharge_disposition.insert(key='41',description='Expired (i.e. died) in a medical facility; e.g., hospital, SNF, ICF, or free standing hospice')
    db.discharge_disposition.insert(key='42',description='Expired (i.e. died) - place unknown')

db.define_table('result_status',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.result_status.id>0).count():
    db.result_status.insert(key='A',description='Some, but not all, results available')
    db.result_status.insert(key='C',description='Correction to results')
    db.result_status.insert(key='F',description='Final results; results stored and verified. Canonly be changed with a corrected result.')
    db.result_status.insert(key='I',description='No results available; specimen received, procedure incomplete')
    db.result_status.insert(key='O',description='Order received; specimen not yet received')
    db.result_status.insert(key='P',description='Preliminary: A verified early result is  available, final results not yet obtained')
    db.result_status.insert(key='R',description='Results stored; not yet verified')
    db.result_status.insert(key='S',description='No results available; procedure scheduled, but not done')
    db.result_status.insert(key='X',description='No results available; Order canceled.')
    db.result_status.insert(key='Y',description='No order on record for this test. (Used only onqueries)')
    db.result_status.insert(key='Z',description='No record of this patient. (Used only on queries)')
    
db.define_table('result_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.result_type.id>0).count():   
        db.result_type.insert(key='34530-6',description=' ABO + Rh Pnl Bld ABO & Rh group panel in Blood')
        db.result_type.insert(key='883-9',description='ABO Group Bld ABO group [Type] in Blood')
        db.result_type.insert(key='882-1',description='ABO+Rh Gp Bld ABO & Rh group [Type] in Blood')
        db.result_type.insert(key='884-7',description='ABO+Rh Gp BldC ABO & Rh group [Type] in Capillary blood')
        db.result_type.insert(key='11218-5',description='Microalbumin Ur Test Str-mCnc Microalbumin [Mass/volume] in Urine by Test stripHSV1')
        db.result_type.insert(key='14956-7',description='Microalbumin 24H Ur-mRate Microalbumin [Mass/time] in 24 hour Urine')
        db.result_type.insert(key='14957-5',description='Microalbumin Ur-mCnc Microalbumin [Mass/volume] in Urine')
        db.result_type.insert(key='1753-3',description='Albumin Ur Ql Albumin [Presence] in Urine')
        db.result_type.insert(key='1754-1',description='Albumin Ur-mCnc Albumin [Mass/volume] in Urine')
        db.result_type.insert(key='1755-8',description='Albumin 24H Ur-mRate Albumin [Mass/time] in 24 hour Urine')
        db.result_type.insert(key='21059-1',description='Albumin 24H Ur-mCnc Albumin [Mass/volume] in 24 hour Urine')
        db.result_type.insert(key='30003-8 ',description='Microalbumin 24H Ur-mCnc Microalbumin [Mass/volume] in 24 hour Urine')
        db.result_type.insert(key='43605-5 ',description='Microalbumin 4H Ur-mCnc Microalbumin [Mass/volume] in 4 hour Urine')
        db.result_type.insert(key='43606-3 ',description='Microalbumin 4H Ur-mRate Microalbumin [Mass/time] in 4 hour Urine')
        db.result_type.insert(key='43607-1 ',description='Microalbumin 12H Ur-mRate Microalbumin [Mass/time] in 12 hour Urine')
        db.result_type.insert(key='1757-4 ',description='Albumin Cl 24H Ur+SerPl-vRate Albumin renal clearance in 24 hour')
        db.result_type.insert(key='13705-9 ',description='Albumin/creat 24H Ur-mRto Albumin/Creatinine [Mass ratio] in 24 hour Urine')
        db.result_type.insert(key='14958-3 ',description='Microalbumin/creat 24H Ur-mRto Microalbumin/Creatinine [Mass ratio] in 24 hour Urine')
        db.result_type.insert(key='14959-1 ',description='Microalbumin/creat Ur-mRto Microalbumin/Creatinine [Mass ratio] in Urine')
        db.result_type.insert(key='20621-9 ',description='Albumin/creat Ur Ql Strip Albumin/Creatinine [Presence] in Urine by Test strip')
        db.result_type.insert(key='30000-4 ',description='Microalbumin/creat Ur-Rto Microalbumin/Creatinine [Ratio] in Urine')
        db.result_type.insert(key='30001-2 ',description='Microalbumin/creat Ur Test Str-Rto Microalbumin/Creatinine [Ratio] in Urine by Test strip')
        db.result_type.insert(key='32294-1 ',description='Albumin/creat Ur-Rto Albumin/Creatinine [Ratio] in Urine')
        db.result_type.insert(key='44292-1 ',description='Microalbumin/creat 12H Ur-mRto Microalbumin/Creatinine [Mass ratio] in 12 hour Urine')
        db.result_type.insert(key='9318-7 ',description='Albumin/creat Ur-mRto Albumin/Creatinine [Mass ratio] in Urine')
        db.result_type.insert(key='15019-3 ',description='AFP Amn-sCnc Alpha-1-Fetoprotein [Molecules/volume] in Amniotic Fluid')
        db.result_type.insert(key='1832-5 ',description='AFP Amn-mCnc Alpha-1-Fetoprotein [Mass/volume] in Amniotic Fluid')
        db.result_type.insert(key='1834-1 ',description='AFP SerPl-mCnc Alpha-1-Fetoprotein [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='19171-8 ',description='AFP Amn-aCnc Alpha-1-Fetoprotein [Units/volume] in Amniotic Fluid')
        db.result_type.insert(key='19176-7 ',description='AFP SerPl-aCnc Alpha-1-Fetoprotein [Units/volume] in Serum or Plasma')
        db.result_type.insert(key='19177-5 ',description='AFP SerPl-sCnc Alpha-1-Fetoprotein [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='31993-9 ',description='AFP SerPl Ql Alpha-1-Fetoprotein [Presence] in Serum or Plasma')
        db.result_type.insert(key='626-2',description=' Bacteria Throat Cult Bacteria identified in Throat by Culture')
        db.result_type.insert(key='24321-2 ',description='Bas Metab HCFA 2000 Pnl SerPl Basic metabolic HCFA 2000 panel in Serum or Plasma')
        db.result_type.insert(key='24320-4 ',description='Bas Metab HCFA 1998 Pnl SerPl Basic metabolic HCFA 1998 panel in Serum or Plasma')
        db.result_type.insert(key='14639-9',description=' Carbamazepine SerPl-sCnc Carbamazepine [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='3432-2',description=' Carbamazepine SerPl-mCnc Carbamazepine [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='18270-9',description=' Carbamazepine EP SerPl-sCnc Carbamazepine 10,11-Epoxide [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='9415-1',description=' Carbamazepine EP SerPl-mCnc Carbamazepine 10,11-Epoxide [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='29147-6',description=' Carbamazepine EP Bnd SerPl-mCnc Carbamazepine 10,11-Epoxide.bound [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='14056-6',description=' Carbamazepine EP Free SerPl-mCnc Carbamazepine 10,11-epoxide free [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='34545-4',description=' Carbamazepine free+Total Pnl SerPlmCnc Carbamazepine free & total panel [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='29148-4',description=' Carbamazepine Bnd SerPl-mCnc Carbamazepine.bound [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='32058-0',description=' Carbamazepine free SerPl-sCnc Carbamazepine free [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='3433-0',description='Carbamazepine free SerPl-mCnc Carbamazepine free [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='32852-6',description=' Carbamazepine free Fr SerPl Carbamazepine free/Carbamazepine total in Serum or Plasma')
        db.result_type.insert(key='34718-7',description=' CFTR Mut Anal Amn CFTR gene mutations found [Identifier] in Amniotic Fluid by Molecular genetics method Nominal')
        db.result_type.insert(key='557-9',description=' Chlamydia Genital Cult Chlamydia sp identified in Genital specimen by Organism specific culture')
        db.result_type.insert(key='560-3',description=' Chlamydia XXX Cult Chlamydia sp identified in Unspecified specimen by Organism specific culture')
        db.result_type.insert(key='14463-4 ',description='C trach Cervix Ql Cult Chlamydia trachomatis [Presence] in Cervix by Organism specific culture')
        db.result_type.insert(key='14464-2 ',description='C trach Vag Ql Cult Chlamydia trachomatis [Presence] in Vaginal fluid by Organism specific culture')
        db.result_type.insert(key='14467-5 ',description='C trach UrnS Ql Cult Chlamydia trachomatis [Presence] in Urine sediment by Organism specific culture')
        db.result_type.insert(key='6349-5 ',description='C trach XXX Ql Cult Chlamydia trachomatis [Presence] in Unspecified specimen by Organism specific culture')
        db.result_type.insert(key='14470-9 ',description='C trach Ag Cervix Ql EIA Chlamydia trachomatis Ag [Presence] in Cervix by Immunoassay')
        db.result_type.insert(key='14471-7 ',description='C trach Ag Vag Ql EIA Chlamydia trachomatis Ag [Presence] in Vaginal fluid by Immunoassay')
        db.result_type.insert(key='14474-1 ',description='C trach Ag UrnS Ql EIA Chlamydia trachomatis Ag [Presence] in Urine sediment by Immunoassay')
        db.result_type.insert(key='14509-4 ',description='C trach Ag Cervix Ql IF Chlamydia trachomatis Ag [Presence] in Cervix by Immunofluorescence')
        db.result_type.insert(key='14510-2 ',description='C trach Ag Vag Ql IF Chlamydia trachomatis Ag [Presence] in Vaginal fluid by Immunofluorescence')
        db.result_type.insert(key='14513-6 ',description='C trach Ag UrnS Ql IF Chlamydia trachomatis Ag [Presence] in Urine sediment by Immunofluorescence')
        db.result_type.insert(key='31771-9 ',description='C trach Ag Cervix Ql Chlamydia trachomatis Ag [Presence] in Cervix')
        db.result_type.insert(key='31772-7 ',description='C trach Ag Vag Ql Chlamydia trachomatis Ag [Presence] in Vaginal fluid')
        db.result_type.insert(key='31775-0 ',description='C trach Ag UrnS Ql Chlamydia trachomatis Ag [Presence] in Urine sediment')
        db.result_type.insert(key='31777-6 ',description='C trach Ag XXX Ql Chlamydia trachomatis Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='6354-5 ',description='C trach Ag XXX Ql EIA Chlamydia trachomatis Ag [Presence] in Unspecified specimen by Immunoassay')
        db.result_type.insert(key='6355-2 ',description='C trach Ag XXX Ql IF Chlamydia trachomatis Ag [Presence] in Unspecified specimen by Immunofluorescence')
        db.result_type.insert(key='21189-6 ',description='C trach DNA Cerv mucus Ql PCR Chlamydia trachomatis DNA [Presence] in Cervical mucus by Probe & target amplification method')
        db.result_type.insert(key='21190-4 ',description='C trach DNA Cervix Ql PCR Chlamydia trachomatis DNA [Presence] in Cervix by Probe & target amplification method')
        db.result_type.insert(key='21191-2 ',description='C trach DNA Urth Ql PCR Chlamydia trachomatis DNA [Presence] in Urethra by Probe & target amplification method')
        db.result_type.insert(key='21613-5 ',description='C trach DNA XXX Ql PCR Chlamydia trachomatis DNA [Presence] in Unspecified specimen by Probe & target amplification method')
        db.result_type.insert(key='43404-3 ',description='C trach DNA XXX Ql bDNA Chlamydia trachomatis DNA [Presence] in Unspecified specimen by Probe & signal amplification method')
        db.result_type.insert(key='6356-0 ',description='C trach DNA Genital Ql PCR Chlamydia trachomatis DNA [Presence] in Genital specimen by Probe & target amplification method')
        db.result_type.insert(key='6357-8 ',description='C trach DNA Ur Ql PCR Chlamydia trachomatis DNA [Presence] in Urine by Probe & target amplification method')
        db.result_type.insert(key='16600-9 ',description='C trach rRNA Genital Ql Prb Chlamydia trachomatis rRNA [Presence] in Genital specimen by DNA probe')
        db.result_type.insert(key='16601-7 ',description='C trach rRNA Ur Ql Prb Chlamydia trachomatis rRNA [Presence] in Urine by DNA probe')
        db.result_type.insert(key='21192-0 ',description='C trach rRNA Urth Ql Prb Chlamydia trachomatis rRNA [Presence] in Urethra by DNA probe')
        db.result_type.insert(key='23838-6 ',description='C trach rRNA Genital fl Ql Prb Chlamydia trachomatis rRNA [Presence] in Genital fluid by DNA probe')
        db.result_type.insert(key='42931-6 ',description='C trach rRNA Ur Ql PCR DL=50 Chlamydia trachomatis rRNA [Presence] in Urine by Probe & target amplification method detection limit = 50 iU/mL')
        db.result_type.insert(key='43304-5 ',description='C trach rRNA XXX Ql PCR Chlamydia trachomatis rRNA [Presence] in Unspecified specimen by Probe & target amplification method')
        db.result_type.insert(key='4993-2 ',description='C trach rRNA XXX Ql Prb Chlamydia trachomatis rRNA [Presence] in Unspecified specimen by DNA probe')
        db.result_type.insert(key='36902-5 ',description='C trach+GC DNA XXX Ql PCR Chlamydia trachomatis+Neisseria gonorrhoeae DNA [Presence] in Unspecified specimen by Probe & target amplification method')
        db.result_type.insert(key='36903-3 ',description='C trach+GC DNA XXX PCR Chlamydia trachomatis+Neisseria gonorrhoeae DNA [Identifier] in Unspecified specimen by Probe & target amplification method')
        db.result_type.insert(key='43406-8 ',description='C trach+GC DNA XXX Ql bDNA Chlamydia trachomatis+Neisseria gonorrhoeae DNA [Presence] in Unspecified specimen by Probe & signal amplification method')
        db.result_type.insert(key='12773-8',description=' LDLc SerPl Elph-aCnc Cholesterol.in LDL [Units/volume] in Serum or Plasma by Electrophoresis')
        db.result_type.insert(key='13457-7',description=' LDLc SerPl Calc-mCnc Cholesterol.in LDL [Mass/volume] in Serum or Plasma by Calculation')
        db.result_type.insert(key='18261-8',description=' LDLc SerPl.Ultracent-mCnc Cholesterol.in LDL [Mass/volume] in Serum or Plasma ultracentrifugate')
        db.result_type.insert(key='18262-6',description=' LDLc SerPl Direct Assay-mCnc Cholesterol.in LDL [Mass/volume] in Serum or Plasma by Direct assay')
        db.result_type.insert(key='2089-1',description=' LDLc SerPl-mCnc Cholesterol.in LDL [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='22748-8',description=' LDLc SerPl-sCnc Cholesterol.in LDL [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='39469-2',description=' LDLc SerPl Calc-sCnc Cholesterol.in LDL [Molecules/volume] in Serum or Plasma by Calculation')
        db.result_type.insert(key='49132-4',description=' LDLc SerPl Elph-mCnc Cholesterol.in LDL [Mass/volume] in Serum or Plasma by Electrophoresis')
        db.result_type.insert(key='19080-1',description=' HCG SerPl-aCnc Choriogonadotropin [Units/volume] in Serum or Plasma')
        db.result_type.insert(key='20994-0',description=' HCG SerPl-Imp Choriogonadotropin [interpretation] in Serum or Plasma')
        db.result_type.insert(key='2106-3',description=' HCG Ur Ql Choriogonadotropin [Presence] in Urine')
        db.result_type.insert(key='2107-1',description=' HCG Ur-sCnc Choriogonadotropin [Molecules/volume] in Urine')
        db.result_type.insert(key='2118-8',description=' HCG SerPl Ql Choriogonadotropin [Presence] in Serum or Plasma')
        db.result_type.insert(key='2119-6',description=' HCG SerPl-sCnc Choriogonadotropin [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='25372-4',description=' HCG Ur-aCnc Choriogonadotropin [Units/volume] in Urine')
        db.result_type.insert(key='34670-0',description=' HCG SerPl-mCnc Choriogonadotropin [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='20415-6 ',description='B-HCG SerPl EIA 3rd IS-aCnc Choriogonadotropin.beta subunit [Units/volume] in Serum or Plasma byImmunoassay (EIA) 3rd IS')
        db.result_type.insert(key='2110-5 ',description='B-HCG SerPl Ql Choriogonadotropin.beta subunit [Presence] in Serum or Plasma')
        db.result_type.insert(key='2111-3 ',description='B-HCG SerPl-sCnc Choriogonadotropin.beta subunit [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='2112-1 ',description='B-HCG Ur Ql Choriogonadotropin.beta subunit [Presence] in Urine')
        db.result_type.insert(key='2113-9 ',description='B-HCG 24H Ur-mRate Choriogonadotropin.beta subunit [Mass/time] in 24 hour Urine')
        db.result_type.insert(key='2114-7 ',description='B-HCG Ur-sCnc Choriogonadotropin.beta subunit [Molecules/volume] in Urine')
        db.result_type.insert(key='21198-7 ',description='B-HCG SerPl-aCnc Choriogonadotropin.beta subunit [Units/volume] in Serum or Plasma')
        db.result_type.insert(key='19180-9 ',description='B-HCG Free SerPl-aCnc Choriogonadotropin.beta subunit free [Units/volume] in Serum or Plasma')
        db.result_type.insert(key='2115-4 ',description='B-HCG Free SerPl-sCnc Choriogonadotropin.beta subunit free [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='25373-2 ',description='B-HCG Free SerPl-mCnc Choriogonadotropin.beta subunit free [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='24323-8 ',description='Comp Metab HCFA 2000 Pnl SerPl Comprehensive metabolic HCFA 2000 panel in Serum or Plasma')
        db.result_type.insert(key='24322-0 ',description='Comp Metab HCFA 1998 Pnl SerPl Comprehensive metabolic HCFA 1998 panel in Serum or Plasma')
        db.result_type.insert(key='14682-9 ',description='Creat SerPl-sCnc Creatinine [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='21232-4 ',description='Creat BldA-mCnc Creatinine [Mass/volume] in Arterial blood')
        db.result_type.insert(key='2160-0 ',description='Creat SerPl-mCnc Creatinine [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='38483-4 ',description='Creat Bld-mCnc Creatinine [Mass/volume] in Blood')
        db.result_type.insert(key='34555-3 ',description='Creat Cl Pnl Ur+SerPl Creatinine renal clearance panel')
        db.result_type.insert(key='13441-1 ',description='Creat Cl 4H Ur+SerPl-vRate Creatinine renal clearance in 4 hour')
        db.result_type.insert(key='13442-9 ',description='Creat Cl 6H Ur+SerPl-vRate Creatinine renal clearance in 6 hour')
        db.result_type.insert(key='13443-7 ',description='Creat Cl 8H Ur+SerPl-vRate Creatinine renal clearance in 8 hour')
        db.result_type.insert(key='2163-4 ',description='Creat Cl 12H Ur+SerPl-vRate Creatinine renal clearance in 12 hour')
        db.result_type.insert(key='2164-2 ',description='Creat Cl 24H Ur+SerPl-vRate Creatinine renal clearance in 24 hour')
        db.result_type.insert(key='26752-6 ',description='Creat Cl 2H Ur+SerPl-vRate Creatinine renal clearance in 2 hour')
        db.result_type.insert(key='33558-8 ',description='Creat Cl ?Tm Ur+SerPl-vRate Creatinine renal clearance in unspecified time')
        db.result_type.insert(key='35591-7 ',description='Creat Cl predicted SerPl C-G-vRate Creatinine renal clearance predicted by Cockroft-Gault formula')
        db.result_type.insert(key='12195-4 ',description='Creat Cl/BSA 24H Ur+SerPl-vRate Creatinine renal clearance/1.73 sq M in 24 hour')
        db.result_type.insert(key='13446-0 ',description='Creat Cl/BSA 4H Ur+SerPl-vRate Creatinine renal clearance/1.73 sq M in 4 hour')
        db.result_type.insert(key='13447-8 ',description='Creat Cl/BSA 6H Ur+SerPl-vRate Creatinine renal clearance/1.73 sq M in 6 hour')
        db.result_type.insert(key='13449-4 ',description='Creat Cl/BSA 8H Ur+SerPl-vRate Creatinine renal clearance/1.73 sq M in 8 hour')
        db.result_type.insert(key='13450-2 ',description='Creat Cl/BSA 12H Ur+SerPl-vRate Creatinine renal clearance/1.73 sq M in 12 hour')
        db.result_type.insert(key='35593-3 ',description='Creat Cl/BSA ?Tm Ur+SerPl-vRate Creatinine renal clearance/1.73 sq M in unspecified time')
        db.result_type.insert(key='35594-1 ',description='Creat Cl/BSA 2H Ur+SerPl-vRate Creatinine renal clearance/1.73 sq M in 2 hour')
        db.result_type.insert(key='35592-5 ',description='Creat Cl/BSA.pred SerPl C-G-vRate Creatinine renal clearance/1.73 sq M.predicted by Cockroft-Gault formula, BSA formula')
        db.result_type.insert(key='16188-5 ',description='Creat 2H spec SerPl-mCnc Creatinine [Mass/volume] in Serum or Plasma --2 hour specimen')
        db.result_type.insert(key='16189-3 ',description='Creat 4H spec SerPl-mCnc Creatinine [Mass/volume] in Serum or Plasma --4 hour specimen')
        db.result_type.insert(key='11041-1 ',description='Creat p dialysis SerPl-mCnc Creatinine [Mass/volume] in Serum or Plasma --post dialysis')
        db.result_type.insert(key='11042-9 ',description='Creat pre dial SerPl-mCnc Creatinine [Mass/volume] in Serum or Plasma --pre dialysis')
        db.result_type.insert(key='47527-7 ',description='Cytology Cvx/Vag Doc Thin Prep Cytology report [Finding] of Cervical or vaginal smear or scraping Cyto stain.thin prep')
        db.result_type.insert(key='19774-9 ',description='Cytology Cmnt Cvx/Vag Cyto-Imp Cytology study comment Cervical or vaginal smear or scraping Cyto stain')
        db.result_type.insert(key='15377-5 ',description='CMV Ab Ser Ql LA Cytomegalovirus Ab [Presence] in Serum by Latex agglutination')
        db.result_type.insert(key='16714-8 ',description='CMV Ab Ser LA-aCnc Cytomegalovirus Ab [Units/volume] in Serum by Latex agglutination')
        db.result_type.insert(key='22239-8 ',description='CMV Ab Ser Ql Cytomegalovirus Ab [Presence] in Serum')
        db.result_type.insert(key='22241-4 ',description='CMV Ab Titr Ser Cytomegalovirus Ab [Titer] in SerumCytology')
        db.result_type.insert(key='32170-3 ',description='CMV Ab Titr Ser IF Cytomegalovirus Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='5121-9 ',description='CMV Ab Titr Ser LA Cytomegalovirus Ab [Titer] in Serum by Latex agglutination')
        db.result_type.insert(key='5122-7 ',description='CMV Ab Ser IF-aCnc Cytomegalovirus Ab [Units/volume] in Serum by Immunofluorescence')
        db.result_type.insert(key='7851-9 ',description='CMV Ab Ser-aCnc Cytomegalovirus Ab [Units/volume] in Serum')
        db.result_type.insert(key='9513-3 ',description='CMV Ab Titr Ser CF Cytomegalovirus Ab [Titer] in Serum by Complement fixation')
        db.result_type.insert(key='34403-6 ',description='CMV Ab Avidity Ser-aCnc Cytomegalovirus Ab avidity [Units/volume] in Serum')
        db.result_type.insert(key='13949-3 ',description='CMV IgG Ser Ql EIA Cytomegalovirus IgG Ab [Presence] in Serum by Immunoassay')
        db.result_type.insert(key='16715-5 ',description='CMV IgG Ser IF-aCnc Cytomegalovirus IgG Ab [Units/volume] in Serum by Immunofluorescence')
        db.result_type.insert(key='22244-8 ',description='CMV IgG Ser Ql Cytomegalovirus IgG Ab [Presence] in Serum')
        db.result_type.insert(key='22246-3 ',description='CMV IgG Titr Ser Cytomegalovirus IgG Ab [Titer] in Serum')
        db.result_type.insert(key='5124-3 ',description='CMV IgG Ser EIA-aCnc Cytomegalovirus IgG Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='5125-0 ',description='CMV IgG Titr Ser IF Cytomegalovirus IgG Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='7852-7 ',description='CMV IgG Ser-aCnc Cytomegalovirus IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='13225-8 ',description='CMV IgG sp1 Ser-aCnc Cytomegalovirus IgG Ab [Units/volume] in Serum --1st specimen')
        db.result_type.insert(key='32791-6 ',description='CMV IgG 1:2 Ser EIA-Rto Cytomegalovirus IgG Ab [Ratio] in Serum by Immunoassay --1st specimen/2nd specimen')
        db.result_type.insert(key='32835-1 ',description='CMV IgG 1:2 Ser-Rto Cytomegalovirus IgG Ab [Ratio] in Serum --1st specimen/2nd specimen')
        db.result_type.insert(key='16716-3 ',description='CMV IgG sp2 Ser EIA-aCnc Cytomegalovirus IgG Ab [Units/volume] in Serum by Immunoassay --2nd specimen')
        db.result_type.insert(key='22247-1 ',description='CMV IgG sp2 Ser-aCnc Cytomegalovirus IgG Ab [Units/volume] in Serum --2nd specimen')
        db.result_type.insert(key='22249-7 ',description='CMV IgM Titr Ser Cytomegalovirus IgM Ab [Titer] in Serum')
        db.result_type.insert(key='24119-0 ',description='CMV IgM Ser Ql EIA Cytomegalovirus IgM Ab [Presence] in Serum by Immunoassay')
        db.result_type.insert(key='30325-5 ',description='CMV IgM Ser Ql Cytomegalovirus IgM Ab [Presence] in Serum')
        db.result_type.insert(key='5126-8 ',description='CMV IgM Ser EIA-aCnc Cytomegalovirus IgM Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='5127-6 ',description='CMV IgM Titr Ser IF Cytomegalovirus IgM Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='7853-5 ',description='CMV IgM Ser-aCnc Cytomegalovirus IgM Ab [Units/volume] in Serum')
        db.result_type.insert(key='34554-6 ',description='Lytes HCFA 1998 + Ven pH Pnl Electrolytes HCFA 1998 & Venous pH panel')
        db.result_type.insert(key='24326-1 ',description='Lytes HCFA 1998 Pnl SerPl Electrolytes HCFA 1998 panel in Serum or Plasma')
        db.result_type.insert(key='20403-2 ',description='Fibronectin Fetal Vag-mCnc Fibronectin.fetal [Mass/volume] in Vaginal fluid')
        db.result_type.insert(key='20404-0 ',description='Fibronectin Fetal Vag Ql Fibronectin.fetal [Presence] in Vaginal fluid')
        db.result_type.insert(key='19762-4 ',description='Gen Categ Cvx/Vag Cyto-Imp General categories [interpretation] in Cervical or vaginal smear or scraping by Cyto stain')
        db.result_type.insert(key='17856-6',description=' Hgb A1c Fr Bld HPLC Hemoglobin A1c (glycated HgB)/Hemoglobin.total in Blood by HPLC')
        db.result_type.insert(key='44548-4',description=' Hgb A1c Fr Bld Hemoglobin A1c (glycated HgB)/Hemoglobin.total in Blood')
        db.result_type.insert(key='549-2',description=' Hgb A1c Fr Bld Elph Hemoglobin A1c (glycated HgB)/Hemoglobin.total in Blood by Electrophoresis')
        db.result_type.insert(key='2335-8',description=' Hemocult Stl Ql Hemoglobin.gastrointestinal [Presence] in Stool')
        db.result_type.insert(key= '27396-1',description=' Hemocult Stl-mCnt Hemoglobin.gastrointestinal [Mass/mass] in Stool')
        db.result_type.insert(key='29771-3',description=' Occult Bld Stl Ql Imm Hemoglobin.gastrointestinal [Presence] in Stool by Immunologic method')
        db.result_type.insert(key='14563-1',description=' Hemocult sp1 Stl Ql Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen')
        db.result_type.insert(key='14564-9 ',description='Hemocult sp2 Stl Ql Hemoglobin.gastrointestinal [Presence] in Stool --2nd specimen')
        db.result_type.insert(key='14565-6 ',description='Hemocult sp3 Stl Ql Hemoglobin.gastrointestinal [Presence] in Stool --3rd specimen')
        db.result_type.insert(key='12503-9 ',description='Hemocult sp4 Stl Ql Hemoglobin.gastrointestinal [Presence] in Stool --4th specimen')
        db.result_type.insert(key='12504-7 ',description='Hemocult sp5 Stl Ql Hemoglobin.gastrointestinal [Presence] in Stool --5th specimen')
        db.result_type.insert(key='27401-9 ',description='Hemocult sp6 Stl Ql Hemoglobin.gastrointestinal [Presence] in Stool --6th specimen')
        db.result_type.insert(key='27925-7 ',description='Hemocult sp7 Stl Ql Hemoglobin.gastrointestinal [Presence] in Stool --7th specimen')
        db.result_type.insert(key='27926-5 ',description='Hemocult sp8 Stl Ql Hemoglobin.gastrointestinal [Presence] in Stool --8th specimen')
        db.result_type.insert(key='13324-9 ',description='HSV1 Ab Ser IF-aCnc Herpes simplex virus 1 Ab [Units/volume] in Serum by Immunofluorescence')
        db.result_type.insert(key='25837-6 ',description='HSV1 Ab Titr Ser IF Herpes simplex virus 1 Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='43031-4 ',description='HSV1 Ab Titr Ser Herpes simplex virus 1 Ab [Titer] in Serum')
        db.result_type.insert(key='43111-4 ',description='HSV1 Ab Ser Ql Herpes simplex virus 1 Ab [Presence] in Serum')
        db.result_type.insert(key='5205-0 ',description='HSV1 Ab Ser EIA-aCnc Herpes simplex virus 1 Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='7908-7 ',description='HSV1 Ab Ser-aCnc Herpes simplex virus 1 Ab [Units/volume] in Serum')
        db.result_type.insert(key='17850-9 ',description='HSV1 IgG Ser Ql Herpes simplex virus 1 IgG Ab [Presence] in Serum')
        db.result_type.insert(key='33291-6 ',description='HSV1 IgG Ser Ql IB Herpes simplex virus 1 IgG Ab [Presence] in Serum by Immunoblot (IB)')
        db.result_type.insert(key='5206-8 ',description='HSV1 IgG Ser EIA-aCnc Herpes simplex virus 1 IgG Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='7909-5 ',description='HSV1 IgG Ser-aCnc Herpes simplex virus 1 IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='16949-0 ',description='HSV1 IgG sp1 Ser-aCnc Herpes simplex virus 1 IgG Ab [Units/volume] in Serum --1st specimen')
        db.result_type.insert(key='32831-0 ',description='HSV1 IgG 1:2 Ser EIA-Rto Herpes simplex virus 1 IgG Ab [Ratio] in Serum by Immunoassay --1st specimen/2nd specimen')
        db.result_type.insert(key='32846-8 ',description='HSV1 IgG 1:2 Ser-Rto Herpes simplex virus 1 IgG Ab [Ratio] in Serum --1st specimen/2nd specimen')
        db.result_type.insert(key='16950-8 ',description='HSV1 IgG sp2 Ser-aCnc Herpes simplex virus 1 IgG Ab [Units/volume] in Serum --2nd specimen')
        db.result_type.insert(key='21326-4 ',description='HSV1 IgM Titr Ser Herpes simplex virus 1 IgM Ab [Titer] in Serum')
        db.result_type.insert(key='32687-6 ',description='HSV1 IgM Ser Ql Herpes simplex virus 1 IgM Ab [Presence] in Serum')
        db.result_type.insert(key='40466-5 ',description='HSV1 IgM Ser Ql IF Herpes simplex virus 1 IgM Ab [Presence] in Serum by Immunofluorescence')
        db.result_type.insert(key='5207-6 ',description='HSV1 IgM Ser EIA-aCnc Herpes simplex virus 1 IgM Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='7910-3 ',description='HSV1 IgM Ser-aCnc Herpes simplex virus 1 IgM Ab [Units/volume] in Serum')
        db.result_type.insert(key='42337-6 ',description='HSV1 gG IgG Ser-aCnc Herpes simplex virus 1 glycoprotein G IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='13505-3 ',description='HSV1+2 Ab pattern Ser-Imp Herpes simplex virus 1+2 Ab pattern [interpretation] in Serum')
        db.result_type.insert(key='27948-9 ',description='HSV1+2 IgG Ser EIA-aCnc Herpes simplex virus 1+2 IgG Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='31411-2 ',description='HSV1+2 IgG Ser-aCnc Herpes simplex virus 1+2 IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='34613-0 ',description='HSV1+2 IgG Titr Ser Herpes simplex virus 1+2 IgG Ab [Titer] in Serum')
        db.result_type.insert(key='36921-5 ',description='HSV1+2 IgG Ser Ql Herpes simplex virus 1+2 IgG Ab [Presence] in Serum')
        db.result_type.insert(key='30355-2 ',description='HSV1+2 IgM Ser Ql IF Herpes simplex virus 1+2 IgM Ab [Presence] in Serum by Immunofluorescence')
        db.result_type.insert(key='34152-9 ',description='HSV1+2 IgM Titr Ser Herpes simplex virus 1+2 IgM Ab [Titer] in Serum')
        db.result_type.insert(key='41149-6 ',description='HSV1+2 IgM Ser Ql Herpes simplex virus 1+2 IgM Ab [Presence] in Serum')
        db.result_type.insert(key='41399-7 ',description='HSV1+2 IgM Ser EIA-aCnc Herpes simplex virus 1+2 IgM Ab [Units/volume] in Serum) by Immunoassay')
        db.result_type.insert(key='43030-6 ',description='HSV1+2 IgM Ser-aCnc Herpes simplex virus 1+2 IgM Ab [Units/volume] in Serum')
        db.result_type.insert(key='13323-1 ',description='HSV2 Ab Ser IF-aCnc Herpes simplex virus 2 Ab [Units/volume] in Serum by Immunofluorescence')
        db.result_type.insert(key='16954-0 ',description='HSV2 Ab Ser Ql Herpes simplex virus 2 Ab [Presence] in Serum')
        db.result_type.insert(key='25839-2 ',description='HSV2 Ab Titr Ser IF Herpes simplex virus 2 Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='43028-0 ',description='HSV2 Ab Titr Ser Herpes simplex virus 2 Ab [Titer] in Serum')
        db.result_type.insert(key='5208-4 ',description='HSV2 Ab Ser EIA-aCnc Herpes simplex virus 2 Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='7911-1 ',description='HSV2 Ab Ser-aCnc Herpes simplex virus 2 Ab [Units/volume] in Serum')
        db.result_type.insert(key='13501-2 ',description='HSV2 Ab pattern Ser-Imp Herpes simplex virus 2 Ab pattern [interpretation] in Serum')
        db.result_type.insert(key='16955-7 ',description='HSV2 IgG Ser Ql IB Herpes simplex virus 2 IgG Ab [Presence] in Serum by Immunoblot (IB)')
        db.result_type.insert(key='17851-7 ',description='HSV2 IgG Ser Ql Herpes simplex virus 2 IgG Ab [Presence] in Serum')
        db.result_type.insert(key='24014-3 ',description='HSV2 IgG Titr Ser Herpes simplex virus 2 IgG Ab [Titer] in Serum')
        db.result_type.insert(key='5209-2 ',description='HSV2 IgG Ser EIA-aCnc Herpes simplex virus 2 IgG Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='7912-9 ',description='HSV2 IgG Ser-aCnc Herpes simplex virus 2 IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='16957-3 ',description='HSV2 IgG sp1 Ser-aCnc Herpes simplex virus 2 IgG Ab [Units/volume] in Serum --1st specimen')
        db.result_type.insert(key='32790-8 ',description='HSV2 IgG 1:2 Ser EIA-Rto Herpes simplex virus 2 IgG Ab [Ratio] in Serum by Immunoassay --1st specimen/2nd specimen')
        db.result_type.insert(key='32834-4 ',description='HSV2 IgG 1:2 Ser-Rto Herpes simplex virus 2 IgG Ab [Ratio] in Serum --1st specimen/2nd specimen')
        db.result_type.insert(key='16958-1 ',description='HSV2 IgG sp2 Ser-aCnc Herpes simplex virus 2 IgG Ab [Units/volume] in Serum --2nd specimen')
        db.result_type.insert(key='21327-2 ',description='HSV2 IgM Titr Ser Herpes simplex virus 2 IgM Ab [Titer] in Serum')
        db.result_type.insert(key='26927-4 ',description='HSV2 IgM Titr Ser IF Herpes simplex virus 2 IgM Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='32688-4 ',description='HSV2 IgM Ser Ql Herpes simplex virus 2 IgM Ab [Presence] in Serum')
        db.result_type.insert(key='5210-0 ',description='HSV2 IgM Ser EIA-aCnc Herpes simplex virus 2 IgM Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='7913-7 ',description='HSV2 IgM Ser-aCnc Herpes simplex virus 2 IgM Ab [Units/volume] in Serum')
        db.result_type.insert(key='42338-4 ',description='HSV2 gG IgG Ser-aCnc Herpes simplex virus 2 glycoprotein G IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='22339-6 ',description='HSV Ab Ser Ql Herpes simplex virus Ab [Presence] in Serum')
        db.result_type.insert(key='22341-2 ',description='HSV Ab Titr Ser Herpes simplex virus Ab [Titer] in Serum')
        db.result_type.insert(key='5202-7 ',description='HSV Ab Ser EIA-aCnc Herpes simplex virus Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='5203-5 ',description='HSV Ab Ser LA-aCnc Herpes simplex virus Ab [Units/volume] in Serum by Latex agglutination')
        db.result_type.insert(key='5204-3 ',description='HSV Ab Titr Ser CF Herpes simplex virus Ab [Titer] in Serum by Complement fixation')
        db.result_type.insert(key='7907-9 ',description='HSV Ab Ser-aCnc Herpes simplex virus Ab [Units/volume] in Serum')
        db.result_type.insert(key='19106-4 ',description='HSV IgG Ser Ql Herpes simplex virus IgG Ab [Presence] in Serum')
        db.result_type.insert(key='40728-8 ',description='HSV IgG Ser Ql EIA Herpes simplex virus IgG Ab [Presence] in Serum by Immunoassay')
        db.result_type.insert(key='9422-7 ',description='HSV IgG Ser-aCnc Herpes simplex virus IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='10350-7 ',description='HSV IgM Titr Ser EIA Herpes simplex virus IgM Ab [Titer] in Serum by Immunoassay')
        db.result_type.insert(key='14213-3 ',description='HSV IgM Titr Ser IF Herpes simplex virus IgM Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='16944-1 ',description='HSV IgM Ser-aCnc Herpes simplex virus IgM Ab [Units/volume] in Serum')
        db.result_type.insert(key='22343-8 ',description='HSV IgM Titr Ser Herpes simplex virus IgM Ab [Titer] in Serum')
        db.result_type.insert(key='25435-9 ',description='HSV IgM Ser Ql Herpes simplex virus IgM Ab [Presence] in Serum')
        db.result_type.insert(key='40729-6 ',description='HSV IgM Ser Ql EIA Herpes simplex virus IgM Ab [Presence] in Serum by Immunoassay')
        db.result_type.insert(key='17398-9',description=' HPV11 Ag XXX Ql Human papilloma virus 11 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17399-7',description=' HPV16 Ag XXX Ql Human papilloma virus 16 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='12223-4',description=' HPV16+18 Ag Genital Ql Human papilloma virus 16+18 Ag [Presence] in Genital specimen')
        db.result_type.insert(key='14503-7',description=' HPV16+18 Ag Cervix Ql Human papilloma virus 16+18 Ag [Presence] in Cervix')
        db.result_type.insert(key='14504-5',description=' HPV16+18 Ag Vag Ql Human papilloma virus 16+18 Ag [Presence] in Vaginal fluid')
        db.result_type.insert(key='14506-0',description=' HPV16+18 Ag Urth Ql Human papilloma virus 16+18 Ag [Presence] in Urethra')
        db.result_type.insert(key='17400-3',description=' HPV16+18 Ag XXX Ql Human papilloma virus 16+18 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='30167-1',description=' HPV I/H Risk 1 DNA Cervix Ql bDNA Human papilloma virus 16+18+31+33+35+39+45+51+52+56+58+59+68 DNA [Presence] in Cervix by Probe & signal amplification method')
        db.result_type.insert(key='21440-3',description=' HPV I/H Risk DNA Cervix Ql Prb Human papilloma virus 16+18+31+33+35+45+51+52+56 DNA [Presence] in Cervix by DNA probe')
        db.result_type.insert(key='17401-1',description=' HPV18 Ag XXX Ql Human papilloma virus 18 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17402-9',description=' HPV31 Ag XXX Ql Human papilloma virus 31 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17403-7',description=' HPV31+33+35 Ag XXX Ql Human papilloma virus 31+33+35 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17404-5',description=' HPV33 Ag XXX Ql Human papilloma virus 33 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17405-2',description=' HPV42 Ag XXX Ql Human papilloma virus 42 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17406-0',description=' HPV43 Ag XXX Ql Human papilloma virus 43 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17407-8',description=' HPV44 Ag XXX Ql Human papilloma virus 44 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17408-6',description=' HPV45 Ag XXX Ql Human papilloma virus 45 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17409-4',description=' HPV5 Ag XXX Ql Human papilloma virus 5 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17410-2',description=' HPV51 Ag XXX Ql Human papilloma virus 51 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17411-0',description=' HPV6 Ag XXX Ql Human papilloma virus 6 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='17412-8',description=' HPV6+11 Ag XXX Ql Human papilloma virus 6+11 Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='38372-9',description=' HPV DNA Cervix Ql bDNA Human Papilloma Virus 6+11+16+18+31+33+35+39+42+43+44+45+51+52+56+58+59+68 DNA [Presence] in Cervix by Probe & signal amplification method')
        db.result_type.insert(key='21441-1 ',description='HPV Low Risk DNA Cervix Ql Prb Human papilloma virus 6+11+42+43+44 DNA [Presence] in Cervix by DNA probe')
        db.result_type.insert(key='42481-2 ',description='HPV Low Risk DNA Cervix Ql bDNA Human papilloma virus 6+11+42+43+44 DNA [Presence] in Cervix by Probe & signal amplification method')
        db.result_type.insert(key='6510-2 ',description='HPV Ab Genital Ql EIA Human papilloma virus Ab [Presence] in Genital specimen by Immunoassay')
        db.result_type.insert(key='6511-0 ',description='HPV Ab Genital Ql IB Human papilloma virus Ab [Presence] in Genital specimen by Immunoblot (IB)')
        db.result_type.insert(key='7975-6 ',description='HPV Ab Genital Ql Human papilloma virus Ab [Presence] in Genital specimen')
        db.result_type.insert(key='10705-2 ',description='HPV Ag Tiss Ql ImStn Human papilloma virus Ag [Presence] in Tissue by Immune stain')
        db.result_type.insert(key='12222-6 ',description='HPV Ag Genital Ql Human papilloma virus Ag [Presence] in Genital specimen')
        db.result_type.insert(key='14499-8 ',description='HPV Ag Cervix Ql Human papilloma virus Ag [Presence] in Cervix')
        db.result_type.insert(key='14500-3 ',description='HPV Ag Vag Ql Human papilloma virus Ag [Presence] in Vaginal fluid')
        db.result_type.insert(key='14502-9 ',description='HPV Ag Urth Ql Human papilloma virus Ag [Presence] in Urethra')
        db.result_type.insert(key='16280-0 ',description='HPV DNA XXX Ql Amp Prb Human papilloma virus DNA [Presence] in Unspecified specimen by Probe with amplification')
        db.result_type.insert(key='11083-3 ',description='HPV Cervix Human papilloma virus identified in Cervix')
        db.result_type.insert(key='11481-9 ',description='HPV XXX Human papilloma virus identified in Unspecified specimen')
        db.result_type.insert(key='6514-4 ',description='HPV rRNA Genital Ql PCR Human papilloma virus rRNA [Presence] in Genital specimen by Probe & target amplification method')
        db.result_type.insert(key='6516-9',description=' HPV rRNA XXX Ql PCR Human papilloma virus rRNA [Presence] in Unspecified specimen by Probe & target amplification method')
        db.result_type.insert(key='33773-3',description=' Karyotyp Amn Karyotype [Identifier] in Amniotic Fluid Nominal')
        db.result_type.insert(key='34656-9',description=' KEL gene Mut Anal Amn KEL gene mutations found [Identifier] in Amniotic Fluid by Molecular genetics method Narrative')
        db.result_type.insert(key='10368-9',description=' Lead BldC-mCnc Lead [Mass/volume] in Capillary blood')
        db.result_type.insert(key='12-4',description=' Lead SerPl-mCnc Lead [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='14807-2',description=' Lead Bld-sCnc Lead [Molecules/volume] in Blood')
        db.result_type.insert(key='17052-2',description=' Lead Bld Ql Lead [Presence] in Blood')
        db.result_type.insert(key='25459-9',description=' Lead SerPl-sCnc Lead [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='27129-6',description=' Lead RBC-mCnt Lead [Mass/mass] in Red Blood Cells')
        db.result_type.insert(key='32325-3',description=' Lead RBC-sCnc Lead [Molecules/volume] in Red Blood Cells')
        db.result_type.insert(key='5671-3',description=' Lead Bld-mCnc Lead [Mass/volume] in Blood')
        db.result_type.insert(key='5674-7',description=' Lead RBC-mCnc Lead [Mass/volume] in Red Blood Cells')
        db.result_type.insert(key='24331-1',description=' Lipid HCFA 1996 Pnl SerPl Lipid HCFA 1996 panel in Serum or Plasma')
        db.result_type.insert(key='35457-1',description=' Maternal Cell Contam Amn Maternal cell contamination [Identifier] in Amniotic Fluid Nominal_d')
        db.result_type.insert(key='34535-5 ',description='Microalbumin/Creat ratio pnl Ur Microalbumin/Creatinine ratio panel in Urine')
        db.result_type.insert(key='10524-7',description=' Cyto Cervix Microscopic observation [Identifier] in Cervix by Cyto stain')
        db.result_type.insert(key='18500-9',description=' Thin Prep Cervix Microscopic observation [Identifier] in Cervix by Cyto stain.thin prep')
        db.result_type.insert(key='19765-7',description=' Cyto Cvx/Vag Microscopic observation [Identifier] in Cervical or vaginal smear or scraping by Cyto stain')
        db.result_type.insert(key='19766-5',description=' Cyto Cvx/Vag Microscopic observation [Identifier] in Cervical or vaginal smear or scraping by Cyto stain')
        db.result_type.insert(key='660-1',description=' Dark Field XXX Microscopic observation [Identifier] in Unspecified specimen by Dark field examination')
        db.result_type.insert(key='688-2 ',description='N gonorrhoea Cervix Ql Cult Neisseria gonorrhoeae [Presence] in Cervix by Organism specific culture')
        db.result_type.insert(key='690-8 ',description='N gonorrhoea Endometrium Ql Cult Neisseria gonorrhoeae [Presence] in Endometrium by Organism specific culture')
        db.result_type.insert(key='691-6 ',description='N gonorrhoea Genital Ql Cult Neisseria gonorrhoeae [Presence] in Genital specimen by Organism specific culture')
        db.result_type.insert(key='692-4 ',description='N gonorrhoea Gen lochia Ql Cult Neisseria gonorrhoeae [Presence] in Genital lochia by Organism specific culture')
        db.result_type.insert(key='693-2 ',description='N gonorrhoea Vag Ql Cult Neisseria gonorrhoeae [Presence] in Vaginal fluid by Organism specific culture')
        db.result_type.insert(key='698-1 ',description='N gonorrhoea XXX Ql Cult Neisseria gonorrhoeae [Presence] in Unspecified specimen by Organism specific culture')
        db.result_type.insert(key='29311-8 ',description='N gonorrhoea Ag XXX Ql IF Neisseria gonorrhoeae Ag [Presence] in Unspecified specimen by Immunofluorescence')
        db.result_type.insert(key='31905-3 ',description='N gonorrhoea Ag Genital Ql Neisseria gonorrhoeae Ag [Presence] in Genital specimen')
        db.result_type.insert(key='31906-1 ',description='N gonorrhoea Ag XXX Ql Neisseria gonorrhoeae Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='6487-3 ',description='N gonorrhoea Ag Genital Ql EIA Neisseria gonorrhoeae Ag [Presence] in Genital specimen) by Immunoassay')
        db.result_type.insert(key='6488-1 ',description='N gonorrhoea Ag Genital Ql IF Neisseria gonorrhoeae Ag [Presence] in Genital specimen) by Immunofluorescence')
        db.result_type.insert(key='6489-9 ',description='N gonorrhoea Ag Genital Ql LA Neisseria gonorrhoeae Ag [Presence] in Genital specimen by Latex agglutination')
        db.result_type.insert(key='21414-8 ',description='N gonorrhoea DNA Cerv mucus Ql PCR Neisseria gonorrhoeae DNA [Presence] in Cervical mucus by Probe & target amplification method')
        db.result_type.insert(key='21415-5 ',description='N gonorrhoea DNA Urth Ql PCR Neisseria gonorrhoeae DNA [Presence] in Urethra by Probe & target amplification method')
        db.result_type.insert(key='21416-3 ',description='N gonorrhoea DNA Ur Ql PCR Neisseria gonorrhoeae DNA [Presence] in Urine by Probe & target amplification method')
        db.result_type.insert(key='24111-7 ',description='N gonorrhoea DNA XXX Ql PCR Neisseria gonorrhoeae DNA [Presence] in Unspecified specimen) by Probe & target amplification method')
        db.result_type.insert(key='32705-6 ',description='N gonorrhoea DNA Vag Ql PCR Neisseria gonorrhoeae DNA [Presence] in Vaginal fluid by Probe & target amplification method')
        db.result_type.insert(key='32198-4 ',description='N gonorrhoea rRNA Cervix Ql Prb Neisseria gonorrhoeae rRNA [Presence] in Cervix by DNA probe')
        db.result_type.insert(key='32199-2 ',description='N gonorrhoea rRNA Urth Ql Prb Neisseria gonorrhoeae rRNA [Presence] in Urethra by DNA probe')
        db.result_type.insert(key='5028-6 ',description='N gonorrhoea rRNA XXX Ql Prb Neisseria gonorrhoeae rRNA [Presence] in Unspecified specimen) by DNA probe')
        db.result_type.insert(key='24364-2',description=' Obstetric HCFA 1996 Pnl Ser+Bld Obstetric HCFA 1996 panel in Serum & Blood')
        db.result_type.insert(key='14874-2 ',description='Phenobarb SerPl-sCnc Phenobarbital [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='3948-7 ',description='Phenobarb SerPl-mCnc Phenobarbital [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='3951-1 ',description='Phenobarb Free SerPl-mCnc Phenobarbital Free [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='14877-5 ',description='Phenytoin SerPl-sCnc Phenytoin [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='3968-5 ',description='Phenytoin SerPl-mCnc Phenytoin [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='34540-5 ',description='Phenytoin Free+Total Pnl SerPlmCncPhenytoin free & total panel [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='32109-1 ',description='Phenytoin Free SerPl-sCnc Phenytoin Free [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='3969-3 ',description='Phenytoin Free SerPl-mCnc Phenytoin Free [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='22760-3 ',description='Potassium SerPl-mCnc Potassium [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='2823-3 ',description='Potassium SerPl-sCnc Potassium [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='2824-1 ',description='Potassium RBC-sCnc Potassium [Molecules/volume] in Red Blood Cells')
        db.result_type.insert(key='32713-0 ',description='Potassium BldA-sCnc Potassium [Molecules/volume] in Arterial blood')
        db.result_type.insert(key='6298-4 ',description='Potassium Bld-sCnc Potassium [Molecules/volume] in Blood')
        db.result_type.insert(key='12812-4 ',description='Potassium sp2 SerPl-sCnc Potassium [Molecules/volume] in Serum or Plasma --2nd specimen')
        db.result_type.insert(key='12813-2 ',description='Potassium sp3 SerPl-sCnc Potassium [Molecules/volume] in Serum or Plasma --3rd specimen')
        db.result_type.insert(key='29349-8 ',description='Potassium p dialysis SerPl-sCnc Potassium [Molecules/volume] in Serum or Plasma --post dialysis')
        db.result_type.insert(key='34493-7',description=' PRF1 gene Mut Anal Amn PRF1 gene mutations found [Identifier] in Amniotic Fluid by Molecular geneticsmethod Narrative')
        db.result_type.insert(key='10547-8',description=' Primidone+Phenobarb SerPl-mCnc Primidone+Phenobarbital [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='34365-7',description=' Primidone+Phenobarb SerPl-sCnc Primidone+Phenobarbital [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='12842-1 ',description='Prot 12H Ur-mCnc Protein [Mass/volume] in 12 hour Urine')
        db.result_type.insert(key='18373-1 ',description='Prot 6H Ur-mRate Protein [Mass/time] in 6 hour Urine')
        db.result_type.insert(key='20454-5 ',description='Prot Ur Ql Strip Protein [Presence] in Urine by Test strip')
        db.result_type.insert(key='21482-5 ',description='Prot 24H Ur-mCnc Protein [Mass/volume] in 24 hour Urine')
        db.result_type.insert(key='26801-1 ',description='Prot 12H Ur-mRate Protein [Mass/time] in 12 hour Urine')
        db.result_type.insert(key='27298-9 ',description='Prot Ur-aCnc Protein [Units/volume] in Urine')
        db.result_type.insert(key='2887-8 ',description='Prot Ur Ql Protein [Presence] in Urine')
        db.result_type.insert(key='2888-6 ',description='Prot Ur-mCnc Protein [Mass/volume] in Urine')
        db.result_type.insert(key='2889-4 ',description='Prot 24H Ur-mRate Protein [Mass/time] in 24 hour Urine')
        db.result_type.insert(key='32209-9 ',description='Prot 24H Ur Ql Strip Protein [Presence] in 24 hour Urine by Test strip')
        db.result_type.insert(key='32551-4 ',description='Prot ?Tm Ur Qn Protein [Mass] in unspecified time Urine')
        db.result_type.insert(key='35663-4 ',description='Prot ?Tm Ur-mCnc Protein [Mass/volume] in unspecified time Urine')
        db.result_type.insert(key='5804-0 ',description='Prot Ur Strip-mCnc Protein [Mass/volume] in Urine by Test strip')
        db.result_type.insert(key='13801-6 ',description='Prot/creat H Ur-mRto Protein/Creatinine [Mass ratio] in 24 hour Urine')
        db.result_type.insert(key='2890-2 ',description='Prot/creat Ur-mRto Protein/Creatinine [Mass ratio] in Urine')
        db.result_type.insert(key='34366-5 ',description='Prot/creat Ur-Rto Protein/Creatinine [Ratio] in Urine')
        db.result_type.insert(key='40486-3 ',description='Prot/creat H Ur-Rto Protein/Creatinine [Ratio] in 24 hour Urine')
        db.result_type.insert(key='40662-9 ',description='Prot Resting 12H Ur-mRate Protein [Mass/time] in 12 hour Urine –resting')
        db.result_type.insert(key='40663-7 ',description='Prot upr 12H Ur-mRate Protein [Mass/time] in 12 hour Urine –upright')
        db.result_type.insert(key='11084-1',description=' Reagin Ab Titr Ser Reagin Ab [Titer] in Serum')
        db.result_type.insert(key='20507-0',description=' RPR Ser Ql-aCnc Reagin Ab [Presence] in Serum by RPR')
        db.result_type.insert(key='20508-8',description=' RPR Ser Qn-aCnc Reagin Ab [Units/volume] in Serum by RPR')
        db.result_type.insert(key='22461-8',description=' Reagin Ab Ser Ql Reagin Ab [Presence] in Serum')
        db.result_type.insert(key='22462-6',description=' Reagin Ab Ser-aCnc Reagin Ab [Units/volume] in Serum')
        db.result_type.insert(key='31147-2',description=' RPR Ser-Titr Reagin Ab [Titer] in Serum by RPR')
        db.result_type.insert(key='5291-0',description=' VDRL Ser Qn-aCnc Reagin Ab [Units/volume] in Serum by VDRL')
        db.result_type.insert(key='5292-8',description=' VDRL Ser Ql-aCnc Reagin Ab [Presence] in Serum by VDRL')
        db.result_type.insert(key='24362-6',description=' Renal Func HCFA 2000 Pnl SerPl Renal function HCFA 2000 panel in Serum or Plasma')
        db.result_type.insert(key='10331-7',description=' Rh Bld Rh [Type] in Blood')
        db.result_type.insert(key='34961-',description='Rh Bld Cfm Rh [Type] in Blood by Confirm method')
        db.result_type.insert(key='42316-0',description='RHD gene Mut Anal Amn RHD gene mutations found [Type] in Amniotic Fluid by Molecular genetics method')
        db.result_type.insert(key='17550-5',description=' RUBV Ab Ser LA-aCnc Rubella virus Ab [Units/volume] in Serum by Latex agglutination')
        db.result_type.insert(key='22496-4 ',description='RUBV Ab Ser Ql Rubella virus Ab [Presence] in Serum')
        db.result_type.insert(key='22497-2 ',description='RUBV Ab Titr Ser Rubella virus Ab [Titer] in Serum')
        db.result_type.insert(key='5330-6 ',description='RUBV Ab Ser HAI-aCnc Rubella virus Ab [Units/volume] in Serum by Hemaglutination inhibition')
        db.result_type.insert(key='5331-4 ',description='RUBV Ab Ser Ql HAI Rubella virus Ab [Presence] in Serum by Hemaglutination inhibition')
        db.result_type.insert(key='5332-2 ',description='RUBV Ab Ser Ql LA Rubella virus Ab [Presence] in Serum by Latex agglutination')
        db.result_type.insert(key='5333-0 ',description='RUBV Ab Titr Ser LA Rubella virus Ab [Titer] in Serum by Latex agglutination')
        db.result_type.insert(key='8013-5 ',description='RUBV Ab Ser-aCnc Rubella virus Ab [Units/volume] in Serum')
        db.result_type.insert(key='25514-1 ',description='RUBV IgG Ser Ql Rubella virus IgG Ab [Presence] in Serum')
        db.result_type.insert(key='41763-4 ',description='RUBV IgG Titr Ser Rubella virus IgG Ab [Titer] in Serum')
        db.result_type.insert(key='5334-8 ',description='RUBV IgG Ser EIA-aCnc Rubella virus IgG Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='8014-3 ',description='RUBV IgG Ser-aCnc Rubella virus IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='34952-2',description=' RUBV IgG+IgM Pnl Ser Rubella virus IgG & IgM panel in Serum')
        db.result_type.insert(key='34421-8',description=' RUBV IgG Avidity Ser-aCnc Rubella virus IgG Ab avidity [Units/volume] in Serum')
        db.result_type.insert(key='13279-5 ',description='RUBV IgG sp1 Ser-aCnc Rubella virus IgG Ab [Units/volume] in Serum --1st specimen')
        db.result_type.insert(key='25298-1 ',description='RUBV IgG 1:2 Ser-Rto Rubella virus IgG Ab [Ratio] in Serum --1st specimen/2nd specimen')
        db.result_type.insert(key='13280-3 ',description='RUBV IgG sp2 Ser-aCnc Rubella virus IgG Ab [Units/volume] in Serum --2nd specimen')
        db.result_type.insert(key='24116-6 ',description='RUBV IgM Ser Ql EIA Rubella virus IgM Ab [Presence] in Serum by Immunoassay')
        db.result_type.insert(key='25420-1',description=' RUBV IgM Ser Ql LA Rubella virus IgM Ab [Presence] in Serum by Latex agglutination')
        db.result_type.insert(key='31616-6 ',description='RUBV IgM Ser Ql Rubella virus IgM Ab [Presence] in Serum')
        db.result_type.insert(key='5335-5 ',description='RUBV IgM Ser EIA-aCnc Rubella virus IgM Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='8015-0 ',description='RUBV IgM Ser-aCnc Rubella virus IgM Ab [Units/volume] in Serum')
        db.result_type.insert(key='34548-8',description=' Sodium + Potassium Pnl SerPl-sCnc Sodium & Potassium panel [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='19764-0',description=' Stat of Adq Cvx/Vag Cyto-Imp Statement of adequacy [interpretation] in Cervical or vaginal smear or scraping by Cyto stain')
        db.result_type.insert(key='11268-0',description=' S pyog Throat Ql Cult Streptococcus pyogenes [Presence] in Throat by Organism specific culture')
        db.result_type.insert(key='18481-2',description=' S pyog Ag Throat Ql Streptococcus pyogenes Ag [Presence] in Throat')
        db.result_type.insert(key='31971-5',description=' S pyog Ag XXX Ql Streptococcus pyogenes Ag [Presence] in Unspecified specimen')
        db.result_type.insert(key='6556-5',description=' S pyog Ag Throat Ql EIA Streptococcus pyogenes Ag [Presence] in Throat by Immunoassay')
        db.result_type.insert(key='6557-3',description=' S pyog Ag Throat Ql IF Streptococcus pyogenes Ag [Presence] in Throat by Immunofluorescence')
        db.result_type.insert(key='6558-1',description=' S pyog Ag XXX Ql EIA Streptococcus pyogenes Ag [Presence] in Unspecified specimen byImmunoassay')
        db.result_type.insert(key='6559-9',description=' S pyog Ag XXX Ql IF Streptococcus pyogenes Ag [Presence] in Unspecified specimen by Immunofluorescence')
        db.result_type.insert(key='17656-0',description=' S pyog XXX Cult Streptococcus pyogenes identified in Unspecified specimen by Organism specific culture')
        db.result_type.insert(key='5036-9',description=' S pyog rRNA XXX Ql Prb Streptococcus pyogenes rRNA [Presence] in Unspecified specimen by DNA probe')
        db.result_type.insert(key='24314-7',description=' TORCH HCFA 1996 Pnl Ser TORCH HCFA 1996 panel in Serum')
        db.result_type.insert(key='11598-0 ',description='T gondii Ab Ser-aCnc Toxoplasma gondii Ab [Units/volume] in Serum')
        db.result_type.insert(key='22577-1 ',description='T gondii Ab Ser Ql Toxoplasma gondii Ab [Presence] in Serum')
        db.result_type.insert(key='23485-6 ',description='T gondii Ab Ser Ql Aggl Toxoplasma gondii Ab [Presence] in Serum by Agglutination')
        db.result_type.insert(key='23486-4 ',description='T gondii Ab Ser Ql LA Toxoplasma gondii Ab [Presence] in Serum by Latex agglutination')
        db.result_type.insert(key='23784-2 ',description='T gondii Ab Titr Ser HA Toxoplasma gondii Ab [Titer] in Serum by Hemagglutination')
        db.result_type.insert(key='42949-8 ',description='T gondii Ab Titr Ser Toxoplasma gondii Ab [Titer] in Serum')
        db.result_type.insert(key='5387-6 ',description='T gondii Ab Ser Ql Dye Test Toxoplasma gondii Ab [Presence] in Serum by Sabin dye test')
        db.result_type.insert(key='12261-4 ',description='T gondii IgG Titr Ser EIA Toxoplasma gondii IgG Ab [Titer] in Serum by Immunoassay')
        db.result_type.insert(key='21570-7 ',description='T gondii IgG Ser Ql Dye Test Toxoplasma gondii IgG Ab [Presence] in Serum by Sabin dye test')
        db.result_type.insert(key='22580-5 ',description='T gondii IgG Ser Ql Toxoplasma gondii IgG Ab [Presence] in Serum')
        db.result_type.insert(key='22582-1 ',description='T gondii IgG Titr Ser Toxoplasma gondii IgG Ab [Titer] in Serum')
        db.result_type.insert(key='35281-5 ',description='T gondii IgG Ser Ql IF Toxoplasma gondii IgG Ab [Presence] in Serum by Immunofluorescence')
        db.result_type.insert(key='40677-7 ',description='T gondii IgG Ser Ql EIA Toxoplasma gondii IgG Ab [Presence] in Serum by Immunoassay')
        db.result_type.insert(key='5388-4 ',description='T gondii IgG Ser EIA-aCnc Toxoplasma gondii IgG Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='5389-2 ',description='T gondii IgG Titr Ser IF Toxoplasma gondii IgG Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='8039-0 ',description='T gondii IgG Ser-aCnc Toxoplasma gondii IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='34422-6 ',description='T gondii IgG Avidity Ser-aCnc Toxoplasma gondii IgG Ab avidity [Units/volume] in Serum')
        db.result_type.insert(key='24242-0 ',description='T gondii IgG sp1 Ser-aCnc Toxoplasma gondii IgG Ab [Units/volume] in Serum --1st specimen')
        db.result_type.insert(key='25300-5 ',description='T gondii IgG 1:2 Ser-Rto Toxoplasma gondii IgG Ab [Ratio] in Serum --1st specimen/2nd specimen')
        db.result_type.insert(key='13286-0',description=' T gondii IgG sp2 Ser-aCnc Toxoplasma gondii IgG Ab [Units/volume] in Serum --2nd specimen')
        db.result_type.insert(key='40786-6',description=' T gondii IgG sp2 Titr Ser Toxoplasma gondii IgG Ab [Titer] in Serum --2nd specimen')
        db.result_type.insert(key='17717-0 ',description='T gondii IgG+IgM Ser Ql Toxoplasma gondii IgG+IgM Ab [Presence] in Serum')
        db.result_type.insert(key='12262-2 ',description='T gondii IgM Titr Ser EIA Toxoplasma gondii IgM Ab [Titer] in Serum by Immunoassay')
        db.result_type.insert(key='22584-7 ',description='T gondii IgM Titr Ser Toxoplasma gondii IgM Ab [Titer] in Serum')
        db.result_type.insert(key='25542-2 ',description='T gondii IgM Ser Ql Toxoplasma gondii IgM Ab [Presence] in Serum')
        db.result_type.insert(key='33336-9 ',description='T gondii IgM Ser Ql Aggl Toxoplasma gondii IgM Ab [Presence] in Serum by Agglutination')
        db.result_type.insert(key='35282-3 ',description='T gondii IgM Ser Ql IF Toxoplasma gondii IgM Ab [Presence] in Serum by Immunofluorescence')
        db.result_type.insert(key='40678-5 ',description='T gondii IgM Ser Ql EIA Toxoplasma gondii IgM Ab [Presence] in Serum by Immunoassay')
        db.result_type.insert(key='5390-0 ',description='T gondii IgM Ser EIA-aCnc Toxoplasma gondii IgM Ab [Units/volume] in Serum by Immunoassay')
        db.result_type.insert(key='5391-8 ',description='T gondii IgM Titr Ser IF Toxoplasma gondii IgM Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='8040-8 ',description='T gondii IgM Ser-aCnc Toxoplasma gondii IgM Ab [Units/volume] in Serum')
        db.result_type.insert(key='40785-8 ',description='T gondii IgM sp1 Titr Ser Toxoplasma gondii IgM Ab [Titer] in Serum --1st specimen')
        db.result_type.insert(key='11597-2 ',description='T pallidum Ab Ser-aCnc Treponema pallidum Ab [Units/volume] in Serum')
        db.result_type.insert(key='17723-8 ',description='T pallidum Ab Ser Ql Immob Treponema pallidum Ab [Presence] in Serum by Immobilization')
        db.result_type.insert(key='17724-6 ',description='T pallidum Ab Ser IF-aCnc Treponema pallidum Ab [Units/volume] in Serum by Immunofluorescence')
        db.result_type.insert(key='17725-3 ',description='T pallidum Ab Ser LA-aCnc Treponema pallidum Ab [Units/volume] in Serum by Latex agglutination')
        db.result_type.insert(key='22587-0 ',description='T pallidum Ab Ser Ql Treponema pallidum Ab [Presence] in Serum')
        db.result_type.insert(key='22590-4 ',description='T pallidum Ab Titr Ser Treponema pallidum Ab [Titer] in Serum')
        db.result_type.insert(key='24110-9 ',description='T pallidum Ab Ser Ql EIA Treponema pallidum Ab [Presence] in Serum by Immunoassay')
        db.result_type.insert(key='24312-1 ',description='T pallidum Ab Ser Ql Aggl Treponema pallidum Ab [Presence] in Serum by Agglutination')
        db.result_type.insert(key='26009-1 ',description='T pallidum Ab Titr Ser HA Treponema pallidum Ab [Titer] in Serum by Hemagglutination')
        db.result_type.insert(key='34382-2 ',description='T pallidum Ab Titr Ser IF Treponema pallidum Ab [Titer] in Serum by Immunofluorescence')
        db.result_type.insert(key='5392-6 ',description='T pallidum Ab Ser Immob-aCnc Treponema pallidum Ab [Units/volume] in Serum by Immobilization')
        db.result_type.insert(key='5393-4 ',description='T pallidum Ab Ser Ql IF Treponema pallidum Ab [Presence] in Serum by Immunofluorescence')
        db.result_type.insert(key='5394-2 ',description='T pallidum Ab Titr Ser LA Treponema pallidum Ab [Titer] in Serum by Latex agglutination')
        db.result_type.insert(key='8041-6 ',description='T pallidum Ab Ser Ql HA Treponema pallidum Ab [Presence] in Serum by Hemagglutination')
        db.result_type.insert(key='17726-1 ',description='T pallidum IgG Ser Ql IF Treponema pallidum IgG Ab [Presence] in Serum by Immunofluorescence')
        db.result_type.insert(key='17727-9 ',description='T pallidum IgG Ser IF-aCnc Treponema pallidum IgG Ab [Units/volume] in Serum by Immunofluorescence')
        db.result_type.insert(key='22592-0 ',description='T pallidum IgG Ser-aCnc Treponema pallidum IgG Ab [Units/volume] in Serum')
        db.result_type.insert(key='6561-5 ',description='T pallidum IgG Ser Ql Treponema pallidum IgG Ab [Presence] in Serum')
        db.result_type.insert(key='17728-7 ',description='T pallidum IgM Ser IF-aCnc Treponema pallidum IgM Ab [Units/volume] in Serum by Immunofluorescence')
        db.result_type.insert(key='17729-5 ',description='T pallidum IgM Ser Ql IF Treponema pallidum IgM Ab [Presence] in Serum by Immunofluorescence')
        db.result_type.insert(key='22594-6 ',description='T pallidum IgM Ser-aCnc Treponema pallidum IgM Ab [Units/volume] in Serum')
        db.result_type.insert(key='6562-3 ',description='T pallidum IgM Ser Ql Treponema pallidum IgM Ab [Presence] in Serum')
        db.result_type.insert(key='24357-6',description=' UA Dipstick Pnl Ur UA dipstick panel in Urine')
        db.result_type.insert(key='14937-7 ',description='BUN SerPl-sCnc Urea nitrogen [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='3094-0 ',description='BUN SerPl-mCnc Urea nitrogen [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='6299-2 ',description='BUN Bld-mCnc Urea nitrogen [Mass/volume] in Blood')
        db.result_type.insert(key='12966-8 ',description='BUN 2H spec SerPl-mCnc Urea nitrogen [Mass/volume] in Serum or Plasma --2 hour specimen')
        db.result_type.insert(key='12965-0 ',description='BUN 70M spec SerPl-mCnc Urea nitrogen [Mass/volume] in Serum or Plasma --70 minute specimen')
        db.result_type.insert(key='12964-3 ',description='BUN BS Bld-mCnc Urea nitrogen [Mass/volume] in Blood –baseline')
        db.result_type.insert(key='11064-3 ',description='BUN p dialysis SerPl-mCnc Urea nitrogen [Mass/volume] in Serum or Plasma --post dialysis')
        db.result_type.insert(key='11065-0 ',description='BUN pre dial SerPl-mCnc Urea nitrogen [Mass/volume] in Serum or Plasma --pre dialysis')
        db.result_type.insert(key='24356-8',description=' Urinalysis Pnl Ur Urinalysis panel in Urine')
        db.result_type.insert(key='14946-8 ',description='Valproate SerPl-sCnc Valproate [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='086-5 ',description='Valproate SerPl-mCnc Valproate [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='21590-5 ',description='Valproate Bnd Fr SerPl Valproate.bound/Valproate.total in Serum or Plasma')
        db.result_type.insert(key='32119-0 ',description='Valproate Free SerPl-sCnc Valproate Free [Molecules/volume] in Serum or Plasma')
        db.result_type.insert(key='4087-3 ',description='Valproate Free SerPl-mCnc Valproate Free [Mass/volume] in Serum or Plasma')
        db.result_type.insert(key='32283-4 ',description='Valproate Free Fr SerPl Valproate Free/Valproate.total in Serum or Plasma')

db.define_table('dispense_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.dispense_type.id>0).count():
    db.dispense_type.insert(key='B',description='Trial Quantity Balance')
    db.dispense_type.insert(key='C',description='Compassionate Fill')
    db.dispense_type.insert(key='N',description='New/Renew - Full Fill')
    db.dispense_type.insert(key='P',description='New/Renew - Part Fill')
    db.dispense_type.insert(key='Q',description='Refill - Part Fill')
    db.dispense_type.insert(key='R',description='Refill - Full Fill')
    db.dispense_type.insert(key='S',description='Manufacturer Sample')
    db.dispense_type.insert(key='T',description='Trial Quantity')
    db.dispense_type.insert(key='Z',description='Non-Prescription Fill')

db.define_table('abnormal_flag',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.abnormal_flag.id>0).count():
    db.abnormal_flag.insert(key='<',description='Below absolute low-off instrument scale')
    db.abnormal_flag.insert(key='>',description='Above absolute high-off instrument scale')
    db.abnormal_flag.insert(key='A',description='Abnormal (applies to non-numeric results)')
    db.abnormal_flag.insert(key='AA',description='Very abnormal (applies to non-numeric units,analogous to panic limits for numeric units)')
    db.abnormal_flag.insert(key='B',description='Better--use when direction not relevant')
    db.abnormal_flag.insert(key='D',description='Significant change down')
    db.abnormal_flag.insert(key='H',description='Above high normal')
    db.abnormal_flag.insert(key='HH',description='Above upper panic limits')
    db.abnormal_flag.insert(key='I',description='Intermediate. Indicates for microbiology susceptibilities only.')
    db.abnormal_flag.insert(key='L',description='Below low normal')
    db.abnormal_flag.insert(key='LL',description='Below lower panic limits')
    db.abnormal_flag.insert(key='MS',description='Moderately susceptible. Indicates for microbiology susceptibilities only.')
    db.abnormal_flag.insert(key='N',description='Normal (applies to non-numeric results)')
    db.abnormal_flag.insert(key='null',description="No range defined, or normal ranges don't apply")
    db.abnormal_flag.insert(key='R',description='Resistant. Indicates for microbiology susceptibilities only.')
    db.abnormal_flag.insert(key='S',description='Susceptible. Indicates for microbiology susceptibilities only.')
    db.abnormal_flag.insert(key='U',description='Significant change up')
    db.abnormal_flag.insert(key='VS',description='Very susceptible. Indicates for microbiology susceptibilities only.')
    db.abnormal_flag.insert(key='W',description='Worse--use when direction not relevant')
    
db.define_table('specimen_rejection_reason',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.specimen_rejection_reason.id>0).count():
    db.specimen_rejection_reason.insert(key='EX',description='Expired')
    db.specimen_rejection_reason.insert(key='QS',description='Quantity not sufficient')
    db.specimen_rejection_reason.insert(key='RA',description='Missing patient ID number')
    db.specimen_rejection_reason.insert(key='RB',description='Broken container')
    db.specimen_rejection_reason.insert(key='RC',description='Clotting')
    db.specimen_rejection_reason.insert(key='RD',description='Missing collection date')
    db.specimen_rejection_reason.insert(key='RE',description='Missing patient name')
    db.specimen_rejection_reason.insert(key='RH',description='Hemolysis')
    db.specimen_rejection_reason.insert(key='RI',description='Identification problem')
    db.specimen_rejection_reason.insert(key='RM',description='Labeling')
    db.specimen_rejection_reason.insert(key='RN',description='Contamination')
    db.specimen_rejection_reason.insert(key='RP',description='Missing phlebotomist ID')
    db.specimen_rejection_reason.insert(key='RR',description='Improper storage')
    db.specimen_rejection_reason.insert(key='RS',description='Name misspelling')
db.define_table('accept_acknowledgment_type',
    Field('key',notnull=True,unique=True),
    Field('description'),
    format='%(description)s',migrate=migrate)

if not db(db.accept_acknowledgment_type.id>0).count():
    db.accept_acknowledgment_type.insert(key='AL',description='Always')
    db.accept_acknowledgment_type.insert(key='ER',description='Error/reject conditions only')
    db.accept_acknowledgment_type.insert(key='NE',description='Never')
    db.accept_acknowledgment_type.insert(key='SU',description='Successful completion only')


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
            print e

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


