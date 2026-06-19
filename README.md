# Hospital Appointment Data Cleaning and MySQL Integration

## Project Overview

This project demonstrates how to clean hospital appointment data using Python and store the cleaned dataset in a MySQL database. The dataset is processed using Pandas, unnecessary columns are removed, column names are standardized, and the cleaned records are inserted into a MySQL table for further analysis.

## Features

* Connects to MySQL using Python.
* Creates a new database automatically if it does not exist.
* Reads cleaned appointment data from a CSV file.
* Renames inconsistent column names.
* Selects only the required columns.
* Creates a MySQL table for storing appointment records.
* Inserts data into the database efficiently using batch insertion.
* Retrieves and displays sample records for verification.

## Technologies Used

* Python
* Pandas
* MySQL
* MySQL Connector for Python

## Dataset Columns

The following columns are stored in the database:

* patientid
* gender
* age
* neighbourhood
* hypertension
* diabetes
* alcoholism
* handicap
* sms_received
* no_show
* waiting_days

## Database Structure

### Database Name

cleaned_appointments

### Table Name

cleaned_appointments

| Column        | Data Type    |
| ------------- | ------------ |
| patientid     | BIGINT       |
| gender        | VARCHAR(10)  |
| age           | INT          |
| neighbourhood | VARCHAR(100) |
| hypertension  | INT          |
| diabetes      | INT          |
| alcoholism    | INT          |
| handicap      | INT          |
| sms_received  | INT          |
| no_show       | INT          |
| waiting_days  | INT          |

## Installation

1. Install Python dependencies:

```bash
pip install pandas mysql-connector-python
```

2. Ensure MySQL Server is running.

3. Place the cleaned CSV file in the project directory:

```text
cleaned_appointments.csv
```

4. Update MySQL credentials in the script if required.

5. Run the script:

```bash
python app.py
```

## Workflow

1. Connect to MySQL Server.
2. Create the database if it does not exist.
3. Load the cleaned CSV dataset.
4. Rename inconsistent column names.
5. Select relevant features.
6. Create the database table.
7. Insert all records into MySQL.
8. Display sample records to verify successful insertion.

## Sample Output

```text
(123456789, 'F', 25, 'CENTRO', 0, 0, 0, 0, 1, 0, 5)
(987654321, 'M', 45, 'JARDIM', 1, 0, 0, 0, 0, 1, 2)
```

## Future Improvements

* Add exception handling.
* Prevent duplicate record insertion.
* Build a dashboard for appointment analysis.
* Perform predictive analytics on patient no-show behavior.

## Author

Fathima Safa

