from google.cloud import bigquery

# Create a BigQuery client
client = bigquery.Client()

# Construct a reference to the "hacker_news" dataset
dataset_ref = client.dataset("hacker_news", project="igquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# List all tables in the dataset
tables = client.list_tables(dataset)

# Print the names of the tables in the dataset ("hacker_news")
for table in tables:
    print(table.table_id)