Feature: run a login test case with background

    Background:
      Given we open WEBSITE 'https://www.amazon.com/'

    Scenario: login
      Given we open WEBSITE 'https://www.clientam.com/sso/Login'
      When we CLICK 'user_name'
      And we TYPE 'user_name' 'uname'
      And we CLICK 'password'
      And we TYPE 'password' 'pass'
      And we CLICK 'submitForm'
      Then an ERROR 'ERRORMSG' 'Invalid username password combination' will be raised

    Scenario: title2
     Given we open WEBSITE 'http://facebook.com'
     And we open WEBSITE 'http://google.com'
      When title is TITLE 'Google'
      And takes a SCREENSHOT 'test.png'
      Then the test will pass!
      And something