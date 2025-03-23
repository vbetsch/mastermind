# Technical specifications

## Technologies

* [Python](https://www.python.org/) : language used in lessons, and easy to use for creating video games in CLI
* [Rich](https://rich.readthedocs.io) : Python library for creating CLI interfaces easily
* [Peewee](https://docs.peewee-orm.com) : Python
  ORM ([Object-Relational Mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping))
* [SQLite](https://www.sqlite.org/) : Serverless database

## Architecture

Here is the architecture of the project, which respects clean architecture :

```
.
├── src
│   ├── app
│   │   ├── controllers
│   │   ├── exceptions
│   │   ├── gateways
│   │   ├── ports
│   │   │   ├── repositories
│   │   │   └── usecases
│   │   ├── presenters
│   │   └── usecases
│   ├── common
│   │   ├── abstract
│   │   ├── communication
│   │   │   └── messages
│   │   │       ├── cli
│   │   │       │   ├── main
│   │   │       │   └── menu
│   │   │       └── controllers
│   │   └── decorators
│   ├── domain
│   │   ├── core
│   │   ├── entities
│   │   └── values
│   │       ├── combinations
│   │       └── sessions
│   ├── infra
│   │   ├── database
│   │   │   └── models
│   │   ├── env
│   │   └── repositories
│   └── ui
│       └── cli
│           └── components
│           └── controllers
└── tests
    ├── archi
    │   └── patterns
    └── libs
        ├── communication
        └── decorators
```

### app

This folder contains the application part of the clean architecture.<br>

Here's the list of items you can find:

* Controllers
* Custom exceptions
* Gateways
* Ports
* Presenters
* Use cases

### common

This folder is the common library for the front-end and back-end.<br>
Here's the list of items you can find:

* Abstract objects
* Decorators
* All about communication between front and back

### domain

This folder covers the domain of clean architecture.<br>

Here's the list of items you can find:

* Entities
* Value objects
* Core objects (responsible for enforcing the rules of the game)

### infra

This folder covers the infrastructure part of clean architecture.<br>

Here's the list of items you can find:

* Repositories
* All about database configuration
* All about environment variables

### ui

This folder contains all the project's graphical interfaces.<br>

Here's the list of items you can find in each UI :

* Components
* Controllers

### tests

This folder contains all the project tests.<br>

Here's the list of types of tests you can find:

## Game rules

## Session management

## Commits convention
