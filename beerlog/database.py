from sqlmodel import create_engine
from config import settings
import models

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)
