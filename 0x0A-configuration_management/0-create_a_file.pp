#!/usr/bin/pup
file { '/tmp/school':
    ensure  => file,
    content => 'I love Puppet',
    owner   => 'www-data',
    mode    => '0744',
}
