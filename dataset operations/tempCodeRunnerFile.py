import boto3
import json

kinesis_client = boto3.client('kinesis', region_name='eu-north-1')

with open('dataset operations/reduced_data.json', 'r', encoding='utf-8') as file:
    for idx, line in enumerate(file):
        line = line.strip()
        if line:
            record = json.loads(line)
            response = kinesis_client.put_record(
                StreamName='SmartEnergyFlowStream',
                Data=json.dumps(record),
                PartitionKey=str(idx)
            )
            print(f"Gönderildi: {record} → Response: {response}")
