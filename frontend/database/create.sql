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
CREATE TABLE guarantor
(
    votation_id integer,
    user_id integer,
    passphrase_ok integer not null,
    hash_ok integer not null,
    order_n integer,
    primary key (votation_id, user_id)
);
CREATE TABLE candidate
(
    votation_id integer,
    user_id integer,
    passphrase_ok integer not null,
    order_n integer,
    primary key (votation_id, user_id)
);
COMMIT;
