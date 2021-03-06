from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django_datatables_view.base_datatable_view import BaseDatatableView

from .models import Keyword, Collection, TestCase, Phase, TestSuite


class KeywordsListJson(LoginRequiredMixin, BaseDatatableView):
    model = Keyword
    columns = ['name', 'description', 'created_at', 'pk']
    order_columns = ['name', 'description', 'created_at', 'pk']
    max_display_length = 100

    def get_initial_queryset(self):
        user = self.request.user
        qs = Keyword.objects.filter(script_type=1).order_by('created_at')
        if not user.is_superuser:
            user_products = user.products.all().values_list('id', flat=True)
            collections = qs.values_list('collection__product__id', flat=True)
            result = [user_products for user_products in collections]
            qs = qs.filter(collection__product__id__in=result)
        return qs

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )
        return qs

    def render_column(self, row, column):
        if column == 'created_at':
            return '{}'.format(row.created_at.strftime("%d/%b/%Y - %H:%M"))
        else:
            return super(KeywordsListJson, self).render_column(row, column)


class TestcasesListJson(LoginRequiredMixin, BaseDatatableView):
    model = TestCase
    columns = ['name', 'description', 'created_at', 'pk']
    order_columns = ['name', 'description', 'created_at', 'pk']
    max_display_length = 100

    def get_initial_queryset(self):
        user = self.request.user
        qs = TestCase.objects.all().order_by('created_at')
        if not user.is_superuser:
            user_products = user.products.all().values_list('id', flat=True)
            collections = qs.values_list('collection__product__id', flat=True)
            result = [user_products for user_products in collections]
            qs = qs.filter(collection__product__id__in=result)
        return qs

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )
        return qs

    def render_column(self, row, column):
        if column == 'created_at':
            return '{}'.format(row.created_at.strftime("%d/%b/%Y - %H:%M"))
        else:
            return super(TestcasesListJson, self).render_column(row, column)


class TestsuitesListJson(LoginRequiredMixin, BaseDatatableView):
    model = TestSuite
    columns = ['name', 'description', 'created_at', 'pk']
    order_columns = ['name', 'description', 'created_at', 'pk']
    max_display_length = 100

    def get_initial_queryset(self):
        user = self.request.user
        qs = TestSuite.objects.all().order_by('created_at')
        if not user.is_superuser:
            user_products = user.products.all().values_list('id', flat=True)
            collections = qs.values_list('collection__product__id', flat=True)
            result = [user_products for user_products in collections]
            qs = qs.filter(collection__product__id__in=result)
        return qs

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__istartswith=search) |
                Q(description__icontains=search)
            )
        return qs

    def render_column(self, row, column):
        if column == 'created_at':
            return '{}'.format(row.created_at.strftime("%d/%b/%Y - %H:%M"))
        else:
            return super(TestsuitesListJson, self).render_column(row, column)


class CollectionsListJson(LoginRequiredMixin, BaseDatatableView):
    model = Collection
    columns = ['name', 'description', 'pk']
    order_columns = ['name', 'description', 'pk']
    max_display_length = 100

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )
        return qs


class PhasesListJson(LoginRequiredMixin, BaseDatatableView):
    model = Phase
    columns = ['name', 'pk']
    order_columns = ['name', 'pk']
    max_display_length = 100

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(name__icontains=search)
        return qs


class KeywordsImportedListJson(LoginRequiredMixin, BaseDatatableView):
    model = Keyword
    columns = ['name', 'description', 'created_at', 'pk']
    order_columns = ['name', 'description', 'created_at', 'pk']
    max_display_length = 100

    def get_initial_queryset(self):
        qs = Keyword.objects.filter(script_type=2).order_by('created_at')
        return qs

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )
        return qs

    def render_column(self, row, column):
        if column == 'created_at':
            return '{}'.format(row.created_at.strftime("%d/%b/%Y - %H:%M"))
        else:
            return super(KeywordsImportedListJson, self).render_column(row, column)
