# -*- coding: utf-8 -*-

from learning_journal.models import MyModel, DBSession


def test_create_mymodel(dbtransaction):
    new_model = MyModel(name="Norton", value=42)
    assert new_model.id is None
    DBSession.add(new_model)
    DBSession.flush()
    assert new_model.id is not None
