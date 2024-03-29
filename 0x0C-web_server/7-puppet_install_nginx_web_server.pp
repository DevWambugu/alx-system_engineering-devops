# configuring your server with Puppet
include stdlib

exec { 'update packages':
  command => '/usr/bin/apt-get update'
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages']
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}				  

file_line { 'Set 301 redirection and listen on port 80':
 ensure   => 'present',
 after    => 'server_name\ _;',
 path     => '/etc/nginx/sites-available/default',
 multiple => true,
 line     => ["$content", "listen 80;"],  # Add 'listen 80;' line
 notify   => Exec['restart nginx'],
 require  => File['/var/www/html/index.html']
}
