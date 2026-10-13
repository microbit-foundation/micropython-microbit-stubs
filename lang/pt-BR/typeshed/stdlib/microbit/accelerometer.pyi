"""Mede a aceleração do micro:bit e reconhece gestos. (acelerômetro)"""
from typing import Tuple

def get_x() -> int:
    """Obtenha a medida da aceleração no eixo ``x`` em milli-g. (Obter x)

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """Obtenha a medida da aceleração no eixo ``y`` em milli-g. (Obter y)

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """Obtenha a medida da aceleração no eixo ``z`` em milli-g. (Obter Z)

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """Obtenha as medidas de aceleração em todos os eixos de uma só vez como uma tupla. (Obter valores)

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Obtenha a medida de aceleração de todos os eixos combinados, como um número inteiro positivo. Esta é a soma Pitagórica dos eixos X, Y e Z. (Obter força)

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """Obter o nome do gesto atual. (Gesto atual)

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """Verificar se o gesto nomeado está ativo no momento. (É gesto)

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (nome) O nome do gesto.
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """Verifique se o gesto nomeado estava ativo desde a última chamada. (Foi gesto)

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (nome) O nome do gesto.
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """Retorna uma tupla do histórico de gestos. (Obter gestos)

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """Define o intervalo de sensibilidade do acelerômetro, em g (gravidade padrão), para os valores mais próximos suportados pelo hardware, então ele é arredondado para ``2``, ``4``ou ``8`` g. (Definir intervalo)

Example: ``accelerometer.set_range(8)``

:param value: (Valor) Novo intervalo para o acelerômetro, um inteiro em ``g``."""