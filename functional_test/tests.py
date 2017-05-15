from cliente.models import Cliente
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10


class IndexTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertTrue(str([row.text for row in rows]).__contains__(row_text))
                # self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_puede_buscar_cliente(self):
        cliente = Cliente()
        cliente.nombre = 'ali'
        cliente.apellido = 'almandoz'
        cliente.telefono = 123456
        cliente.direccion = 'ali'
        cliente.slug = 'ali-ali'
        cliente.mail = 'ali@h.com'
        cliente.save()

        self.browser.get(self.live_server_url)
        # ivan ingresa a la pagina.
        #  nota que el titulo es: Bienvenido:
        self.assertIn('ArchivoImprimir.com.ar', self.browser.title)
        # Ivan hace una búsqueda en el sistema para averiguar si el cliente esta registrado en la base de datos.
        inputbox = self.browser.find_element_by_id('id_buscador')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Buscar Cliente'
        )
        inputbox.send_keys('ali')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('ali')

    # si el cliente no esta en la db,
    # Comienza con el registro del cliente en la base de datos.

    def test_puede_crear_clientes(self):
        self.browser.get("http://127.0.0.1:8000/crear_cliente/")
        in_nombre = self.browser.find_element_by_id('id_nombre')
        in_apellido = self.browser.find_element_by_id('id_apellido')
        in_mail = self.browser.find_element_by_id('id_mail')
        in_telefono = self.browser.find_element_by_id('id_telefono')
        in_direccion = self.browser.find_element_by_id('id_direccion')
        boton = self.browser.find_element_by_id('id_boton')
        # el cliente le debe  dar a ivan su nombre apellido y mail,
        in_nombre.send_keys('Ivan')
        in_apellido.send_keys('Almandoz')
        in_mail.send_keys('Almandoz@gmail.com')
        # opcionalmente también un teléfono de contacto y una dirección para la entrega de trabajos.
        in_telefono.send_keys(1234560)
        in_direccion.send_keys('casita')
        boton.click()

        self.browser.get("http://127.0.0.1:8000")

        inputbox = self.browser.find_element_by_id('id_buscador')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Buscar Cliente'
        )
        inputbox.send_keys('Ivan')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('Ivan')






# una vez registrado el cliente  ivan es redireccionado a una pagina donde  puede hacer clic en un botón
# para crear una orden de trabajo  así  como editar los datos para este cliente.


# en esta pagina ivan tiene un form donde descrivir los trabajos a realizar con una casilla para
# cargar el costo de cada uno y los detalles inherentes a cada trabajo.


# la orden de trabajo se completa pidiendo una seña y dando una fecha de entrega.
# (opcional ) un cuadro donde se arrastren los trabajos y queden asociados a la orden de trabajo que se esta procesando.
#  - Poder relacionar los trabajos por proceso ej laminado guillotinado etc.


# Una vez creada la orden ivan es llevado a una pagina que muestra el detalle se la orden y a su ves le permite editar
# su contenido asi como agregar mas trabajos y detalles. Y un menú para volver.
'''
    def test_can_start_a_list_for_one_user(self):
        print('test_can_start_a_list_for_one_user starts here')
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        # She visits that URL - her to-do list is still there.
        #  TODO support more than one list
        # Satisfied, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        print('test_multiple_users_can_start_lists_at_different_urls starts here')
        # Edith start a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site.
        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page.  There is no sign of Edith's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep


        '''
