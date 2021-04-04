# Create a file

file { 'holberton':
  ensure  => 'present',
  path    => '/tmp/holberton',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  content => 'I love Puppet',
}
