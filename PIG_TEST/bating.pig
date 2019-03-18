

batting_list = LOAD '/home/cloudera/ABD/LAB_TEST/Batting.csv' USING PigStorage(',') as (playerID:chararray,yearID:int,stint:int,teamID:chararray,lgID:chararray,G:int,G_batting:int,AB:int,R:int,H:int,B2:int,B3:int,HR:int,RBI:int,SB:int,CS:int,BB:int,SO:int,IBB:int,HBP:int,SH:int,SF:int,GIDP:int,G_old:int);


--1 List the teamID of "aardsda01"

player_id = FILTER batting_list BY(playerID MATCHES 'aardsda01.*');


team_id_aardsda01 = FOREACH player_id generate teamID;

DUMP team_id_aardsda01;



--2 Average of g_batting for 1976 and 1984

year_filter = FILTER batting_list BY yearID IN(1976, 1984);

year_Group = Group year_filter All;

year_avg = foreach year_Group Generate AVG(year_filter.G_batting);


DUMP year_avg;


