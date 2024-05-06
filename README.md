# Ghost AI Assistant

Ghost AI Assistant is a command-line application that helps users generate cold emails for job applications based on their personal information and job search queries.

## Features

- **Job Search**: Query job listings based on user input.
- **Personalization**: Generate cold emails tailored to each job listing and user's personal information.
- **PDF Support**: Accept user resumes in PDF format for personalization.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/franklinAnozie/ghost_ai.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ghost-ai
    ```

3. Build the docker container:

    ```bash
    docker build -t new_app .
    ```
## Usage

1. Start the application by running the container

    ```bash
    docker run -it -v ./:/app/ new_app
    ```
    or 
    ```bash
    docker run -it new_app
    ```
    you may need to use sudo to gain administrative privileges

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
