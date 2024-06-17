from google.cloud import bigquery

client = bigquery.Client()

dataset_ref = client.dataset("openaq", project='bigquery-public-data')
dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))

for table in tables:
    print(table.table_id)

table_ref = dataset_ref.table("global_air_quality")
table = client.get_table(table_ref)

print(table.schema)
print(client.list_rows(table, max_results=5).to_dataframe())

query = """
        SELECT city
        FROM `bigquery-public-data.openaq.global_air_quality`
        WHERE country = 'US'
        """

query_job = client.query(query)

us_cities = query_job.to_dataframe()
print(us_cities.city.value_counts().head())
