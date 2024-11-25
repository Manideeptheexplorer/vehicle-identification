# Vehicle Recognition Web Application

This is a Django-based web application that detects static and dynamic vehicle number plates using **PyTesseract** (OCR). The system also identifies the state to which the vehicle belongs. The application is styled with **Bootstrap** for a responsive and user-friendly interface.

---

## Features

- **Home Page**: An introductory page that provides an overview of the application.
- **User Authentication**:
  - **Register**: Create a new user account.
  - **Login**: Securely log in to your account.
- **Image Upload**: Upload static images of vehicle number plates for recognition.
- **Video Upload**: Upload videos to detect dynamic number plates.
- **Results Page**: Displays the detected number plate and the state of registration.
- **Services Page**: Highlights the functionalities and capabilities of the application.
- **Contact Page**: Contact form for users to reach out for support or inquiries.

---

## Technologies Used

- **Backend**: Django Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **OCR**: PyTesseract for text recognition
- **Database**: SQLite (`dbsqlite3`)

---

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or above
- pip (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/Manideeptheexplorer/vehicle-identification.git
cd vehicle-identification/vehiclerecognition
