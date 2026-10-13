"""Pinos, imagens, sons, temperatura e volume."""
from typing import Any, Callable, List, Optional, Tuple, Union, overload
from _typeshed import ReadableBuffer
from . import accelerometer as accelerometer
from . import audio as audio
from . import compass as compass
from . import display as display
from . import i2c as i2c
from . import microphone as microphone
from . import speaker as speaker
from . import spi as spi
from . import uart as uart

def run_every(callback: Optional[Callable[[], None]]=None, days: int=0, h: int=0, min: int=0, s: int=0, ms: int=0) -> Callable[[Callable[[], None]], Callable[[], None]]:
    """Programe a execução de uma função no intervalo especificado pelos argumentos de tempo **V2 only**. (microbit.run_every)

Example: ``run_every(my_logging, min=5)``

``run_every`` can be used in two ways:

As a Decorator - placed on top of the function to schedule. For example::

    @run_every(h=1, min=20, s=30, ms=50)
    def my_function():
        # Do something here

As a Function - passing the callback as a positional argument. For example::

    def my_function():
        # Do something here
    run_every(my_function, s=30)

Each argument corresponds to a different time unit and they are additive.
So ``run_every(min=1, s=30)`` schedules the callback every minute and a half.

When an exception is thrown inside the callback function it deschedules the
function. To avoid this you can catch exceptions with ``try/except``.

:param callback: (retorno de chamada) Função a ser chamada no intervalo fornecido. Omitir ao usar como um decorador.
:param days: (Dias) Defina a meta do dia para a programação.
:param h: Define a hora marcada para o agendamento.
:param min: Define a marca de minutos para o agendamento.
:param s: Define a marca de segundos para o agendamento.
:param ms: Define a marca de milissegundos para o agendamento."""

def panic(n: int) -> None:
    """Entrar no modo pânico. (pânico)

Example: ``panic(127)``

:param n: Um número inteiro arbitrário ≤ 255 para indicar um status.

Requires restart."""

def reset() -> None:
    """Reinicie o micro:bit (redefinir)"""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """Converte um valor de um intervalo para um intervalo de inteiros. (escala)

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: (Valor) Um número para converter.
:param from_: (De) Uma tupla para definir o intervalo de conversão.
:param to: (para) Uma tupla para definir o intervalo para o qual converter.
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """Converte um valor de um intervalo para um ponto flutuante. (Escala)

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: (Valor) Um número para converter.
:param from_: (De) Uma tupla para definir o intervalo de conversão.
:param to: (para) Uma tupla para definir o intervalo para o qual converter.
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """Espere por ``n`` milissegundos. (dormir)

Example: ``sleep(1000)``

:param n: O número de milissegundos a esperar

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Obtenha o tempo de execução da placa. (tempo de execução)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Obtenha a temperatura do micro:bit em graus Celsius. (temperatura)"""

def set_volume(v: int) -> None:
    """Define o volume. (Definir volume)

Example: ``set_volume(127)``

:param v: um valor entre 0 (baixo) e 255 (alto).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """A classe dos botões ``button_a`` e ``button_b``. (botão)"""

    def is_pressed(self) -> bool:
        """Verifique se o botão está pressionado. (está pressionado)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Verifique se o botão foi pressionado desde o início do dispositivo ou a última vez que esse método foi chamado. (foi pressionado)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Obtenha o total de toques de botões, e redefina este total
para zero antes de retornar. (recebe toques)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""O botão à esquerda ``Button`` objeto. (botão A)"""
button_b: Button
"""O botão direito ``Button`` objeto. (botão B)"""

class MicroBitDigitalPin:
    """Um pino digital. (pinomicrobitdigital)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Obtenha o valor digital do pino. (ler digital)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Defina o valor digital do pino. (escrever no digital)

Example: ``pin0.write_digital(1)``

:param value: (Valor) 1 para definir o pin alto ou 0 para definir o pin baixo"""
        ...

    def set_pull(self, value: int) -> None:
        """Defina o estado do pull para um dos três valores possíveis: ``PULL_UP``, ``PULL_DOWN`` ou ``NO_PULL``. (defina pull)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (Valor) O estado de pull do pino relevante, por exemplo, ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Obter o estado de pull em um pino (obter pull)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Retorna o modo pino. (modo de obtenção)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Efetua um sinal PWM no pino, com o ciclo de serviço proporcional a ``value``. (escrever analógico)

Example: ``pin0.write_analog(254)``

:param value: (Valor) Um número inteiro ou de vírgula flutuante entre 0 (0% de ciclo de funcionamento) e 1023 (100% de funcionamento)."""

    def set_analog_period(self, period: int) -> None:
        """Define o período de saída do sinal PWM para ``period`` em milissegundos. (definir período analógico)

Example: ``pin0.set_analog_period(10)``

:param period: (período) O período em milissegundos com um valor mínimo válido de 1ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Defina o período do sinal PWM sendo enviado para ``period`` em microssegundos. (definir analog período microseconds)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (período) O período em micro segundos com um valor mínimo válido de 256µs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Um pin com recursos analógicos e digitais."""

    def read_analog(self) -> int:
        """Leia a tensão aplicada ao pin. (leitura analógica)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Um pin com recursos analógicos, digitais e de toque."""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Verifique se o pin está sendo tocado. (é tocado)

Example: ``pin0.is_touched()``

The default touch mode for the pins on the edge connector is ``resistive``.
The default for the logo pin **V2** is ``capacitive``.

**Resistive touch**
This test is done by measuring how much resistance there is between the
pin and ground.  A low resistance gives a reading of ``True``.  To get
a reliable reading using a finger you may need to touch the ground pin
with another part of your body, for example your other hand.

**Capacitive touch**
This test is done by interacting with the electric field of a capacitor
using a finger as a conductor. `Capacitive touch
<https://www.allaboutcircuits.com/technical-articles/introduction-to-capacitive-touch-sensing>`_
does not require you to make a ground connection as part of a circuit.

:return: ``True`` if the pin is being touched with a finger, otherwise return ``False``."""
        ...

    def set_touch_mode(self, value: int) -> None:
        """Defina o modo de toque para o pin. (definir modo de toque)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (Valor) ``CAPACITIVE`` ou ``RESISTIVE`` do pin relevante."""
        ...
pin0: MicroBitTouchPin
"""Pin com recursos digitais, analógicos e de toque."""
pin1: MicroBitTouchPin
"""Pin com recursos digitais, analógicos e de toque."""
pin2: MicroBitTouchPin
"""Pin com recursos digitais, analógicos e de toque."""
pin3: MicroBitAnalogDigitalPin
"""Pin com recursos digitais e analógicos."""
pin4: MicroBitAnalogDigitalPin
"""Pin com recursos digitais e analógicos."""
pin5: MicroBitDigitalPin
"""Pin com recursos digitais."""
pin6: MicroBitDigitalPin
"""Pin com recursos digitais."""
pin7: MicroBitDigitalPin
"""Pin com recursos digitais."""
pin8: MicroBitDigitalPin
"""Pin com recursos digitais."""
pin9: MicroBitDigitalPin
"""Pin com recursos digitais."""
pin10: MicroBitAnalogDigitalPin
"""Pin com recursos digitais e analógicos."""
pin11: MicroBitDigitalPin
"""Pin com recursos digitais."""
pin12: MicroBitDigitalPin
"""Pin com recursos digitais."""
pin13: MicroBitDigitalPin
"""Pin com recursos digitais."""
pin14: MicroBitDigitalPin
"""Fixar com recursos digitais."""
pin15: MicroBitDigitalPin
"""Fixar com recursos digitais."""
pin16: MicroBitDigitalPin
"""Fixar com recursos digitais."""
pin19: MicroBitDigitalPin
"""Fixar com recursos digitais."""
pin20: MicroBitDigitalPin
"""Fixar com recursos digitais."""
pin_logo: MicroBitTouchPin
"""Um pino de logo sensível ao toque na frente do micro:bit, que por padrão está configurado para o modo de toque capacitivo. (fixar logo)"""
pin_speaker: MicroBitAnalogDigitalPin
"""Um pino para conectar ao alto-falante do micro:bit. (pino do alto-falante)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Uma imagem para exibir no display de LEDs do micro:bit. (imagem)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Imagem do coração (coração)"""
    HEART_SMALL: Image
    """Imagem pequena do coração. (coração pequeno)"""
    HAPPY: Image
    """Imagem de um rosto feliz (feliz)"""
    SMILE: Image
    """Imagem de uma boca sorridente. (sorriso)"""
    SAD: Image
    """Imagem de um rosto triste. (triste)"""
    CONFUSED: Image
    """Imagem de um rosto confuso. (confuso)"""
    ANGRY: Image
    """Imagem de um rosto bravo. (bravo)"""
    ASLEEP: Image
    """Imagem de um rosto dormindo. (adormecido)"""
    SURPRISED: Image
    """Imagem de um rosto surpreso. (surpreso)"""
    SILLY: Image
    """Imagem de um rosto engraçado. (engraçado)"""
    FABULOUS: Image
    """Imagem de um rosto com óculos de sol. (fabuloso)"""
    MEH: Image
    """Imagem de um rosto desapontado."""
    YES: Image
    """Imagem de correto. (sim)"""
    NO: Image
    """Imagem de uma cruz. (não)"""
    CLOCK12: Image
    """Imagem com uma linha apontando para as 12 horas."""
    CLOCK11: Image
    """Imagem com uma linha apontando para as 11 horas."""
    CLOCK10: Image
    """Imagem com uma linha apontando para as 10 horas."""
    CLOCK9: Image
    """Imagem com uma linha apontando para as 9 horas."""
    CLOCK8: Image
    """Imagem com uma linha apontando para as 8 horas."""
    CLOCK7: Image
    """Imagem com uma linha apontando para as 7 horas."""
    CLOCK6: Image
    """Imagem com uma linha apontando para as 6 horas."""
    CLOCK5: Image
    """Imagem com uma linha apontando para as 5 horas."""
    CLOCK4: Image
    """Imagem com uma linha apontando para as 4 horas."""
    CLOCK3: Image
    """Imagem com uma linha apontando para as 3 horas. (Relógio 3)"""
    CLOCK2: Image
    """Imagem com uma linha apontando para as 2 horas. (Relógio 2)"""
    CLOCK1: Image
    """Imagem com uma linha apontando para as 1 horas. (Relógio 1)"""
    ARROW_N: Image
    """Imagem da seta apontando para norte. (seta n)"""
    ARROW_NE: Image
    """Imagem da seta apontando para nordeste. (seta nordeste)"""
    ARROW_E: Image
    """Imagem da seta apontando para leste. (seta leste)"""
    ARROW_SE: Image
    """Imagem da seta apontando para leste. (seta sudeste)"""
    ARROW_S: Image
    """Imagem da seta apontando para sul. (seta sul)"""
    ARROW_SW: Image
    """Imagem da seta apontando para sudeste. (seta sudeste)"""
    ARROW_W: Image
    """Imagem da seta apontando para oeste. (seta oeste)"""
    ARROW_NW: Image
    """Imagem da seta apontando para noroeste. (seta noroeste)"""
    TRIANGLE: Image
    """Imagem de um triângulo apontando para cima. (triângulo)"""
    TRIANGLE_LEFT: Image
    """Imagem de um triângulo no canto esquerdo. (triângulo à esquerda)"""
    CHESSBOARD: Image
    """LEDs alternados acesos em um padrão xadrez. (tabuleiro de xadrez)"""
    DIAMOND: Image
    """Imagem de um diamante (diamante)"""
    DIAMOND_SMALL: Image
    """Imagem de diamante pequeno. (diamante pequeno)"""
    SQUARE: Image
    """Imagem do quadrado (quadrado)"""
    SQUARE_SMALL: Image
    """Imagem de quadrado pequena. (quadrado pequeno)"""
    RABBIT: Image
    """Imagem do coelho. (coelho)"""
    COW: Image
    """Imagem de uma vaca (vaca)"""
    MUSIC_CROTCHET: Image
    """Imagem de clave musical (Clave musical)"""
    MUSIC_QUAVER: Image
    """Imagem de nota clave (compasso musical)"""
    MUSIC_QUAVERS: Image
    """Imagem de par de claves musicais (Notas musicais)"""
    PITCHFORK: Image
    """Imagem de forquilha (Forquilha)"""
    XMAS: Image
    """Imagem de árvore de Natal (Natal)"""
    PACMAN: Image
    """Imagem do personagem do jogo Pacman (Pacman)"""
    TARGET: Image
    """Imagem alvo (Alvo)"""
    TSHIRT: Image
    """Imagem de camiseta (Camiseta)"""
    ROLLERSKATE: Image
    """Imagem de "skate" ("Skate")"""
    DUCK: Image
    """Imagem de pato (Pato)"""
    HOUSE: Image
    """Imagem de casa (Casa)"""
    TORTOISE: Image
    """Imagem de tartaruga (Tartaruga)"""
    BUTTERFLY: Image
    """Imagem de borboleta (Borboleta)"""
    STICKFIGURE: Image
    """Imagem de boneco palito (Boneco palito)"""
    GHOST: Image
    """Imagem de fantasma (Fantasma)"""
    SWORD: Image
    """Imagem de espada (Espada)"""
    GIRAFFE: Image
    """Imagem de girafa (Girafa)"""
    SKULL: Image
    """Imagem de caveira (Caveira)"""
    UMBRELLA: Image
    """Imagem de guarda-chuva (Guarda-chuva)"""
    SNAKE: Image
    """Imagem de cobra. (Cobra)"""
    SCISSORS: Image
    """Imagem de tesoura. (tesoura)"""
    ALL_CLOCKS: List[Image]
    """Uma lista contendo todas as imagens de CLOCK_ em sequência. (todos os relógios)"""
    ALL_ARROWS: List[Image]
    """Uma lista contendo todas as imagens de ARROW_ em sequência. (todas as setas)"""

    @overload
    def __init__(self, string: str) -> None:
        """Crie uma imagem a partir de uma cadeia que descreva quais LEDs estão acesos. (iniciar)

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (cadeia) A cadeia de caracteres que descreve a imagem."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Crie uma imagem com ``width`` colunas e ``height`` fileiras. (iniciar)

:param width: (Largura) Largura opcional da imagem
:param height: (Peso) Peso opcional da imagem
:param buffer: (Tampão) Forma e bytes opcionais de ``width``×``height`` inteiros no intervalo de 0-9 para iniciar a imagem

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Procurar número de colunas. (Largura)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Obter o número das linhas. (Peso)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Configurar brilho de um píxel (Configurar píxel)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: Número da coluna
:param y: Número da fileira
:param value: (Valor) O brilho com um intervalo entre 0 (escuro) e 9 (claro)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Configurar brilho de um píxel. (Configurar píxel)

Example: ``my_image.get_pixel(0, 0)``

:param x: Número da coluna
:param y: Número da fileira
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Criar imagem arrastando foto à direita (Arrastar para esquerda)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: Número de colunas para arrastar para
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Criar imagem arrastando foto à direita. (Arrastar para a direita)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: O número das colunas a serem deslocadas
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Criar imagem arrastando foto para cima (Arrastar pra cima)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: Número de colunas para arrastar para
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Criar imagem arrastando imagem para baixo (Arrastar para baixo)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: Número de colunas para arrastar para
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Criar imagem recortando a foto (Recortar)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: A coluna de compensação da colheita
:param y: A linha de compensação da colheita
:param w: (W) Largura do recorte
:param h: Tamanho recorte
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Criar uma cópia exata da imagem. (Copiar)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Criar imagem invertendo o brilho de pixels na imagem pesquisada. (Inverter)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Configurar brilho da imagem (Completar)

Example: ``my_image.fill(5)``

:param value: (Valor) Novo brilho como um número entre 0 (escuro) e 9 (claro).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Copiar uma área de outra imagem para esta imagem.

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: A imagem de origem
:param x: O deslocamento inicial da coluna na imagem de origem
:param y: O deslocamento inicial da linha na imagem de origem
:param w: (W) O número de colunas a copiar
:param h: O número de linhas a copiar
:param xdest: O deslocamento da coluna a ser modificado nesta imagem
:param ydest: O deslocamento da linha a ser modificado nesta imagem

Pixels outside the source image are treated as having a brightness of 0.

``shift_left()``, ``shift_right()``, ``shift_up()``, ``shift_down()``
and ``crop()`` can are all implemented by using ``blit()``.

For example, img.crop(x, y, w, h) can be implemented as::

    def crop(self, x, y, w, h):
        res = Image(w, h)
        res.blit(self, x, y, w, h)
        return res"""
        ...

    def __repr__(self) -> str:
        """Obter uma representação de string compacta da imagem."""
        ...

    def __str__(self) -> str:
        """Obter uma representação de string legível da imagem."""
        ...

    def __add__(self, other: Image) -> Image:
        """Criar uma nova imagem adicionando os valores de brilho das duas imagens para cada pixel. (adicionar)

Example: ``Image.HEART + Image.HAPPY``

:param other: (outro) A imagem a ser adicionada."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Criar uma nova imagem subtraindo os valores de brilho da outra imagem desta imagem.

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (outro) A imagem a ser subtraída."""
        ...

    def __mul__(self, n: float) -> Image:
        """Criar uma nova imagem multiplicando o brilho de cada pixel por ``n``.

Example: ``Image.HEART * 0.5``

:param n: O valor para multiplicar."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Criar uma nova imagem dividindo o brilho de cada pixel por ``n``.

Example: ``Image.HEART / 2``

:param n: O valor para dividir."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Representa a transição de eventos sonoros, de ``quiet`` para ``loud``, como aplausos ou gritos. (alto)"""
    QUIET: SoundEvent
    """Representa a transição de eventos sonoros, de ``loud`` para ``quiet``, como fala ou música de fundo. (silencioso)"""

class Sound:
    """Os sons embutidos podem ser chamados usando ``audio.play(Sound.NAME)``. (som)"""
    GIGGLE: Sound
    """Som de risada. (risadinha)"""
    HAPPY: Sound
    """Som feliz. (feliz)"""
    HELLO: Sound
    """Som de cumprimento. (olá)"""
    MYSTERIOUS: Sound
    """Som misterioso. (misterioso)"""
    SAD: Sound
    """Som triste. (triste)"""
    SLIDE: Sound
    """Som de deslizamento. (deslizar)"""
    SOARING: Sound
    """Som de planar. (planar)"""
    SPRING: Sound
    """Som da primavera. (primavera/mola)"""
    TWINKLE: Sound
    """Som de brilho (brilho)"""
    YAWN: Sound
    """Som de bocejo (bocejo)"""