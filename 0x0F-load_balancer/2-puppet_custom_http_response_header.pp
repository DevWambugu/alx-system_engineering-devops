# create a custom HTTP header response, but with Puppet.
include stdlib

$redirect_link = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$redirect_content = "\trewrite ^/redirect_me/$ ${redirect_link} permanent;"
$custom_header = "add_header X-Served-By \$hostname;"

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

file_line { 'Set 301 redirection':
    ensure   => 'present',
    after    => 'server_name\ _;',
    path     => '/etc/nginx/sites-available/default',
    multiple => true,
    line     => $redirect_content,
    notify   => Exec['restart nginx'],
    require  => File['/var/www/html/index.html']
}

file_line { 'Set X-Served-By header':
   ensure   => 'present',
   after    => 'http {',
   path     => '/etc/nginx/nginx.conf',
   multiple => true,
   line     => $custom_header,
   notify   => Exec['restart nginx'],
   require  => File['/var/www/html/index.html']
}
