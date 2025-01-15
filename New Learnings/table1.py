# Obter o esquema da tabela
table_ref = dataset_ref.table('crime')
table = client.get_table(table_ref)

# Contar colunas com tipo TIMESTAMP
timestamp_count = len([field for field in table.schema if field.field_type == 'TIMESTAMP']) #run this to find out the number of columns with TIMESTAMP

print(f"Número de colunas com TIMESTAMP: {timestamp_count}")


'''OBS'''

# table.schema is a list of schema fields. Each field is represented by a SchemaField object. --> therefore use this to get the schema of the table, schema is english for structure!