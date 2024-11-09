import sqlite3
import json
from models import Subscriptions


def get_all_subscriptions():
    # Open a connection to the database
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.follower_id,
            a.author_id,
            a.created_on
        FROM Subscriptions a
        """)

        # Initialize an empty list to hold all subscriptions representations
        subscriptions = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create subscription instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Subscription class above.
            subscription = Subscriptions(row['id'], row['follower_id'], row['author_id'], row['created_on'])

            subscriptions.append(subscription.__dict__) # see the notes below for an explanation on this line of code.

    return subscriptions
  
def get_single_subscription(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
            SELECT
            a.id,
            a.follower_id,
            a.author_id,
            a.created_on
        FROM Subscriptions a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an subs instance from the current row
        subscription = Subscriptions(data['id'], data['follower_id'], data['author_id'], data['created_on'])

        return subscription.__dict__
    
def create_subscription(sub):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Subscriptions 
            ( follower_id, author_id, created_on )
        VALUES
            ( ?, ?, ?);
        """, (sub['follower_id'],
              sub['author_id'], sub['created_on'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        sub['id'] = id


    return sub
