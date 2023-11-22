# Documentation about DB Module

## Requirements

Install library to use MySQL in python.
- `mysql-connector`
- `mysql-connector-python`

```
$ (venv) python -m install mysql-connector mysql-connector-python
```

## DB Connector (`db_connector.py`)

### Init
Create connector instance
```
connector = Connector(
    host="IP_ADDRESS_TO_DATABASE",
    username="USERNAME",
    password="PASSWORD",
    database="DATABASE_NAME"
)
```
### Send data
Send(Insert) data to specific table in database.
```
connector.send(
    "TABLE_NAME",
    "ARGUMENT_1",
    "ARGUMENT_2",
    "ARGUMENT_3",
    ...
)
```

### Getting data
Get(Select) last data(sorted in descending order of time) from specific table in database.  
`return_value` is list type.
```
return_value = connector.get("TABLE_NAME", LIMITS)
```

### Delete rows 
Delete with specific id and table from database
```
connector.delete("TABLE_NAME", ID)
```

### Close
Close database and handler(cursor)
```
connector.close()
```