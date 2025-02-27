# automated puppet fix (to find out why Apache is returning a 500 error)

exec { 'fix-wordpress':
  command => '/bin/chown -R www-data:www-data /var/www/html/wordpress && /bin/chmod -R 755 /var/www/html/wordpress',
  path    => ['/bin', '/usr/bin'],
  unless  => '/bin/test -d /var/www/html/wordpress',
}
