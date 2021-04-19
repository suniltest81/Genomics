from behave import given, when, then, step
import requests

api_endpoints = {}
request_headers = {}
response_codes ={}
response_texts={}
request_bodies = {}
api_url=None

@when(u'I Set HEADER param request content type as "{header_conent_type}"')
def step_impl(context, header_conent_type):
    request_headers['Content-Type'] = header_conent_type

@given(u'I set sample REST API url')
def step_impl(context):
    global api_url
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=6a7482c902e1caa93bc41ecebeca463d'


@then(u'I receive invalid HTTP response code 204')
def step_impl(context):
    print('Post rep code ;'+str(response_codes['POST']))
    assert response_codes['POST'] is 204

@then(u'Response error BODY for "{request_name}" is not empty')
def step_impl(context, request_name):
    print('request_name: ' + request_name)
    print(response_texts)
    assert response_texts[request_name] is not None
# END POST Scenario

# START GET Scenario
@given(u'I perform the GET request on products end point')
#@given(u'I perform the GET request on products end point with id "{id}"')
def step_impl(context):
    api_endpoints['GET_URL'] = api_url
    #print('url :'+api_endpoints['GET_URL'])

@given(u'I Set GET posts api endpoint for products')
def step_impl(context):
    api_endpoints['GET_URL'] = api_url+'/v1/products'
    print('url :'+api_endpoints['GET_URL'])

@when(u'Send GET HTTP request')
def step_impl(context):
    # sending get request and saving response as response object
    response = requests.get(url=api_endpoints['GET_URL'], headers=request_headers) #
    # extracting response text
    response_texts['GET']=response.text
    # extracting response status_code
    statuscode = response.status_code
    response_codes['GET'] = statuscode
    print(statuscode)

@then(u'I receive valid HTTP response code 200 for "{request_name}"')
def step_impl(context,request_name):
    print('Get rep code for '+request_name+':'+ str(response_codes[request_name]))
    assert response_codes[request_name] is 200

@then(u'Response BODY "{request_name}" is non-empty')
def step_impl(context, request_name):
    print('request_name: ' + request_name)
    print(response_texts)
    assert response_texts[request_name] is not None

# END GET Scenario

#START DELETE
@given(u'I Set DELETE posts api endpoint for "{id}"')
def step_impl(context,id):
    api_endpoints['DELETE_URL'] = api_url + '/v1/product/'+id
    print('url :' + api_endpoints['DELETE_URL'])

@when(u'I Send DELETE HTTP request')
def step_impl(context):
    # sending get request and saving response as response object
    response = requests.delete(url=api_endpoints['DELETE_URL'])
    # extracting response text
    response_texts['DELETE'] = response.text
    print("DELETE response :" + response.text)
    # extracting response status_code
    statuscode = response.status_code
    response_codes['DELETE'] = statuscode

@then(u'I receive valid HTTP response code 204 for "{request_name}"')
def step_impl(context, request_name):
    print('Get rep code for '+request_name+':'+ str(response_codes[request_name]))
    assert response_codes[request_name] is 204
#END DELETE

#START PUT
@given(u'I Set PUT posts api endpoint for "{id}"')
def step_impl(context,id):
    api_endpoints['PUT_URL'] = api_url + '/v1/product/'+id
    print('url :' + api_endpoints['PUT_URL'])

@when(u'I Set Update request Body')
def step_impl(context):
    request_bodies['PUT']={"name": "Leather boots", "price": 350}

@when(u'Send PUT HTTP request')
def step_impl(context):
    response = requests.put(url=api_endpoints['PUT_URL'], json=request_bodies['PUT'], headers=request_headers)
    # extracting response text
    response_texts['PUT'] = response.text
    print("update response :" + response.text)
    # extracting response status_code
    statuscode = response.status_code
    response_codes['PUT'] = statuscode
#END PUT







