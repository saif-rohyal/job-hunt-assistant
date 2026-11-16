# Job Hunt Assistant

### AI-Powered Job Search & Application Management

**Job Hunt Assistant** is a Python-based AI application designed to assist users throughout the job search and application process. Built with **CrewAI, Google Gemini, Streamlit, and the USAJOBS API**, the project uses specialized AI agents to support job description analysis, resume assistance, professional messaging, and application tracking.

The goal is to make job searching more organized, efficient, and AI-assisted.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Architecture](#project-architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Environment Configuration](#environment-configuration)
- [Running the Application](#running-the-application)
- [Core Components](#core-components)
- [Security](#security)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## Overview

Finding suitable jobs and preparing effective applications can be time-consuming. Job Hunt Assistant aims to simplify parts of this process through AI-powered assistance and a modular multi-agent architecture.

The application combines specialized Python modules and AI agents to support different stages of a job application workflow.

It integrates:

- **CrewAI** for AI agent orchestration.
- **Google Gemini** for language-model capabilities.
- **Streamlit** for the interactive application interface.
- **USAJOBS API** for job-related data integration.
- **CSV-based tracking** for maintaining application records.

The application is developed in Python with a modular structure to support maintainability and future enhancements.

## Key Features

### 1. Job Description Analysis

The job description analyst agent is designed to assist with analyzing job descriptions and understanding relevant job requirements.

### 2. Resume Assistance

The resume and cover-letter agent supports resume-related assistance and application document preparation.

### 3. Professional Messaging

The messaging agent helps generate professional communication relevant to job applications.

### 4. Job Search Integration

The USAJOBS API integration provides a connection to job-related information from the USAJOBS platform.

### 5. Application Tracking

The tracking modules and application log support recording and organizing job application activity.

### 6. Multi-Agent Architecture

The project uses CrewAI to organize specialized agents and coordinate AI-assisted tasks.

### 7. Interactive User Interface

The Streamlit application provides a user-facing interface for interacting with the project.

---

## Technology Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core programming language       |
| CrewAI        | Multi-agent orchestration       |
| Google Gemini | Large language model            |
| Streamlit     | Interactive web interface       |
| USAJOBS API   | Job search data integration     |
| Python-dotenv | Environment variable management |
| CSV           | Application data storage        |

---

## Project Architecture

The project follows a modular architecture in which individual components handle specific responsibilities.

### Architecture Overview

```text
                 USER
                   |
                   v
          STREAMLIT INTERFACE
            streamlit_app.py
                   |
                   v
             ORCHESTRATOR
            orchestrator.py
                   |
          +--------+--------+
          |        |        |
          v        v        v
       JOB JD   RESUME   MESSAGING
      ANALYST    AGENT     AGENT
          |        |        |
          +--------+--------+
                   |
                   v
             GOOGLE GEMINI
                CREWAI
                   |
          +--------+--------+
          |                 |
          v                 v
      USAJOBS API       APPLICATION
      INTEGRATION        TRACKING
```

*Conceptual overview of the project's main components.*

---

## Project Structure

```text
job_hunt_assistant/
│
├── agents/
│   ├── jd_analyst.py
│   ├── messaging_agent.py
│   └── resume_cl_agent.py
│
├── data/
│   ├── applications_log.csv
│   └── sample_resume.txt
│
├── utils/
│   ├── __init__.py
│   ├── config.py
│   ├── llm.py
│   ├── tracking.py
│   └── usajobs_api.py
│
├── config.py
├── orchestrator.py
├── streamlit_app.py
├── tracking.py
├── usajobs_api.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### Directory Description

| File / Directory       | Responsibility                       |
| ---------------------- | ------------------------------------ |
| `agents/`              | Specialized AI agent modules         |
| `jd_analyst.py`        | Job description analysis agent       |
| `resume_cl_agent.py`   | Resume and cover-letter assistance   |
| `messaging_agent.py`   | Professional messaging agent         |
| `utils/`               | Shared utilities and configuration   |
| `utils/llm.py`         | Gemini language model initialization |
| `utils/config.py`      | Environment configuration            |
| `utils/tracking.py`    | Application tracking utilities       |
| `utils/usajobs_api.py` | USAJOBS API utilities                |
| `orchestrator.py`      | Coordinates application workflow     |
| `streamlit_app.py`     | Streamlit application interface      |
| `tracking.py`          | Application tracking functionality   |
| `usajobs_api.py`       | USAJOBS API integration              |
| `data/`                | Application data and sample resume   |

---

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Make sure the following software is installed:

- Python 3.11 or a compatible supported version.
- pip (Python package manager).
- Git.
- A Google Gemini API key.
- USAJOBS API credentials for the job-search integration.

### 1. Clone the Repository

```bash
git clone https://github.com/saif-rohyal/job-hunt-assistant.git
```

Navigate to the project directory:

```bash
cd job-hunt-assistant
```

### 2. Create a Virtual Environment

On Windows:

```powershell
python -m venv venv
```

Activate the environment:

```powershell
venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the dependencies listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

---

## Environment Configuration

The application uses environment variables to manage API credentials.

Create a `.env` file in the project's root directory.

Use the following template:

```env
USAJOBS_API_KEY=your_usajobs_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder values with your own API credentials.

### API Configuration

| Environment Variable | Description                            |
| -------------------- | -------------------------------------- |
| `USAJOBS_API_KEY`    | API credential for USAJOBS integration |
| `GEMINI_API_KEY`     | API credential for Google Gemini       |

**Important:** Never upload your actual `.env` file or API credentials to GitHub.

The `.env.example` file should contain placeholders only.

---

## Running the Application

After installing dependencies and configuring the environment variables, launch the Streamlit application:

```bash
streamlit run streamlit_app.py
```

Streamlit will display a local URL in the terminal.

Open that URL in your browser to access the application.

---

## Core Components

### CrewAI Agents

The project organizes AI-related responsibilities into separate agent modules:

- **Job Description Analyst:** Supports job description analysis.
- **Resume/Cover Letter Agent:** Supports resume and cover-letter assistance.
- **Messaging Agent:** Supports professional messaging.

### Language Model

The project initializes a Google Gemini model through CrewAI's `LLM` interface.

The configured model is:

```text
gemini/gemini-2.5-flash
```

### USAJOBS Integration

The USAJOBS integration is implemented through dedicated Python modules and uses API credentials supplied through environment variables.

### Application Tracking

Application tracking functionality is organized into dedicated tracking modules, with a CSV file available for application records.

---

## Security

Security and responsible credential management are important parts of this project.

Follow these practices:

- Keep API keys inside environment variables.
- Never commit `.env` files.
- Never expose API credentials in source code.
- Exclude virtual environments from version control.
- Exclude Python cache files.
- Avoid publishing personal resumes or confidential application records.
- Review files before making a public GitHub commit.

---

## Future Improvements

Potential areas for future development include:

- Advanced job-to-resume matching.
- Automated resume optimization.
- Improved job recommendation capabilities.
- Enhanced application analytics and reporting.
- Additional job platform integrations.
- More advanced AI agent collaboration.
- Application status monitoring.
- Improved user experience and dashboard functionality.

---

## Contributing

Contributions, suggestions, and feedback are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test your changes.
5. Submit a pull request with a clear description.

```bash
git checkout -b feature/your-feature-name
```

---

## Author

**Saif Ullah**

- GitHub: [@saif-rohyal](https://github.com/saif-rohyal)
- Repository: [Job Hunt Assistant](https://github.com/saif-rohyal/job-hunt-assistant)

---

\<p align="center">   \<strong>Job Hunt Assistant\</strong>\<br>   Making the job search process smarter with AI. \</p>
