
def hello(name="world", count=1):
    """
    Greeting via saying hello

    :param name: the person to hello
    :param count: times to hello
    :return: None
    """
    for i in range(count):
        print("Hello %s!" % name)


def goodbye(name='world'):
    """
    Goodbye to a person.

    :param name: the person to goodbye.
    :type name: string
    :return: None

    """

    print("Goodbye %s" % name)


