class CallbackManager:

    """
    A class that manages callbacks for different events. Class is a singleton for maximum versitility.

    This class provides functionality to register and unregister callbacks for specific events,
    as well as invoking the registered callbacks when the corresponding event occurs.

    Usage:
        - Create an instance of CallbackManager: manager = CallbackManager()
        - Register a callback for an event: manager.register_callback(event_name, callback)
        - Unregister a callback for an event: manager.unregister_callback(event_name, callback)
        - Invoke all registered callbacks for an event: manager.invoke_callbacks(event_name, *args, **kwargs)

    Attributes:
        callbacks (dict): A dictionary that stores the registered callbacks. The keys are event names,
                          and the values are lists of associated callback functions.

    Methods:
        __contains__(callback_name):
            Check if a given callback name is already registered.

        register_callback(event_name, callback):
            Register a new callback function for a specified event name.

            Args:
                event_name (str): The name of the event to associate with this callback.
                callback (function): The function to be called when the specified event occurs.

        unregister_callback(event_name, callback):
            Unregister a callback function for a specified event name.

            Args:
                event_name (str): The name of the event associated with the callback.
                callback (function): The function to be unregistered.

        invoke_callbacks(event_name, *args, **kwargs):
            Invoke all registered callbacks for a specified event name.

            Args:
                event_name (str): The name of the event to trigger the callbacks.
                *args: Variable length argument list to pass to the callbacks.
                **kwargs: Arbitrary keyword arguments to pass to the callbacks.

        async_invoke_callbacks(event_name, *args, **kwargs):
            Asynchronously invoke all registered callbacks for a specified event name. This method is intended
            for use with asynchronous functions or coroutines as callbacks.

            Args:
                event_name (str): The name of the event to trigger the asynchronous callbacks.
                *args: Variable length argument list to pass to the asynchronous callbacks.
                **kwargs: Arbitrary keyword arguments to pass to the asynchronous callbacks.

    """

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.callbacks = {}
        return cls._instance

    def __contains__(self, callback_name):
        return callback_name in self.callbacks

    @property
    def keys(self):
        return list(self.callbacks.keys())

    def register_callback(self, event_name, callback):
        if event_name not in self.callbacks:
            self.callbacks[event_name] = []
        self.callbacks[event_name].append(callback)

    def unregister_callback(self, event_name, callback):
        if event_name in self.callbacks:
            if callback in self.callbacks[event_name]:
                self.callbacks[event_name].remove(callback)

    def invoke_callbacks(self, event_name, *args, **kwargs):
        if event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                callback(*args, **kwargs)

    async def async_invoke_callbacks(self, event_name, *args, **kwargs):
        if event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                await callback(*args, **kwargs)