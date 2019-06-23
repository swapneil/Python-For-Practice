import sys
import requests
from bs4 import BeautifulSoup
import json
# Fill in your details here to be posted to the login form.
loginid=raw_input("Enter Your Flipkart Username:")
password=raw_input("Enter Your Flipkart Credential:")
payload = {
    'loginId': loginid,
    'password': password
}
headers={
    'X-user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0 FKUA/website/41/website/Desktop'
}

cookies={
    'T':'TI156129373672188449189534257924823988200124673344169934817247935759', 
    'SN':'2.VI6DF547D773024A4B87BE32AB87468383.SIE4004A793ECB4E009F86BF9CA1979990.VS84742A7BEACD483A8178B5BB07506213.1561293736', 
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg':'-227196251%7CMCIDTS%7C18071%7CMCMID%7C18488450496170713392220671589943051205%7CMCAAMLH-1561898540%7C12%7CMCAAMB-1561898540%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1561300940s%7CNONE%7CMCAID%7CNONE', 
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg':'1',
    'gpv_pn':'HomePage',
    'gpv_pn_t':'FLIPKART%3AHomePage', 's_cc':'true',
    'S':'d1t15Iz8/Pz9jPy5MPz93HQY/VwpbjPJMiNo4mV8lsxnJzzBlnIjm/7r5GFjchIKY0tvDQLIzIYCOReE8VFYhKLC6Mg==','s_sq':'%5B%5BB%5D%5D'
}
# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://www.flipkart.com/api/4/user/authenticate', data=payload,headers=headers,cookies=cookies)
    # print the html returned or something more intelligent to see if it's a successful login page.
    if (p.status_code!=200):
	print "Sorry Wrong Credentials. Please try again later.\n"
	sys.exit()
    print p.text
    json_obj = json.loads(p.text)
    print "*************************************************"
    print "Account Id:"+ json_obj['SESSION']['accountId']
    print "First Name:"+json_obj['SESSION']['firstName']
    print "Last Name:"+json_obj['SESSION']['lastName']
    print "Email Id:"+json_obj['SESSION']['email']
    print "*************************************************"
    # An authorised request.
    r = s.get('https://www.flipkart.com/api/3/self-serve/orders/?page=1&order_before_time_stamp=1561303789668',headers=headers,cookies=cookies)
#    print r.content
#Response-multipleOrderDetailsView-orderMetaData-orderID
    json_orderID=json.loads(r.text)
#    print json_orderID
    orderDict=json_orderID['RESPONSE']['multipleOrderDetailsView']['orders']
    for i in range(len(orderDict)):
	print "****************************************************************************"
	print "Product Name :"+orderDict[i].values()[7].values()[0].values()[1].values()[3]
        print "OrderId :"+orderDict[i].values()[5].values()[0]
        print "****************************************************************************\n\n"
