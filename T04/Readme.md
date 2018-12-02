# Paso a paso de la Tarea 4

### Servidor y Cliente
* Primero, es necesario ejecutar el servidor (este se encuentra en `servidor/servidor.py`.
* Una vez abierto el servidor, será posible abrir el Cliente (se encuentra en `cliente/cliente.py`).

### Menú de inicio
* Lo primero que se verá será un menú de inicio que da la bienvenida, con un logo al lado izquierdo, y un fondo que irá cambiando (las imágenes son de *Fortnite*, que es algo irónico por la historia de la tarea xd), además de dos botones, uno para ingresar y otro para registrar.
* En resumen, ya sea para iniciar sesión o para registrarse, el cliente envía una solicitud al servidor, el servidor revisa la base de datos (ubicada en `servidor/bd/usuarios.txt`) y, si es necesario, agrega datos, para luego informar al cliente si esta solicitud fue realizada con éxito para así continuar.
* En el caso de que se desee registrar un usuario, luego hay que cambiar a la pestaña de ingresar, e iniciar sesión (los casilleros quedan con los datos de la pestaña anterior).

### Menú de Partidas
* A continuación aparecerá un menú con las partidas disponibles. Si no hay ninguna partida funcionando en el servidor, el cuadro aparecerá en blanco.
* Para crear una nueva partida se debe presionar el botón `Nueva Partida`, ingresar un nombre y presionar `Crear`, lo que llevará al usuario a la sala de espera (en modo administrador de la partida).
* En caso de que ya exista una partida creada, el usuario puede seleccionarla y luego presionar el otón `Seleccionar Partida` para ingresar. Además existe un botón de `Actualizar` arriba del cuadro de partidas que permite revisar si una partida fue creada últimamente.

### Sala de Espera
* La sala de espera tarda un momento en cargar, pero una vez que el usuario aparezca dentro de los cuadros, esta ya debería funcionar.
* En la parte izquierda hay un chat que permite establecer comunicación entre los usuarios de la partida.
* En la parte inferior derecha podemos encontrar varios cuadros de colores, estos son para cambiar el color del jugador. Para esto, primero se selecciona el color, y luego se presiona `Seleccionar Color`, que cambiará el cuadro del usuario, si este color no estaba en uso.
* A un lado del botón `Seleccionar Color`, está ubicado `Agregar Invitado`, que permitirá agregar un nuevo usuario a la partida, y que podrá ser controlado desde el mismo computador. Para cambiar el color del invitado, se debe realizar el mismo procedimiento, pero esta vez presionando `Sleccionar Color Invitado` que reemplaza al botón `Agregar invitado` cuando este es presionado.
* Si la ventana es para administrador, aparecerá un listado de poderes que se pueden marcar o desmarcar, además de una casilla para la velocidad, y otra para el puntaje máximo. Una vez que es presionada `Iniciar Partida`, comenzará el contador.

### Ventana de Botones
* A continuación aparecerá una ventana para indicar los botones a elegir, para esto se presiona el botón a modificar, y luego la tecla a la cuál se quiere cambiar. S esto funcionó, el texto del botón debería cambiar por el de la tecla respectiva. Una vez que esto decidido, se puede presionar el botón `Listo`.
* A continuación aparecera una ventana con NyanCat y un mensaje que da a entender que se necesita esperar a que los demás usuarios estén listos. Una vez que estén todos listos, se pasará a la ventana de juego, donde se permanecerá en pausa por unos segundos antes de coenzar.

### Ventana de Juego.
* Finalmente llegamos a la ventana de juego. En el lado izquierdo primero aparecen los jugadores (con su respectivo color y puntaje actual). Bajo estos cuadros se ubica un cuadro con el puntaje máximo, para luego llegar a los botones.
* Los botones disponibles son: `Pausar`, que pausa el juego (también fuciona presionando barra espaciadora), y `Salir`, que te permite volver al Menú Principal. `Volver al Menú de Partidas` no funciona actualmente.
* En el juego aparecerán los poderes en lugares al azar, los jugadores se pueden mover, sin embargo, no es completamente jugable, ya que no se acumulan puntos, los poderes no son utilizables, y los usuarios cuando chocan con los bordes o con su rastro, dejan de moverse, pero no da aviso de que haya perdido.
