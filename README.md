## 1. Initialisez le docker-compose 
`docker-compose up`

## 2. Insérer les données dans la base de données mongo
`docker exec pyspark_notebook python3 ./work/load_db.py`


|               | Port  | Description                    |   |   |
|---------------|-------|-----------------------|---|---|
| Mongo-Express | 8081  | Interface Web MongoDB                      |   |   |
| MongoDB       | 27017 |                       |   |   |
| Hadoop-WebUI  | 9870  |                       |   |   |
| Hadoop-HDFS   | 9000  |                       |   |   |
| Streamlit     | 8501  | Business Intelligence |   |   |

## Credits & Licence
05/02/2021 - GPL3 Licence (Open Source)

# Team

**Noé ABDEL KALEK**  - *Developer*

**Geoffrey DAZELLE**  - *Developer*

**Robert KAYAT**  - *Developer*    

**Mohamed BOUROUCHE** - *Developer*