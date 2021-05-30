from urllib.parse import urlparse


def get_database_path(url: str) -> str:
    path = urlparse(url).path
    return path[path.index("data") :]
