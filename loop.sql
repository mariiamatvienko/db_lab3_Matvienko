select * from ERUPTION;
create table eruptioncopy as select * from eruption; 
delete from eruptioncopy
select * from eruptioncopy;

DO $$
DECLARE
    volcanic_numb eruptioncopy.volc_number%TYPE;
    high_elev eruptioncopy.elevation%TYPE;
  id_type eruptioncopy.eruption_id%TYPE;


BEGIN
    volcanic_numb := 220000;
    high_elev := 850;
  id_type := 5;
    FOR i IN 1..8
        LOOP
            INSERT INTO eruptioncopy(volc_number, eruption_id, elevation)
            VALUES (10*i + volcanic_numb,id_type+i ,high_elev+250*i);
        END LOOP;
END;
$$