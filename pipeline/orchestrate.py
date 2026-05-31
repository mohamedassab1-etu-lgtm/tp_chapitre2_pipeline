from dagster import job, op
import os

@op
def ingest():
    os.system("python pipeline/ingest.py")

@op
def validate(dependency):
    os.system("python pipeline/validate.py")

@op
def transform(dependency):
    os.system("cd dbt_pipeline && dbt run --profiles-dir .")

@op
def test_data(dependency):
    os.system("cd dbt_pipeline && dbt test --profiles-dir .")

@job
def ventes_pipeline():
    test_data(transform(validate(ingest())))
