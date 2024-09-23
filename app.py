from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

# Route for the upload page
@app.route('/')
def index():
    return render_template('index.html')

# Handle CSV file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and file.filename.endswith('.csv'):
        # Save the file to /ec2-user/repo-automation
        upload_path = '/ec2-user/repo-automation/uploaded_file.csv'
        file.save(upload_path)
        return "File uploaded successfully!"
    return "Invalid file type. Please upload a CSV."

# Run the run.sh script
@app.route('/run_sh')
def run_sh():
    try:
        process = subprocess.Popen(['bash', '/ec2-user/repo-automation/run.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if process.returncode == 0:
            return "run.sh completed successfully!"
        else:
            return f"run.sh failed with error: {error.decode()}"
    except Exception as e:
        return f"Error running script: {str(e)}"

# Run the start.sh script
@app.route('/start_sh')
def start_sh():
    try:
        process = subprocess.Popen(['bash', '/ec2-user/repo-automation/start.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if process.returncode == 0:
            return "start.sh completed successfully!"
        else:
            return f"start.sh failed with error: {error.decode()}"
    except Exception as e:
        return f"Error running script: {str(e)}"

# Allow downloading the TAR file
@app.route('/download')
def download_file():
    tar_path = '/ec2-user/repo-automation/generated_file.tar'  # Adjust this to match your TAR file's name
    if os.path.exists(tar_path):
        return send_file(tar_path, as_attachment=True)
    return "TAR file not found!"

if __name__ == '__main__':
    app.run(debug=True)
