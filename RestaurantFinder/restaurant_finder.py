import requests
import argparse
import zomato_key

user_key = zomato_key.key

parser = argparse.ArgumentParser()
parser.add_argument('--city', action='store', dest='city', help='Name of city', type=str)
parser.add_argument('--count', default=10, action='store', dest='count', help='No. of restaurants', type=int)
parser.add_argument('--cuisine', action='store', dest='cuisine', help='Type of cuisine', type=str)
parser.add_argument('--sort-by', action='store', dest='sort', help='cost / rating', type=str)
parser.add_argument('--order', action='store', dest='order', help='asc / desc', type=str)

results = parser.parse_args()
city = results.city
count = results.count
cuisine = results.cuisine
sort = results.sort
order = results.order

if(cuisine):
	cuisine = cuisine.lower()

location_url = 'https://developers.zomato.com/api/v2.1/locations'
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": user_key}
payload = {'query': city}

r = requests.get(location_url, params=payload, headers=header)
r = r.json()["location_suggestions"][0]

entityId = r["entity_id"]
entityType = r["entity_type"]

cuisines_url = "https://developers.zomato.com/api/v2.1/cuisines"
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": user_key}
payload = {'city_id': entityId}
r = requests.get(cuisines_url, params=payload, headers=header).json()
cuisine_dict = {}

for i in range(len(r["cuisines"])):
	cuisine_dict[r["cuisines"][i]["cuisine"]["cuisine_name"].lower()] = r["cuisines"][i]["cuisine"]["cuisine_id"]


search_url = 'https://developers.zomato.com/api/v2.1/search'
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": user_key}

if(cuisine):
	payload = {'q': city, 'count': count, 'cuisines': cuisine_dict[cuisine], 'sort': sort, 'order': order}
else:
	payload = {'q': city, 'count': count, 'sort': sort, 'order': order}

try:
	r = requests.get(search_url, params=payload, headers=header)
	print(r.url)
	data = r.json()

	restaurant_list = data['restaurants']
	for i in range(len(restaurant_list)):
		print(restaurant_list[i]["restaurant"]["name"])
		print("Address: %s" % restaurant_list[i]["restaurant"]["location"]["address"])
		print("Cuisine: %s" % restaurant_list[i]["restaurant"]["cuisines"])
		print("Price for two: %s" % restaurant_list[i]["restaurant"]["average_cost_for_two"])
		if(restaurant_list[i]["restaurant"]["offers"]):
			print("Offers: %s" % restaurant_list[i]["restaurant"]["offers"])
		print("Rating: %s" % restaurant_list[i]["restaurant"]["user_rating"]["aggregate_rating"])
		print("\n\n")
except ConnectionError as e:
	print("Problem with Internet Connection. Please try later.")