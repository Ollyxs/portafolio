import reflex as rx

def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    if icon == "github":
        icon_component = rx.box(class_name="devicon-github-original", font_size="1.2em")
    elif icon == "linkedin":
        icon_component = rx.box(class_name="devicon-linkedin-plain", font_size="1.2em")
    else:
        icon_component = rx.icon(icon)

    return rx.link(
        rx.button(
            icon_component,
            text,
            variant="solid" if solid else "surface"
        ),
        href=url,
        is_external=True
    )
