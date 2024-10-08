from flask import Blueprint, render_template


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    print("hello")
    return render_template(
        "index.html",
        title="Movies Watchlist",
    )
