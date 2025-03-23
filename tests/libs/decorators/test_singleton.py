from unittest import TestCase, main

from src.common.decorators.Singleton import Singleton


@Singleton
class TestConfig:
    def __init__(self, value):
        self.value = value

    @classmethod
    def clear_instance(cls):
        pass



class TestSingleton(TestCase):
    def setUp(self):
        TestConfig.clear_instance()

    def test_singleton_uniqueness(self):
        obj1 = TestConfig("instance 1")
        obj2 = TestConfig("instance 2")
        self.assertIs(obj1, obj2)

    def test_singleton_value_persistence(self):
        obj1 = TestConfig("first value")
        obj2 = TestConfig("new value")
        self.assertEqual(obj1.value, "first value")
        self.assertEqual(obj2.value, "first value")

    def test_singleton_modification(self):
        obj1 = TestConfig("test")
        obj2 = TestConfig("another test")
        obj1.value = "modified"
        self.assertEqual(obj2.value, "modified")


if __name__ == "__main__":
    main()
