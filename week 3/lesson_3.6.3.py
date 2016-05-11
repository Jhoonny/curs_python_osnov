import requests

fin = 'dataset_24476_3.txt'
fou = 'lesson_3.6.3.txt'

with open(fin, 'r') as f, open(fou, "w") as out:
  for row in f:
    numbers = row.strip()
    number = int(numbers)
    # print(number)
    type = 'math'
    api_ulr = "http://numbersapi.com/"
    params = {
      'json': True
    }
    api_ulr += str(number) + '/' + type
    # print(api_ulr)
    res = requests.get(api_ulr, params=params)
    # print(res.status_code)
    # print(res.headers["Content-Type"])
    data = res.json()
    if data['found']:
      out.write("Interesting\n")
    else:
      out.write("Boring\n")

# api_ulr = "http://api.openweathermap.org/data/2.5/weather"
#
# params = {
#   'q': 'Chisinau',
#   'units': 'metric',
#   'appid': '11c0d3dc6093f7442898ee49d2430d20'
# }
#
# res = requests.get(api_ulr,params=params)
# print(res.status_code)
# print(res.headers["Content-Type"])
# data = res.json()
# print(data['main']['temp'])
#
