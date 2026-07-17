from config import IT_KEYWORDS


def is_it_job(title: str, description: str = "") -> bool:

    text = f"{title} {description}".lower()

    return any(

        keyword in text

        for keyword in IT_KEYWORDS

    )
