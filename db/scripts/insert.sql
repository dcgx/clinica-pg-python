-- Medicos
INSERT INTO medicos (nombre, especialidad) VALUES ('Dr. House', 'Oncología');
INSERT INTO medicos (nombre, especialidad) VALUES ('Dr. Strange', 'Neurología');
INSERT INTO medicos (nombre, especialidad) VALUES ('Dr. Who', 'Cardiología');
INSERT INTO medicos (nombre, especialidad) VALUES ('Dr. Doom', 'Traumatología');
INSERT INTO medicos (nombre, especialidad) VALUES ('Dr. Manhattan', 'Psiquiatría');


-- Pacientes
INSERT INTO pacientes (nombre, rut, medico_id) VALUES ('Peter Parker', '12345678-9', 1);
INSERT INTO pacientes (nombre, rut, medico_id) VALUES ('Bruce Wayne', '87654321-0', 2);
INSERT INTO pacientes (nombre, rut, medico_id) VALUES ('Clark Kent', '11223344-5', 3);
INSERT INTO pacientes (nombre, rut, medico_id) VALUES ('Tony Stark', '55443322-1', 5);
INSERT INTO pacientes (nombre, rut, medico_id) VALUES ('Steve Rogers', '99887766-3', 5);


-- Examenes
INSERT INTO examenes (paciente_id, tipo, resultado) VALUES (1, 'Radiografía', 'Fractura en la pierna');
INSERT INTO examenes (paciente_id, tipo, resultado) VALUES (2, 'Tomografía', 'Tumor en el cerebro');
INSERT INTO examenes (paciente_id, tipo, resultado) VALUES (3, 'Electrocardiograma', 'Arritmia');
INSERT INTO examenes (paciente_id, tipo, resultado) VALUES (4, 'Resonancia', 'Trastorno de personalidad');
INSERT INTO examenes (paciente_id, tipo, resultado) VALUES (5, 'Radiografía', 'Fractura en el brazo');

-- Diagnosticos
INSERT INTO diagnosticos (examen_id, enfermedad) VALUES (1, 'Fractura');
INSERT INTO diagnosticos (examen_id, enfermedad) VALUES (2, 'Tumor');
INSERT INTO diagnosticos (examen_id, enfermedad) VALUES (3, 'Arritmia');
INSERT INTO diagnosticos (examen_id, enfermedad) VALUES (4, 'Trastorno de personalidad');

-- Habitaciones
INSERT INTO habitaciones (numero) VALUES (101);
INSERT INTO habitaciones (numero) VALUES (102);
INSERT INTO habitaciones (numero) VALUES (103);
INSERT INTO habitaciones (numero) VALUES (104);

-- Camas
INSERT INTO camas (habitacion_id, habilitada) VALUES (1, TRUE);
INSERT INTO camas (habitacion_id, habilitada) VALUES (1, TRUE);
INSERT INTO camas (habitacion_id, habilitada) VALUES (2, TRUE);
INSERT INTO camas (habitacion_id, habilitada) VALUES (2, FALSE);
INSERT INTO camas (habitacion_id, habilitada) VALUES (2, FALSE);
INSERT INTO camas (habitacion_id, habilitada) VALUES (3, TRUE);
INSERT INTO camas (habitacion_id, habilitada) VALUES (3, TRUE);
INSERT INTO camas (habitacion_id, habilitada) VALUES (3, TRUE);
INSERT INTO camas (habitacion_id, habilitada) VALUES (4, FALSE);
INSERT INTO camas (habitacion_id, habilitada) VALUES (4, TRUE);
