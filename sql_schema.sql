-- Creating Clients Table
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20)
);

-- Creating Stores Table
CREATE TABLE Stores (
    store_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    CONSTRAINT fk_client
        FOREIGN KEY(client_id) 
        REFERENCES Clients(client_id)
        ON DELETE CASCADE
);

-- Creating Locations Table
CREATE TABLE Locations (
    location_id SERIAL PRIMARY KEY,
    store_id INT NOT NULL,
    description TEXT NOT NULL,
    barcode VARCHAR(255),  -- Nullable for locations without a physical barcode
    CONSTRAINT fk_store
        FOREIGN KEY(store_id) 
        REFERENCES Stores(store_id)
        ON DELETE CASCADE
);

-- Creating Zones Table
CREATE TABLE Zones (
    zone_id SERIAL PRIMARY KEY,
    store_id INT NOT NULL,
    description TEXT NOT NULL,
    CONSTRAINT fk_zone_store
        FOREIGN KEY(store_id)
        REFERENCES Stores(store_id)
        ON DELETE CASCADE
);

-- Creating StockTakeEvents Table
CREATE TABLE StockTakeEvents (
    event_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_by INT NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,  -- Nullable, might not be set until the event ends
    status VARCHAR(50) NOT NULL,
    CONSTRAINT fk_event_creator
        FOREIGN KEY(created_by)
        REFERENCES Users(user_id)
        ON DELETE SET NULL
);

-- Creating Users Table
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    password_hash VARCHAR(255) NOT NULL
);

-- Creating SKUs Table
CREATE TABLE SKUs (
    sku_id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    barcode VARCHAR(255) UNIQUE  -- Barcode that is unique to each SKU
);

-- Creating Barcodes Table
CREATE TABLE Barcodes (
    barcode VARCHAR(255) PRIMARY KEY,
    sku_id INT,
    location_id INT,
    CONSTRAINT fk_barcode_sku
        FOREIGN KEY(sku_id)
        REFERENCES SKUs(sku_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_barcode_location
        FOREIGN KEY(location_id)
        REFERENCES Locations(location_id)
        ON DELETE SET NULL
);

-- Creating StockCounts Table
CREATE TABLE StockCounts (
    count_id SERIAL PRIMARY KEY,
    event_id INT NOT NULL,
    location_id INT NOT NULL,
    barcode VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    count_date TIMESTAMP NOT NULL,
    CONSTRAINT fk_count_event
        FOREIGN KEY(event_id)
        REFERENCES StockTakeEvents(event_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_count_location
        FOREIGN KEY(location_id)
        REFERENCES Locations(location_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_count_barcode
        FOREIGN KEY(barcode)
        REFERENCES Barcodes(barcode)
        ON DELETE RESTRICT
);

-- Optionally, create indexes for frequently accessed fields
CREATE INDEX idx_store_client ON Stores(client_id);
CREATE INDEX idx_location_store ON Locations(store_id);
CREATE INDEX idx_event_user ON StockTakeEvents(created_by);
CREATE INDEX idx_count_event ON StockCounts(event_id);
CREATE INDEX idx_barcode_sku ON Barcodes(sku_id);
