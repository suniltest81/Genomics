Feature: Test QA App controller in Sample REST API testing framework

Background:
	Given I set sample REST API url

Scenario:  Performing the GET request on products end point with id
    #Given I perform the GET request on products end point with city "London"
	Given I perform the GET request on products end point
    When I Set HEADER param request content type as "application/json"
	And Send GET HTTP request
    Then I receive valid HTTP response code 200 for "GET"
	And Response BODY "GET" is non-empty






