from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import NoteModel
# Create your tests here.


class NoteTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username = 'debugger',
            password = 'uncommon'
        )
        testuser1.save()

        test_note = NoteModel.objects.create(
            author = testuser1,
            title = 'First Note',
            body = 'Test note body',
        )
        test_note.save()
    
    def test_note_content(self):
        note = NoteModel.objects.get(id=1)
        actual_author = str(note.author)
        actual_title = str(note.title)
        actual_body = str(note.body)

        self.assertEqual([
            actual_author,
            actual_title,
            actual_body
        ], [
            'debugger',
            'First Note',
            'Test note body'
        ])