from enum import Enum

from pydantic import BaseModel


class Info(BaseModel):
    station_name: str


class MessageFormatKind(int, Enum):
    ARTIST_TITLE = 0
    SHOW_ARTIST_TITLE = 1
    RADIO_SHOW = 2


class StreamPreferences(BaseModel):
    input_fade_transition: float
    default_crossfade_duration: float
    default_fade_in: float
    default_fade_out: float
    message_format: MessageFormatKind
    message_offline: str


class StreamState(BaseModel):
    input_main_connected: bool
    input_main_streaming: bool
    input_show_connected: bool
    input_show_streaming: bool
    schedule_streaming: bool
