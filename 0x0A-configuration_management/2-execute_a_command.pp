# Kills process - killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
  path     => ['/bin', '/usr/bin'],
  onlyif   => 'pgrep -f killmenow',
}
