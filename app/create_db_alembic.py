import alembic.config
import alembic.command

# Set the database connection string
DATABASE_URI = "postgresql://user:password@localhost:5432/database_name"

# Set the path to the alembic configuration file
ALEMBIC_CONFIG = "alembic.ini"

# Set the path to the alembic scripts directory
ALEMBIC_SCRIPT_LOCATION = "alembic/versions"

def create_database():
    # Load the alembic configuration
    alembic_config = alembic.config.Config(ALEMBIC_CONFIG)

    # Set the database connection string in the alembic configuration
    alembic_config.set_main_option("sqlalchemy.url", DATABASE_URI)

    # Create the database
    alembic.command.upgrade(alembic_config, "head")

if __name__ == "__main__":
    create_database()
