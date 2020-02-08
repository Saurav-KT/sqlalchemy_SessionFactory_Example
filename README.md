# SqlAlchemy SessionFactory Example with postgres database
 Sql Alchemy ORM example with file and postgres database using python flask framework
 
 following instructions needs to be followed in order to test the API
 
1.go to common folder>base.py change to database connection string
2. Table in database will be created automatically since sqlalchemy being used as ORM

Note-This set of functionality are tested with Postgres database


4.POST Api /api/readwritelog/writelog pass pramater in below format

[{
"flag":"2",
"logMsg":"new open account request has been processed",
"ipAddress":"127.45.67.89"
},{
"flag":"2",
"logMsg":"new temporary account open request has been processed",
"ipAddress":"127.80.67.79"
}]

Note: pass flag 2 if you wish to write log in databse;Pass flag 1 if you wish to write log in storage txt file.

5.POST Api /api/readwritelog/readlog pass pramater in below format

{"flag":"1","searchkeyword":"processed"}

Note: pass flag 2 if you wish to read the logs with search keyword in databse;Pass flag 1 if you wish to read the logs with search keyword in storage txt file.


