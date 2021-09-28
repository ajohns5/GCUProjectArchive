USE AdventureWorks2016CTP3;
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET NOCOUNT ON
GO

	BEGIN TRANSACTION transaction1;
	
		UPDATE HumanResources.JobCandidate
			set BusinessEntityID = 334
				where JobCandidateID = 4

			SELECT *
			 FROM HumanResources.JobCandidate
					READONLY

			SELECT *
				FROM HumanResources.JobCandidate
					WHERE JobCandidateID = 4

			WAITFOR DELAY '00:00:05'

			IF @@TRANCOUNT > 0
			 ROLLBACK TRANSACTION transaction1
			else
			 COMMIT TRANSACTION
			