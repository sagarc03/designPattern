# Prototype

Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

Prototype allows us to hide the complexity of making new instances from the client. The concept is to copy an existing object rather than creating a new instance from scratch, something that may include costly operations. The existing object acts as a prototype and contains the state of the object. The newly copied object may change same properties only if required. This approach saves costly resources and time, especially when the object creation is a heavy process

Use the Prototype pattern when a system should be independent of how its products are created, composed, and represented; and

* when the classes to instantiate are specified at run-time, for example, by dynamic loading; or
* to avoid building a class hierarchy of factories that parallels the class hierarchy of products; or
* when instances of a class can have one of only a few different combinations of state. It may be more convenient to install a corresponding number of prototypes and clone them rather than instantiating the class manually, each time with the appropriate state.

Structure Participants

* Prototype – declares an interface for cloning itself.
* ConcretePrototype – implements an operation for cloning itself.
* Client – creates a new object by asking a prototype to clone itself.