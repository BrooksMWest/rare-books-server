import sqlite3
import json
from models import Post

# Sample data (could be replaced with data from DB)
POSTS = [
  {
    "id": 1,
    "user_id": 1,
    "title": "The Power of Habit: Why We Do What We Do",
    "publication_date": "2024-10-01",
    "image_url": "https://example.com/the-power-of-habit.jpg",
    "content": "A deep dive into how habits work and how we can change them for a better life.",
    "approved": 1  
  },
  {
    "id": 2,
    "user_id": 2,
    "title": "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones",
    "publication_date": "2024-09-15",
    "image_url": "https://example.com/atomic-habits.jpg",
    "content": "A practical guide on how to form lasting habits and make lasting changes in your life.",
    "approved": 1
  },
  {
    "id": 3,
    "user_id": 3,
    "title": "Sapiens: A Brief History of Humankind",
    "publication_date": "2024-08-10",
    "image_url": "https://example.com/sapiens.jpg",
    "content": "Explore the history of humankind and how we evolved to dominate the world.",
    "approved": 1  
  }
]


def get_all_posts():
    """Fetch all posts from the database."""
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            id,
            user_id,
            title,
            publication_date,
            image_url,
            content,
            approved
        FROM Post
        """)

        # Initialize an empty list to hold all post representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate through dataset to build Post instances
        for row in dataset:
            post = Post(row['id'], row['user_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
            posts.append(post.__dict__)  # Add each post to the list

    return posts


def get_single_post(id):
    """Fetch a single post from the database by its ID."""
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            id,
            user_id,
            title,
            publication_date,
            image_url,
            content,
            approved
        FROM Post
        WHERE id = ?
        """, (id,))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create Post instance from the data
        if data:
            post = Post(data['id'], data['user_id'], data['title'], data['publication_date'], data['image_url'], data['content'], data['approved'])
            return post.__dict__  # Return the post dictionary representation
        else:
            return None  # If no post was found

    
def create_post(new_post):
    """Insert a new post into the database."""
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Post (user_id, title, publication_date, image_url, content, approved)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (new_post['user_id'], new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved']))

        # Get the last inserted row id (primary key)
        new_post['id'] = db_cursor.lastrowid

    return new_post


def delete_post(id):
    """Delete a post from the database by its ID."""
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Post
        WHERE id = ?
        """, (id,))


def update_post(id, updated_post):
    """Update an existing post's details in the database."""
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Post
        SET
            title = ?,
            publication_date = ?,
            image_url = ?,
            content = ?,
            approved = ?
        WHERE id = ?
        """, (updated_post['title'], updated_post['publication_date'], updated_post['image_url'], updated_post['content'], updated_post['approved'], id))

        # Check if any rows were affected
        rows_affected = db_cursor.rowcount

    return rows_affected > 0  # Return True if the post was updated, otherwise False