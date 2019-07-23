class NoteCollectionResource(CollectionResource):
    model = Note
    methods = ['GET', 'POST']


class NoteResource(SingleResource):
    model = Note

