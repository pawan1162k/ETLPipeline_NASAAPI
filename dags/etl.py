from airflow import DAG
from airflow.decorators import task
from airflow.providers.http.operators.http import HttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import json


with DAG(
    dag_id = 'nasa_api',
    start_date=datetime(2024,1,1),
    schedule='@daily',
    catchup=False
)as dag:
    #Step 1 create the table in postgres
    @task
    def create_table():
        ##initialize the connection
        postgres_hook = PostgresHook(postgres_conn_id = "my_postgres_connection")
        ## SQL Query to create a table
        create_table_query = """
            CREATE TABLE IF NOT EXIST apod_data(
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                explanation TEXT,
                url TEXT,
                date DATE,
                media_type VARCHAR(50)
            );
        """ 
        
        ## EXECUTE THE TABLE CREATE QUERY 
        postgres_hook.run(create_table_query)
        
    #Step 2 Extract nasa api data (APOD) - Astronomy picture of day
    
    extract_apod = HttpOperator(
        task_id = "extract_apod", 
        http_conn_id='nasa_api', ##Connection id defined in airflow
        endpoint='planatory/apod', ##NASA api endpoint 
        method='GET', 
        data={"api_key": "{{conn.nasa_api.extra_dejson.api_key}}"}, ## use the api key from connection
        response_filter= lambda response: response.json(),
    )
    #Step 3 Transform the data 
    
    @task
    def transform_apod_data(response):
        apod_data = {
            'title': response.get('title', ''),
            'explanation': response.get('explanation', ''),
            'url': response.get('url', ''),
            'date': response.get('date', ''),
            'media_type': response.get('media_type', ''),
        }
        return apod_data


    #Step 4 Load the data in postgres
    @task
    def load_data_postgres(apod_data):
        ##initialize the postgres hook
        postgres_hook = PostgresHook(postgres_conn_id = "my_postgres_connection")
        
        #Define the SQL insert query
        insert_query = """
        INSERT INTO apod_data (title, explanation, url, date, media_type)
        VALUES (%s, %s, %s, %s, %s);
        """
        
        ## Execute the SQL Query 
        postgres_hook.run(insert_query, parameters=(
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type'],
        ))
        
    #Step 5 Verify the data - DBViewer
    verify =0
    
    
    ## Define the dependencies
    c= create_table()
    e = extract_apod()
    t = transform_apod_data()
    l = load_data_postgres()
    v = verify()