from django.test import TestCase


class TestIndex(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'cliente/index.html', 'layouts/base.html')

    def test_hay_buscador(self):
        response = self.client.get('/')
        self.assertContains(response, 'id_buscador')
        self.assertContains(response, '<button class="btn btn-primary" type="submit">Buscar</button>')
        self.assertContains(response, '<ul class="pagination pagination-sm">')
