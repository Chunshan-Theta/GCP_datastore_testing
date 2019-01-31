from google.cloud import datastore
import datetime


# connect to db
def create_client(project_id):
    return datastore.Client(project_id)

# new a user
def add_task(client, description):
    key = client.key('users')

    task = datastore.Entity(
        key, exclude_from_indexes=['description'])

    task.update({
        'created': datetime.datetime.now(),
        'description': description,
        'done': False,
        'name':"Tom3",
        'age':25,
        'school':'ncu'
    })

    client.put(task)

    return task.key

# select user
def select_tasks(client,k='users'):
    query = client.query(kind=k)
    query.add_filter('age','>',19)
    #query.order = ['age']
    return list(query.fetch())

#show a entity
def detail_entity(e):
    print(e.kind)
    print(dict(e))
    print(e.key.id)
    print(e.key)


#updata data of a user
def update(db,key,value):
    entity = datastore.Entity(key=key)
    entity.update(value)
    db.put(entity)
    
    #get uptated entity
    return db.get(key)

#delete a user
def delete_user(db,key):
    db.delete(key)



db = create_client("nosql-230306")

content = select_tasks(db)
for i in content:
    detail_entity(i)
    
add_task(db,'a normal student')

content = select_tasks(db)
for i in content:
    detail_entity(i)
    k = i.key

update(db,k,{"age":100})

content = select_tasks(db)
for i in content:
    detail_entity(i)
    
delete_user(db,k)
