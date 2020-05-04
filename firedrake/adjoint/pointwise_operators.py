from firedrake.adjoint.function import FunctionMixin


class PointwiseOperatorsMixin(FunctionMixin):

    @staticmethod
    def _ad_annotate_init(init):
        def wrapper(self, *args, **kwargs):
            FunctionMixin.__init__(self, *args, **kwargs)
            init(self, *args, **kwargs)
        return wrapper
