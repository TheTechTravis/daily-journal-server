CREATE TABLE `Journal_Entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept` VARCHAR,
    `entry` VARCHAR,
    `date` DATE,
    `mood_id` INTEGER
);
CREATE TABLE `Moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood` VARCHAR,
    FOREIGN KEY(`id`) REFERENCES `Journal_Entries`(`mood_id`)
);
-- Generate Moods data
INSERT INTO `Moods`
VALUES (NULL, 'Ecstatic');
INSERT INTO `Moods`
VALUES (NULL, 'Happy');
INSERT INTO `Moods`
VALUES (NULL, 'Content');
INSERT INTO `Moods`
VALUES (NULL, 'Worried');
INSERT INTO `Moods`
VALUES (NULL, 'Frustrated');
-- Generate Journal_Entries data
INSERT INTO `Journal_Entries`
VALUES (
        NULL,
        'React',
        'React is awesome!',
        '07/24/2020',
        NULL
    );
INSERT INTO `Journal_Entries`
VALUES (
        NULL,
        'Capstones',
        "I can't wait to do my backend capstone ! ",
        '08/25/2020',
        NULL
    );
INSERT INTO `Journal_Entries`
VALUES (
        NULL,
        'Future Job ',
        "I'm going to work at FANG!",
        '09/24/2020',
        NULL
    );