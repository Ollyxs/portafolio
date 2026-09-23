import reflex as rx
from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.components.icon_badge import icon_badge
from portafolio.data import Extra
from portafolio.styles.styles import Size


def extra(extras: list[Extra]) -> rx.Component:
    text_extras = [extra for extra in extras if extra.image == ""]
    card_extras = [extra for extra in extras if extra.image != ""]
    
    return rx.vstack(
        heading("Extra"),
        
        # Render text-based extras
        rx.cond(
            len(text_extras) > 0,
            rx.vstack(
                *[
                    rx.hstack(
                        icon_badge("languages"), # Hardcoding an icon since Extra doesn't have one
                        rx.vstack(
                            rx.text.strong(item.title),
                            rx.text(
                                item.description,
                                size=Size.SMALL.value,
                                color_scheme="gray"
                            ),
                            spacing=Size.SMALL.value,
                            width="100%"
                        ),
                        spacing=Size.DEFAULT.value,
                        width="100%"
                    )
                    for item in text_extras
                ],
                spacing=Size.DEFAULT.value,
                width="100%"
            ),
            rx.fragment()
        ),
        
        # Render card-based extras
        rx.cond(
            len(card_extras) > 0,
            rx.vstack(
                rx.mobile_only(
                    rx.vstack(
                        *[
                            card_detail(item)
                            for item in card_extras
                        ],
                        spacing=Size.DEFAULT.value
                    ),
                    width="100%"
                ),
                rx.tablet_and_desktop(
                    rx.grid(
                        *[
                            card_detail(item)
                            for item in card_extras
                        ],
                        spacing=Size.DEFAULT.value,
                        columns="3"
                    ),
                    width="100%"
                ),
                width="100%"
            ),
            rx.fragment()
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
