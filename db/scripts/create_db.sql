CREATE DATABASE clinica_db;

CREATE TABLE medicos (
    medico_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100) NOT NULL
);

CREATE TABLE pacientes (
    paciente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    rut VARCHAR(12) UNIQUE NOT NULL,
    medico_id INT REFERENCES medicos(medico_id)
);

CREATE table examenes (
    examen_id SERIAL PRIMARY KEY,
    paciente_id INT REFERENCES pacientes(paciente_id),
    tipo VARCHAR(100) NOT NULL,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    resultado TEXT
);

CREATE TABLE diagnosticos (
    diagnostico_id SERIAL PRIMARY KEY,
    examen_id INT REFERENCES examenes(examen_id),
    enfermedad VARCHAR(100) NOT NULL
);

CREATE TABLE habitaciones (
    habitacion_id SERIAL PRIMARY KEY,
    paciente_id INT REFERENCES pacientes(paciente_id),
    numero INT NOT NULL
);

CREATE TABLE camas (
    cama_id SERIAL PRIMARY KEY,
    habitacion_id INT REFERENCES habitaciones(habitacion_id),
    habilitada BOOLEAN NOT NULL DEFAULT FALSE
);