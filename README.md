# AirBnB Clone

## The console

![The Console](https://res.cloudinary.com/dytnpjxrd/image/upload/v1689005913/airbnb_clone/the_console_y9hao0.png)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

### How to start project:

In order to start the console, use the following command: ./console.py

### How to use project:

- manage (create, update, destroy, etc) objects via a console / command interprete
- store and persist objects to a file (JSON file)
- Commands: create, show, destroy, all (shows all), update, help, quit

### Example how to open:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
