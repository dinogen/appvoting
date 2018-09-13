create table voting_user (
    user_id integer primary key autoincrement,
    user_name text unique,
    pass_word text
);

create table votation (
    votation_id text primary key,
    promoter_user_id integer,
    votation_description text,
    begin_date date,
    end_date date,
    votation_type text
);

create table guarantor (
    votation_id text,
    user_id integer,
    primary key (votation_id, user_id)
);

create table candidate (
    votation_id text,
    user_id integer,
    primary key (votation_id, user_id)
);

insert into voting_user(user_name, pass_word) values ('aldo','aldo');
insert into voting_user(user_name, pass_word) values ('beppe','beppe');
insert into voting_user(user_name, pass_word) values ('carlo','carlo');
