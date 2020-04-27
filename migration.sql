CREATE TABLE URLS
(
    link VARCHAR(255) NOT NULL,
    hash VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (hash)
);
/* link -- исходная ссылка, hash -- сокращенная ссылка, в роли первичного ключа хеш сокращенной ссылки */

CREATE TABLE Logs
(
    hash VARCHAR(255) NOT NULL UNIQUE,
    milliseconds BIGINT, 
    IP VARCHAR(20), 
    referrer VARCHAR(255),
    PRIMARY KEY (hash)
);
/* hash -- сокращенная, milliseconds -- время в стандартном формате UNIX от 01.01.1970, 
IP -- ip-адрес зашедшего, referrer -- источник перехода, если неизвестен источник, то NULL,
в роли первичного ключа хеш сокращенной ссылки */

