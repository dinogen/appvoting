create table voting_user (
    user_id integer primary key autoincrement,
    user_name text unique,
    pass_word text
);

create table votation
(
    votation_id integer primary key autoincrement,
    promoter_user_id integer,
    votation_description text unique,
    begin_date date,
    end_date date,
    votation_type text,
    votation_status integer
);

create table guarantor
(
    votation_id integer,
    user_id integer,
    primary key (votation_id, user_id)
);

create table candidate
(
    votation_id integer,
    user_id integer,
    primary key (votation_id, user_id)
);

insert into voting_user
    (user_name, pass_word)
values
    ('aldo', 'aldo');
insert into voting_user
    (user_name, pass_word)
values
    ('beppe', 'beppe');
insert into voting_user    (user_name, pass_word) values    ('carlo', 'carlo');
insert into voting_user    (user_name, pass_word) values    ('dario', 'dario');
insert into voting_user    (user_name, pass_word) values    ('ernesto', 'ernesto');
insert into voting_user    (user_name, pass_word) values    ('fabio', 'fabio');

INSERT INTO votation
    (
    promoter_user_id,
    votation_description,
    begin_date,
    end_date,
    votation_type,
    votation_status
    )
VALUES
    (
        1,
        'votation test 1',
        '2018-10-01',
        '2018-10-30',
        'random',
        1);

INSERT INTO votation
    (
    promoter_user_id,
    votation_description,
    begin_date,
    end_date,
    votation_type,
    votation_status
    )
VALUES
    (
        1,
        'votation test 2',
        '2018-10-01',
        '2018-10-30',
        'random',
        1);

INSERT INTO votation
    (
    promoter_user_id,
    votation_description,
    begin_date,
    end_date,
    votation_type,
    votation_status
    )
VALUES
    (
        1,
        'votation test 3',
        '2018-09-21',
        '2018-10-15',
        'random',
        1);

INSERT INTO votation
    (
    promoter_user_id,
    votation_description,
    begin_date,
    end_date,
    votation_type,
    votation_status
    )
VALUES
    (
        1,
        'votation test 4',
        '2018-10-03',
        '2018-10-10',
        'random',
        1);

