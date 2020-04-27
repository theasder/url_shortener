from bottle import Bottle, get, post, delete, request, run

app = Bottle()


@app.post("/v1/urls")
def add_url():
    """
    :return:
    {
        "url": "https://example.com",
        "hash": <hash_url>
    }

    Создаем ссылку. В тело запроса передается ссылка, которую нужно сократить. Опционально в теле может содержаться
    конкретный хеш для ссылки.
    """
    return "added url"


@app.get("/v1/urls/<hash_url>")
def get_url(hash_url):
    """
    :param hash_url:
    :return:
    Сокращенная ссылка. При отправке запроса редирект на соответствующую ему ссылку.
    """
    return hash_url


@app.get("/v1/urls/<hash_url>/logs")
def get_url_logs(hash_url):
    """
    :param hash_url:
    :return:
    Извлекаем логи по сокращенной ссылке: в ответ JSON с количеством кликов, IP-адресами, временем перехода в
    стандартном формате времени UNIX, источником перехода по ссылке
    """
    return hash_url


# @app.get("/")
# def hello():
#     return "hello"


@app.delete("/v1/urls/<hash_url")
def delete_url(hash_url):
    """
    :param hash_url:
    :return:
    Удалить сокращенную ссылку из базы.
    """
    return hash_url


run(app, host='0.0.0.0', port=8080)
