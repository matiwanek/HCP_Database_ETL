# DROP TABLES
doctors_table_drop = "DROP TABLE IF EXISTS doctors"
# CREATE TABLES

doctors_table_create = (
    """CREATE TABLE IF NOT EXISTS doctors(
                        id int PRIMARY KEY, 
                        lastName varchar,
                        firstName varchar,
                        isActive boolean,
                        Role varchar,
                        Specialty varchar,
                        HCO_ID int,
                        Canton varchar,
                        Street varchar,
                        Zip_Code varchar)
                        """)

# INSERT DATA
doctors_table_insert = (
    """INSERT INTO doctors (
                id,
                lastName,
                firstName,
                isActive,
                Role,
                Specialty,
                HCO_ID,
                Canton,
                Street,
                Zip_Code) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """)

# FIND Doctor

doctors_select = ("""
    SELECT d.firstName, d.lastName, d.Specialty
    FROM doctors d
    JOIN artists a ON s.artist_id = a.artist_id
    WHERE d.Canton = 'Bern';
""")
