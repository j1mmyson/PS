set @hour := -1;

SELECT (@hour := @hour + 1) as HOUR, (select count(*) from animal_outs where HOUR(datetime) = @hour) as count from animal_outs where @hour < 23