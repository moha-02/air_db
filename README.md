# air_db
An example of a small airline database

**POLIMORFISMO**

![](Aspose.Words.1bb849e8-405d-4932-9546-cb8f24522943.001.png)

Mohammed Salhi DAW 1 A

24 de marzo del 2023

<a name="_page1_x72.00_y72.00"></a>Índice

[**2**](#_page1_x72.00_y72.00)

1. [**Introducción 3**](#_page2_x72.00_y72.00)
1. [**Algoritmo 3**](#_page2_x72.00_y167.92)
1. [**Ejemplo del código 4**](#_page3_x72.00_y230.69)
1. [**Conclusion 5**](#_page4_x72.00_y72.00)
1. [**Webgrafia 6**](#_page5_x72.00_y72.00)
1. Introducción

<a name="_page2_x72.00_y72.00"></a>El polimorfismo es la capacidad de los cuerpos de tomar diferentes formas, es decir, tener diferentes comportamientos dependiendo del contexto en el que se encuentre. En el caso de Java, el polimorfismo se logra mediante la utilización de clases y métodos que pueden ser sobreescritos por las subclases que heredan de ellas.

2. Algoritmo

<a name="_page2_x72.00_y167.92"></a>Implementaremos una clase Vehículo que tiene un método mover() que es sobreescrito por las clases Coche y Bicicleta. Luego, en el método main, se creará una instancia de la clase Coche y se asigna a una variable de tipo Vehículo. Eso es exactamente el polimorfismo.

class Vehiculo {

public void mover(int distancia) {

System.out.println("El vehículo se está moviendo " + distancia + "

metros"); }

}

class Coche extends Vehiculo {

public void mover(int distancia) {

System.out.println("El coche está avanzando " + distancia + " metros"); if (distancia > 10) {

System.out.println("El coche está yendo rápido");

} else {

System.out.println("El coche está yendo lento");

}

}

}

class Bicicleta extends Vehiculo {

public void mover(int distancia) {

System.out.println("La bicicleta está pedaleando " + distancia + " metros"); if (distancia > 5) {

System.out.println("La bicicleta está yendo rápido");

} else {

System.out.println("La bicicleta está yendo lento");

}

}

}

public class PolimorfismoEjemplo {

public static void main(String[] args) {

Vehiculo miVehiculo = new Coche();

miVehiculo.mover(15); // El coche está avanzando 15 metros

// El coche está yendo rápido

miVehiculo = new Bicicleta();

miVehiculo.mover(3); // La bicicleta está pedaleando 3 metros

// La bicicleta está yendo lento

}

}

3. Ejemplo<a name="_page3_x72.00_y230.69"></a> del código

En la clase Coche se utiliza el método mover() para imprimir el mensaje "El coche está avanzando" seguido de la distancia recorrida, y si la distancia es mayor a 10 metros se imprime un mensaje adicional indicando que el coche está yendo rápido. En la clase Bicicleta se utiliza el método mover() para imprimir el mensaje "La bicicleta está pedaleando" seguido de la distancia recorrida, y si la distancia es mayor a 5 metros se imprime un mensaje adicional indicando que la bicicleta está yendo rápido.

En el método main se crea una instancia de la clase Coche y se asigna a una variable de tipo Vehículo. Luego se llama al método mover() utilizando esa variable, lo que hace que se ejecute el método sobreescrito en la clase Coche. Lo mismo sucede cuando se crea una instancia de la clase Bicicleta y se llama al método mover().

4. Conclusion

<a name="_page4_x72.00_y72.00"></a>Para resumir, el polimorfismo permite que un “objeto” pueda adoptar formas distintas. En el caso propuesto, un vehículo puede ser una Bicicleta o un Coche. El polimorfismo permite que se puedan compartir los métodos comunes.

5. Webgrafia

<a name="_page5_x72.00_y72.00"></a>**- Maximo Fernandez Riera: [https://github.com/maximofernandezriera/ejemplo-polimorfismo**](https://github.com/maximofernandezriera/ejemplo-polimorfismo)**
