#Execute a command

exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
