from unittest import TestCase, main

from src.common.abstract.mediator.IMediator import IMediator
from src.common.communication.Mediator import Mediator
from src.common.communication.Subscriber import Subscriber


class SubscriberTest(Subscriber):
    def __init__(self, name: str, mediator: IMediator) -> None:
        super().__init__(name, mediator)
        self.received_messages = []

    def handle(self, message: str, sender: 'SubscriberTest') -> None:
        self.received_messages.append((message, sender.name))

class TestMediatorPattern(TestCase):
    def setUp(self):
        self.mediator = Mediator()
        self.subscriber1 = SubscriberTest("Alice", self.mediator)
        self.subscriber2 = SubscriberTest("Bob", self.mediator)
        self.subscriber3 = SubscriberTest("Charlie", self.mediator)

    def test_subscriber_receives_message(self):
        self.subscriber1.send("Hello, everyone!")
        self.assertIn(("Hello, everyone!", "Alice"), self.subscriber2.received_messages)
        self.assertIn(("Hello, everyone!", "Alice"), self.subscriber3.received_messages)

    def test_sender_does_not_receive_own_message(self):
        self.subscriber2.send("Hi, I'm Bob.")
        self.assertNotIn(("Hi, I'm Bob.", "Bob"), self.subscriber2.received_messages)

    def test_multiple_messages(self):
        self.subscriber1.send("First message")
        self.subscriber2.send("Second message")
        self.assertIn(("First message", "Alice"), self.subscriber2.received_messages)
        self.assertIn(("First message", "Alice"), self.subscriber3.received_messages)
        self.assertIn(("Second message", "Bob"), self.subscriber1.received_messages)
        self.assertIn(("Second message", "Bob"), self.subscriber3.received_messages)

if __name__ == '__main__':
    main()
