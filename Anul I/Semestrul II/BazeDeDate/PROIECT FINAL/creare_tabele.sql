create table SCENA (
	id integer identity(1,1),
	nume varchar(50) not null,
	constraint PK_SCENA_ID 
	primary key clustered(id)
);

create table PREZENTATOR(
	id integer identity(1,1),
	nume varchar(50) not null,
	constraint PK_PREZENTATOR_ID 
	primary key clustered(id)
);

create table MOD_JOC(
	id integer identity(1,1),
	nume varchar(50) not null,
	harta varchar(50) not null,
	dimensiune integer not null,
	constraint PK_MOD_JOC_ID 
	primary key clustered(id)
);

create table MECI(
	id integer identity(1,1),
	titlu varchar(20) not null,
	data_incepere datetime not null,
	constraint PK_MECI_ID 
	primary key clustered(id)
);

create table CAMPION(
	id integer identity(1,1),
	nume varchar(20) not null,
	titlu varchar(50) not null,
	resursa varchar(20) not null,
	constraint PK_CAMPION_ID 
	primary key clustered(id)
);

create table TURNEU(
	id integer,
	nume varchar(50) not null,
	oras varchar(20) not null,
	data_incepere date not null,
	constraint PK_TURNEU_ID 
	primary key clustered(id)
);

create table REGIUNE(
	id integer identity(1,1),
	nume varchar(20) not null,
	constraint PK_REGIUNE_ID 
	primary key clustered(id)
);

create table GRUPA(
	id integer identity(1,1),
	nume varchar(20) not null,
	id_turneu integer not null,
	constraint FK_ID_TURNEU_GRUPA 
	foreign key(id_turneu) references TURNEU(id),
	constraint PK_GRUPA_ID 
	primary key clustered(id)
);

create table ECHIPA(
	id integer identity(1,1),
	id_regiune integer not null,
	nume varchar(20) not null,
	tag varchar(3) not null,
	constraint FK_ID_REGIUNE_ECHIPA 
	foreign key (id_regiune) references REGIUNE(id),
	constraint PK_ECHIPA_ID 
	primary key clustered(id)
);

create table GRUPA_MAP(
	id_grupa integer,
	id_echipa integer,
	constraint FK_ID_JUCATOR_GRUPA_MAP 
	foreign key(id_grupa) references GRUPA(id),
	constraint FK_ID_ECHIPA_GRUPA_MAP 
	foreign key(id_echipa) references ECHIPA(id),
	constraint PK_GRUPA_MAP_ID 
	primary key clustered(id_grupa,id_echipa)
);

create table JUCATOR(
	id integer identity(1,1),
	id_echipa integer not null,
	id_regiune integer not null,
	nume varchar(50) not null,
	lane varchar(6) not null,
	constraint FK_ID_ECHIPA_JUCATOR 
	foreign key (id_echipa) references ECHIPA(id),
	constraint FK_ID_REGIUNE_REGIUNE
	foreign key (id_regiune) references REGIUNE(id),
	constraint PK_JUCATOR_ID 
	primary key clustered(id)
);

create table CAMPION_POOL(
	id_jucator integer,
	id_campion integer,
	constraint FK_ID_JUCATOR_CAMPION_POOL 
	foreign key(id_jucator) references JUCATOR(id),
	constraint FK_ID_CAMPION_CAMPION_POOL
	foreign key(id_campion) references CAMPION(id),
	constraint PK_CAMPION_POOL_ID 
	primary key clustered(id_jucator,id_campion)
);

create table MECI_MAP(
	id_echipa integer,
	id_meci integer,
	constraint FK_ID_ECHIPA_MECI_MAP 
	foreign key(id_echipa) references ECHIPA(id),
	constraint FK_ID_MECI_MECI_MAP 
	foreign key(id_meci) references MECI(id),
	constraint PK_MECI_MAP_ID 
	primary key clustered(id_echipa,id_meci)
);

create table MECI_HEADER(
	id integer identity(1,1) not null,
	id_meci integer,
	id_prezentator integer,
	id_scena integer,
	id_mod integer,
	constraint FK_ID_MECI_MECI_HEADER 
	foreign key(id_meci) references MECI(id),
	constraint FK_ID_PREZENTATOR_MECI_HEADER 
	foreign key(id_prezentator) references PREZENTATOR(id),
	constraint FK_ID_SCENA_MECI_HEADER
	foreign key(id_scena) references SCENA(id),
	constraint FK_ID_MOD_MECI_HEADER
	foreign key(id_mod) references MOD_JOC(id),
	constraint PK_MECI_HEADER_ID 
	primary key clustered(id_prezentator,id_meci,id_scena,id_mod)
);