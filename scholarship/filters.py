from django_filters import FilterSet
from .models import Scholarship

class ArticleFilter(FilterSet):

    class Meta:
        model = Scholarship
        fields = all

    @property
    def qs(self):
        parent = super().qs
        author = getattr(self.request, 'user', None)
        return parent.filter(author=author)