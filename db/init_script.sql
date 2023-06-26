BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "item_status" (
	"uid"	INTEGER NOT NULL,
	"label"	TEXT NOT NULL,
	"is_sharing"	INTEGER NOT NULL,
	"is_gift"	INTEGER NOT NULL,
	PRIMARY KEY("uid")
);
CREATE TABLE IF NOT EXISTS "offer" (
	"uid"	INTEGER NOT NULL,
	"timestamp"	INTEGER NOT NULL,
	"informations"	TEXT,
	"item_uid"	INTEGER NOT NULL,
	"user_group_uid"	INTEGER NOT NULL,
	PRIMARY KEY("uid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "item" (
	"uid"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"informations"	TEXT,
	"availability"	INTEGER,
	"constraint"	TEXT,
	"instance_information"	TEXT,
	"owner_uid"	INTEGER,
	"status_uid"	INTEGER,
	PRIMARY KEY("uid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "user_group_relation" (
	"user_uid"	INTEGER NOT NULL,
	"user_group_uid"	INTEGER NOT NULL,
	PRIMARY KEY("user_uid","user_group_uid")
);
CREATE TABLE IF NOT EXISTS "user" (
	"uid"	INTEGER NOT NULL,
	"login"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"contact_informations"	TEXT,
	"location_information"	TEXT,
	"trust_score"	INTEGER,
	"is_active"	INTEGER,
	PRIMARY KEY("uid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "user_group" (
	"uid"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"informations"	TEXT,
	"access_code"	TEXT,
	"is_public"	INTEGER,
	"group_owner"	INTEGER,
	PRIMARY KEY("uid" AUTOINCREMENT)
);
INSERT INTO "item_status" VALUES (1,'share',1,0);
INSERT INTO "item_status" VALUES (2,'gift',0,1);
INSERT INTO "offer" VALUES (1,1686126411,'',1,2);
INSERT INTO "offer" VALUES (2,1686126411,'Adhesion nécessaire au club',2,4);
INSERT INTO "offer" VALUES (3,1686126411,NULL,3,1);
INSERT INTO "offer" VALUES (4,0,NULL,1,4);
INSERT INTO "item" VALUES (1,'Hard-drive IDE to USB2 adapter','Doesn''t work for SATA',1,NULL,'category:computer',1,1);
INSERT INTO "item" VALUES (2,'Nikkor 50mm F/1.8D','Nikon - no stabilization - With polariezd filter',1,NULL,'category:art',1,1);
INSERT INTO "item" VALUES (3,'Graine Ipomee pourpre','Plante grimpante - 10 graines',1,NULL,'category:seed',1,2);
INSERT INTO "user_group_relation" VALUES (2,2);
INSERT INTO "user" VALUES (1,'demo','$2b$12$yR4h8eisqWKiolnW2748HOIfg9A/58JKJ5S0d/.Bf.NyJf7R68NB.','Demo user','demo@mail.eu','Strasbourg, rue des grandes arcades',NULL,1);
INSERT INTO "user" VALUES (2,'besac guy','$2b$12$6s9UtK7bLT.M0wYbPpTfkusbamobEac2021ek/aEaUA7A8KyqgSVe','Besac guy','besac@mail.eu','Besac city - Pont Battant',NULL,1);
INSERT INTO "user" VALUES (3,'','','',NULL,NULL,NULL,NULL);
INSERT INTO "user_group" VALUES (1,'Nadaq community','All users',NULL,1,NULL);
INSERT INTO "user_group" VALUES (2,'Besac-city','People near Besac',NULL,1,NULL);
INSERT INTO "user_group" VALUES (3,'My lovely family',NULL,NULL,0,1);
INSERT INTO "user_group" VALUES (4,'My Photo Club',NULL,NULL,0,1);
COMMIT;
