# automated puppet fix (to find out why Apache is returning a 500 error)

package { ['php', 'php-mysql', 'libapache2-mod-php']:
    ensure => installed,
}

file { '/var/www/html':
    ensure  => directory,
    recurse => true,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0755',
}

exec { 'restart_apache':
    command     => '/etc/init.d/apache2 restart',
    refreshonly => true,
}
