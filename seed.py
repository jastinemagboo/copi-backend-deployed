# seed.py
from models.post_model import Post
from extensions import db
from datetime import datetime
import uuid

def run_seed():
    from app import app

    with app.app_context():
        if not Post.query.first():
            post = Post(
                id=uuid.uuid4(),
                title="Welcome, What is your favorite coffee?",
                content="Coffee plays an important role in helping people cope with life's challenges. Share your story: How has coffee helped you cope during tough times?",
                created_at=datetime.now()
            )
            db.session.add(post)
            db.session.commit()
            print("Seed data added.")
        else:
            print("Seed skipped — there's already existing data.")
