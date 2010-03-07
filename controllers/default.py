# coding: utf8

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################  


def index():
    session.patient = session.patient_id = None
    return dict()

def about():
    session.patient = session.patient_id = None
    return dict()

def sysusers():
    session.patient = session.patient_id = None
    return dict(users = db(db.auth_user.id>0).select(orderby=db.auth_user.first_name|db.auth_user.last_name))

def sysuser():
    session.patient = session.patient_id = None
    user = db(db.auth_user.id==request.args(0)).select().first() or error()
    return dict(user=user)

@auth.requires_login()
def map():
    googlemap_key='ABQIAAAAnfs7bKE82qgb3Zc2YyS-oBT2yXp_ZAY8_ufC3CFXhHIE1NvwkxSySz_REpPq-4WZA27OwgbtyR3VcA'
    if request.args(0):
        dbset=db(db.patient.active==True)(db.patient.id==request.args(0))
    else:
        dbset=db(db.patient.active==True)
    rows=dbset.select(db.patient.id,db.patient.first_name,db.patient.last_name,db.patient.latitude,db.patient.longitude)
    return dict(rows=rows,googlemap_key=googlemap_key)

@auth.requires_login()
def patient_logs():    
    if not session.patient_id:
        session.flash = 'please select a patient first'
        redirect(URL(r=request,f='select',args='patient'))
    return dict(logs=db(db.patient_log.patient==session.patient_id).select(orderby=~db.patient_log.created_on))    

@auth.requires_login()
def calendar():
    import datetime
    appointments=db(db.appointment.active==True)(
        db.appointment.start_time>request.now-datetime.timedelta(days=1))\
        .select(db.appointment.patient,db.appointment.start_time,db.appointment.stop_time)
    return dict(appointments=appointments)

@auth.requires(enforce_authorization(request.args(0),'write'))
def auxiliary_tables():
    return dict()

@auth.requires_login()
def data_tables():
    return dict()

@auth.requires_login()
def auxiliary():
    tablename=request.args(0)
    if not tablename in AUXILIARY_TABLES: error()
    table=db[tablename]
    form=crud.update(table,request.args(1),onaccept=crud.archive)
    rows = db(table.id).select()        
    table.id.represent = \
        lambda id: SPAN(id,' ',A('edit',_href=URL(r=request,args=[table,id])))
    return dict(rows=rows,form=form)

@auth.requires(enforce_authorization(request.args(0),'read'))
def select():
    tablename=request.args(0)
    if not tablename in DATA_TABLES: error()
    table=db[tablename]    
    table.id.represent=lambda id: \
        SPAN(id,' ',A('open',_href=URL(r=request,f='read',args=[table,id])))
    create_button = A('New %s' % capitalize(tablename),_href=URL(r=request,f='edit',args=table))
    return dict(table=table,create_button=create_button)

@auth.requires(enforce_authorization(request.args(0),'read'))
def read():
    tablename=request.args(0)
    if not tablename in DATA_TABLES+['patient']: error()
    table=db[tablename]
    form=crud.read(table,request.args(1))
    if not form.record: error()
    if tablename=='patient':
        session.patient = form.record.as_dict()
        session.patient_id = form.record_id
    edit_button = A('edit',_href=URL(r=request,f='edit',args=[table,form.record.id]))
    references=[]
    for (tablename,fieldname) in sorted(table._referenced_by):
        references.append(A(pluralize(capitalize(tablename)),
                            _href=URL(r=request,f='select',
                                      args=(tablename,fieldname,
                                            request.args(1)))))
    return dict(form=form,edit_button=edit_button,references=references)

@auth.requires(enforce_authorization(request.args(0),'write'))
def edit():
    tablename=request.args(0)
    if not tablename in DATA_TABLES+['patient']: error()
    if not tablename=='patient' and not session.patient_id:
        redirect(URL(r=request,f='select',args='patient'))
    table=db[tablename]
    def log_it(form):
        if not request.args(1) and table._format:
            db.patient_log.insert(tablename=tablename,
                                  record_id=form.vars.id,
                                  message=table._format % form.vars) 
    form=crud.update(table,request.args(1),
                     onaccept=lambda form: (crud.archive(form),log_it(form)),
                     next='read/%s/[id]'%tablename)
    return dict(form=form)
       
def error():
    return dict()

@auth.requires(enforce_authorization(request.args(0),'read'))
def data():
    "http://trirand.com/blog/jqgrid/server.php?q=1&_search=false&nd=1267835445772&rows=10&page=1&sidx=amount&sord=asc&searchField=&searchString=&searchOper="
    tablename = request.args(0) or error()
    condition = request.args(1)
    id = request.args(2)
    rows=int(request.vars.rows or 25)
    page=int(request.vars.page or 0)
    sidx=request.vars.sidx or 'id'
    sord=request.vars.sord or 'asc'
    searchField=request.vars.searchField
    searchString=request.vars.searchString
    searchOper={'eq':lambda a,b: a==b,
                'nq':lambda a,b: a!=b,
                'gt':lambda a,b: a>b,
                'ge':lambda a,b: a>=b,
                'lt':lambda a,b: a<b,
                'le':lambda a,b: a<=b,
                'bw':lambda a,b: a.like(b+'%'),
                'bn':lambda a,b: ~a.like(b+'%'),
                'ew':lambda a,b: a.like('%'+b),
                'en':lambda a,b: ~a.like('%'+b),
                'cn':lambda a,b: a.like('%'+b+'%'),
                'nc':lambda a,b: ~a.like('%'+b+'%'),
                'in':lambda a,b: a.belongs(b.split()),
                'ni':lambda a,b: ~a.belongs(b.split())}[request.vars.searchOper or 'eq']
    table=db[tablename]
    dbset=db(table.active==True)
    if condition: dbset=dbset(table[condition]==id)
    if searchField: dbset=dbset(searchOper(table[searchField],searchString))
    orderby = table[sidx]
    if sord=='desc': orderby=~orderby
    limitby=(rows*(page-1),rows*page)
    records = dbset.select(table.ALL,orderby=orderby,limitby=limitby)
    nrecords = dbset.count()
    items = {}
    items['page']=page
    items['total']=int((nrecords+(rows-1))/rows)
    items['records']=nrecords
    readable_fields=[f for f in table.fields if table[f].readable]    
    def f(value,fieldname):
        if fieldname=='id':
            return SPAN(value,' [',A('open',_href=URL(r=request,f='read',args=(tablename,value))),']').xml()
        elif table[fieldname].type=='reference patient':
            v = table[fieldname].represent(value)
            return A(v,_href=URL(r=request,f='read',args=('patient',value))).xml()
        elif table[fieldname].type[:9]=='reference':
            return table[fieldname].represent(value)
        else:
            return value
    items['rows']=[{'id':r.id,'cell':[f(r[x],x) for x in readable_fields]} for r in records]
    return json(items)

    
def user():
    """
    exposes:
    http://..../[app]/default/user/login 
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    session.forget()
    return service()

