from setuptools import find_packages, setup

setup(
    name="dagster_dbt_tutorial",
    packages=find_packages(),
    install_requires=["dagster", "duckdb", "dagster-duckdb", "dagster-dbt", "dbt-core", "dbt-duckdb", "pandas", "pytest", "setuptools"],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
