import reflex as rx
from portafolio.components.media import media
from portafolio.data import Data, Media
from portafolio.styles.styles import Size


def footer(d: Data, data: Media) -> rx.Component:
    return rx.vstack(
        rx.text(d.name),
        media(data),
        spacing=Size.SMALL.value
    )
