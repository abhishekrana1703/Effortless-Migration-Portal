# Effortless-Migration-Portal

/your_project_directory
│
├── app.py                     # Your Flask application
├── templates                  # Directory for HTML templates
│   └── index.html            # The main HTML file for the UI
│
├── /ec2-user/repo-automation  # Your working directory on the EC2 instance
│   ├── run.sh                 # Your run.sh script
│   ├── start.sh               # Your start.sh script
│   ├── uploaded_file.csv       # The uploaded CSV file (will be generated)
│   └── generated_file.tar      # The generated TAR file (will be created)
│
└── requirements.txt           # List of dependencies (if needed)


# Steps to Run Your Flask App

**1. Set Up the Environment:**

If you haven’t already, create a Python virtual environment (optional but recommended):


cd /your_project_directory
python3 -m venv venv
source venv/bin/activate


**2.Install Flask:**

If you have a requirements.txt file, you can install Flask and other dependencies using:

pip install -r requirements.txt

**3.Run the Flask Application:**

python app.py


**4.Access the Application:**

Open your web browser and go to http://localhost:5000 (or the appropriate IP address if you’re accessing it from a different machine).
