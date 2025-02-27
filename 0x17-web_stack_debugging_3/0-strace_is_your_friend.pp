# automated puppet fix (to find out why Apache is returning a 500 error)

exec { 'fix-wordpress':
  command => 'chown -R www-data:www-data /var/www/html',
  path    => ['/bin', '/usr/bin'],
  unless  => 'stat -c %U:%G /var/www/html | grep -q www-data:www-data',
}
