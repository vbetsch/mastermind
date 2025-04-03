# Design patterns

## Singleton

I decided to use this creation pattern for objects requiring a single instance that will not be modified during game
launch. It is used, for example, for the class that manages environment variables.

## Decorator

I decided to use this structural pattern to simplify the code and make it more readable. It is used in particular for
the Singleton.

## Mediator

I decided to use this behavioral model for communication between my front-end and back-end. Each controller (frontend or
backend) will subscribe to the same mediator. This will enable simple, efficient communication with a system for sending
and responding to events. When I need to trigger an event from one subscriber to another, I send a message and all the
other subscribers receive it. Each of them decides whether or not to process it. This model also allows me to evolve the
application: I can add as many controllers as I want.

## Memento

I've decided to use this behavioral pattern to manage session saves and restores. When I save a game, it will create a
snapshot of the state of the session and save it in a history. When I need to resume a game, the capture will be
retrieved
from the history and restored to the exact state it was in.

> Note : The Factory design pattern is also used by python libraries
