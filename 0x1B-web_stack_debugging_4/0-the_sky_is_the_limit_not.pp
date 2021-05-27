# fix number of request
exec { 'More_Request':
        command => 'sed -i s/15/1000/ /etc/default/nginx',
        path => '/usr/local/bin/:/bin/'
 } -> exec { 'restart-nginx-service':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
