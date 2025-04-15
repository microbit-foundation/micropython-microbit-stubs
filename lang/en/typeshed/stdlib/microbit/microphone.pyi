"""Respond to sound using the built-in microphone (V2 only).
"""

from typing import Optional, Tuple, Union
from ..microbit import SoundEvent
from ..microbit.audio import AudioRecording, AudioTrack

def current_event() -> Optional[SoundEvent]:
    """Get the last recorded sound event

    Example: ``microphone.current_event()``

    :return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``.
    """
    ...

def was_event(event: SoundEvent) -> bool:
    """Check if a sound was heard at least once since the last call.

    Example: ``microphone.was_event(SoundEvent.LOUD)``

    This call clears the sound history before returning.

    :param event: The event to check for,  such as ``SoundEvent.LOUD`` or ``SoundEvent.QUIET``
    :return: ``True`` if sound was heard at least once since the last call, otherwise ``False``.
    """
    ...

def is_event(event: SoundEvent) -> bool:
    """Check the most recent sound event detected.

    Example: ``microphone.is_event(SoundEvent.LOUD)``

    This call does not clear the sound event history.

    :param event: The event to check for,  such as ``SoundEvent.LOUD`` or ``SoundEvent.QUIET``
    :return: ``True`` if sound was the most recent heard, ``False`` otherwise.
    """
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Get the sound event history as a tuple.

    Example: ``microphone.get_events()``

    This call clears the sound history before returning.

    :return: A tuple of the event history with the most recent event last.
    """
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Set the threshold for a sound event.

    Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

    The ``SoundEvent.LOUD`` event is triggered when the sound level crosses the 
    threshold from "quiet" to "loud", and the ``SoundEvent.QUIET`` event is 
    triggered when the sound level crosses from "loud" to "quiet".

    If the ``SoundEvent.LOUD`` threshold is set lower than the 
    ``SoundEvent.QUIET`` threshold, then the ``SoundEvent.QUIET`` threshold 
    will decrease by one unit below the ``SoundEvent.LOUD`` threshold. If the 
    ``SoundEvent.QUIET`` threshold is set higher than the ``SoundEvent.LOUD``
    threshold, then the ``SoundEvent.LOUD`` threshold will increase by one unit 
    above the ``SoundEvent.QUIET`` threshold.

    :param event: A sound event, such as ``SoundEvent.LOUD`` or ``SoundEvent.QUIET``.
    :param value: The threshold level in the range 0-255. Values outside this range will be clamped.
    """
    ...

def sound_level() -> int:
    """Get the sound pressure level in the range 0 to 255.

    Example: ``microphone.sound_level()``

    :return: A representation of the sound pressure level in the range 0 to 255.
    """
    ...

def sound_level_db() -> int:
    """Get the sound pressure level in decibels.

    Example: ``microphone.sound_level_db()``

    :return: A representation of the sound pressure level in decibels (dB).
    """
    ...

def record(duration: int, rate: int = 11_000) -> AudioRecording:
    """Record sound into an ``AudioRecording`` for the amount of time indicated by
    ``duration`` at the sampling rate indicated by ``rate``.

    The amount of memory consumed is directly related to the length of the
    recording and the sampling rate. The higher these values, the more memory
    it will use.

    A lower sampling rate will reduce both memory consumption and sound
    quality.

    If there isn't enough memory available a ``MemoryError`` will be raised.

    :param duration: How long to record in milliseconds.
    :param rate: Number of samples to capture per second.
    :returns: An ``AudioRecording`` with the sound samples.
    """
    ...

def record_into(buffer: Union[AudioRecording, AudioTrack], wait: bool = True) -> AudioTrack:
    """Record sound into an existing ``AudioRecording`` or ``AudioTrack``
    until it is filled, or the ``stop_recording()`` function is called.

    This function also returns an ``AudioTrack`` created from the provided
    input buffer, which length matches the recording duration.
    This is useful when recording with ``wait`` set to ``False``, and the
    recording is stopped before the input buffer is filled.

    :param buffer: ``AudioRecording`` or ``AudioTrack`` to record sound into.
    :param wait: When set to ``True`` it blocks until the recording is
        done, if it is set to ``False`` it will run in the background.
    :returns: An ``AudioTrack`` which ends where the recording ended.
    """
    ...

def is_recording() -> bool:
    """Checks whether the microphone is currently recording.

    Example: ``is_recording = microphone.is_recording()``

    :return: ``True`` if the microphone is currently recording sound, otherwise returns ``False``.
    """
    ...

def stop_recording() -> None:
    """Stops a recording running in the background.

    Example: ``microphone.stop_recording()``
    """
    ...

SENSITIVITY_LOW: float;
"""Low microphone sensitivity."""

SENSITIVITY_MEDIUM: float;
"""Medium microphone sensitivity."""

SENSITIVITY_HIGH: float;
"""High microphone sensitivity."""


def set_sensitivity(gain: float) -> None:
    """Configure the microphone sensitivity.

    Example: ``microphone.set_sensitivity(microphone.SENSITIVITY_HIGH)``

    The default sensitivity is ``microphone.SENSITIVITY_MEDIUM``.

    :param gain: The microphone gain. Use ``microphone.SENSITIVITY_LOW``, ``microphone.SENSITIVITY_MEDIUM``, ``microphone.SENSITIVITY_HIGH``, or a value between these levels.
    """
    ...