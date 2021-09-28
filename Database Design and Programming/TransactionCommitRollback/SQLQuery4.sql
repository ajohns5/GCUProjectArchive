USE AdventureWorks2016CTP3;
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET NOCOUNT ON
GO

BEGIN TRANSACTION transaction3
SELECT * FROM HumanResources.JobCandidate
DELETE FROM HumanResources.JobCandidate where JobCandidateID = 8
SELECT * FROM HumanResources.JobCandidate
ROLLBACK
SELECT * FROM HumanResources.JobCandidate