from datetime import datetime
from extensions import db  # ✅ not from app
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Post(db.Model):
    __tablename__ = 'copi_posts'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Post {self.title}>"
