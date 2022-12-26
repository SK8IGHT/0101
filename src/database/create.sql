create table if not exists Excavation(
	id integer primary key autoincrement,
	date_start varchar(256) not null,
	date_end varchar(256) not null,
	placeID integer not null,
	userID integer no null,
	foreign key (placeID) references Place(id),
	foreign key (userID) references User(id)
);

create table if not exists Place(
	id integer primary key autoincrement,
	name varchar(256) not null
);

create table if not exists Artifact(
	id integer primary key autoincrement,
	name varchar(256) not null,
	age integer not null,
	cultureID integer not null,
	foreign key (cultureID) references Culture(id)
);

create table if not exists Culture(
	id integer primary key autoincrement,
	name integer not null
);

create table if not exists User(
	id integer primary key autoincrement,
    name varchar(256) not null,
    password varchar(256) not null,
    post varchar(256) not null default "User"
);
