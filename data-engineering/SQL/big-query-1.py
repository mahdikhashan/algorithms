from google.cloud import bigquery

client = bigquery.Client()

dataset_ref = client.dataset('hacker_news', project='bigquery-public-data')
dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))

for table in tables:
    print(table.table_id)

table_ref = dataset_ref.table("full")

table = client.get_table(table_ref)

# print(table.schema)

print(client.list_rows(table, max_results=5).to_dataframe())
print(client.list_rows(table, selected_fields=table.schema[:4], max_results=5).to_dataframe())
