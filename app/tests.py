import psycopg2
import os

def get_connection(db_config):
    host = db_config.get("Host")
    port = db_config.get("Port")
    user_name = db_config.get("UserName")
    password = db_config.get("Password")
    database = db_config.get("DatabaseName")
    schema_name = db_config.get("SchemaName")
    print("postgres host : ", host, " and port : ", port, schema_name)
    error = ""
    try:
        connection = psycopg2.connect(host=host,
                                      port=port,
                                      database=database,
                                      user=user_name,
                                      password=password
                                      )
        if connection is not None:
            print("You're connected to database.")
            return connection, error
        else:
            return connection, error
    except Exception as error:
        print("Error while connecting to POSTGRESQL")
        return None, error



def SaveSampleImage():
    dir_path = os.path.realpath("app/static/images")
    lists = os.listdir(dir_path)
    i = 0

    config={
        "Host": "localhost",
        "Port": "5432",
        "UserName": "admin",
        "Password": "admin",
        "DatabaseName": "imagesearch",
        "SchemaName": "public"
    }
    conn, pErr = get_connection(config)
    print("Err ", pErr)
    cursor = conn.cursor()
    for i,feature_path in enumerate(lists):
        i = i+1
        file_name = feature_path.split(".")[0]
        Query = "INSERT INTO app_storedimage(id, name,image, img_feature_path) values("+str(i)+",'"+file_name+"','static/images/"+feature_path+"','static/features/"+file_name+".npy')"
        print("filename : ",Query)
        cursor.execute(Query)
        conn.commit()
        
    return None

if __name__ == '__main__':
    SaveSampleImage()