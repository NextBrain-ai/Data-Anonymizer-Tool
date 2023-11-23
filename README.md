# NB Anonymizer

## Introduction

NextBrain's data Anonymizer tool ensures top-tier privacy by irreversibly obscuring personal identifiers without storing any data. Ideal for businesses prioritizing data security and compliance, it offers a reliable solution for safeguarding sensitive information.

This project is inspired by a need we recognized during the development of our machine learning solution, NextBrain. It empowers us to transcend the barriers typically encountered in the proof of concept phase. Furthermore, through this initiative, we are eager to support the open-source community, tackling some of the foremost challenges encountered in employing these types of tools.

## Table of Contents

- [NB Anonymizer](#nb-anonymizer)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Windows](#windows)
    - [Mac](#mac)
    - [Linux](#linux)
  - [Getting Started](#getting-started)
    - [For Developers](#for-developers)
    - [Using Jupyter Notebook](#using-jupyter-notebook)
    - [Using Docker](#using-docker)
  - [Building the Project](#building-the-project)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Installation

### Windows

Coming soon

### Mac

Coming soon

### Linux

Coming soon

## Getting Started

### For Developers

To get started with the development of NB-Anonymizer, follow these steps:

1. **Clone the Repository**: First, clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/NextBrain-ai/NB-Anonymizer
   ```
2. **Create a Virtual Environment**: Navigate to the project directory and create a Python virtual environment:
   ```bash
   cd NB-Anonymizer
   python3 -m venv venv
   ```
   Required Python 3.10+
3. **Activate the Virtual Environment**: Activate the virtual environment. The command varies depending on your operating system:
   - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On Linux:
        ```bash
        source venv/bin/activate
        ```
4. **Install Dependencies**: Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
5. **Launch the Application**: Start the application with Streamlit:
   streamlit run streamlit_app/streamlit_app.py
6. 🎉 At this point, the application should be accessible at http://localhost:8501.


### Using Jupyter Notebook

Coming soon

### Using Docker


If you have Docker and Docker Compose already installed on your system, running NB-Anonymizer is straightforward. Just follow these steps:

1. **Navigate to the Project Directory**: Open a terminal and navigate to the root directory of the NB-Anonymizer project.

2. **Start the Application with Docker Compose**: Run the following command to start the application in a Docker container:
   ```bash
   docker compose up -d
   ```

This command will pull the necessary Docker images, create a container, and start the application.

🎉 Once the process is complete, NB-Anonymizer should be running in a Docker container, typically accessible at http://localhost:8501.

## Building the Project

To build a distribution of the project, use the following commands:

```bash
npm run dump streamlit_app -- -r requirements.txt
```

```bash
npm run dist
```

Before building a distribution of NB-Anonymizer, ensure that you meet the following prerequisites:

- **Python 3.10 or Higher**: The project requires Python version 3.10 or newer. You can download and install the latest version of Python from [python.org](https://www.python.org/downloads/).
  
- **Node.js and npm**: npm (Node Package Manager) is needed for handling the project's JavaScript dependencies. You can download and install Node.js and npm from [nodejs.org](https://nodejs.org/).

Once you have these prerequisites installed, follow these steps to build the project:

1. **Install JavaScript Dependencies**: Navigate to the project directory and run `npm install`. This will install Electron along with other necessary dependencies:
   ```bash
   npm install
   ```
2. **Build the Project**: Execute the following commands to build a distribution of the project:
   ```bash
   npm run dump streamlit_app -- -r requirements.txt
   npm run dist
   ```
   These commands will package the application and prepare it for distribution. After running these commands, the built version of NB-Anonymizer will be available in the distribution directory of the project.

## Contributing

Contributions to NB-Anonymizer are welcome and appreciated. If you want to contribute, please:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

For more detailed information, please refer to the [CONTRIBUTING](CONTRIBUTING) file.

## License

NB-Anonymizer is licensed under the [MIT License](LICENSE).

## Contact

For support or any queries, feel free to contact us at [info@nextbrain.ai](mailto:info@nextbrain.ai).
