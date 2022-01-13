from allennlp.models import Model


@Model.register("foo")
class Foo(Model):
    pass
