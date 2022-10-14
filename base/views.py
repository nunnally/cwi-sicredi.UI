from tempfile import template
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context = {
    
            'left_items': [
                {
                    'item': 'Conta Corrent',
                    "href": '#'
                },
                {
                    'item': 'Cartôes ',
                    "href": '#'
                },
                {
                    'item': 'Pix ',
                    'badge': 'Novo',
                    "href": '#'                },
                {
                    'item': 'Consórcios',
                    "href": '#'
                },
                {
                    'item': 'Crédito',
                    "href": '#'
                },
                                {
                    'item': 'Investimentos',
                    "href": '#'
                },
                                {
                    'item': 'Pagamentos',
                    "href": '#'
                },
                                {
                    'item': 'Previdência',
                    "href": '#'
                },
                                {
                    'item': 'Máquina de Cartões',
                    "href": '#'
                },
            ]
        }

        return context
