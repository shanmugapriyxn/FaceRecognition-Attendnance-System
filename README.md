# Face Recognition Attendance System

This is a Python-based Face Recognition Attendance System that uses OpenCV and KNN to recognize faces in real-time and mark attendance. A simple web interface built using Streamlit displays live updates from the attendance CSV.

---

## Features

- Face recognition using webcam and KNN classifier
- Voice feedback when attendance is marked
- Auto-generation of date-wise attendance CSV files
- Web dashboard to view attendance in real-time (auto-refreshes every 5 seconds)
- Includes reset functionality to clear face data
- Designed for small-scale, offline attendance systems (e.g., classrooms, labs)

---

## Technologies Used

- Python
- OpenCV
- scikit-learn (KNN)
- Streamlit
- Pandas
- win32com (for voice feedback)
- Pickle (to store face and name data)

---

## Project Structure

