CREATE TABLE links (
    id SERIAL PRIMARY KEY,
    link TEXT NOT NULL,
    date_added TIMESTAMP NOT NULL,
    UNIQUE (link)
);
