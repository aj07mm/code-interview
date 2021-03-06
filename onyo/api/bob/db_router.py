# -*- coding: utf-8 -*-
# https://docs.djangoproject.com/en/1.9/topics/db/multi-db/


class BobDBRouter(object):

    def db_for_read(self, model, **hints):
        """
        Attempts to read bob models go to bob_db.
        """
        if model._meta.app_label == 'bob':
            return 'bob_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write bob models go to bob_db.
        """
        if model._meta.app_label == 'bob':
            return 'bob_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the bob app is involved.
        """
        if obj1._meta.app_label == 'bob' or obj2._meta.app_label == 'bob':
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the bob app only appears in the 'bob_db'
        database.
        """
        if app_label == 'bob':
            return db == 'bob_db'
        return None
