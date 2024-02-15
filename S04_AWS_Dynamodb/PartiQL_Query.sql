Select * from Article;

Select * from Article where id in(1,2);

--insert into Article value{
--	'id':5,
--    'pub_date':'2022-02-12',
--    'title':'my newest title 2',
--    'body':'this is newest partiql body',
--    'author':'testuser'
--    };
--
DELETE
FROM Article
WHERE
  id = 5 AND pub_date = '2022-02-12';

--how to access index in DynomoDb
-- "tableName"."IndexName"
select * from "Article"."author-index"