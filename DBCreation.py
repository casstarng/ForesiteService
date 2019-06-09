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
    'password': 'abc'
}

db.user.insert_one(query)
print('1 User has been created')


# Insert user
query = {
    'user_id': 'U124',
    'user_name': 'bgava',
    'first_name': 'Bhargava',
    'last_name': 'Ramisetty',
    'email': 'bgava@scu.edu',
    'phone_number': '4083823992',
    'events_attended': [''],
    'events_not_attended': [''],
    'events_published': [''],
    'events_registered': [''],
    'event_tickets': [''],
    'attendance_history': [0, 1, 0, 0, 0, 0, 0],
    'creation_date': '2019-02-20 01:16:21',
    'password': 'abc'
}

db.user.insert_one(query)
print('2 User has been created')

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
    'add_ons': [{'name': 'VIP Tickets', 'price': 2000, 'quantity': 28}, {'name': 'Laptop Rental', 'price': 1500, 'quantity': 10}],
    'add_ons_live': [{'name': 'VIP Tickets', 'price': 2000, 'quantity': 3}, {'name': 'Laptop Rental', 'price': 1500, 'quantity': 4}],
    'add_ons_total': [{'name': 'VIP Tickets', 'price': 2000, 'quantity': 30}, {'name': 'Laptop Rental', 'price': 1500, 'quantity': 23}],
    'survey_questions': [{'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': ['M', 'F']},
                            {'type': 'multipleChoice', 'question': 'What merch would you like?', 'answers': ['Shirt', 'Bag', 'Charger', 'Hat', 'Sunglasses']},
                            {'type': 'freeResponse', 'question': 'What are you looking forward to?'}],
    'event_tickets': ['T123'],
    'attendance_prediction': 20,
    'attendance_total': 25,
    'attendance_live': 10,
    'survey_prediction': [{'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': [{'M': 12}, {'F': 8}]},
                            {'type': 'multipleChoice', 'question': 'What merch would you like?', 'answers': [{'Shirt': 19}, {'Bag': 10}, {'Charger': 2}, {'Hat': 20}, {'Sunglasses': 5}]},
                            {'type': 'freeResponse', 'question': 'What are you looking forward to?', 'answers': ['Everything', 'Nothing', 'I am looking forward to free stuff']}],
    'survey_prediction_total': [{'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': [{'M': 20}, {'F': 8}]},
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
    'thumbnail_icon': 'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F57130434%2F124577588249%2F1%2Foriginal.20190220-163808?w=800&auto=compress&rect=0%2C160%2C2000%2C1000&s=605ccd4ed392249f6c25d0418a974a8f',
    'title': 'Bay Area Taco & Beer Festival',
    'street': '588 E. Alma Avenue',
    'city': 'San Jose',
    'state': 'CA',
    'zip_code': '95112',
    'start_time': '15:00',
    'start_date': '7-15-2019',
    'end_time': '19:00',
    'end_date': '7-15-2019',
    'is_tbd': 0,
    'category': 'Education',
    'description': 'Guests will experience unlimited pours of 60+ selection of craft beers from local and regional breweries as well as unlimited taco tastings from dozens of the top restaurants & food trucks in California. In addition to the free unlimited taco tastings, restaurants & food trucks will be selling additional food and beverage items. While sampling beer and tacos, make sure to stop by our boutique vendors where you can purchase orginal art. There will also be a boutique bendors, photo booth, lucha libre wrestling, bull riding, and more!',
    'max_purchase_quantity': 4,
    'max_quantity_available': 500,
    'subtotal_price': 3900,
    'add_ons': [{'name': 'VIP Tickets', 'price': 2000, 'quantity': 0}],
    'add_ons': [{'name': 'VIP Tickets', 'price': 2000, 'quantity': 0}],
    'add_ons': [{'name': 'VIP Tickets', 'price': 2000, 'quantity': 0}],
    'survey_questions': [],
    'event_tickets': [],
    'attendance_prediction': 0,
    'attendance_total': 0,
    'attendance_live': 0,
    'survey_prediction': [
        {'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': [{'M': 0}, {'F': 0}]},
        {'type': 'multipleChoice', 'question': 'What merch would you like?',
         'answers': [{'Shirt': 0}, {'Bag': 0}, {'Charger': 0}, {'Hat': 0}, {'Sunglasses': 0}]},
        {'type': 'freeResponse', 'question': 'What are you looking forward to?',
         'answers': ['Everything', 'Nothing', 'I am looking forward to free stuff']}],
    'survey_prediction_total': [
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
    'thumbnail_icon': 'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F53078843%2F27734885637%2F1%2Foriginal.jpg?w=800&auto=compress&rect=0%2C0%2C2160%2C1080&s=7121cf376a03b46a86c1ae6561431656',
    'title': 'Mind the Product San Francisco 2019',
    'street': '201 Van Ness Avenue',
    'city': 'San Francisco',
    'state': 'CA',
    'zip_code': '94102',
    'start_time': '09:00',
    'start_date': '7-16-2019',
    'end_time': '18:00',
    'end_date': '7-16-2019',
    'is_tbd': 0,
    'category': 'Technology',
    'description': 'Speakers Weve already announced six of our epic speakers for #mtocon San Francisco and well be announcing more very soon. Elizabeth Churchill, Director of UX, Google Dr Elizabeth Churchill is a Director of User Experience at Google, the Executive Vice President of the Association of Computing Machinery (ACM), a member of the ACMs CHI Academy, and an ACM Distinguished Scientist and Distinguished Speaker. With a background in psychology (neuro, experimental, cognitive and social), Artificial Intelligence and Cognitive Science, for the past 20 years she has drawn on social, computer, engineering and data sciences to create innovative end-user applications and services. She has built research teams at Google, eBay, Yahoo, PARC and FujiXerox. She holds a PhD from the University of Cambridge, an honorary Doctor of Science (DSc.) from the University of Sussex, and in September will be awarded an honorary doctorate from the University of Stockholm. In 2016 she received a Citris-Banatao Institute Award Athena Award for Women in Technology for her Executive Leadership. David J Bland, Founder, Precoil David J Bland joined his first startup in 1999 and quickly learned that a pivot can be the life or death of a company. The struggling financial services startup thought it was B2C, until a well timed shift to B2B helped it take off and be acquired for $16 million. Since then, he has been helping companies all around the world find their own product market fit using lean startup, design thinking, and business model innovation. He has validated new product ideas at corporations such as Toyota, Adobe, GE, and Behr but still stays connected to startups through his advising work at accelerators in Silicon Valley. Hes currently co-authoring a Wiley business book with Alexander Osterwalder on how to help people test new business ideas. Tricia Wang, Co-Founder, Sudden Compass Tricia Wang is obsessed with discovering the unknown. Tricia is a global tech ethnographer living at the intersection of data, design, and digital. Her passion is to help organizations uncover how our bias towards the quantifiable comes at the expense of profits and people, and how to fix it. She is the co-founder of Sudden Compass, a consulting firm that helps enterprises move at the speed of their customers by unlocking new growth opportunities in their big data with human insights in their digital transformation. Organizations shes worked with include P&G, Kickstarter, Spotify, and GE. She also co-founded Magpie Kingdom, a consultancy that helps globally minded companies gain actionable insights about the Chinese consumer. She has taught global organizations how to identify new customers and markets hidden behind their data, and amplified IDEOs design thinking practice as an expert-in-residence. Michael Sippey, VP Product at Medium Michael leads product and design at Medium, which he joined when it acquired his startup Talkshow Industries. He has a storied career across enterprise and consumer products, and has been a product manager since the pre-internet era in the early 90s. He was the VP of Product at blogging platform Six Apart, created new media properties and influential content creators as VP Artist Development at Say Media, and then led Product and Design at Twitter from 2012 to 2014. Teresa Torres, Product Discovery Coach Teresa is a product discovery coach who helps teams adopt user-centered, hypothesis-driven product development practices. She works with companies of all sizes on integrating user research, experimentation, and the right analytics into the product development process resulting in better product decisions. Recent clients include Allstate, Capital One, The Guardian, and Snagajob. Before becoming a coach, Teresa spent the majority of her career leading product and design teams at early-stage internet companies. Most recently, Teresa was VP of Products at AfterCollege, a startup that helps college students find their first job. She was CEO of Affinity Circles, an online community provider for university alumni associations and a social recruiting service used by Fortune 500 companies. She also held product and design roles at Become.com and HighWire Press. Kathy Pham, Fellow at Mozilla, Harvard, and MIT Kathy is a product leader, computer scientist, and serial founder who has held roles in product management, consulting, software engineering, data science, and leadership in the private, non-profit, and public sector. Her work has spanned Google, IBM, Harris Healthcare Solutions, and the federal government at the United States Digital Service at the White House, where she was a founding product and engineering member. She has founded Women in Product Boston, the Cancer Sidekick Foundation, Team Curious, and Unite for Sight Southeast. She is a Fellow at the Harvard Berkman Klein Center and MIT Media Lab where she leads the Ethical Tech Working Group and focuses on ethics in technology, with an emphasis on artificial intelligence, engineering culture, and computer science curricula. She is also a Senior Fellow at digital HKS, faculty affiliate at the Center for Research on Computation and Society (CRCS) at the Harvard John A. Paulson School of Engineering and Applied Sciences (SEAS), and Fellow in Residence at the Mozilla Foundation partnering with Omidyar Network where she co-leads the Responsible Computer Science Challenge. Through her fellowship with digital HKS, she launched Product and Society. Fareed Mosavat, Director of Product Lifecycle at Slack With over a decade of engineering experience and far-reaching achievements in product and growth, few people have touched as many disciplines and verticals as Fareed. He started his career by working on computer graphics at Pixar for seven years. He built the physical simulation network that was used to animate vehicle motion and was used throughout the movies Cars, WALL-E, Finding Nemo, Up, and is still used in all Pixar feature films to this day. He moved into product when he joined Boston-based social games startup Conduit Labs, which was later acquired by Zynga and made him General Manager and studio head for Zynga Boston. He was the VP Product at Runkeeper and Instacart before joining Slack in 2012 where he now leads its efforts around growth, adoption, retention, and administration. Brandon Chu, VP Product, Shopify Brandon is the VP of Product, and General Manager of the Platform team at Shopify, which enables thousands of developers to build commerce apps for businesses on the platform. Previously, he was a Product Director at FreshBooks, and co-founded Tunezy, a YouTube music startup that was acquired in 2013. Brandon is the author of a popular product management publication called The Black Box of PM, and is a co-founder of APM Toronto, a community lead, cross-company initiative to level up junior PMs. Denise Jacobs, Author, Banish Your Inner Critic Denise Jacobs is a Speaker + Author + Creativity Evangelist who speaks at conferences and consults with companies worldwide. As the Founder + CEO of The Creative Dose, keynote speaker, and trainer, she helps individuals in companies unleash their creativity through banishing their inner critic and hacking their creative brains. Denises keynotes and trainings give an injection of inspiration and immediately applicable tools to help people do their best work. Through working with Denise, people become engaged contributors, synergistic collaborators, and authentic leaders. Denise is the author of Banish Your Inner Critic, the premier handbook on silencing fears to unleash creativity. A web and tech industry veteran, Denise is also the author of The CSS Detective Guide and co-author of the Smashing Book #3 1/3 and Interact with Web Standards. She is also the founder of Rawk The Web and the Head Instigator of The Creativity (R)Evolution. Steve Portigal, Author, Doorbells, Danger, and Dead Batteries Steve Portigal helps companies to think and act strategically when innovating with user insights. Based outside of San Francisco, he conducted research with thoracic surgeons, families eating breakfast, rock musicians, home-automation enthusiasts, credit-default swap traders, and radiologists. His work has informed the development of professional audio gear, wine packaging, medical information systems, design systems, video-conferencing technology, and music streaming services. Hes also the host of the Dollars to Donuts podcast, where he interviews people who lead user research in their organizations. Steve is an accomplished presenter who speaks about culture, innovation, and design at companies and conferences across the globe. Take a look at all of our previous #mtpcon speakers to see the sorts of topics covered.',
    'max_purchase_quantity': 4,
    'max_quantity_available': 500,
    'subtotal_price': 0,
    'add_ons': [],
    'add_ons_live': [],
    'add_ons_total': [],
    'survey_questions': [{'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': ['M', 'F']}],
    'event_tickets': ['T123'],
    'attendance_prediction': 43,
    'attendance_total': 50,
    'attendance_live': 0,
    'survey_prediction': [
        {'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': [{'M': 31}, {'F': 12}]}],
    'survey_prediction_total': [
        {'type': 'singleChoice', 'question': 'Are you Male or Female?', 'answers': [{'M': 40}, {'F': 15}]}],
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
    'title': 'Santa Clara Tech Conference',
    'thumbnail_icon': 'https://res.cloudinary.com/dz0okos1w/image/upload/v1555275330/Santa_Clara_U_Seal.svg.png',
    'street': '5001 Great America Pkwy',
    'city': 'Santa Clara',
    'state': 'CA',
    'zip_code': '95054',
    'start_time': '13:00',
    'start_date': '4-12-2019',
    'end_time': '20:00',
    'end_date': '4-12-2019',
    'qr_code': 'QR Code placeholder',
    'amount_bought': 2,
    'tickets_redeemed': 0,
    'add_ons': [],
    'survey_questions': {'survey': [{'question': 'Male or Female', 'answers': 'M'}]},
    'creation_date': 'Tue, 21 May 2019 11:42:20 GMT'
}

db.ticket.insert_one(query)
print('1 Event Ticket has been created')

print('Everything has been created successfully')


