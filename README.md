# Location Tracker
A simple Django project that implements multi-user login and permission-based access to data via API endpoints in order to visualise location coordinates on Google Map. Django Restframework was utilized for the API implementations.

## Pre-requisite Installation

- Install the latest version of [python](https://www.python.org/downloads/)

- Install *pipenv* from the command line using the command:
    ```bash
    $ pip install --user pipenv
    ```

- Clone the repository or download the repository and the navigate to the repository on the command line.

- Install dependencies for the project:
    ```bash
    $ pipenv install
    ```
 
 ## Running the Django App
 
 - Activate the virtual environement created by *pipenv* by typing in the command line:
   ```bash
    $ pipenv shell
   ```

 - Run the server:
    ```bash
    $ cd LocationTracker
    $ python manage.py runserver
    ```
  
  ## API Endpoints
  A list of the implemented API endpoints are listed below:
  
  - **/api/user** - *GET, POST, HEAD request to view all basic users and create a new user.*

  - **/api/user/<int: pk>** - *GET, PUT/PATCH, DELETE request to view specific basic user, edit and delete methods is reserved only admin and logged in users whose public key (pk) matches the endpoint.*

  - **/api/courier** - *GET, POST, HEAD request to view all registered couriers and create a new courier.*

  - **/api/courier/<int: pk>** - *GET, PUT/PATCH, DELETE request to view specific courier data, edit and delete methods is reserved only admin and logged in users whose public key (pk) matches the endpoint.*

  - **/api/device** - *GET, POST, HEAD request to view all registered devices and register a new device. POST request is reserved for admin and logged in users.*

  - **/api/device/<int: pk>** - *GET, PUT/PATCH, DELETE request to view a specific device, editing and deleting is reserved only for admin and logged in users whose public key (pk) matches the endpoint.*

  - **/tracker/api/location** - *GET, POST, HEAD request to view all locations in the database and create a new location cordinate. Reserved for only the admin and registered devices.*

  - **/tracker/api/location/<int: pk>** - *GET, PUT/PATCH, DELETE request to view a specific location cordinate. Editing and deleting is reserved only for admin and registered device calling the endpoint.*
  
  ## Contributing
  Please make a pull request if you want to contribute to this project
  
  ## License
  MIT License