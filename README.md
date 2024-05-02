# Ghost AI Assistant

Ghost AI Assistant is a command-line application that helps users generate cold emails for job applications based on their personal information and job search queries.

## Features

- **Job Search**: Query job listings based on user input.
- **Personalization**: Generate cold emails tailored to each job listing and user's personal information.
- **PDF Support**: Accept user resumes in PDF format for personalization.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd ghost-ai
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
5. Create a .env file and paste in the following env variables.
   it's recommended however, if you want to use this app for production, don't share your env files on the internet.

   - GOOGLE_API_KEY=AIzaSyD2koNV4lTZQfHjbS89ctznFjQmhJVlP50
   - X-RapidAPI-KEY=668672dbf5msh447e3e120075196p1638c9jsn4168fab68a64
   - X-RapidAPI-Host=jsearch.p.rapidapi.com

## Usage

1. Start the application by running `init.py`:

    ```bash
    python -m main.__init__
    ```

2. Follow the prompts to provide your personal information and specify your job search query.
   
3. The application will search for relevant job listings and generate cold emails based on your input.

4. Review and customize the generated emails as needed before sending them to potential employers.

## Configuration

- Ensure you have set up the required environment variables for authentication and API access. Refer to the `auth.py` module for more information.

## Contributing

Contributions to Ghost AI Assistant are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes and commit them (`git commit -am 'Add feature/improvement'`).
4. Push to the branch (`git push origin feature/improvement`).
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
