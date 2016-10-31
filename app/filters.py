def short_intro(intro):
    if (len(intro) > 32):
        intro = intro[:32] + "..."

    return intro

def register_filter(app):
    env = app.jinja_env
    env.filters["short_intro"] = short_intro