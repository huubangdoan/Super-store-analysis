from sqlalchemy import create_engine
import dotenv
import os 
import pandas as pd
dotenv.load_dotenv()
engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@localhost:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
df=pd.read_csv(r"data\raw\SampleSuperstore.csv")
df.to_sql(name="super_store_table", con=engine, if_exists="replace", index=False)
