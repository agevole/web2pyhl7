# -*- coding: utf-8 -*- 
#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################
response.title = T('Web2py HL7')
response.subtitle = T('Empowering Patients and Provider with Open Source')

#########################################################################
## custom menu
#########################################################################

response.menu = [    
    ['Patients',False,
     URL(r=request,f='select',args='patient')],
    ['Calendar', False, URL(r=request,f='calendar')],
    ['Data', False, URL(r=request,f='data_tables')],
    ['Auxiliary', False, URL(r=request,f='auxiliary_tables')],
    ['Users', False, URL(r=request,f='sysusers')]
    ]

if session.patient_id:
    response.menu.insert(0,['Last Patient',False,
                            URL(r=request,f='read',
                                args=('patient',session.patient_id))])

"""
response.menu=[
    ['Search Patients',False,URL(r=request,f='select/patient')],
    ['Make Appointment',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in APPOINTMENTS]],
    ['Patient Appointments',False,URL(r=request,f='calendar')],
    ['Patient Encounters',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in ENCOUNTERS]],
    
    ['Patient Information',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in PATIENT]],
    ['Insurance Data',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in INSURANCE_DATA]],
    
    ['Patient Immunization Data',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in IMMUNIZATION_DATA]],
    
    ['Patient Lab Data',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in LABORATORY_DATA]],
    ['Patient Prescription Data',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in PRESCRIPTION_DATA]],
    ['Patient Genetics Data',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in GENETICS_DATA]],
    
    
    ['Make Lab Orders',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in LAB_ORDERS]],
    ['Send Lab Orders to Labs',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in SEND_LAB_ORDERS]],
    ['Patient Lab Results  Data',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in LAB_RESULTS]], 
    
    ['Make Prescription Orders',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in DRUG_ORDERS]],
    ['Send Prescription to Pharmacy',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in SEND_PRESCRIPTION_ORDERS]],
    
    ['Make Immunization Query and Get a Response',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in IMMUNIZATION_REQUEST]] , 
    
    ['Make Lab Results',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in LAB_RESULTS]],
    ['Send Lab Results to Distribution List',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in SEND_LAB_RESULTS]],
    
    
   
    ['List of Patient Healthcare Providers',False,'#nil',[(title(t),False,URL(r=request,f='auxiliary',args=t)) for  t in PROVIDER_DATA]],
]
if session.patient_id:
    response.menu.append(('Current Patient',False,URL(r=request,f='read',args=['patient',session.patient_id])))
"""
