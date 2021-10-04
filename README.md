# PyConES2021
Workshop at PyConES2021

Taller: Utilizando PYTHON para mejorar mi cyber-Swiss army knife

El objetivo del taller, es implementar una mejora con python, de una herramienta ofensiva de ciberseguridad que se utiliza en pentesting, llamada Rubber Ducky (BAD USB)

Si habeis trabajado alguna vez con Rubber, tiene un tedioso problema y es que cada "payload" que le cargas que ejecute una serie de instrucciones, tiene que compilarse e introducirse en la tarjeta que lleva interna. Esto dificulta que durante un pentesting interno, podamos cambiar facilmente el modo de ataque. Se ahí la versatilidad que nos ofrece python, permitiendonos montar un servicio de API con Flask con el que se comunicará nuestra víctima, y un bot de telegram para controlar el tipo de payload que se va a ejecutar, sin necesidad de compilar y cargar el conjunto de instrucciones a nuestro rubber.

Presentación del diseño actual:

![image](![[image1.png]])

Esquema del nuevo diseño

![[image2.png]]

REFERENCIAS

Rubber Ducky

Tienda Hak5 aprox 45$ -> https://hak5.org/products/usb-rubber-ducky-deluxe
Guia paso a paso de uso de Rubber (Spanish)-> https://ingoroman.medium.com/hacking-con-rubber-ducky-eda784b6e5b4


Alternativas

https://github.com/mharjac/bad_ducky
https://github.com/dbisu/pico-ducky

