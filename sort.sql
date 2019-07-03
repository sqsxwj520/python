create table students(
	id int(4)  auto_increment primary key,
	name varchar(50) not null, 
	score int(4) not null
	);
  
先简单的创建一个测试用表，并插入数据：
 
insert into students(name,score) values('curry', 100),
	('klay', 99),
	('KD', 100), 
	('green', 90), 
	('James', 99), 
	('AD', 96);
  
 查看一下插入的数据：
  
 select * from students;
  

使用三种方式进行排序：
select id, name, rank() over(order by score desc) as r,
  DENSE_RANK() OVER(order by score desc) as dense_r,
  row_number() OVER(order by score desc) as row_r
from students;
