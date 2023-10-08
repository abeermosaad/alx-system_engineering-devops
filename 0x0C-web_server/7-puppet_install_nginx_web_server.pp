# Configuring server with Puppet!

package { 'nginx':
  ensure => 'installed',
}

exec { 'mk dir':
    path    => '/usr/bin',
    command => 'sudo mkdir -p /var/www/abeermosaad.tech/html',
    returns => [0, 1],
}

file { '/var/www/html/index.nginx-debian.html':
    ensure  => 'present',
    content => "Hello World!\n",
    require => Package['nginx'],
    notify  => Service['nginx'],
}

file { '/var/www/abeermosaad.tech/html/custom_404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page\n",
    require => Package['nginx'],
    notify  => Service['nginx'],
}

file { '/etc/nginx/sites-available/default':
    ensure  => 'present',
    content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name abeermosaad.tech;
        add_header X-Served-By ${{hostname}};

        location /hbnb_static/ {
                alias /data/web_static/current/;
        }

        error_page 404 /custom_404.html;
        location = /custom_404.html {
                internal;
                root /var/www/abeermosaad.tech/html;
        }

        location /redirect_me {
                return 301 https://www.linkedin.com/in/abeermosaad/;
        }

        location / {
                root /var/www/abeermosaad.tech/html;
                index index.html;
                try_files ${{uri}} ${{uri}}/ =404;
        }
}
"
}

service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}
