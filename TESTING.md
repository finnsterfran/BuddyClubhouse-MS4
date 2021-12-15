# TESTING 

<p>&nbsp;</p>

# TABLE OF CONTENT
## 1.&nbsp;&nbsp;&nbsp;&nbsp;[COVERAGE](#coverage_-_django_testing)
## 2.&nbsp;&nbsp;&nbsp;&nbsp;[MANUAL TEST]
## 3.&nbsp;&nbsp;&nbsp;&nbsp;[VALIDATORS]()
* [HTML](#something)
* [CSS]
* [PEP8]
* [JAVASCRIPT]






# Coverage - Django Testing
## To generate reports on the automated testing:
    *   install coverage : pip3 install coverage
    *   python3 -m coverage run --source=`APPNAME` manage.py test : create test database
    *   python3 -m coverage report : generate the report
    *   python3 -m coverage html : render the report in html in a file named htmlcov
        * to see the file online : 
            *   python3 -m http.server
            *   click htmlcov
<p>&nbsp;</p>

## To run Django Unit Testing:
    * test_views, test_models, test_forms (only if app has forms) were created to generate these test
    * to run the test : e.g.  python3 manage.py test checkout.test_views
 <p>&nbsp;</p>

### **This shows an error in the test which caused it to fail**
<p>&nbsp;</p>

*   ![django_testing_error](README_images/django_testing_error.png)
<p>&nbsp;</p>

### **The OK means the test ran as they were instructed and with no errors**
<p>&nbsp;</p>

*   ![django_testing_ok](README_images/django_testing_ok.png)

<p>&nbsp;</p>

* BLOGBOARD
![Blogboard](README_images/coverage_report_blogboard.png)

<p>&nbsp;</p>

* CHECKOUT
![Checkout](README_images/coverage_report_checkout.png)

<p>&nbsp;</p>

* CONTRIBUTION
![Contribution](README_images/coverage_report_contribution.png)

<p>&nbsp;</p>

* DOGS
![Dogs](README_images/coverage_report_dogs.png)

<p>&nbsp;</p>

* EVENTS
![Events](README_images/coverage_report_events.png)

<p>&nbsp;</p>

* HOME
![Home](README_images/coverage_report_home.png)

<p>&nbsp;</p>

* USERS
![Users](README_images/coverage_report_users.png)

<p>&nbsp;</p>

# MANUEL TESTING
## FORMS 
