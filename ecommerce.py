import pandas as pd
import sqlite3

def run_etl():
    # 1. Extraction 
    print("Extracting data")
    file_path = 'ecommerce_sales_analytics_5000.csv'
    df = pd.read_csv(file_path)
    
    print(f"successfully reading data: {df.shape}")
    
    # 2. عرض أول 3 صفوف للتأكد
    print("\n Sample from data")
    print(df.head(3))
    
    # 3. عرض معلومات الأعمدة وأنواع البيانات
    print("\n colomn's Data")
    print(df.info())

    print("\n--- 2. Transformation Phase ---")

    missing_values = df.isnull().sum().sum()

    print(f"Total missing values: {missing_values}")

    if missing_values > 0:
            df = df.dropna()
            print("Done cleaning missing values")

    print("Done transfomation")

    print("\n--- 3. Loading Phase ---")
    output_path = 'cleaned_ecommerce_sales.csv'
    df.to_csv(output_path, index=False)
    print(f"Done saving : {output_path}")

    print("\n--- 3. Loading Phase ---")

    db_name = "ecommerce_warehouse.db"
    conn = sqlite3.connect(db_name)

    table_name = "sales_data"
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    print(f"Successfully loaded and stored data into table '{table_name}' inside database '{db_name}'!")

    conn.close()

if __name__ == "__main__":
    run_etl()



    
   