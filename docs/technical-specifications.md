# Technical specifications

## Technologies

* [Python](https://www.python.org/) : language used in lessons, and easy to use for creating video games in CLI
* [Rich](https://rich.readthedocs.io) : Python library for creating CLI interfaces easily
* [Peewee](https://docs.peewee-orm.com) : Python ORM ([Object-Relational Mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping))
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
└── tests
    ├── archi
    │   └── patterns
    └── libs
        ├── communication
        └── decorators
```

## Game rules

## Session management

## Commits convention
