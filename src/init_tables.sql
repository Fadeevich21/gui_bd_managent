INSERT INTO levels_setting_down
VALUES
     (1, 'docent'),
     (2, 'lecturer'),
     (3, 'senior lecturer');

INSERT INTO teachers
VALUES
    (1, 'Voskovskiy', 2),
    (2, 'Osipov', 1),
    (3, 'Karatach', 2),
    (4, 'Gavriuschenko', 1),
    (5, 'Stolyarova', 1),
    (6, 'Panchenko', 3),
    (7, 'Lukyanov', 3),
    (8, 'Shamraev', 1);

INSERT INTO groups
VALUES
    (1, 'BT-201'),
    (2, 'BT-202'),
    (3, 'PV-201'),
    (4, 'PV-202');

INSERT INTO departments
VALUES
    (1, 'POVTAS'),
    (2, 'TK'),
    (3, 'Ekonom');

INSERT INTO departments_teachers
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8);

INSERT INTO departments_groups
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4);

INSERT INTO sessions
VALUES
    (1, '08:15', '09:50'),
    (2, '10:00', '11:35'),
    (3, '11:45', '13:20'),
    (4, '14:20', '15:55'),
    (5, '16:05', '17:40'),
    (6, '17:50', '19:25'),
    (7, '19:35', '21:10'),
    (8, '21:20', '22:55');

INSERT INTO disciplines
VALUES
    (1, 'BD'),
    (2, 'IB'),
    (3, 'Physical education'),
    (4, 'OS'),
    (5, 'ACS'),
    (6, 'ICS'),
    (7, 'Economy'),
    (8, 'Programming of microcontrollers');

INSERT INTO parlours
VALUES
    (1, 'gym'),
    (2, 'gyk 032'),
    (3, 'gyk 033'),
    (4, 'yk4 424'),
    (5, 'yk4 218'),
    (6, 'yk2 423'),
    (7, 'yk4 415'),
    (8, 'yk1 2'),
    (9, 'yk2 401'),
    (10, 'yk5 401'),
    (11, 'gyk 426'),
    (12, 'gyk 427'),
    (13, 'gyk 425'),
    (14, 'gyk 430');

INSERT INTO schedules
VALUES
    -- Только числитель
    ('Monday', 3, 5, 1, 2, 2),
    ('Monday', 4, 2, 1, 4, 4),
    ('Monday', 5, 7, 1, 5, 5),
    ('Monday', 2, 3, 1, 1, 1),

    ('Wednesday', 1, 3, 1, 1, 1),
    ('Wednesday', 2, 1, 1, 6, 7),
    ('Wednesday', 3, 7, 1, 5, 8),
    ('Wednesday', 4, 6, 1, 7, 9),

    ('Friday', 1, 6, 1, 7, 10),
    ('Friday', 2, 1, 1, 6, 11),
    ('Friday', 3, 4, 1, 3, 12),
    ('Friday', 4, 5, 1, 2, 13),

    ('Saturday', 1, 8, 1, 8, 12),
    ('Saturday', 2, 8, 1, 8, 12),
    ('Saturday', 3, 8, 1, 8, 3),
    ('Saturday', 4, 8, 1, 8, 3);

