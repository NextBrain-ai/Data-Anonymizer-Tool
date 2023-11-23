# Data Anonymization Tool

## Introduction

NextBrain's data Anonymizer tool ensures top-tier privacy by irreversibly obscuring personal identifiers without storing any data. Ideal for businesses prioritizing data security and compliance, it offers a reliable solution for safeguarding sensitive information.

This project is inspired by a need we recognized during the development of our machine learning solution, NextBrain. It empowers us to transcend the barriers typically encountered in the proof of concept phase. Furthermore, through this initiative, we are eager to support the open-source community, tackling some of the foremost challenges encountered in employing these types of tools.

---

The anonymization process maintains the original data distribution while injecting noise into the statistics. This approach helps to prevent the re-identification of the data. For more details about the anonymization process, refer to the following paper: [DataSynthesizer](https://github.com/DataResponsibly/DataSynthesizer/blob/master/docs/cr-datasynthesizer-privacy.pdf)

## Table of Contents

- [Data Anonymization Tool](#data-anonymization-tool)
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
  - [Roadmap](#roadmap)
    - [Phase 1: Initial Setup](#phase-1-initial-setup)
    - [Phase 2: Web Platform Development](#phase-2-web-platform-development)
    - [Phase 3: Integration with Popular Tools](#phase-3-integration-with-popular-tools)
    - [Phase 4: Desktop Application](#phase-4-desktop-application)
    - [Phase 5: Advanced Algorithm Testing](#phase-5-advanced-algorithm-testing)
    - [Phase 6: Evaluation and Analysis](#phase-6-evaluation-and-analysis)
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

**Download the [NB Anonymizer Jupyter Notebook](NB_Anonymizer.ipynb) now** and dive into a user-friendly, step-by-step guide designed for effortless navigation and comprehension.

Prefer not to install anything? No problem! You can also utilize **Google Colab** to run the notebook seamlessly. Simply click [here](https://colab.research.google.com/drive/1nYl800vK7yzudFJFqe5HDJFEMzKumpnq?usp=sharing) to execute the code in a cloud-based environment, hassle-free.

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

## Roadmap

### Phase 1: Initial Setup
- [x] **Initial Anonymization System**: Develop a basic system for data anonymization to lay the groundwork for more advanced features.

### Phase 2: Web Platform Development
- [x] **Web Platform for Anonymization**: Create a user-friendly web interface that allows users to easily anonymize their data.

### Phase 3: Integration with Popular Tools
- [x] **Jupyter Notebook and Google Colab Integration**: Ensure our system is compatible with Jupyter Notebook and Google Colab for wider accessibility.
- [x] **Docker and Docker Compose Deployment**: Implement Docker and Docker Compose to facilitate easy deployment and scaling of our application.

### Phase 4: Desktop Application
- [ ] **Desktop Application**: Develop a standalone desktop application for users who prefer a dedicated software solution.

### Phase 5: Advanced Algorithm Testing
- [ ] **Testing More Powerful Algorithms**: Experiment with more advanced algorithms to improve the efficiency and effectiveness of the anonymization process.

### Phase 6: Evaluation and Analysis
- [ ] **Evaluation of Original vs Anonymized Data**: Conduct thorough evaluations to ensure the integrity of the data post-anonymization.
- [ ] **Statistical Graph Generation**: Implement features for generating statistical graphs to visualize the effectiveness of our anonymization processes.

## Contributing

Contributions to NB-Anonymizer are welcome and appreciated. If you want to contribute, please:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

For more detailed information, please refer to the [CONTRIBUTING](CONTRIBUTING.md) file.

## License

NB-Anonymizer is licensed under the [MIT License](LICENSE).

## Contact

For support or any queries, feel free to contact us at [info@nextbrain.ai](mailto:info@nextbrain.ai).
