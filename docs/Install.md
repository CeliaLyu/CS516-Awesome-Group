The username in install.sh was changed to 'cs516' and the last line was commented out. 

Install postgresql.  
```sh
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Make sure that the postgresql service is started.   
```
sudo service postgresql start
```

Run install.sh. It should ask you to set the password of DB user.  
```sh
bash install.sh
```

Create the basic tables with postgres user. This does NOT create the "cs516" user, you will need to create one by yourself.  
```sh
sudo -u postgres bash db/setup.sh
```

Log in with postgres and start psql.  
```sh
sudo su postgres
psql
```

You should see the database `amazon` was created, with  
```sh
\l
```

There should only be one user named postgres when checking with  
```sh
\du 
```

Create the user cs516 and set password.
```sh
CREATE USER 'cs516';
ALTER ROLE 'cs516' 
WITH PASSWORD '[THE PASSWORD YOU SET IN STEP 3]';
```

Grant privileges to the user cs516
```sh
ALTER USER cs516 WITH SUPERUSER;
```

Now typing `\du` to terminate, you should see something like
```
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 cs516     | Superuser                                                  | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
```

Log back to your own user by `\q` and `exit`. You should see `your_name@your_machine` at the beginning of each line. 

Activate the virtualenv with 
```sh
source env/bin/activate
```
If it successes, a `(env)` will appear at the beginning of each line. 

Finally, 
```sh
flask run
```
Access the ip and the webpage should appear. 
