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
    api_url = 'http://api.openweathermap.org/data/2.5/weather'


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
@given(u'I perform the GET request on products end point with city "{city_name}"')
def step_impl(context, city_name):
    api_endpoints['GET_URL'] = api_url+'?q='+city_name+'&appid=6a7482c902e1caa93bc41ecebeca463d'
    print('url :'+api_endpoints['GET_URL'])

@given(u'I Set GET posts api endpoint for products')
def step_impl(context):
    api_endpoints['GET_URL'] = api_url
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

@then(u'I receive an invalid HTTP response code 404 for "{request_name}"')
def step_impl(context, request_name):
    print('Get rep code updated for '+request_name+':'+ str(response_codes[request_name]))
    print(response_codes[request_name])
    assert response_codes[request_name] == 404









