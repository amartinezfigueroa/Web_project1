# Project 1

paginas html:
    book.html = Se muestra un libro en especifico(isn,author,title,year) donde se puede escribir una breve reseña y por consiguiente darle una puntuacion a dicha reseña, la cual podra enviar.

    busqueda.html = Página donde se realiza la busqueda de un libro ya sea por su isbn,titulo,año o autor
    index.html = Barra de busqueda
    inisiosecion.html = Se encuentran los campos de usuario, contraseña y confirmacion de contraseña, los cuales el usuario debera llenar para poder iniciar secion en caso de que tenga una cuenta
    layout.html = Página principal de donde se heredan las demas paginas como inicio de secion, registro y cerrar secion esto haciendo uso de flash y jinja. Ademas un apartado donde se trabaja los mensajes de flash.
    registro.hmtl = Apartado para registrarse en caso de no tener una cuenta

application.py = Archivo donde se programaron todas las rutas:
...primero que todo se agrego el uri de la base de datos a trabajar todo el proyecto

    index: se renderiza la página index
    inicio de secion: se realizan una serie de condiciones para asegurar que el usuario llene todos los campos correspondiente para iniciar secion. Se hace una consulta a la base de datos para extraer los campos(usuario y contraseña) de la tabla usuarios. 
    registro: se capturan los campos que se crearon en el html y se realiza una condicion para saber si la contraseña coincide con la de la confirmacion. Se realiza un select y un insert a la tabla usuarios. por ultimo se valora si el usuario ya existe.
    busqueda: se realiza una consulta a la tabla de libros. Se manda un mensaje flash para decir que no se encontraron coincidencias.
    busquedad/isbn: se realizo un select a la tabla libros y un insert a la tabla puntuacion.
    cerrar: se hizo un "session.clear()" para cerrar secion
    api: Se hace una consulta a la tabla libros y try except en caso de que un libro no tenga una puntuacion o reseñas. Al igual que se realiza una condicion en caso de que no se encuentre un dato en la base de datos.
