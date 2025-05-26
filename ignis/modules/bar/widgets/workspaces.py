from ignis.widgets import Widget

class Apps(Widget.Box):
    def __init__(self):
        super().__init__(
            child=applications.bind(
                "pinned",
                transform=lambda value: [AppItem(app) for app in value]
                + [
                    Widget.Button(
                        child=Widget.Icon(image="start-here-symbolic", pixel_size=32),
                        on_click=lambda x: app.toggle_window("ignis_LAUNCHER"),
                        css_classes=["pinned-app", "unset"],
                    )
                ],
            )
        )
    
