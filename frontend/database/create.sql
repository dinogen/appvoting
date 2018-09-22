PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE voting_user (
    user_id integer primary key autoincrement,
    user_name text unique,
    pass_word text
);
INSERT INTO voting_user VALUES(1,'aldo','aldo');
INSERT INTO voting_user VALUES(2,'beppe','beppe');
INSERT INTO voting_user VALUES(3,'carlo','carlo');
INSERT INTO voting_user VALUES(4,'dario','dario');
INSERT INTO voting_user VALUES(5,'ernesto','ernesto');
INSERT INTO voting_user VALUES(6,'fabio','fabio');
CREATE TABLE votation
(
    votation_id integer primary key autoincrement,
    promoter_user_id integer,
    votation_description text unique,
    begin_date date,
    end_date date,
    votation_type text,
    votation_status integer
);
INSERT INTO votation VALUES(1,1,'votation test 1','2018-10-01','2018-10-30','random',0);
INSERT INTO votation VALUES(2,1,'votation test 2','2018-10-01','2018-10-30','random',0);
INSERT INTO votation VALUES(3,1,'votation test 3','2018-09-21','2018-10-15','random',0);
INSERT INTO votation VALUES(4,1,'votation test 4','2018-10-03','2018-10-10','random',1);
CREATE TABLE guarantor
(
    votation_id integer,
    user_id integer,
    passphrase_ok integer,
    hash_ok integer,
    primary key (votation_id, user_id)
);
INSERT INTO guarantor VALUES(2,5,0,0);
INSERT INTO guarantor VALUES(3,5,0,0);
INSERT INTO guarantor VALUES(4,5,0,0);
INSERT INTO guarantor VALUES(2,6,0,0);
INSERT INTO guarantor VALUES(3,6,0,0);
INSERT INTO guarantor VALUES(4,6,0,0);
CREATE TABLE candidate
(
    votation_id integer,
    user_id integer,
    passphrase_ok integer,
    primary key (votation_id, user_id)
);
INSERT INTO candidate VALUES(2,2,0);
INSERT INTO candidate VALUES(3,2,0);
INSERT INTO candidate VALUES(4,2,0);
INSERT INTO candidate VALUES(2,3,0);
INSERT INTO candidate VALUES(3,3,0);
INSERT INTO candidate VALUES(4,3,0);
INSERT INTO candidate VALUES(2,4,0);
INSERT INTO candidate VALUES(3,4,0);
INSERT INTO candidate VALUES(4,4,0);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('voting_user',6);
INSERT INTO sqlite_sequence VALUES('votation',4);
COMMIT;
