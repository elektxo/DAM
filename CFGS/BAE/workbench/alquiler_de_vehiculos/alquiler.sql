-- MySQL Script generated by MySQL Workbench
-- lun 08 nov 2021 11:26:42
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema alquilerdevehiculos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema alquilerdevehiculos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `alquilerdevehiculos` ;
USE `alquilerdevehiculos` ;

-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`cliente` (
  `dni` VARCHAR(9) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `prapellido` VARCHAR(45) NOT NULL,
  `sgapellido` VARCHAR(45) NULL,
  `domicilio` VARCHAR(45) NOT NULL,
  `NumTarjeta` INT(16) NOT NULL,
  PRIMARY KEY (`dni`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`fabricante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`fabricante` (
  `CodFab` INT NOT NULL,
  `Fabricante` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CodFab`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`marca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`marca` (
  `CodMarca` INT NOT NULL,
  `Marca` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CodMarca`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`vehiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`vehiculo` (
  `CodVeh` INT NOT NULL,
  `modelo` VARCHAR(45) NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `FabVehic` INT NOT NULL,
  `MarcaVehic` INT NOT NULL,
  PRIMARY KEY (`CodVeh`, `FabVehic`, `MarcaVehic`),
  INDEX `fk_vehiculo_fabricante1_idx` (`FabVehic` ASC) VISIBLE,
  INDEX `fk_vehiculo_marca1_idx` (`MarcaVehic` ASC) VISIBLE,
  CONSTRAINT `fk_vehiculo_fabricante1`
    FOREIGN KEY (`FabVehic`)
    REFERENCES `alquilerdevehiculos`.`fabricante` (`CodFab`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vehiculo_marca1`
    FOREIGN KEY (`MarcaVehic`)
    REFERENCES `alquilerdevehiculos`.`marca` (`CodMarca`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`empleado` (
  `dni` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `prApellido` VARCHAR(45) NOT NULL,
  `sgApellido` VARCHAR(45) NULL,
  `domicilio` VARCHAR(45) NOT NULL,
  `NumCuenta` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`dni`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`alquiler`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`alquiler` (
  `CodAlquiler` INT NOT NULL,
  `fecha` DATETIME NOT NULL,
  `NumDias` INT(3) NOT NULL,
  `KmActules` INT(10) NOT NULL,
  `KmEntrega` INT(10) NOT NULL,
  `ClAlquila` VARCHAR(9) NOT NULL,
  `VehAlquila` INT NOT NULL,
  `EmplAlq` INT NOT NULL,
  PRIMARY KEY (`CodAlquiler`, `EmplAlq`),
  INDEX `fk_alquiler_cliente1_idx` (`ClAlquila` ASC) VISIBLE,
  INDEX `fk_alquiler_vehiculo1_idx` (`VehAlquila` ASC) VISIBLE,
  INDEX `fk_alquiler_empleado1_idx` (`EmplAlq` ASC) VISIBLE,
  CONSTRAINT `fk_alquiler_cliente1`
    FOREIGN KEY (`ClAlquila`)
    REFERENCES `alquilerdevehiculos`.`cliente` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_alquiler_vehiculo1`
    FOREIGN KEY (`VehAlquila`)
    REFERENCES `alquilerdevehiculos`.`vehiculo` (`CodVeh`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_alquiler_empleado1`
    FOREIGN KEY (`EmplAlq`)
    REFERENCES `alquilerdevehiculos`.`empleado` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`oficina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`oficina` (
  `CodOficina` INT NOT NULL,
  `domicilio` VARCHAR(45) NOT NULL,
  `telefono` INT(9) NOT NULL,
  PRIMARY KEY (`CodOficina`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`curso` (
  `CodCurso` INT NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `numHoras` INT(4) NOT NULL,
  `fecha` DATETIME NOT NULL,
  PRIMARY KEY (`CodCurso`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`OficinasAlq`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`OficinasAlq` (
  `oficina_CodOficina` INT NOT NULL,
  `alquiler_CodAlquiler` INT NOT NULL,
  PRIMARY KEY (`oficina_CodOficina`, `alquiler_CodAlquiler`),
  INDEX `fk_oficina_has_alquiler_alquiler1_idx` (`alquiler_CodAlquiler` ASC) VISIBLE,
  INDEX `fk_oficina_has_alquiler_oficina_idx` (`oficina_CodOficina` ASC) VISIBLE,
  CONSTRAINT `fk_oficina_has_alquiler_oficina`
    FOREIGN KEY (`oficina_CodOficina`)
    REFERENCES `alquilerdevehiculos`.`oficina` (`CodOficina`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_oficina_has_alquiler_alquiler1`
    FOREIGN KEY (`alquiler_CodAlquiler`)
    REFERENCES `alquilerdevehiculos`.`alquiler` (`CodAlquiler`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alquilerdevehiculos`.`CursoEmpl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alquilerdevehiculos`.`CursoEmpl` (
  `empleado_dni` INT NOT NULL,
  `curso_CodCurso` INT NOT NULL,
  PRIMARY KEY (`empleado_dni`, `curso_CodCurso`),
  INDEX `fk_empleado_has_curso_curso1_idx` (`curso_CodCurso` ASC) VISIBLE,
  INDEX `fk_empleado_has_curso_empleado1_idx` (`empleado_dni` ASC) VISIBLE,
  CONSTRAINT `fk_empleado_has_curso_empleado1`
    FOREIGN KEY (`empleado_dni`)
    REFERENCES `alquilerdevehiculos`.`empleado` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_empleado_has_curso_curso1`
    FOREIGN KEY (`curso_CodCurso`)
    REFERENCES `alquilerdevehiculos`.`curso` (`CodCurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
