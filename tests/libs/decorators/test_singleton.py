from unittest import TestCase, main

from src.common.decorators.Singleton import Singleton


@Singleton
class Config:
    def __init__(self, value):
        self.value = value


class TestSingleton(TestCase):
    def setUp(self):
        Config.clear_instance()

    def test_singleton_uniqueness(self):
        obj1 = Config("instance 1")
        obj2 = Config("instance 2")
        self.assertIs(obj1, obj2)

    def test_singleton_value_persistence(self):
        obj1 = Config("first value")
        obj2 = Config("new value")
        self.assertEqual(obj1.value, "first value")
        self.assertEqual(obj2.value, "first value")

    def test_singleton_modification(self):
        obj1 = Config("test")
        obj2 = Config("another test")
        obj1.value = "modified"
        self.assertEqual(obj2.value, "modified")


if __name__ == "__main__":
    main()
