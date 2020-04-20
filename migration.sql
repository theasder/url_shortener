CREATE TABLE URLS
(
    link VARCHAR(255) NOT NULL,
    id VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);
/* link -- исходная ссылка, id -- сокращенная, в роли первичного ключа хеш сокращенной ссылки */

CREATE TABLE Logs
(
    id VARCHAR(255) NOT NULL UNIQUE,
    milliseconds BIGINT, 
    IP VARCHAR(20), 
    referrer VARCHAR(255),
    PRIMARY KEY (id)
);
/* shortened_link -- сокращенная, milliseconds -- время в стандартном формате UNIX от 01.01.1970, 
IP -- ip-адрес зашедшего, referrer -- источник перехода, если неизвестен источник, то NULL,
в роли первичного ключа хеш сокращенной ссылки */

