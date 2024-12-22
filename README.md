# Image Caption Generator

This project is an **Image Caption Generator** powered by the **BLIP model** for image-to-text generation. The **FastAPI backend** processes images and generates captions, while the **User Interface** lets users upload images and view captions seamlessly.

## Features
- Upload images (JPEG or PNG) for caption generation.
- Generate captions using the BLIP model (Salesforce/blip-image-captioning-large).
- Easy-to-use interface to upload images and view captions.

## Table of Contents
- [Tech Stack](#tech-stack)
- [Installation](#installation)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)

## Tech Stack

### Backend
- **FastAPI**: For creating the RESTful API.
- **PyTorch**: For model handling.
- **Transformers**: For using the BLIP model for image captioning.
- **Pillow**: For image processing.

### Frontend
- **HTML**: Structure of the web page.
- **CSS**: Styling the frontend.
- **JavaScript**: Handling image upload and interacting with the backend.

## Installation

### Frontend

1. Clone the frontend repository:
   ```bash
   git clone https://github.com/amMistic/image-caption-project.git
   cd image-caption-project/frontend
   ```

2. Install dependencies (for local development, no external packages are required for frontend):
   - The frontend only relies on the assets you have already created (e.g., the `style.css`, `main.js`).
   - Ensure your files are placed correctly in the `frontend` folder as mentioned in the project structure.

3. Open `index.html` in your browser to view the frontend interface.

### Backend

1. Clone the backend repository (or the same repo if it's one):
   ```bash
   git clone https://github.com/amMistic/image-caption-project.git
   cd image-caption-project/backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .ic
   ```

3. Activate the virtual environment:
   - On **Windows**:
     ```bash
     .ic\Scripts\activate
     ```
   - On **Linux/macOS**:
     ```bash
     source .ic/bin/activate
     ```

4. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Install **PyTorch** and **Transformers** (if not installed automatically):
   ```bash
   pip install torch transformers
   ```

6. Verify the installation of PyTorch:
   ```bash
   python -c "import torch; print(torch.__version__)"
   ```

## Running the Application

### Backend
1. In your terminal, navigate to the backend directory and start the FastAPI app using `uvicorn`:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The backend will run on `http://localhost:8000`.

   You can test the API directly by navigating to `http://localhost:8000/docs`, which will show an interactive Swagger UI for the API.

### Frontend
1. Open the `index.html` file in a browser to load the frontend.

2. Use the "Drag and Drop" area or click to upload an image.

## Usage

1. On the frontend, drag and drop an image (JPEG or PNG), or click to upload an image from your local machine.
2. The backend will process the image and generate a caption using the BLIP model.
3. The caption will appear below the upload area once generated.

## Contributing

Feel free to fork the repository, submit issues, and create pull requests. Contributions are always welcome!

Steps for contributing:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a Pull Request.
