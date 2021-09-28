USE AdventureWorks2016CTP3;  
GO  
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET NOCOUNT ON
CREATE TABLE Inserted ([address] int);  
GO  
  
DECLARE @TransactionName varchar(20) = 'Transaction2';  
  
BEGIN TRAN @TransactionName  
       INSERT INTO Inserted VALUES(1702), (3342);  
ROLLBACK TRAN @TransactionName;  
  
INSERT INTO Inserted VALUES(8894),(4222);  
  
SELECT [address] FROM Inserted;  
  
DROP TABLE Inserted;  