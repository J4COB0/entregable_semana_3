from flask import Flask
from flask_api import status
import pandas as pd

app = Flask(__name__)
# DEFINING THE URL
URL = 'https://docs.google.com/spreadsheets/d/1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU/export?format=csv&id=1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU&gid=135007174'

@app.route('/')
def index():
    """
    This function handling the operations to do when the route is the home page
    """
    # RETURNING A STATUS WITH THE SERVER RUNNING
    return {'status': 'Server is running'}, status.HTTP_200_OK

@app.route('/read')
def read():
    """
    This function handling the operations to do when the route is read
    it read a spreadsheet by a URL next it return a value with the amount of students in this spreadsheet
    """
    # USING PANDAS READ A CSV BY A URL
    df = pd.read_csv(URL)
    # THE NUMBER OF STUDENTS IS EQUAL TO THE LENGTH OF THE ARCHIVE
    number_of_students = len(df)

    # RETURNING A STATUS SUCCESS IN THE HOME PAGE
    return {'number of students': number_of_students}, status.HTTP_200_OK

# HOST AND PORT CONFIGURATION
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)