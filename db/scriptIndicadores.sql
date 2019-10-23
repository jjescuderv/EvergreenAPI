create table indicadores (
	codigo			INT				PRIMARY KEY,
    nombre 			VARCHAR(100)	NOT NULL,
    descripcion 	VARCHAR(255)	NOT NULL,
    tipoIndicador 	ENUM('Estrés hídrico', 'Nitrógeno foliar', 'Índice cosecha', 'Densidad volumétrica radial') NOT NULL,
    prioridad 		TINYINT(2)		NOT NULL,
    imagen          VARCHAR(255)    NOT NULL
)