"""
Test custom django management commands
"""

from unittest.mock import patch 

from psycopg2 import OperartionError as psycopg2Error 

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch("core.management.commands.wait_for_db.command.check")
class CommandTests(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self):
        "Test waiting for db "