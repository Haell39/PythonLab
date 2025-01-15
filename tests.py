# Obter o esquema da tabela
table_ref = dataset_ref.table('crime')
table = client.get_table(table_ref)

# Contar colunas com tipo TIMESTAMP
timestamp_count = len([field for field in table.schema if field.field_type == 'TIMESTAMP'])

print(f"Número de colunas com TIMESTAMP: {timestamp_count}")
