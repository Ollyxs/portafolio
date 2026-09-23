import reflex as rx
from reflex_base.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="portafolio",
    plugins=[
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="grass",
                radius="full"
            )
        )
    ],
    disable_plugins=[SitemapPlugin]
)
