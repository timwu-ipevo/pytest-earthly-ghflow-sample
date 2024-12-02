import pytest

from notes_app import NotesApp


@pytest.fixture
def app():
    """Returns an instance of the NotesApp class."""
    app = NotesApp()
    return app


@pytest.fixture
def app_without_notes():
    """Returns an instance of the NotesApp class with zero notes."""
    app = NotesApp()
    return app


@pytest.fixture
def app_with_notes():
    """Returns an instance of the NotesApp class with two notes."""
    app = NotesApp()
    app.add_note("Test note 1")
    app.add_note("Test note 2")
    return app
