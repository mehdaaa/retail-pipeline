import os
from cosmos.config import ProfileConfig, ProjectConfig
from pathlib import Path

DBT_CONFIG = ProfileConfig(
    profile_name=os.getenv('DBT_PROFILE_NAME', 'retail'),
    target_name=os.getenv('DBT_TARGET_NAME', 'dev'),
    profiles_yml_filepath=Path(os.getenv('DBT_PROFILES_PATH', '/usr/local/airflow/include/dbt/profiles.yml'))
)

DBT_PROJECT_CONFIG = ProjectConfig(
    dbt_project_path=os.getenv('DBT_PROJECT_PATH', '/usr/local/airflow/include/dbt/')
)
