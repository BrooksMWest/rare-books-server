import sqlite3
import json
from models import Comment
COMMENTS = [
    {
      "id": 1,
      "author_id":1,
      "post_id":1,
      "content":"This old book totally rules."
    },
    {
      "id": 2,
      "author_id":2,
      "post_id":2,
      "content":"This new book sucks so bad."
    },
    {
      "id": 3,
      "author_id":3,
      "post_id":3,
      "content":"This new book is terrible."
    }
]

def get_all_comments():
    # Open a connection to the database
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.author_id,
            a.post_id,
            a.content
        FROM Comments a
        """)

        # Initialize an empty list to hold all animal representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

        # Create an animal instance from the current row
            comment = Comment(row['id'], row['author_id'], row['post_id'], row['content'])

        # Add the dictionary representation of the animal to the list
            comments.append(comment.__dict__)

    return comments

# Function with a single parameter
def get_single_comment(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.author_id,
            a.post_id,
            a.content
        FROM Comments a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        comment = Comment(data['id'], data['author_id'], data['post_id'],
                            data['content'])

        return comment.__dict__

def create_comment(new_comment):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( content )
        VALUES
            ( ?, ?, ? );
        """, (new_comment['author_id'],
              new_comment['post_id'], new_comment['content'] ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the comment dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id


    return new_comment

def delete_comment(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))

def update_comment(id, new_comment):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comments
            SET
                content = ?
        WHERE id = ?
        """, (new_comment['content'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    # return value of this function
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
