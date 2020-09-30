-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/dvTVBy
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Drivers" (
    "d_num" int   NOT NULL,
    "d_l_name" varchar   NOT NULL,
    "d_f_name" varchar   NOT NULL,
    "d_location" varchar   NOT NULL,
    CONSTRAINT "pk_Drivers" PRIMARY KEY (
        "d_num"
     )
);

CREATE TABLE "Routes" (
    "rt_run" serial   NOT NULL,
    "rt_num" int   NOT NULL,
    "rt_d_num" int   NOT NULL,
    "rt_l_name" varchar   NOT NULL,
    "rt_truck_num" int   NOT NULL,
    "rt_day" int   NOT NULL,
    CONSTRAINT "pk_Routes" PRIMARY KEY (
        "rt_run"
     )
);

CREATE TABLE "Reports" (
    "rp_run" int   NOT NULL,
    "rp_driverlog" bool   NOT NULL,
    "rp_catg" bool   NOT NULL,
    "rp_time_completed" time   NOT NULL
);

ALTER TABLE "Routes" ADD CONSTRAINT "fk_Routes_rt_d_num_rt_l_name" FOREIGN KEY("rt_d_num", "rt_l_name")
REFERENCES "Drivers" ("d_num", "d_l_name");

ALTER TABLE "Reports" ADD CONSTRAINT "fk_Reports_rp_run" FOREIGN KEY("rp_run")
REFERENCES "Routes" ("rt_run");

