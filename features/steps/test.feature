Feature: Testing weather api in Sample REST API testing framework

Background:
	Given I set sample REST API url

Scenario:Performing a valid GET request on weather api by city name
    Given I perform the GET request on products end point with city "London"
    When I Set HEADER param request content type as "application/json"
	And Send GET HTTP request
    Then I receive valid HTTP response code 200 for "GET"
	And Response BODY "GET" is non-empty
	
Scenario:Performing a valid GET request on weather api by city name
    Given I perform the GET request on products end point with city "Paris"
    When I Set HEADER param request content type as "application/json"
	And Send GET HTTP request
    Then I receive valid HTTP response code 200 for "GET"
	And Response BODY "GET" is non-empty	

Scenario:  Performing an invalid GET request on weather api with a random name
    Given I perform the GET request on products end point with city "test"
    When I Set HEADER param request content type as "application/json"
	And Send GET HTTP request
    Then I receive an invalid HTTP response code 404 for "GET"	





