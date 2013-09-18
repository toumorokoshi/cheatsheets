MSSQL Cheatsheet
================

Useful Commands
---------------

* GETDATE() : returns the current date in datetime format

Delete With Join
--------------
Example:

You can use joins in deletes like so:

..code:: mssql

    DELETE FROM {{T1}} 
        FROM {{T1}} as {{t1name}} 
        JOIN {{T2}} as {{t2name}}
        ON {{T1}}.Col = {{T2}}.Col
    
Examples
--------

* Alter a table: ALTER [TABLE] ALTER COLUMN [COLUMN_NAME] [TYPE] [NULL/NOT NULL]
