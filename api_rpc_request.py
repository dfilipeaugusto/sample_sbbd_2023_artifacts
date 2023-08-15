import json
from datetime import datetime
import snowflake.connector

def lambda_handler(event, context):
    
    body = json.loads(event['body'])
    
    query_id = body.get('id') or '51e1c39f-13f5-4d59-a540-e356b46580a1'
    query_description = body.get('description') or "''"
    query_created_at = body.get('created_at') or "''"
    query_logs = json.dumps(body.get('logs')) or "''"
    query_epoch = body.get('epoch') or "null"
    
    query_text = f"INSERT INTO raw_link(id, description, created_at, logs, epoch) VALUES ('{query_id}', '{query_description}', '{query_created_at}', '{query_logs}', {query_epoch})"
    
    print("Descrição:", body['description'])
    print("Horário:", datetime.fromtimestamp(body['created_at']))
    print("Logs:", body['logs'])
    print("Época:", body['epoch'])
    print("Query:", query_text)
    
    conn = snowflake.connector.connect(
            user='user_xpto',
            password='pass_xpto',
            account='sf_account_xpto',
            warehouse='compute_wh',
            database='integra_xpto',
            schema='public'
    )
        
    conn.cursor().execute(query_text)
        
    conn.close()
    
    return {
        'statusCode': 200
    }
