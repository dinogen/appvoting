PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE voting_user (
    user_id integer primary key autoincrement,
    user_name text unique not null,
    pass_word text not null
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
    promoter_user_id integer not null,
    votation_description text unique not null,
    begin_date date not null,
    end_date date not null,
    votation_type text not null,
    votation_status integer not null
);
INSERT INTO votation VALUES(1,1,'votation test 1','2018-10-01','2018-10-30','random',0);
INSERT INTO votation VALUES(2,1,'votation test 2','2018-10-01','2018-10-30','random',0);
INSERT INTO votation VALUES(3,1,'votation test 3','2018-09-21','2018-10-15','random',0);
INSERT INTO votation VALUES(4,1,'votation test 4','2018-10-03','2018-10-10','random',1);
INSERT INTO votation VALUES(5,1,'Test guarantors have to confirm','2018-01-01','2018-01-31','random',3);
CREATE TABLE guarantor
(
    votation_id integer,
    user_id integer,
    passphrase_ok integer not null,
    hash_ok integer not null,
    order_n integer,
    primary key (votation_id, user_id)
);
INSERT INTO guarantor VALUES(4,5,1,0,0);
INSERT INTO guarantor VALUES(4,6,2,0,0);
INSERT INTO guarantor VALUES(5,5,1,0,1);
INSERT INTO guarantor VALUES(5,6,2,0,1);
INSERT INTO guarantor VALUES(1,5,0,0,1);
INSERT INTO guarantor VALUES(1,6,0,0,2);
CREATE TABLE candidate
(
    votation_id integer,
    user_id integer,
    passphrase_ok integer not null,
    order_n integer,
    primary key (votation_id, user_id)
);
INSERT INTO candidate VALUES(4,4,1,0);
INSERT INTO candidate VALUES(4,3,2,0);
INSERT INTO candidate VALUES(4,2,3,0);
INSERT INTO candidate VALUES(5,2,1,1);
INSERT INTO candidate VALUES(5,3,2,1);
INSERT INTO candidate VALUES(5,4,3,1);
INSERT INTO candidate VALUES(1,2,0,1);
INSERT INTO candidate VALUES(1,3,0,2);
INSERT INTO candidate VALUES(1,4,0,3);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('voting_user',6);
INSERT INTO sqlite_sequence VALUES('votation',5);
COMMIT;
