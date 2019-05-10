import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client.foresite
cursor = db.user.find()

# This exits if there already exists a user in the collection.
# This will prevent you from creating duplicate users if you run this script multiple times
if len(list(cursor)) > 0:
    client.drop_database('foresite')

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
    'attendance_history': [0, 1, 1, 0, 1, 1, 1],
    'creation_date': '2019-02-20 01:16:21',
    'password': 'tempPassword'
}

db.user.insert_one(query)
print('1 User has been created')

# Insert event
query = {
    'event_id': 'TEMP',
    'user_name': 'ctarng',
    'thumbnail_icon': 'https://res.cloudinary.com/dz0okos1w/image/upload/v1555275330/Santa_Clara_U_Seal.svg.png',
    'title': 'Santa Clara Tech Conference',
    'street': '5001 Great America Pkwy',
    'city': 'Santa Clara',
    'state': 'CA',
    'zip_code': '95054',
    'start_time': '13:00',
    'start_date': '4-12-2019',
    'end_time': '20:00',
    'end_date': '4-12-2019',
    'is_tbd': 0,
    'category': 'Technology',
    'description': 'The Santa Clara Tech COnference is a tech conference that....',
    'max_purchase_quantity': 4,
    'max_quantity_available': 500,
    'subtotal_price': 4500,
    'add_ons': [{'name': 'VIP Tickets', 'price': 2000, 'count': 0}, {'name': 'Laptop Rental', 'price': 1500, 'count': 0}],
    'survey_questions': [{'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': ['M', 'F']},
                            {'type': 'multipleChoice', 'question': 'What merch would you like?', 'answers': ['Shirt', 'Bag', 'Charger', 'Hat', 'Sunglasses']},
                            {'type': 'freeResponse', 'question': 'What are you looking forward to?'}],
    'event_tickets': ['T123'],
    'attendance_prediction': 20,
    'survey_prediction': [{'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': [{'M': 12}, {'F': 8}]},
                            {'type': 'multipleChoice', 'question': 'What merch would you like?', 'answers': [{'Shirt': 19}, {'Bag': 10}, {'Charger': 2}, {'Hat': 20}, {'Sunglasses': 5}]},
                            {'type': 'freeResponse', 'question': 'What are you looking forward to?', 'answers': ['Everything', 'Nothing', 'I am looking forward to free stuff']}],
    'creation_date': '2019-02-20 01:16:21',
    'last_updated': '2019-02-20 01:16:21'
}

db.event.insert_one(query)

results = db.event.find({'event_id': 'TEMP'})

for r in results:
    r['event_id'] = str(r['_id'])
    db.event.update({'event_id': 'TEMP'}, r)

print('1 Event has been created')

# Insert event 2
query = {
    'event_id': 'TEMP',
    'user_name': 'ctarng',
    'thumbnail_icon': 'https://res.cloudinary.com/dz0okos1w/image/upload/v1555275330/Santa_Clara_U_Seal.svg.png',
    'title': 'San Jose State University New Orientation date',
    'street': '2443 Santa Clara St',
    'city': 'San Jose',
    'state': 'CA',
    'zip_code': '95054',
    'start_time': '13:00',
    'start_date': '6-12-2019',
    'end_time': '20:00',
    'end_date': '6-12-2019',
    'is_tbd': 0,
    'category': 'Education',
    'description': 'San Jose State is hosting a new orientation educational session. This session will involve creating schedules, tours of the campus, and much more. This description will have a lot of text for testing purposes so that Bhargava can test the front end for inconsistencies and stuff like that. Foresite Forever.',
    'max_purchase_quantity': 4,
    'max_quantity_available': 500,
    'subtotal_price': 10000,
    'add_ons': [],
    'survey_questions': [],
    'event_tickets': [],
    'attendance_prediction': 0,
    'survey_prediction': [
        {'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': [{'M': 0}, {'F': 0}]},
        {'type': 'multipleChoice', 'question': 'What merch would you like?',
         'answers': [{'Shirt': 0}, {'Bag': 0}, {'Charger': 0}, {'Hat': 0}, {'Sunglasses': 0}]},
        {'type': 'freeResponse', 'question': 'What are you looking forward to?',
         'answers': ['Everything', 'Nothing', 'I am looking forward to free stuff']}],
    'creation_date': '2019-02-20 01:16:21',
    'last_updated': '2019-02-20 01:16:21'
}

db.event.insert_one(query)

results = db.event.find({'event_id': 'TEMP'})

for r in results:
    r['event_id'] = str(r['_id'])
    db.event.update({'event_id': 'TEMP'}, r)

print('2 Event has been created')

# Insert event 3
query = {
    'event_id': 'TEMP',
    'user_name': 'ctarng',
    'thumbnail_icon': 'https://res.cloudinary.com/dz0okos1w/image/upload/v1555275330/Santa_Clara_U_Seal.svg.png',
    'title': 'Google Cloud Conference',
    'street': '5001 Great America Pkwy',
    'city': 'Santa Clara',
    'state': 'CA',
    'zip_code': '95054',
    'start_time': '13:00',
    'start_date': '4-16-2019',
    'end_time': '20:00',
    'end_date': '4-16-2019',
    'is_tbd': 0,
    'category': 'Technology',
    'description': 'Google Cloud is hosting a free session. Come for free stuff.',
    'max_purchase_quantity': 4,
    'max_quantity_available': 500,
    'subtotal_price': 0,
    'add_ons': [],
    'survey_questions': [{'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': ['M', 'F']}],
    'event_tickets': ['T123'],
    'attendance_prediction': 43,
    'survey_prediction': [
        {'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': [{'M': 31}, {'F': 12}]}],
    'creation_date': '2019-02-20 01:16:21',
    'last_updated': '2019-02-20 01:16:21'
}

db.event.insert_one(query)

results = db.event.find({'event_id': 'TEMP'})

for r in results:
    r['event_id'] = str(r['_id'])
    db.event.update({'event_id': 'TEMP'}, r)

print('3 Event has been created')

# Insert event_ticket
query = {
    'ticket_id': 'T123',
    'user_name': 'ctarng',
    'user_id': 'U123',
    'event_id': 'E001',
    'qr_code': 'QR Code placeholder',
    'amount_bought': 2,
    'is_ticket_redeemed': 0,
    'add_ons': [],
    'survey_questions': {'survey': [{'question': 'Male or Female', 'answers': 'M'}]},
    'creation_date': '2019-02-20 01:16:21'
}

db.ticket.insert_one(query)
print('1 Event Ticket has been created')

print('Everything has been created successfully')


