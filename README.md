## To run the code for the Django REST Framework API that you've developed using SQLite as the database, follow these instructions:
**Clone the Repository:** If your code is stored in a version control repository (such as Git), clone the repository to your local machine using the following command:

`git clone ‘https://github.com/Varinder-KM/Event-management-system’`

**Navigate to Project Directory:** Move to the directory where your Django project is located:

`cd EventFinderAPI`

**Set up Virtual Environment (Optional but Recommended):** It's recommended to use a virtual environment to manage dependencies. If you haven't set up a virtual environment, you can create one using virtualenv:

`Python –m venv venv`

**Activate the virtual environment:**
- On Windows: ``venv\Scripts\activate``
- On macOS and Linux: ``source venv/bin/activate``

**Install Dependencies:** Install the required Python packages specified in your requirements.txt file. Make sure you have Django and Django REST Framework installed:

`pip install -r requirements.txt`

**Run Migrations:** Since you're using SQLite as the database, run migrations to create the necessary database schema:

``python manage.py migrate``

**Start the Django Development Server:** Launch the Django development server to run your API:

``python manage.py runserver``

**Access the API Endpoints:** Once the server is running, you can access your API endpoints using a web browser or tools like Postman. The endpoints should be available at:
- `http://127.0.0.1:8000/events/add/` for adding events
- `http://127.0.0.1:8000/events/find/` for finding events (replace <latitude>, <longitude>, and <date> with appropriate values)

**Test the Endpoints:** Use appropriate HTTP methods (e.g., POST for adding events, POST for finding events) along with the required parameters to test your API endpoints.
