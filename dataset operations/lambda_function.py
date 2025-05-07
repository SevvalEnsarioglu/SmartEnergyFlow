import json
import boto3
import base64
import decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SmartEnergyFlowDB')

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        print("Payload:", payload)
        
        try:
            data = json.loads(payload, parse_float=decimal.Decimal)
        except json.JSONDecodeError:
            print("JSON çözümleme hatası:", payload)
            continue
        
        try:

            table.put_item(Item={
                'id': data['time'],
                'Garage door': data['Garage door'],
                'Well': data['Well'],
                'Furnace': data['Furnace'],
                'Kitchen': data['Kitchen'],
                'Living room': data['Living room'],
                'Home office': data['Home office'],
                'gen': data['gen'],
                'Microwave': data['Microwave'],
                'hour': data['hour'],
                'Fridge': data['Fridge'],
                'Dishwasher': data['Dishwasher'],
                'dewPoint': data['dewPoint'],
                'use': data['use']
            })
            print(f"Başarıyla eklendi: {data['time']}")
        except Exception as e:
            print(f"DynamoDB Error: {e}")
    
    return {'statusCode': 200, 'body': 'Tüm kayıtlar başarıyla işlendi'}
