# create a manifest that kills a process

exec {'pkill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin'
}
