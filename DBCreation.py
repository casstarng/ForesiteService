import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client.foresite
cursor = db.user.find()

# This exits if there already exists a user in the collection.
# This will prevent you from creating duplicate users if you run this script multiple times
if len(list(cursor)) > 0:
    exit()

for doc in cursor:
    print(doc)

# Insert user
query = {
    'user_id': 'U123',
    'user_name': 'ctarng',
    'first_name': 'Cassidy',
    'last_name': 'Tarng',
    'email': 'ctarng@scu.edu',
    'phone_number': '5106762337',
    'events_attended': [''],
    'events_not_attended': [''],
    'events_published': [''],
    'events_registered': ['E001'],
    'event_tickets': ['T123'],
    'creation_date': 'T123',
    'password': 'tempPassword'
}

db.user.insert_one(query)
print('1 User has been created')

# Insert event
query = {
    'event_id': 'E001',
    'user_id': 'U123',
    'thumbnail_icon': 'icon placeholder',
    'title': 'Santa Clara Tech Conference',
    'street': '5001 Great America Pkwy',
    'city': 'Santa Clara',
    'state': 'CA',
    'zip_code': '95054',
    'start_time': '13:00',
    'end_time': '20:00',
    'is_tbd': 0,
    'category': 'Technology',
    'description': 'The Santa Clara Tech COnference is a tech conference that....',
    'max_purchase_quantity': 4,
    'max_quantity_available': 500,
    'subtotal_price': 4500,
    'add_ons': {},
    'survey_questions': {'survey': [{'question': 'Male or Female', 'answers': ['M', 'F']}]},
    'event_tickets': ['T123'],
    'creation_date': '2019-02-20 01:16:21',
    'last_updated': '2019-02-20 01:16:21'
}

db.event.insert_one(query)
print('1 Event has been created')

# Insert event_ticket
query = {
    'order_id': 'T123',
    'user_name': 'ctarng',
    'user_id': 'U123',
    'event_id': 'E001',
    'qr_code': 'QR Code placeholder',
    'is_ticket_redeemed': 0,
    'add_ons': {},
    'survey_questions': {'survey': [{'question': 'Male or Female', 'answers': 'M'}]},
    'creation_date': '2019-02-20 01:16:21'
}

db.event_ticket.insert_one(query)
print('1 Event Ticket has been created')

print('Everything has been created successfully')


