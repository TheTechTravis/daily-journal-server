import json
from models import JournalEntry
import sqlite3


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            je.id,
            je.concept,
            je.entry,
            je.date,
            je.mood_id
        FROM journal_entries je
        """)

        # Initialize an empty list to hold all journal entry representations
        journal_entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an journal_entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # JournalEntry class.
            journal_entry = JournalEntry(row['id'], row['concept'], row['entry'],
                                         row['date'], row['mood_id'])

            journal_entries.append(journal_entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(journal_entries)


def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            je.id,
            je.concept,
            je.entry,
            je.date,
            je.mood_id
        FROM journal_entries je
        WHERE je.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        journal_entry = JournalEntry(data['id'], data['concept'], data['entry'],
                                     data['date'], data['mood_id'])

        return json.dumps(journal_entry.__dict__)


def get_animals_by_location(location):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.location_id = ?
        """, (location, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(
                row['id'], row['name'], row['breed'], row['status'],
                row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def get_animals_by_status(status):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.status = ?
        """, (status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(
                row['id'], row['name'], row['breed'],
                row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM journal_entries
        WHERE id = ?
        """, (id, ))
