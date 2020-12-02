Lab 4 PR: https://github.com/batoolmalkawii/pythonic-garage-band/pull/1

In this project, we created an OOP program using classes. 
We created five classes, **Band**, linked to several **Musician**s, which is a superclass that contains a **Guitarist**, a **Bassist**, and a **Drummer**, which were handled as subclasses of *Musician* superclass.

***Band:*** Each band includes the following:
    **Attributes:**
        * Name.
        * Members (list of musicians).
    **Methods**
        * `play_solos()`: asks each member musician to play a solo, in the order they were added to band.
        * `to_list()`: returns a list of previously created Band instances.
        * `__repr__`.
        * `__str__`.

***Musician:*** Each musician includes the following:
    **Attributes:**
        * Name.
        * instrument.
    **Methods**
        * `play_solo()`: returns string.
        * `get_instrument()`: returns string.
        * `__repr__`
        * `__str__`

