CREATE TABLE levels_setting_down
(
    level_setting_down_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE teachers
(
    teacher_id INT NOT NULL PRIMARY KEY,
    fcs VARCHAR(100) NOT NULL,
    level_setting_down_id INT REFERENCES levels_setting_down(level_setting_down_id)
);

CREATE TABLE groups
(
    group_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(10) NOT NULL
);

CREATE TABLE departments
(
    department_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(70) NOT NULL
);

CREATE TABLE departments_teachers
(
    department_id INT NOT NULL,
    teacher_id INT REFERENCES teachers(teacher_id) ON DELETE CASCADE NOT NULL,

    CONSTRAINT departments_teachers_pkey PRIMARY KEY (department_id, teacher_id)
);

CREATE TABLE departments_groups
(
    department_id INT NOT NULL,
    group_id INT REFERENCES groups(group_id) ON DELETE CASCADE NOT NULL,

    CONSTRAINT departments_groups_pkey PRIMARY KEY(department_id, group_id)
);

CREATE TABLE disciplines
(
    discipline_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE parlours
(
    parlour_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE sessions
(
    session_id INT PRIMARY KEY NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE schedules
(
    day_week VARCHAR(20) NOT NULL,
    session_id INT REFERENCES sessions(session_id) ON DELETE CASCADE NOT NULL,
    discipline_id INT REFERENCES disciplines(discipline_id) ON DELETE CASCADE NOT NULL,
    group_id INT REFERENCES groups(group_id) ON DELETE CASCADE NOT NULL,
    teacher_id INT REFERENCES teachers(teacher_id) ON DELETE CASCADE NOT NULL,
    parlour_id INT REFERENCES parlours(parlour_id) ON DELETE CASCADE NOT NULL
);CREATE TABLE levels_setting_down
(
    level_setting_down_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE teachers
(
    teacher_id INT NOT NULL PRIMARY KEY,
    fcs VARCHAR(100) NOT NULL,
    level_setting_down_id INT REFERENCES levels_setting_down(level_setting_down_id)
);

CREATE TABLE groups
(
    group_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(10) NOT NULL
);

CREATE TABLE departments
(
    department_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(70) NOT NULL
);

CREATE TABLE departments_teachers
(
    department_id INT NOT NULL,
    teacher_id INT REFERENCES teachers(teacher_id) ON DELETE CASCADE NOT NULL,

    CONSTRAINT departments_teachers_pkey PRIMARY KEY (department_id, teacher_id)
);

CREATE TABLE departments_groups
(
    department_id INT NOT NULL,
    group_id INT REFERENCES groups(group_id) ON DELETE CASCADE NOT NULL,

    CONSTRAINT departments_groups_pkey PRIMARY KEY(department_id, group_id)
);

CREATE TABLE disciplines
(
    discipline_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE parlours
(
    parlour_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE sessions
(
    session_id INT PRIMARY KEY NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE schedules
(
    day_week VARCHAR(20) NOT NULL,
    session_id INT REFERENCES sessions(session_id) ON DELETE CASCADE NOT NULL,
    discipline_id INT REFERENCES disciplines(discipline_id) ON DELETE CASCADE NOT NULL,
    group_id INT REFERENCES groups(group_id) ON DELETE CASCADE NOT NULL,
    teacher_id INT REFERENCES teachers(teacher_id) ON DELETE CASCADE NOT NULL,
    parlour_id INT REFERENCES parlours(parlour_id) ON DELETE CASCADE NOT NULL
);