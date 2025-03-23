# Design patterns

## Singleton

I decided to use this creation pattern for objects requiring a single instance that will not be modified during game
launch. It is used, for example, for the class that manages environment variables.

## Decorator

I decided to use this structural pattern to simplify the code and make it more readable. It is used in particular for
the Singleton.

## Mediator

I've decided to use this behavioral pattern for communication between my front-end and back-end. Each controller will
subscribe to the same mediator. This will enable simple, efficient communication with a system of sending
and responding to events. When I need to trigger an event from one subscriber to another, I send a message and all the
other subscribers receive it. Each of them will decide whether or not to handle it. This pattern also lets me scale the
application: I can add as many controllers and graphical interfaces as I like.

## Memento

I've decided to use this behavioral pattern to manage session saves and restores. When I save a game, it will create a
snapshot of the state of the session and save it in a history. When I need to resume a game, the capture will be retrieved
from the history and restored to the exact state it was in.
