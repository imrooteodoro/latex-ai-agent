# LaTeX AI

LaTeX AI is an AI-powered tool that allows users to generate LaTeX documents from user inputs such as titles, content, themes, and images. The tool automatically creates structured LaTeX code for both articles and presentations, simplifying the creation of academic and professional documents.

## Features

- Automatic LaTeX document generation for articles and presentations.
- Support for image inclusion (formats: `.png`, `.jpg`, etc.).
- Customizable style and themes for `beamer` presentations and `article` documents.
- Generation of LaTeX files (`.tex`) and PDFs (`.pdf`).

## Technologies Used

- **Python 3.10+** - The primary language for the backend.
- **Flask** - Web framework for creating APIs and routes.
- **Gemini** - LaTeX content generation powered by AI.
- **LaTeX** - LaTeX code compilation to generate PDF documents.
- **Docker** - Containerization for easy development and production environment setup.

## Installation

Follow the steps below to set up the development environment.

### Prerequisites

Before you begin, ensure you have the following:

- **Python 3.10+** installed on your system.
- **Docker** (optional, but recommended for containerized environment).
- **TeX Live** installed for LaTeX compilation.
- **Gemini API Key** for generating LaTeX content using AI (explained below).

### Step 1: Clone the Repository
Clone this repository to your local environment:

```bash
        git clone https://github.com/yourusername/latex-ai.git
        cd latex-ai
```

### Step 2: Install Dependencies
```bash
        pip install -r requirements.txt
```
### Step 3: Set up LaTeX

- Ubuntu/Debian:

```bash
        sudo apt-get install texlive
```
- Macos:

```bash
    brew install --cask mactex
```

- Windows:
Download and install TeX Live from the official website: [TexLive](https://tug.org/texlive/)

### Step 4: Set up Gemini API Key

To use the AI functionality for generating LaTeX content, you need to configure your Gemini API key.

- Go to the Gemini platform and sign up or log in to obtain your API key.
- Create a `.env` file in the root of your project directory if it doesn't already exist.
- In the `.env` file, add the following line with your Gemini API key:

   ```env
   API_KEY=your_gemini_api_key_here

### Step 5: Docker Setup (Optional)

If you prefer running the project in a Docker container, you can build the image and run the container with:

```bash
docker build -t latex-ai .
docker run -p 5000:5000 latex-ai
```

### Step 6: Run the Project

Start the Flask development server:

```bash
        python3 app.py
```
This will start the server at: http://localhost:5000.
How to Use

-    Go to the project homepage in your browser: http://localhost:5000.
-    Fill in the necessary fields like title, name, content, and choose the document type (article or presentation).
-    Upload an image file if needed.
-    Click the "Generate Document" button.
-   The LaTeX document will be generated, and you can download the .tex file or the .pdf file.
[Screencast from 2025-01-04 15-52-40.webm](https://github.com/user-attachments/assets/9bf4315a-bf5c-4714-aabf-099f44486cce)

