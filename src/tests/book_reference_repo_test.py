import os
import sqlite3
import unittest
from database import Database
from repositories.book_reference_repo import BookReference


class TestBookReference(unittest.TestCase):
    def SetUp(self):
        self.database = Database()
        self.connection = database.get_database_connection()
