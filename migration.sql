CREATE TABLE URLS
(
    link VARCHAR(255) NOT NULL,
    shortened_link VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (shortened_link)
);
/* link -- исходная ссылка, shortened_link -- сокращенная, в роли первичного ключа хеш сокращенной ссылки */

CREATE TABLE Logs
(
    shortened_link VARCHAR(255) NOT NULL UNIQUE,
    milliseconds BIGINT, 
    IP VARCHAR(20), 
    referrer VARCHAR(255),
    PRIMARY KEY (shortened_link)
);
/* shortened_link -- сокращенная, milliseconds -- время в стандартном формате UNIX от 01.01.1970, 
IP -- ip-адрес зашедшего, referrer -- источник перехода, если неизвестен источник, то NULL,
в роли первичного ключа хеш сокращенной ссылки */

