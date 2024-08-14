# Flask Backend Assignment

<details>
  <summary><strong>Backend Assignment Details</strong></summary>
  
## Intern Assignment

## **Assignment: Flask Application for CRUD operations on MongoDB**

You need to develop a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The REST API endpoints should be accessible via HTTP requests and tested using Postman.

### **Requirements**

- The application **must** be developed using Flask and MongoDB.
- The application should provide REST API endpoints for CRUD operations on a User resource.
- The User resource should have the following fields:
  - id (a unique identifier for the user)
  - name (the name of the user)
  - email (the email address of the user)
  - password (the password of the user)
- The application should connect to a MongoDB database.
- The application should provide the following REST API endpoints:
  - GET /users - Returns a list of all users.
  - GET /users/&lt;id&gt; - Returns the user with the specified ID.
  - POST /users - Creates a new user with the specified data.
  - PUT /users/&lt;id&gt; - Updates the user with the specified ID with the new data.
  - DELETE /users/&lt;id&gt; - Deletes the user with the specified ID.
- Use the most suitable libraries to complete the assignment. Think beyond the simplest solution. Go for the best solution.
- The application is fairly simple, what we are trying to see is how well you know Flask and libraries around it to achieve this in the most scalable way possible.
- High emphasis will be placed on how the code is structured.
- We will judge you on the beauty of system design. A plain solution to the assignment will not take you further.
- **Using Docker is mandatory**

### **Testing**

1. Open Postman and create a new HTTP request for each of the REST API endpoints.
2. Send requests to the endpoints to test the CRUD operations on the User resource.
3. Verify that the responses are correct and the database is being updated correctly.

### **Submission**

1. Submit the complete code for the Flask application and any additional files needed.
2. Include a README file with instructions on how to set up and run the application.
3. Push the code to your GitHub repo.
4. Share the link to GitHub repo.

**Any assignment submitted which reeks of ChatGPT will be immediately rejected. Since, there are hundreds of submissions it is not very difficult to determine which are the ones solved by AI.**

Good luck with your assignment! Let me know if you have any questions.

</details>

## Project Overview

This repository contains the code for the backend assignment for internship. The application is built using Flask, MongoDB, and Docker.

## Tech Stack

- **Language**: Python 3.11
- **Framework**: Flask
- **Database**: MongoDB
- **Containerization**: Docker

## Getting Started

To run the project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mdzahid80/backend_assignment.git
   cd backend_assignment
   ```

2. **Set Up Environment Variables:**

   Create a `.env` file in the project root directory:

   ```bash
   cp .example.env .env
   ```

   Then, edit the `.env` file and set the following variables:

   ```env
   SECRET_KEY=your_secret_key
   MONGO_URI=mongodb://localhost:27017
   ```

3. **Build and Run with Docker:**

   Ensure Docker and Docker Compose are installed on your machine. Build and start the application using Docker Compose:

   ```bash
   docker-compose up --build
   ```

4. **Access the Application:**

   The application will be available at `http://localhost:5000`.

## API Endpoints

### User Endpoints

- **Create User:**

  `POST /users`

  Request body (JSON):

  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "securepassword"
  }
  ```

- **Get All Users:**

  `GET /users`

- **Get User by ID:**

  `GET /users/<id>`

- **Update User:**

  `PUT /users/<id>`

  Request body (JSON):

  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "newpassword"
  }
  ```

- **Delete User:**

  `DELETE /users/<id>`

### Ride Endpoints

- **Post Ride:**

  `POST /post-ride`

  Request body (JSON):

  ```json
  {
    "name": "John Doe",
    "phone_number": 1234567890,
    "email": "john.doe@example.com",
    "start_location": "Location A",
    "end_location": "Location B",
    "date_time": "2024-08-14T15:00",
    "available_seats": 3,
    "price_per_seat": 20
  }
  ```

- **Get All Rides:**

  `GET /get-ride`

- **Search Rides:**

  `GET /search?start=<start_location>&end=<end_location>`

## Running Tests

1. **Open Postman** or any HTTP client of your choice.
2. **Test** each endpoint as described in the API Endpoints section.
3. **Verify** that the responses and database updates are correct.

## Docker Configuration

- **Dockerfile:** Contains instructions to build the Flask application container.
- **docker-compose.yml:** Defines services for the Flask application and MongoDB.

## Dependencies

Install the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## File Structure and Breakdown

The project is organized into the following structure:

```
├── ./docker-compose.yml          # Docker Compose configuration file for defining services
├── ./Dockerfile                  # Dockerfile for building the Flask application container
├── ./readme.md                   # This README file
├── ./requirements.txt            # Python dependencies
└── ./src
    ├── ./src/app.py              # Main Flask application file
    ├── ./src/forms.py            # Forms used in the application
    └── ./src/templates           # HTML templates for rendering views
        ├── ./src/templates/admin.html  # Admin dashboard template
        ├── ./src/templates/index.html  # Home page template
        └── ./src/templates/rides.html  # Rides listing template
```

- **`docker-compose.yml`**: Defines the Docker services, including the Flask app and MongoDB database.
- **`Dockerfile`**: Contains instructions to build the Docker image for the Flask application.
- **`requirements.txt`**: Lists the Python packages required for the project.
- **`readme.md`**: This file, which provides an overview and instructions for the project.
- **`src/app.py`**: The main file where the Flask application is defined, including routes and database interactions.
- **`src/forms.py`**: Contains form definitions for handling user input.
- **`src/templates`**: Directory containing HTML templates used for rendering web pages.
