
# ci-cd-deploy
=======
# Flask Application

This project is a simple Flask web application that serves a greeting message. Below are the instructions on how to set up and run the application.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository to your local machine:

   ```
   git clone <repository-url>
   cd flask-app
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask application, execute the following command:

```
python app.py
```

The application will be accessible at `http://0.0.0.0:80` or `http://localhost:80`.

## Project Structure

```
flask-app
├── app.py            # Main entry point of the Flask application
├── requirements.txt   # Lists the dependencies required for the application
└── README.md         # Documentation for the project
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
>>>>>>> ae971b6 (Initial commit with Flask app, Dockerfile, and CI/CD workflow)
