# Stadium Booking System

Welcome to the Stadium Booking System! This application allows users to book stadiums for various events. Below you will find the necessary information to set up and run the project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   
   git clone https://github.com/mminuwaali/stadium-booking-system.git
   
2. Navigate to the project directory:
   
   cd stadium-booking-system
   
3. Install the required packages:
   
   pip install -r requirements.txt
   

## Usage

To run the application, use the following command:

python manage.py runserver

Then open your web browser and go to `http://127.0.0.1:8000/`.

### Steps to Start and Successfully Run the Project

1. Ensure you have Python and Django installed.
2. Set up your database by running migrations:
   
   python manage.py migrate
   
3. Create a superuser for the admin dashboard:
   
   python manage.py createsuperuser
   
4. Start the server:
   
   python manage.py runserver

Then open your web browser and go to `http://127.0.0.1:8000/`.

## Features

- User authentication
- Stadium availability checking
- Event booking
- Admin dashboard for managing bookings

## Contributing

We welcome contributions! Please fork the repository and submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

