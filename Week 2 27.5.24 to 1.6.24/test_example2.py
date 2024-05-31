def greet(person):
    return "hi {name}".format(**person)

def test_greet():
    bob = {"name": "Bob"}       # Arrange
    greeting = greet(bob)       # Act
    assert greeting == "hi Bob" # Assert