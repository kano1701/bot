CREATE TABLE `forBot`.`user` ( `telegram_id` INT NULL DEFAULT NULL , `lang` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'ru' , `status` VARCHAR(255) NOT NULL DEFAULT 'registration' , PRIMARY KEY (`telegram_id`)) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;
