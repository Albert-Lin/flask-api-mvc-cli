def repository_factory(model, repository):
    class BaseRepository(repository):
        def __init__(self):
            self.objects = model.objects

        def insert(self, entity):
            entity.save()
            if entity.pk is None:
                raise Exception(entity.__class__.__name__, "Insert Error")
            return entity

        def update(self, entity):
            entity.save()
            if entity.pk is None:
                raise Exception(entity.__class__.__name__, "Update Error")
            return entity

        def delete(self, entity):
            entity.delete()
            return True

        def delete_by_condition(self, condition):
            self.objects(__raw__=condition).delete()
            return True

        def get_all(self, key, value):
            return self.objects(__raw__={key: value})

        def get_first(self, key, value):
            return self.objects(__raw__={key: value}).first()

        def get_by_condition(self, condition):
            return self.objects(__raw__=condition)

        def get_first_by_condition(self, condition):
            return self.objects(__raw__=condition).first()

        def get_count_by_condition(self, condition):
            return self.objects(__raw__=condition).count()

        def get_by_pk(self, pk):
            return self.objects.with_id(pk)

    return BaseRepository()
