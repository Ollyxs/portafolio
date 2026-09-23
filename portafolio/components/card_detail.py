import reflex as rx
from portafolio.data import Extra
from portafolio.styles.styles import IMAGE_HEIGHT, Size

def card_content(extra: Extra) -> rx.Component:
    return rx.vstack(
        rx.image(
            src=extra.image,
            height=IMAGE_HEIGHT,
            width="100%",
            object_fit="cover",
            border_radius="15px 15px 0 0" 
        ) if extra.image != "" else rx.fragment(),
        rx.vstack(
            rx.text.strong(extra.title),
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray"
            ),
            padding="1.5em",
            align_items="start",
            spacing=Size.SMALL.value
        ),
        width="100%",
        spacing="0",
        align_items="start"
    )

def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            card_content(extra),
            href=extra.url,
            is_external=True,
            _hover={"text_decoration": "none"}
        ) if extra.url != "" else rx.dialog.root(
            rx.dialog.trigger(
                rx.box(
                    card_content(extra),
                    cursor="pointer",
                    _hover={"opacity": 0.8}
                )
            ),
            rx.dialog.content(
                rx.image(
                    src=extra.image,
                    width="100%",
                    height="auto",
                    border_radius="15px"
                ),
                rx.dialog.close(
                    rx.button("Cerrar", margin_top="1em", variant="soft", color_scheme="gray")
                ),
                padding="1em",
                max_width="800px"
            )
        ),
        width="100%",
        padding="0",
        overflow="hidden"
    )
