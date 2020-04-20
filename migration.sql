CREATE TABLE URLS
(
    link VARCHAR(255) NOT NULL,
    shortened_link VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (shortened_link)
);

CREATE TABLE Logs
(
    shortened_link VARCHAR(255) NOT NULL UNIQUE,
    milliseconds BIGINT, 
    IP VARCHAR(20), 
    referrer VARCHAR(255),
    PRIMARY KEY (shortened_link)
);


