CREATE SCHEMA offers;

CREATE TABLE offers.offers (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    hiring_organization TEXT NOT NULL,
    date_posted TIMESTAMP NOT NULL,
    valid_through TIMESTAMP NOT NULL,
    address_country TEXT NOT NULL,
    address_region TEXT NOT NULL,
    address_locality TEXT NOT NULL,
    postal_code TEXT,
    street_address TEXT,
    employment_type TEXT NOT NULL,
    industry TEXT NOT NULL,
    base_salary FLOAT,
    job_benefits TEXT,
    responsibilities TEXT NOT NULL,
    experience_requirements TEXT NOT NULL,
    link_id INTEGER,
    FOREIGN KEY (link_id) REFERENCES links.links(id)
);
