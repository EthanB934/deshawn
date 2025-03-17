DROP TABLE IF EXISTS Appointments;

CREATE TABLE "Appointments" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "walker_id" INTEGER,
    "date" DATE,
    "completed" BOOLEAN,
    FOREIGN KEY(`walker_id`) REFERENCES `deshawnapi_walker`(`id`)
)
    