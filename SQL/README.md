# SQL exercises 

# How to start 

You can write queries in VS Code 
Setup: https://code.visualstudio.com/docs/languages/tsql

# Docker MS SQL server 

docker pull mcr.microsoft.com/mssql/server:2019-latest

# Launch SQL Server Image

docker run --name ms_sql_server -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=123Tom!' -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest

# Connect from VS CODE

1) Open new file

1) View -> Command Pallet -> MS SQL: Connect 

2) Set language to SQL

3) Create Connection Profile 

4) 127.0.0.1

5) user name and password (password needs to be 8 characters or longer)

6) add connection profile name 

# You can now write sql in VS CODE 

SELECT * FROM sys.dm_os_host_info


# Option 2 

pip install ipython-sql

## In your jupyter notebook 

%load_ext sql 

%sql sqlite://


# SQL Basics

```sql
SELECT * 
FROM tablename t
INNER JOIN tablename2 f 
    ON t.id = f.id 
GROUP BY t.id
HAVING count()
```

```sql
SELECT * 
FROM tablename t
WHERE (t.title='TITLE' AND t.start_date > '2022-10-31') 
    OR (t.title='TITLE 2')
```

```sql
SELECT * 
FROM tablename t 
INNER JOIN 
    ON
WHERE
```

```sql
SELECT *
FROM tablename t
WHERE ( SELECT f.column1 
        FROM tablename2 f 
        WHERE a.something = t.something)
```


