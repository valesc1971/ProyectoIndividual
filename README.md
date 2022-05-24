# Proyecto Individual - VS - Handmade Shop & More

Este proyecto consiste en el desarrollo de un sitio web para un negocio independiente

El objetivo de este sitio es presentar la empresa y sus productos / servicios, permitir la interacción con clientes (compras y mensajes / comentario) y la administración de este (datos usuarios, productos, compras)


## Tabla de Contenidos

* [Tecnologias Usadas](#Tecnologias)
* [Instalacion](#Instalacion)
* [Consideraciones](#Consideraciones)
* [Funcionalidad](#Funcionalidad)

<a name="Tecnologias"></a>
## Tecnologias

Este proyecto fue creado usando:
* HTML
* CSS
* Boostrap   (https://getbootstrap.com/)
* JavaScript (https://datatables.net/)
* JQuery    (https://jquery.com/)
* DataTable plugin (https://datatables.net/)
* Python (https://www.python.org/)
* Django (https://www.djangoproject.com/)
* PostgreSQL (https://www.postgresql.org/)
* FancyBox (http://fancybox.net/)
* SweetAlert plugin (https://sweetalert.js.org/)
* FontAwsome (https://fontawesome.com/)

<a name="Instalacion"></a>
## Instalacion
Para descargar este proyecto, se debe clonar desde este repositorio remoto a un repositorio local.

$git clone https://github.com/valesc1971/ProyectoIndividual.git

Se debe tambien correr dentro de un entorno virtual de Python (virtualenv) (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

Las librerías instaladas se encuentran en el archivo requirements.txt


<a name="Consideraciones"></a>
## Consideraciones

Para el desarrollo del código de frontend, se utilizó HTML como herramienta principal. Para el formato, se utilizandó CSS y las herramientas JavaScript, JQuery, Boostrap, DataTable, Fancybox y FontAwsome las que son llamadas usando CDNs.

Los archivos de HTML se encuentran en una carpeta dentro de la aplicacion (aplicacion1/templates)
 ![image](https://user-images.githubusercontent.com/99301347/169719544-42b98166-ce87-45ae-8b84-ae3bb9dc1a82.png)

 
Se creo una plantilla de html (proyecto/templates/base_layout.html) que contiene el logo de la tienda, la barra de navegacion , el footer y mensajes de alerta de tal forma de usar el principio de diseño DRY. De esta forma, se usa el concepto de “block content” para llamar a este template dentro de los archivos HTML principales. Este template también incluye los archivos y CDNs para las herramientas de diseño.
  
 ![image](https://user-images.githubusercontent.com/99301347/169719549-e47f3ed5-5bdd-4483-8de9-beeb917548b1.png)
 ![image](https://user-images.githubusercontent.com/99301347/169719553-07f4b4e0-de4e-4602-8969-aa7dab9a83f9.png)
![image](https://user-images.githubusercontent.com/99301347/169719556-f9fc79b5-9409-43c5-a911-a16e4fe57a9b.png)
![image](https://user-images.githubusercontent.com/99301347/169719559-7d61d699-893a-45fe-a5ad-6e91cec20ecb.png)
 
Los archivos de imagenes, CSS y JS se encuentran dentro de un directorio static (aplicacion1/static)

![image](https://user-images.githubusercontent.com/99301347/169719568-3dc04c13-3981-4d21-8aef-67d77b6a758e.png)
 
Se puede navegar a través del sitio usando las opciones que entrega la barra de navegación. Estas opciones tienes visibilidad de acuerdo al tipo de usuario que ha ingresado.

En caso de no haber ingresado como usuario de la aplicacion, se despliegan también opciones reducidas de la barra de navegación.
Los links incluidos en la barra de navegacion son los siguientes:

•	Inicio, Mis trabajos y Productos: presentacion de la tienda y productos. Una vez ingresado el usuario, desde la opción “productos” puede tambien comenzar a comprar
•	Contacto: formulario para enviar mensaje. Una vez enviado un mensaje, el usuario recibe un mail de agradecimiento/informativo
•	Menu: Este menú permite el acceso a registro de visitantes (Inscripcion Club), Revisar ordenes de compra anteriores, Registro de usuarios, Ingresar y Salir
 
 ![image](https://user-images.githubusercontent.com/99301347/169719575-3873548c-e0ba-4524-98c3-16e504ebfe14.png)
 
•	Admin: Este menú permite el acceso a opciones de usuarios “Staff” o “Superusuarios”. Las opciones que entrega permiten ingresar nuevos productos, ver la lista de productos, revisar mensajes recibidos de visitantes, y revisar la lista de clientes registrados
 
![image](https://user-images.githubusercontent.com/99301347/169719579-e5fac681-c990-4ff7-b81f-10c2fd66a2f5.png)

El desarrollo del codigo de backend se hizo usando la framework django en conjunto con python.

Existe un Superusuario creado y se agregó la opción de registro de nuevos usuarios a través del sitio con la opción "Registro Usuarios" en la barra de navegación. Esta opcion permite registrar usuarios del tipo “Active”. Para darle permisos de usuarios “Staff2 o “Superusuario” se debe hacer desde Admin

El sitio también permite el ingreso de usuarios ya registrados a través de la opción "Ingresar". Una vez que el usuario ingresa, se despliega un mensaje de bienvenida personalizado, y el nombre aparece en la esquina superior derecha con el tipo de usuario registrado.

La opción "Salir" permite al usuario desconectarse.

Se crearon también 2 modelos (Usuarios y Mensajes) las que almacenas datos de usuarios y mensajes enviados. Estas clases se pueden también accesar desde la barra de navegación en la opción "Ingresar Datos Usuario" y "Contacto". Estos ingresos se pueden visualizar desde el sitio en "Lista Datos Usuarios" y en "Revisar Mensajes". Se creo además un tercer modelo (Productos) para listar los productos y su precio. Se crearon posteriormente 2 modelos (Order y OrderItem) para gestionar el carro de compras

La tabla/modelo “Usuarios” permite registrar datos de usuarios y se pueden ver en su totalidad desde la opción "Lista Datos clientes" habiendo ingresado como superusuario o staff. Este formulario cuenta con una validación adicional para el RUT realizada en Python llamada desde el archivo validator.py
 
![image](https://user-images.githubusercontent.com/99301347/169719581-454bb04c-a0f2-4716-af3d-cbf1ab163cfb.png)

Se realizo la migracion de las tablas desde SQLite a PostgreSQL.

El sitio presenta tambien 3 restricciones: Las opciones "Revisar Mensajes", "Ingresar Datos Usuarios" y "Lista Datos Usuarios" tiene restricciones de acceso, por lo que el usuario debe haber ingresado antes de poder revisar estas opciones. Las restricciones se hicieron usando el decorador @login_required  

![image](https://user-images.githubusercontent.com/99301347/169719595-4152e3b1-d9a1-4fa5-a47a-ed6d7b3e85df.png)

La administración de permisos se realiza también con accesos restringidos en la barra de navegación, dependiendo si el usuario ha ingresado o no y que tipo de usuario es.

![image](https://user-images.githubusercontent.com/99301347/169719606-30d1201d-5f12-461c-98f9-31f5da043a92.png)
![image](https://user-images.githubusercontent.com/99301347/169719612-09982706-93ee-4d3f-b217-71a08313b6fd.png)
![image](https://user-images.githubusercontent.com/99301347/169719619-c98df162-a9d3-4c16-8b76-9279c5754992.png)

Si el usuario no ha ingresado, se despliegan las siguientes opciones 
![image](https://user-images.githubusercontent.com/99301347/169719624-9b1c16d5-81a6-42ec-8c15-be3cd6acc7bd.png)
 
Los mensajes enviados a través de la página contacto, se pueden editar, borrar y visualizar en forma filtrada por el email. Si se está ingresado como Superusuario/staff, estos se pueden modificar/eliminar/filtrar por email desde el link "revisar mensajes"
 
 ![image](https://user-images.githubusercontent.com/99301347/169719629-bd33f7ae-0b85-48cd-87d4-0b5930302c35.png)
 
Si el usuario ha ingresado como usuario Active (cliente), solamente puede visualizar, editar o eliminar los mensajes que están bajo su email. De esta forma, puede entrar a la opción "contacto" y desde ahí revisar sus mensajes

 ![image](https://user-images.githubusercontent.com/99301347/169719633-b7e6130b-958c-424a-b57b-626a8e58b802.png)
 
Para realizar el ejercicio de relaciones entre modelos, se usó el modelo anterior "Producto" y se creó un formulario para el ingreso de nuevos productos
 
 ![image](https://user-images.githubusercontent.com/99301347/169719643-55d17b3a-dc13-4b1d-94eb-7b793900b933.png)
 
 De esta forma, se crearon los modelos Clasificacion, Codigo, Color con los siguientes tipos de relaciones con el modelo Producto
 
Clasificacion: uno a muchos 
Codigo: uno a uno 
Color: muchos a muchos

De esta forma, cuando se ingresa un nuevo producto a través del formulario (o admin), se puede elegir de distintas clasificaciones (pero solo 1 clasificación para el producto), se puede tomar solo 1 código (1 código para cada producto sin repetirse) y se pueden elegir más de 1 color para 1 solo producto. 

La lista de los productos se puede visualizar en la tabla Productos que se puede accesar desde la barra de navegación. En esta opción también se puede descargar la lista de productos y sus precios a un formulario Excel.

 ![image](https://user-images.githubusercontent.com/99301347/169719648-09eb01bb-1835-434d-965b-65d8794442c1.png)

![image](https://user-images.githubusercontent.com/99301347/169719653-d22527cf-5a49-480a-af33-5b95306424a8.png)
 
Para realizar el ejercicio de migraciones (revertir y restaurar) se creó un nuevo modelo "Pregunta"

Se implemento la personalización de la página de error 404, sin embargo, no es posible activarla considerando que su implementación significa llevar un ambiente de producción donde los archivos static no son reconocidos, por lo que los archivos de estilo e imágenes se desactivan.

Para visualizarla, se debe hacer los siguientes cambios en el archivo setting.py
 
 ![image](https://user-images.githubusercontent.com/99301347/169719661-19d5e48f-51d2-4697-81fe-68e7b493821e.png)

 ![image](https://user-images.githubusercontent.com/99301347/169719664-123a21bf-d8e8-4010-bf07-12746ae20b83.png)

<a name="Funcionalidad"></a>
## Funcionalidad

Si un usuario visita el sitio y no ingresa, puede enviar un formulario de contacto, registrarse en el club (ingreso solo de datos) o registrarse como usuario. Esta opción lo registra como usuario “Active”.

Si no ha ingresado como usuario, puede visualizar los productos en la opción “Productos”, pero no puede comprar, solo ver los productos.

![image](https://user-images.githubusercontent.com/99301347/169719679-706693bf-684d-41af-a5e0-eebfcf3e74a6.png)

Si el usuario ha ingresado, tanto la opción “Comprar” como “Ver” están visibles. Si no, solo esta disponible la opción Ver.

A través de esta opción se puede también Comprar (disponible solo para usuarios ingresados). Una vez en Productos, se puede agregar directamente el producto al carro de compras (opción comprar)

Si se presiona la opción Ver, se despliega una pagina donde se ve en forma única el producto. Desde esta opción, se puede también agregar/eliminar del carro de compras.

![image](https://user-images.githubusercontent.com/99301347/169719684-ee27240b-617c-47de-9b33-9c163216bf2b.png)

El carrito de compras se puede visualizar presionado el carrito de compras visible en la esquina superior derecha

![image](https://user-images.githubusercontent.com/99301347/169719700-9dd464d3-8fa5-4bb3-9bd9-c81dc77ec053.png)

En el Resumen de la Orden, se pueden cambiar las cantidades a comprar o elminar el producto de la orden. 

Esta opción permite seguir comprando o finalizar la compra. Una vez que se presiona “Finalizar Compra”, se despliega una pantalla con el resumen de la orden. 

![image](https://user-images.githubusercontent.com/99301347/169719712-22907215-e0a1-44ca-88ca-4862f2374d83.png)

Si se presiona “confirmar compra”, se despliega un mensaje de agradecimiento y la orden queda vacía. La idea es conectar esta opcion con una pasarela de pago para realizar el pago de la orden. Por el momento, se dejo de esta forma considerando las implicancias de la implementacion de la pasarela de pago.

Un usuario que ha ingresado puede revisar las ordenes anteriores, a través del Menu

![image](https://user-images.githubusercontent.com/99301347/169719721-22407ae5-0007-4c19-a1c6-8bab6cb250a5.png)

El usuario (ingresado o no) puede enviar mensajes en la opción contacto. Si ha ingresado, puede revisar los mensajes anteriores que ha enviado, modificarlos o eliminarlos.

![image](https://user-images.githubusercontent.com/99301347/169719725-fcf1ccd5-c8b1-4fbe-bd3e-f89585dae700.png)

Un usuario administrativo (Staff O SuperUser) tienen permisos adicionales al usuarioActive.

Los usuarios Staff o Superuser, una vez que han ingresado tienen visibilidad del usuario Active y del link Admin que permite pueden ingresar / modificar / eliminar productos, revisar todos los mensajes anteriores (editarlos/eliminarlos) y revisar la lista de clientes registrados. 

![image](https://user-images.githubusercontent.com/99301347/169719736-b939fca3-a00c-4b28-9e31-a729b63b8443.png)





