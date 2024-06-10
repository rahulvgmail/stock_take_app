CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(15)
);

CREATE TABLE Contracts (
    contract_id SERIAL PRIMARY KEY,
    client_id INT REFERENCES Clients(client_id),
    start_date DATE,
    end_date DATE,
    status VARCHAR(50)
);

CREATE TABLE SKUs (
    sku_id SERIAL PRIMARY KEY,
    contract_id INT REFERENCES Contracts(contract_id),
    description TEXT
);

CREATE TABLE Barcodes (
    barcode VARCHAR(255) PRIMARY KEY,
    sku_id INT REFERENCES SKUs(sku_id),
    description TEXT
);



CREATE TABLE Locations (
    location_id SERIAL PRIMARY KEY,
    contract_id INT REFERENCES Contracts(contract_id),
    description TEXT
);

CREATE TABLE Agents (
    agent_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE StockTakeEvents (
    event_id SERIAL PRIMARY KEY,
    location_id INT REFERENCES Locations(location_id),
    agent_id INT REFERENCES Agents(agent_id),
    status VARCHAR(50),
    start_date TIMESTAMP,
    end_date TIMESTAMP
);

CREATE TABLE StockCounts (
    count_id SERIAL PRIMARY KEY,
    event_id INT REFERENCES StockTakeEvents(event_id),
    sku_id INT REFERENCES SKUs(sku_id),
    barcode VARCHAR(255) REFERENCES Barcodes(barcode),
    quantity INT,
    count_date DATE
);
