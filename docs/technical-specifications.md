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
│   │   │       ├── player
│   │   │       ├── prepare
│   │   │       └── session
│   │   ├── presenters
│   │   └── usecases
│   │       ├── player
│   │       ├── prepare
│   │       └── session
│   ├── common
│   │   ├── communication
│   │   │   └── dto
│   │   ├── decorators
│   │   │   └── dto
│   │   ├── exceptions
│   │   ├── logs
│   │   └── patterns
│   │       ├── mediator
│   │       └── memento
│   ├── domain
│   │   ├── core
│   │   ├── entities
│   │   └── values
│   │       ├── combinations
│   │       ├── players
│   │       ├── sessions
│   │       └── turns
│   │           └── indicators
│   ├── infra
│   │   ├── database
│   │   │   └── models
│   │   ├── env
│   │   └── repositories
│   └── ui
│       └── cli
│           ├── components
│           └── handlers
└── tests
    ├── archi
    │   └── patterns
    └── units
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

* All about design patterns structure
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
* Handlers (middleware between CLI and Controllers)

### tests

This folder contains all the project tests.<br>

Here's the list of types of tests you can find:

* Architecture tests (clean architecture, design patterns, etc)
* Unit tests

## Game rules

Game rules are managed mainly by the [Rules](../src/domain/core/Rules.py) object but also
by [entities](../src/domain/entities), [value objects](../src/domain/values) and
others [core objects](../src/domain/core) :

### Entities

* [Player](../src/domain/entities/Player.py)
* [Session](../src/domain/entities/Session.py)

### Value objects

* [Combination](../src/domain/values/combinations/Combination.py) : represents combinations
  of [Beads](../src/domain/values/combinations/Bead.py)
* [Turn](../src/domain/values/sessions/Turn.py) : element of Session
* [Feedback](../src/domain/values/turns/Feedback.py) : represents feedbacks returned by the system for a proposal
* [Indicator](../src/domain/values/turns/indicators/Indicator.py) : element of Feedbacks (represents red and white
  pawns)

### Core objects

* [Arbitrator](../src/domain/core/Arbitrator.py) : defines whether a combination is right or wrong
* [Generator](../src/domain/core/Generator.py) : generates random combinations
* [Rules](../src/domain/core/Rules.py) : handle game rules
* [Storage](../src/domain/core/Storage.py) : manage local storage

## Session management

[Sessions](../src/domain/entities/Session.py) are managed using a memento pattern. When I save a
game, a snapshot ([SessionMemento](../src/domain/values/sessions/SessionMemento.py)) is created of the state of the game
and saves it in
a history ([SessionHistory](../src/domain/values/sessions/SessionHistory.py)). When I need to resume a game, the
snapshot is retrieved from the history and restored to the exact state it
was in.

## User interfaces

## Communication

Communication between backend and frontend is managed by a [Mediator](../src/common/communication/Mediator.py). Every controller, every manager and every user
interface subscribes to it. Handlers act as intermediaries between controllers and user interfaces, and are used in
particular for menus. This enables communication with a system for sending and responding to [events](../src/common/communication/EventEnum.py). When I need to
trigger an event from a [subscriber](../src/common/communication/Subscriber.py), I send a message and all the other subscribers receive it. Each of them then decides
whether or not to process it (using the handle function). It's also possible to transmit data using the [dtos](../src/common/communication/dto).
This model also allows me to evolve the application: I can add as many handlers, controllers and graphical interfaces as
I like.

### CLI

The CLI graphical interface is managed by the [CLI](../src/ui/cli/CLI.py) object, which uses
the [Displayer](../src/ui/cli/Displayer.py) object to display elements on the
screen. The Displayer uses [components](../src/ui/cli/components). The CLI will call events
using [handlers](../src/ui/cli/handlers).

## Commits convention

To make commits legible and easy to write, I use the [Gitmoji](https://gitmoji.dev/) convention.
