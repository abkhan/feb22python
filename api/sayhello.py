"""First API, local access only"""
import hug


@hug.get()
def hello():
    """Says hello"""
    return 'Hi there'

@hug.get()
def why():
    """Says why"""
    return 'Why there'


