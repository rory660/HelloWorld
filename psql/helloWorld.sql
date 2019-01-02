create or replace function helloWorld()
returns void as $$
begin
	raise notice "Hello World!";
end;
$$ language plpgsql;
select helloWorld();