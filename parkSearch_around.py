import requests
import xlwt,os,json

#署名：cpf
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

keywords = "停车场"
location= "121.560595,29.877157"
page = 1
radius = 50000
key = "b92a02827391808c39ff27e233e227a5"

# url = "http://restapi.amap.com/v3/place/text?&keywords={keywords}" \
#       "&city={city}&output=json&offset=20&page={page}&key={key}&extensions=all"
# url="http://restapi.amap.com/v3/place/text?key={key}&keywords={keywords}&city={city}&children=0&offset=20&&page={page}&extensions=all&output=json"
url="http://restapi.amap.com/v3/place/around?key={key}&location={location}&output=json&radius={radius}&keywords={keywords}&offset=20&page={page}&extensions=all"


def gethtml(url,keywords,location,radius,page,key,headers):
    url = url.format(keywords = keywords ,location = location,radius = radius ,page = page ,key = key)
    try:
        r = requests.get(url,headers = headers)
        r.raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        result = r.json()
        return result



def parse(jsons,details):
    try:
        for item in jsons['pois']:
            name = item['name']
            types = item['type'].split(';')
            location = item['location'].split(',')
            address = item['address']
            restaurant = { 'name' :name ,'tag' : types,'location' :location,'address' : address}
            details.append(restaurant)
    except:
        pass

def loop(num):
    global page
    while page < num:
        jsons = gethtml(url, keywords, location,radius, page, key, headers)
        parse(jsons, details)
        page = page + 1
details = []
loop(100)
for i in details:
    print(i)