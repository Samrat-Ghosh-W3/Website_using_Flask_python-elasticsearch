from flask import Flask, render_template
from elasticsearch import Elasticsearch
from database import *
app = Flask(__name__)

es = Elasticsearch()

body = {
        'hImage': 'https://q-xx.bstatic.com/xdata/images/hotel/max300/157674722.jpg?k=bab6297144d0e071750f7c475116b051ee97b547a0c37805d66099999f4b3901&o=',
        'hCost': '13520',
        'hName': 'Universal\'s Aventura Hotel',
        'hType': 'Resort',
        'hReview': '1092',
        'hGuests': '20',
        'hBedRooms': '600',
        'hFeatures': ["Air Conditioner", "Breakfast", "Internet", "Laundry", "Parking", "Pool", "Smoking"],
        'hDescription': ' Universal\'s Aventura Hotel offers early park admission to The Wizarding World of Harry Potter™ and Universal\'s Volcano Bay water theme park 1 hour before park opening (Valid theme park admission required; attractions).<span id="dots">...</span><span id="more"><br><br>All rooms include a 43-inch flat-screen TV. A small refrigerator and coffee maker are also available. Complimentary toiletries and a hairdryer are included, as well. Certain rooms feature a seating area.<br><br>A resort-style pool with a hot tub and kids\' splash area is available for guests to enjoy. Complimentary WiFi and a free transfer to all Universal Orlando theme parks and Universal CityWalk are provided.<br><br>Restaurants come together inside a food hall offering multiple cuisines for breakfast, lunch, and dinner. The rooftop bar, lobby bar, and pool bar offer a wide range of cocktails. The Aventura also includes an onsite Starbucks®.<br><br> Universal Studios Islands of Adventure is 1 km from Universal Aventura Hotel, while The Wizarding World of Harry Potter™ is 1.1 km away. The nearest airport is Orlando International Airport, 16 km from the property.</span>'
    }

es.index(index='data', doc_type='_doc', id=1, body=body)    

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/rentbyowner/<int:id>')
def hotel(id):
    hotelId = id
    res = es.get(index='data', id=hotelId)
    hotelData = res['_source']


    return render_template('index.html', allHotelImages=allHotelImages, hotelDataById=hotelData)



if __name__ == '__main__':
    app.run(port=5000, debug=True)




