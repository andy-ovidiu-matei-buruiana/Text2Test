Feature: run a simple selenium test case

  Scenario: run a simple test
     Given we open WEBSITE 'https://www.amazon.com/'
      When we CLICK 'twotabsearchtextbox' 
      And we TYPE 'twotabsearchtextbox' 'J.K. Rowling'
      And CLICK 'nav-search-submit-button'
      Then the test will pass!

  Scenario: title
     Given we open WEBSITE 'http://facebook.com'
     And we open WEBSITE 'http://google.com'
      When title is TITLE 'Google'
      And takes a SCREENSHOT 'test2.png'
      Then the test will pass!