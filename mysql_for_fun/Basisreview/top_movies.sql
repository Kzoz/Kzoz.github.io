CREATE TABLE [dbo].[top_movies]
(
  [Id] INT NOT NULL PRIMARY KEY,
  [Title] TEXT NOT NULL,
  [Year] INTEGER,
  [Genre1] TEXT,
  [Genre2] TEXT NULL,
  [Imdb] INTEGER,
  [Review] INTEGER 
);

