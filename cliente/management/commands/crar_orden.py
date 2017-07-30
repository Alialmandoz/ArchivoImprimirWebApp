import random
import datetime
import cliente.choices as choises
from cliente.models import Cliente
from cliente.models import Ordenes
from cliente.models import Trabajo


def gen_orden_trabajo():
    count = Cliente.objects.count()
    rand_cliente = Cliente.objects.all()[random.randint(0, count - 1)]  # single random Cliente
    cant_trab = random.randint(1, 9)


    orden = Ordenes(
        fecha_encargo=datetime.datetime.now(),
        fecha_entrega=datetime.date.today() + datetime.timedelta(days=1),
        cliente=rand_cliente
    )
    orden.save()
    lista_trabajos = []
    for t in range(cant_trab):
        monto = random.randint(0, 100000)
        adelanto = random.randint(0, monto)
        trabajo = Trabajo(
            tipo=str(choises.TIPO_TRABAJO[random.randint(0, 1)][0]),
            detalle='detalle del trabajo',
            monto=monto,
            adelanto=adelanto,
            saldo=monto - adelanto,
            orden=orden
        )
        trabajo.save()