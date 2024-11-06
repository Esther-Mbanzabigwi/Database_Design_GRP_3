-- Creating the Customers table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Gender VARCHAR(10),
    PriorPurchases INT
);

-- Creating the Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Cost DECIMAL(10, 2), 
    ProductImportance VARCHAR(20),
    WeightInGms INT
);

-- Creating the Orders table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    DiscountOffered DECIMAL(5, 2),
    ProductID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Creating the Shipments table
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY,
    OrderID INT,
    WarehouseBlock VARCHAR(1),
    ModeOfShipment VARCHAR(20),
    CustomerCareCalls INT,
    CustomerRating INT,
    ReachedOnTime BOOLEAN, 
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);