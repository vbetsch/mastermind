def Singleton(cls):
    cls._instance = None

    def get_instance(*args, **kwargs):
        if cls._instance is None:
            cls._instance = cls(*args, **kwargs)
        return cls._instance

    def clear_instance():
        cls._instance = None

    get_instance.clear_instance = clear_instance
    return get_instance
