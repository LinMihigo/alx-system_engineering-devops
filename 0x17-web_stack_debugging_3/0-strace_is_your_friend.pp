# automated puppet fix (to find out why Apache is returning a 500 error)

file { '/etc/apache2/missing.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => '# Automatically created by Puppet',
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  require => File['/etc/apache2/missing.conf'],
}
