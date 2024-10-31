

# Gym Freak

Gym Freak is a Django-based web application offering various gym-related services, such as Zumba classes, fitness plans, and an interactive AI chatbot for fitness queries. This project provides a full-stack solution with user authentication and personalized features to engage users in their fitness journeys.

## Features

- Zumba Classes: A selection of Zumba sessions tailored to diverse fitness needs.
- Fitness Plans: Access customized fitness plans focused on various goals like weight loss, endurance, and muscle gain.
- AI Chatbot: An AI-powered chatbot to assist users with gym and fitness-related questions.
- User Authentication: Secure login and registration services for personalized access.

## Project Structure

- Folders:
  - `bodyboy`: Core Django app for handling fitness plans and class schedules.
  - `gymbro`: Secondary app focusing on user interactions and chatbot functionality.
  - `static`: Contains static assets (CSS, JavaScript, images).
  - `templates`: Holds HTML templates for rendering views.

- Files:
  - `.env`: Stores environment variables (like secret keys and database settings).
  - `db.sqlite3`: SQLite database to manage app data.
  - `manage.py`: Django’s command-line utility for various tasks.

## Getting Started

### Prerequisites

- Python 3.x
- Django installed (`pip install django`)
- Clone the repository:
  ```bash
  git clone https://github.com/ameyaatmaa/GymFreak.git
  cd GymFreak
  ```

### Installation

1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up environment variables by creating a `.env` file.
3. Run migrations to initialize the database:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Visit [http://localhost:8000](http://localhost:8000) to start using Gym Freak.

## Usage

- Register/Login: Create an account to access the platform's services.
- Explore Classes and Plans: Navigate through the Zumba classes and fitness plans available.
- Chatbot Support: Ask fitness-related questions through the AI chatbot.

## Contribution

Contributions are welcome. Please fork the repo, create a new branch, and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License.

