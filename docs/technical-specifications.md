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
│           ├── components
│           └── controllers
└── tests
    ├── archi
    │   └── patterns
    └── units
        ├── app
        │   ├── controllers
        │   └── usecases
        └── domain
            ├── core
            ├── entities
            └── values
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

* Architecture tests (clean architecture, design patterns, etc)
* Unit tests

## Game rules

Game rules are managed by [entities](../src/domain/entities) and [core objects](../src/domain/core).

### Entities

* [Session](../src/domain/entities/Session.py) : represents games
* [Combination](../src/domain/entities/Combination.py) : represents combinations
  of [Beads](../src/domain/values/combinations/Bead.py)

### Core objects

* [Arbitrator](../src/domain/core/Arbitrator.py) : defines whether a combination is right or wrong

## Session management

[Sessions](../src/domain/entities/Session.py) are managed using a memento pattern. When I save a
game, a snapshot ([SessionMemento](../src/domain/values/sessions/SessionMemento.py)) is created of the state of the game
and saves it in
a history ([SessionHistory](../src/domain/values/sessions/SessionHistory.py)). When I need to resume a game, the
snapshot is retrieved from the history and restored to the exact state it
was in.

## User interfaces

### CLI

The CLI graphical interface is managed by the [CLIController](../src/ui/cli/CLIController.py), which uses
the [Displayer](../src/ui/cli/Displayer.py) object to display elements on the
screen. The Displayer uses [components](../src/ui/cli/components).

## Communication

Communication between the backend and frontend is managed by [Mediator](../src/common/communication/Mediator.py). Each
controller (backend and frontend) subscribes to it. This makes communication with a
system for sending and responding to [events](../src/common/communication/messages). When I
need to trigger an event from a [subscriber](../src/common/communication/Subscriber.py), I send a message and all the
other subscribers receive it. Each of them then
decides whether or not to process it (with the handle function). This model also allows me to evolve the application: I
can add as many controllers
and graphical interfaces as I like.

## Commits convention

To make commits legible and easy to write, I use the [Gitmoji](https://gitmoji.dev/) convention.
