# Сокращатель ссылок

## API

### POST `/create_link/{link}`
Создаем ссылку, `link` -- ссылка, которую нужно сократить. Опционально в ней может содержаться конкретный хеш для ссылки.

### GET `/u/{hash}`
Сокращенная ссылка. При отправке запроса редирект на соответствующую ему ссылку.

### POST `/edit/{link}`
Меняем хеш для исходной ссылки.

### GET `/logs/{hash}`
Извлекаем логи по сокращенной ссылке: в ответ JSON с количеством кликов, IP-адресами, временем перехода в стандартном формате времени UNIX, источником перехода по ссылке

### DELETE `/u/{hash}`
Удалить сокращенную ссылку из базы.

## База данных

* `URLS {id INT NOT NULL UNIQUE, link VARCHAR(255)}` -- исходные ссылки
* `ShortenedURLS {id INT NOT NULL UNIQUE, link VARCHAR(255)}` -- укороченные ссылки
* `AllURLs {id INT NOT NULL UNIQUE, url_link_id VARCHAR(255), shortened_url_id VARCHAR(255)}` -- список сокращенных ссылок
* `Logs {id INT NOT NULL UNIQUE, all_url_id VARCHAR(255), milliseconds BIGINT, IP VARCHAR(20), referrer VARCHAR(255)}` -- логи по исходной ссылки. `milliseconds` --  количество миллисекунд с 01.01.1970 00:00:00



