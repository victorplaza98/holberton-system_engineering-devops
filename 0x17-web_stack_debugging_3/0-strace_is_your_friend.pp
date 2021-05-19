# fixe apache 500 error 
exec { 'Fix':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => shell,
}
