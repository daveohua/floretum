CREATE TABLE "users" (
  "id" INTEGER PRIMARY KEY,
  "username" TEXT NOT NULL,
  "password_hash" TEXT NOT NULL 
);

CREATE TABLE "observations" (
  "id" INTEGER PRIMARY KEY,
  "user_id" INTEGER REFERENCES user(id),
  "species" TEXT NOT NULL,
  "latitude" REAL NOT NULL, 
  "longitude" REAL NOT NULL,
  "unix_time" INTEGER NOT NULL,
  "photograph" INTEGER NOT NULL
);